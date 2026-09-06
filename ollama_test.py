"""Ollama end-to-end strength test - 5-dimension JSON scoring + deterministic rule gate."""
import json, os, re, sys, time, urllib.request

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

REJECT_TITLE_HINTS = ("engineer", "developer", "programmer", "devops", "software",
                      "full-stack", "full stack", "backend", "frontend", "data scientist")
REJECT_TEXT_HINTS = ("commission only", "quota", "sales target")
VISA_BLOCKER_HINTS = ("citizenship required", "us citizenship required", "u.s. citizenship required",
                      "visa sponsorship required", "sponsorship required", "visa required",
                      "must have citizenship", "must be a citizen")
VISA_NEGATIONS = ("no visa", "without visa", "no sponsorship", "without sponsorship",
                  "free visa", "visa assistance", "sponsorship available",
                  "no visa sponsorship", "without visa sponsorship", "no sponsorship required",
                  "does not require", "doesn't require", "not required")

def visa_blocker(text):
    if not any(k in text for k in ("citizenship", "visa", "sponsorship")):
        return False
    if any(n in text for n in VISA_NEGATIONS):
        return False
    return any(h in text for h in VISA_BLOCKER_HINTS) or ("visa" in text or "citizenship" in text)

def enforce(job, scoring):
    if not scoring: return scoring
    text = " ".join(filter(None, [str(job.get("title", "")), str(job.get("description", ""))])).lower()
    s = int(float(scoring.get("overall_score") or 0))
    loc = dict(scoring.get("location_logistics") or {"verdict": "PASS", "reason": ""})
    touched = []
    if any(h in text for h in REJECT_TITLE_HINTS):
        s = min(s, 39); touched.append("engineering cap (<40)")
    if visa_blocker(text):
        loc["verdict"] = "FAIL"; s = min(s, 49); touched.append("citizenship/visa => FAIL (<50)")
    if any(h in text for h in REJECT_TEXT_HINTS):
        s = min(s, 49); touched.append("commission/quota cap (<50)")
    if str(loc.get("verdict", "")).upper() == "FAIL":
        s = min(s, 49)
    s = max(0, min(100, s))
    verdict = ("Poor Fit" if s < 40 else "Weak Fit" if s < 50 else
               "Moderate Fit" if s < 65 else "Good Fit" if s < 80 else "Strong Fit")
    scoring["overall_score"] = s
    scoring["location_logistics"] = loc
    scoring["verdict"] = verdict
    if touched: scoring["_rules_applied"] = touched
    return scoring

def api(path, payload=None, timeout=180):
    url = OLLAMA_URL + path
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read().decode()
    return json.loads(body), time.time() - t0

SCORING_PROMPT = """You are a senior career advisor evaluating job fit for a specific candidate. Be precise and honest.

CANDIDATE PROFILE:
Name: Waleed Ballag
Background: ESL Instructor and Academic Secondary Supervisor with MA in Applied Linguistics. Supervised 15 graduate-level research studies. Experienced in Arabic-English translation (legal, academic, technical). Native Arabic speaker with C1 Advanced English.
Primary Skills: ESL/EFL Instruction, Arabic-English Bidirectional Translation, Academic Editing, Thesis Review, Curriculum Development, Legal Translation
Career Goals: Secure stable remote work in translation or ESL teaching
Location: Remote (worldwide)

JOB LISTING:
Title: {title}
Company: {company}
Location: {location}
Description: {description}

RULES: Technical (30%), Experience (25%), Behavioral (15%), Career (30%) each 0-100, plus location_logistics PASS/FAIL/FLAG.
- Engineering/developer/programming jobs or US/visa-required roles MUST score below 40 / location FAIL.
- Respond ONLY with ONE JSON object with keys: technical_skills{{score,reason}}, experience_match{{score,reason}}, behavioral_fit{{score,reason}}, location_logistics{{verdict,reason}}, career_alignment{{score,reason}}, overall_score, verdict, strengths[], gaps[], recommendation, one_line_summary"""

JOBS = [
    {"title": "Remote Arabic-English Legal Translator", "company": "Global Language Services", "location": "Remote (worldwide)",
     "description": "Translate legal contracts, academic papers and business correspondence. Native Arabic, C1+ English. Remote, worldwide, no visa sponsorship."},
    {"title": "Senior Full-Stack Engineer (React/Node)", "company": "TechCorp", "location": "Remote (US only)",
     "description": "Build production React/Node applications in TypeScript, run Kubernetes. Requires 8+ years engineering, US citizenship required."},
    {"title": "Remote Data Entry Virtual Assistant", "company": "Remote Assist Co", "location": "Remote (worldwide)",
     "description": "Enter and organize data in spreadsheets, manage schedules, respond to emails. Basic English. 20 hours/week, fully remote."},
]

GATES = [
    ("GOOD-FIT must stay >=70 & loc PASS", lambda s, loc: s >= 70 and "PASS" in str(loc.get("verdict", "")).upper()),
    ("REJECT engineering/citizenship => <50 & loc FAIL", lambda s, loc: s < 50 and str(loc.get("verdict", "")).upper() == "FAIL"),
    ("SANE range 50-90", lambda s, loc: 50 <= s <= 90),
]

def main():
    print("== OLLAMA STRENGTH TEST v3 (negation-aware rule gate) ==")
    tags, t = api("/api/tags", timeout=10)
    models = [m["name"] for m in tags.get("models", [])]
    print("Server OK in %.2fs | models: %s" % (t, ", ".join(models) or "NONE"))
    if MODEL not in models:
        print("FATAL: model %s missing" % MODEL); sys.exit(1)

    ok, fail = 0, 0
    for idx, job in enumerate(JOBS, 1):
        prompt = SCORING_PROMPT.format(**job)
        payload = {"model": MODEL, "prompt": prompt, "stream": False, "format": "json",
                   "options": {"temperature": 0.3, "num_predict": 700, "num_ctx": 8192}}
        data, dt = api("/api/generate", payload)
        resp = data.get("response", "")
        edur = data.get("eval_duration", 1) or 1
        ec = data.get("eval_count", 0)
        raw = json.loads(resp) if resp.strip().startswith("{") else {}
        before = (raw.get("overall_score"), raw.get("verdict"), raw.get("location_logistics", {}).get("verdict"))
        scored = enforce(job, raw)
        after = (scored.get("overall_score"), scored.get("verdict"), scored.get("location_logistics", {}).get("verdict"))
        print("\n--- %s ---" % job["title"])
        print("  wall %.1fs | output %d tok @ %.1f tok/s" % (dt, ec, ec/(edur/1e9)))
        print("  MODEL BEFORE:  overall=%s verdict=%r loc=%s" % before)
        print("  RULES AFTER:   overall=%s verdict=%r loc=%s rules=%s" % (after[0], after[1], after[2], scored.get("_rules_applied", [])))
        desc, gate = GATES[idx-1]
        passed = gate(after[0], scored.get("location_logistics") or {})
        ok += passed; fail += (not passed)
        print("  GATE %d '%s': %s" % (idx, desc, "PASS" if passed else "FAIL"))

    print("\n=== GATES: %d/%d passed ===" % (ok, len(JOBS)))
    sys.exit(0 if fail == 0 else 1)

if __name__ == "__main__":
    main()
