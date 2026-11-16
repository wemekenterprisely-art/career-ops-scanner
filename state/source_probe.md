# Source probe — 2026-11-16 11:52 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 49 | responded with parseable jobs → **can be added** |
| empty | 17 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 21 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 52 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 3 | DNS/TLS/timeout |

## Answer: **42 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 130 | Werkstudent:in / Praktikant:in Customer Succe; Cloud Engineer (Generative AI & LLM) (m/w/d); Praktikant für Nachhaltiges Investment (m/w/d |
| ✅ ok | `baseline:wwr` | 100 | 200 | 800 | BBE Marketing Inc: Business Development Manag; FELYRI CONSULTING LIMITED: Research Consultan; Roofr: Sales Development Representative |
| ✅ ok | `baseline:remoteok` | 97 | 200 | 356 | Global Partnerships BD Lead; Scaled Account Manager EMEA; Software Engineer AI Tooling |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 434 | Senior DevOps Engineer; IT Department Lead - Remote, Worldwide; Site Reliability Engineer |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 44 | Implementation Specialist, US; Content Designer, AI Experiences; SAP Close Automation Consultant, Global (UK a |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 10 | Comprehensive Fintech App Flow Analysis; Fix Google Title Duplication; Pixel Animator for Horror Platformer |
| ✅ ok | `baseline:remotive` | 16 | 200 | 47 | Content Creator - YouTube; Remote Office Assistant; Senior Data Engineer |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 99 | 200 | 377 | Global Partnerships BD Lead; Research Engineer Privacy and Anonymization; Freelance Question Reviewers |
| ✅ ok | `precision:wwr-all-other` | 91 | 200 | 237 | FELYRI CONSULTING LIMITED: Research Consultan; D2B: Australian Healthcare Recruiter (AU Expe; D2B: Senior Roofing Estimator &amp; Takeoff S |
| ✅ ok | `precision:workingnomads-api` | 34 | 200 | 64 | QA Testers Wanted to Jump on an AI Assistant ; Senior React Full-stack Developer; Senior UI & UX Designer |
| ✅ ok | `precision:jobicy-teaching` | 33 | 200 | 845 | Supply Chain Coordinator Coach; 1 on 1 AMC 8 Tutor (Remote in US); Senior Editor, AI and Technology, Deloitte Gl |
| ✅ ok | `precision:jobicy-translation` | 24 | 200 | 125 | Solution Consultant; Senior Manager, Services Portfolio Production; Sr. Clinical Research Associate (Hungary) |
| ✅ ok | `precision:remotive-translator` | 16 | 200 | 13 | Content Creator - YouTube; Remote Office Assistant; Senior Data Engineer |
| ✅ ok | `precision:remotive-teacher` | 16 | 200 | 35 | Content Creator - YouTube; Remote Office Assistant; Senior Data Engineer |
| ✅ ok | `precision:remotive-writer` | 16 | 200 | 12 | Content Creator - YouTube; Remote Office Assistant; Senior Data Engineer |

## aggregator-keyed  <sub>ok 0 · empty 0 · blocked 1 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| 🔑 needs_key | `jsearch:arabic-translator` | 0 |  |  | missing secret(s): RAPIDAPI_KEY |
| 🔑 needs_key | `jsearch:esl-teacher` | 0 |  |  | missing secret(s): RAPIDAPI_KEY |
| 🔑 needs_key | `adzuna:gb` | 0 |  |  | missing secret(s): ADZUNA_APP_ID, ADZUNA_APP_KEY |
| 🔑 needs_key | `adzuna:us` | 0 |  |  | missing secret(s): ADZUNA_APP_ID, ADZUNA_APP_KEY |
| 🔑 needs_key | `jooble:arabic-translator` | 0 |  |  | missing secret(s): JOOBLE_API_KEY |
| 🔑 needs_key | `careerjet:arabic-translator` | 0 |  |  | missing secret(s): CAREERJET_AFFID |
| 🔑 needs_key | `reliefweb:arabic` | 0 |  |  | missing secret(s): RELIEFWEB_APPNAME |
| 🔑 needs_key | `reed:arabic-translator` | 0 |  |  | missing secret(s): REED_API_KEY_B64 |
| ⛔ blocked | `themuse:writing-editing` | 0 | 403 | 43 | HTTP 403 + challenge page |

## linkedin  <sub>ok 4 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 430 | 西班牙语翻译; Translator Mandarin (TM); Translator (English ↔ Korean)번역 담당 |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 451 | General Qualifications Examiner - Internation; 音乐内容与本地化编辑（上海onsite）; Afrikaans Linguist CAT III |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 432 | Specialista Linguistico da Remoto; 英語コーチ/フルリモート; English Tutor |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 427 | Senior Copy Editor; Editor; Arabic Linguistics Editor |

## freelance  <sub>ok 4 · empty 0 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 93 | Russian-Bulgarian Website Translation; Thai translator needed (long term); Handwritten Letter Typing & Translation |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 106 | English Letter Handwriting Transcription; Colmar Site Visit: Employment Verification; Design 8 High-Impact Website Banners |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 133 | Excel Data Entry & Some Corrections; High-Energy Band Showreel Video; Complete TikTok Video Podcast Setup |
| ✅ ok | `pph:search-arabic` | 1 | 200 | 185 | Post Project |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 19 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 20 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 20 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 827 | 200 | 122 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `html:dataannotation` | 133 | 200 | 132 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `ashby:mercor` | 91 | 200 | 65 | Infrastructure Software Engineer ; Strategic Project Lead; Strategic Projects Lead, Deeptune |
| ✅ ok | `greenhouse:turing` | 45 | 200 | 38 | Account Director, Enterprise AI - Consumer Pa; AI Engagement Lead; Client Director, Financial Services (BFSI) |
| ✅ ok | `greenhouse:labelbox` | 11 | 200 | 71 | Forward Deployed Engineer, Enterprise Account; Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments |
| ⚪ empty | `ashby:deel` | 0 | 200 | 53 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 60 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 45 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 52 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 346 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 353 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 33 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 10 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 40 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 273 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 21 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 1 · not_found 15 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 29 | 200 | 393 | Rendering Engineer; シニア3D背景アーティスト; 3D 背景アーティスト |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 360 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 266 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 277 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 346 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 43 | 5576 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 338 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 343 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 2523 | 133427 bytes, text/html |
| ⛔ blocked | `html:futuregroup-careers` | 0 | 202 | 286 | HTTP 202 + challenge page |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 256 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 276 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 10 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 89 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 26 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 36 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 319 | 163017 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 113 | 220902 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 72 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 309 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 123 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 283 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 401 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 138 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 34 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 36 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 264 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 8 | 200 | 40 | AI Artist; AI Artist; AI Artist |
| ❓ not_found | `lever:anghami` | 0 | 404 | 290 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 128 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 239 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 29 | HTTP 404 |

## remote-boards  <sub>ok 5 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 37806 | 200 | 3368 | Senior Product Manager - Growth; Senior Product Manager - Growth; Senior Manager, Accounting |
| ✅ ok | `html:remowork-arabic` | 211 | 200 | 608 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 451 | Project Manager; Project Manager (LATAM &#8211; Remote); Bioinformatics Scientist |
| ✅ ok | `html:jobgether` | 7 | 200 | 222 | Job search playbook; Job search playbook; Jobseekers guide |
| ✅ ok | `html:dailyremote` | 2 | 200 | 97 | Job Application Tracker; Search Jobs by Job Title |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 134 | 79774 bytes, text/html |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 530 | HTTP 202 + challenge page |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 658 | HTTP 403 |
| 💥 error | `html:remote-co` | 0 |  | 15220 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 1541 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 56 | 387893 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 21 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 167 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 44 | 200 | 2080 | Get job alerts; Get job alerts; Teachers Needed in Budapest for Pre-School, P |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 432 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 56 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 174 | HTTP 404 |

## un-ngo  <sub>ok 1 · empty 0 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:idealist-arabic` | 4 | 200 | 105 | Find a Job; Jobs; Find a Job |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 56 | HTTP 403 + challenge page |
| ⛔ blocked | `html:impactpool-arabic` | 0 | 403 | 79 | HTTP 403 + challenge page |
| ⛔ blocked | `html:untalent-arabic` | 0 | 403 | 144 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 3 · empty 0 · blocked 4 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:mostaql-writing-translation` | 9 | 200 | 355 | مشاريع أعمال; مشاريع برمجة; مشاريع ذكاء اصطناعي |
| ✅ ok | `html:tanqeeb-translator` | 7 | 200 | 139 | إدارة وظائفي; وظائف برواتب; صاحب عمل؟
                                    |
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1179 | Jobs in Jordan (40); Jobs in Saudi Arabia (6); Jobs in Qatar (3) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 48 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 47 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 63 | HTTP 403 + challenge page |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 46 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15662 | timeout >15s |

## academic-editing-watchers  <sub>ok 3 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:cactus` | 18 | 200 | 1421 | Employer Brand Promise; Life at CACTUS; Open Positions |
| ✅ ok | `watch:enago` | 9 | 200 | 65 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 535 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 679 | 385787 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 19 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 149 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1328 | HTTP 404 |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 4 · not_found 1 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 62 | 200 | 253 | Find Jobs; Senior SDET; Senior Sales Executive, Strategic Banking |
| ⚪ empty | `google:jobs` | 0 | 200 | 92 | 93798 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 22 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 21 | HTTP 403 + challenge page |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 22 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 21 | HTTP 403 + challenge page |
| ❓ not_found | `indeed:rss` | 0 | 404 | 56 | HTTP 404 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 827 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 11 jobs
    ("Turing", "turing"),   # 45 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 91 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 8 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 29 jobs
    ("TransPerfect", "TransPerfect"),   # 18 jobs
```

```json
// source_registry.json additions
{"url": "https://weworkremotely.com/categories/all-other-remote-jobs.rss", "source_name": "wwr-all-other", "type": "rss"},
{"url": "https://www.workingnomads.com/api/exposed_jobs/", "source_name": "workingnomads-api", "type": "json"},
{"url": "https://www.remotejobleads.com/feed/", "source_name": "remotejobleads", "type": "rss"},
{"url": "https://www.remote1stjobs.com/jobs.json", "source_name": "remote1stjobs", "type": "json"},
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
