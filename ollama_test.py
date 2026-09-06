"""Ollama end-to-end strength test - the scanner's real 5-dimension scoring prompt."""
import json, os, re, sys, time, urllib.request

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

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
    ("Remote Arabic-English Legal Translator", "Global Language Services", "Remote (worldwide)",
     "Translate legal contracts, academic papers and business correspondence. Native Arabic, C1+ English. Remote, worldwide, no visa sponsorship."),
    ("Senior Full-Stack Engineer (React/Node)", "TechCorp", "Remote (US only)",
     "Build production React/Node applications in TypeScript, run Kubernetes. Requires 8+ years engineering, US citizenship required."),
    ("Remote Data Entry Virtual Assistant", "Remote Assist Co", "Remote (worldwide)",
     "Enter and organize data in spreadsheets, manage schedules, respond to emails. Basic English. 20 hours/week, fully remote."),
]

def main():
    print("== OLLAMA STRENGTH TEST ==")
    tags, t = api("/api/tags", timeout=10)
    models = [m["name"] for m in tags.get("models", [])]
    print("Server OK in %.2fs | models: %s" % (t, ", ".join(models) or "NONE"))
    if MODEL not in models:
        print("FATAL: model %s missing" % MODEL); sys.exit(1)

    for title, company, loc, desc in JOBS:
        prompt = SCORING_PROMPT.format(title=title, company=company, location=loc, description=desc)
        payload = {"model": MODEL, "prompt": prompt, "stream": False, "format": "json",
                   "options": {"temperature": 0.3, "num_predict": 700, "num_ctx": 8192}}
        data, dt = api("/api/generate", payload)
        resp = data.get("response", "")
        pdur = data.get("prompt_eval_duration", 1) or 1
        edur = data.get("eval_duration", 1) or 1
        pec = data.get("prompt_eval_count", 0); ec = data.get("eval_count", 0)
        print("\n--- %s ---" % title)
        print("  wall %.1fs | input %d tok @ %.1f tok/s | output %d tok @ %.1f tok/s | total %d ms"
              % (dt, pec, pec/(pdur/1e9), ec, ec/(edur/1e9), data.get("total_duration", 0)//1_000_000))
        try:
            j = json.loads(resp)
            print("  PARSED: overall=%s verdict=%s loc=%s" % (j.get("overall_score"), j.get("verdict"), j.get("location_logistics", {}).get("verdict")))
            print("  summary: %s" % j.get("one_line_summary", "")[:140])
            print("  strengths: %s | gaps: %s" % (j.get("strengths", [])[:2], j.get("gaps", [])[:2]))
        except Exception as e:
            print("  PARSE FAIL (%s): %s" % (e, resp[:200]))

if __name__ == "__main__":
    main()
