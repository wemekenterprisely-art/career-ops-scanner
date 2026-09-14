# Source probe — 2026-09-14 03:41 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 47 | responded with parseable jobs → **can be added** |
| empty | 18 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 23 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 50 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 4 | DNS/TLS/timeout |

## Answer: **40 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 250 | 200 | 275 | Senior Marketing Specialist (w/m/d); Working Student Export Control & Trade Compli; Working Student – Hardware Engineering (UAS P |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 797 | Technical Product Lead AI Finance App; Software Engineer; HR Operations Specialist |
| ✅ ok | `baseline:wwr` | 87 | 200 | 614 | Pinterest: Data Scientist II, ML Infrastructu; Fastly: Threat Detection Analyst (Japanese &a; Everpure: Account Executive, Commercial (Pitt |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 591 | Staff Software Engineer (SRE); GTM Talent Community; IT Associate |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 173 | Growth Manager, Americas; Senior Data Engineer; Technical Product Owner (Core Team, AI techno |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 194 | Healthcare Lead Gen Specialist; Proprietorship Tax Audit &amp; Filing; A-line Party Dress Pattern |
| ✅ ok | `baseline:remotive` | 16 | 200 | 125 | Remote Office Assistant; AI Response Evaluator; Inside Sales Contractor |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 576 | HR Operations Specialist; Marketing Student Assistant; Social Comms |
| ✅ ok | `precision:jobicy-teaching` | 50 | 200 | 930 | Manager, Cyber Compliance, Deloitte Global Te; Brand & Events Lead; Proposal Manager |
| ✅ ok | `precision:wwr-all-other` | 45 | 200 | 256 | Fastly: Threat Detection Analyst (Japanese &a; Toptal : Professional Photoshop Artists; Vonage: Technical Account Manager |
| ✅ ok | `precision:workingnomads-api` | 44 | 200 | 707 | Product Lead (Strategy + Full Stack); Face Deduplication Collection; Senior Google Ads Account Manager - Remote (W |
| ✅ ok | `precision:jobicy-translation` | 42 | 200 | 980 | Translation Project Manager; Alliance Manager, Translational Medicine; Project Director, Qualitative Research |
| ✅ ok | `precision:remotive-translator` | 16 | 200 | 32 | Remote Office Assistant; AI Response Evaluator; Inside Sales Contractor |
| ✅ ok | `precision:remotive-teacher` | 16 | 200 | 31 | Remote Office Assistant; AI Response Evaluator; Inside Sales Contractor |
| ✅ ok | `precision:remotive-writer` | 16 | 200 | 31 | Remote Office Assistant; AI Response Evaluator; Inside Sales Contractor |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 282 | Analyst,Underwriter; Writing and Annotation Task - Fula (Adlam Scr; P&C Middle Market Energy Renewal Underwriter |
| 🔑 needs_key | `jsearch:arabic-translator` | 0 |  |  | missing secret(s): RAPIDAPI_KEY |
| 🔑 needs_key | `jsearch:esl-teacher` | 0 |  |  | missing secret(s): RAPIDAPI_KEY |
| 🔑 needs_key | `adzuna:gb` | 0 |  |  | missing secret(s): ADZUNA_APP_ID, ADZUNA_APP_KEY |
| 🔑 needs_key | `adzuna:us` | 0 |  |  | missing secret(s): ADZUNA_APP_ID, ADZUNA_APP_KEY |
| 🔑 needs_key | `jooble:arabic-translator` | 0 |  |  | missing secret(s): JOOBLE_API_KEY |
| 🔑 needs_key | `careerjet:arabic-translator` | 0 |  |  | missing secret(s): CAREERJET_AFFID |
| 🔑 needs_key | `reliefweb:arabic` | 0 |  |  | missing secret(s): RELIEFWEB_APPNAME |
| 🔑 needs_key | `reed:arabic-translator` | 0 |  |  | missing secret(s): REED_API_KEY_B64 |

## linkedin  <sub>ok 4 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 494 | Translation Specialist; Creative Translator/PM; Translation Team Member |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 409 | Afrikaans Linguist CAT III; General Qualifications Examiner - Internation; PhD Fellow in Linguistics |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 446 | ESL Teacher (Online English Instructor); MY English Teacher (Full-Time); Online Bilingual English/French Teacher |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 517 | Editor, Alto; Proofreader; Senior Copy Editor |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 209 | Customer Support Needed; Wikipedia Biography Page Creation; AI-Generated Arabic Promo Video Creation |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 221 | Virtual Assistant - Procurement Support; Virtual Assistant with Procurement Experience; Etsy Jewelry Listing & Photo Optimization |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 194 | Digitise 50-100 Page Manuscript; WordPress Website Manager Needed; Etsy Jewelry Listing & Photo Optimization |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 186 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 101 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 150 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 145 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 831 | 200 | 271 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 103 | 200 | 150 | Infrastructure Engineer ; Strategic Project Lead; Strategic Projects Lead, Deeptune |
| ✅ ok | `html:dataannotation` | 94 | 200 | 443 | Software EngineerCoding$75 – $150+ / hr312 hi; GeneralistGeneral$25 – $50 / hr452 hired rece; Data ScientistData &amp; ML$75 – $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 21 | 200 | 82 | AI Engagement Lead; Chief of Staff (CEO's Office); Client Director, Frontier Data - US |
| ✅ ok | `greenhouse:labelbox` | 10 | 200 | 140 | Accounts Payable, Spend Management Coordinato; Cyber Security Intern; Forward Deployed Engineering Manager |
| ⚪ empty | `ashby:deel` | 0 | 200 | 71 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 221 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 229 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 152 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 521 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 530 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 114 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 97 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 153 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 73 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 62 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 75 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 65 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 65 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 189 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 68 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 1 · not_found 15 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 51 | 200 | 443 | Technical Artist ; Game Designer – Japan & Global Game Developme; Game Programmer – Japan & Global Game Develop |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 432 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 529 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 799 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 417 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 466 | 243547 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 375 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 383 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 2885 | 132990 bytes, text/html |
| ⛔ blocked | `html:futuregroup-careers` | 0 | 202 | 322 | HTTP 202 + challenge page |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 213 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 70 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 44 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 73 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 96 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 85 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 88 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 66 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 398 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 1 · not_found 16 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 3914 | 186383 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 471 | 213026 bytes, text/html |
| ⛔ blocked | `personio:lingoda` | 0 | 429 | 875 | HTTP 429 |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 46 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 74 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 519 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 233 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 389 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 72 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 168 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 206 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 73 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 84 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 391 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 19 | 200 | 89 | Business Development/ Sales Executive - EMEA ; Community & Support Intern - UAE Nationals; Community and Support Specialist |
| ❓ not_found | `lever:anghami` | 0 | 404 | 46 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 218 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 508 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 122 | HTTP 404 |

## remote-boards  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:remowork-arabic` | 203 | 200 | 1176 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `json:remote1stjobs` | 50 | 200 | 1542 | Senior Backend Engineer (Python) - Remote; Advertising Account Manager - eCommerce; Senior Software Engineer |
| ✅ ok | `html:jobgether` | 6 | 200 | 289 | Job  Search  Tips; Jobseekers guide; Review Jobgether &nbsp;→ |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 317 | 79755 bytes, text/html |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 649 | HTTP 202 + challenge page |
| ⛔ blocked | `rss:remotejobleads` | 0 | 403 | 129 | HTTP 403 + challenge page |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 146 | HTTP 403 + challenge page |
| 💥 error | `html:remote-co` | 0 |  | 15242 | timeout >15s |
| 💥 error | `html:europeremotely` | 0 |  | 465 | ClientConnectorError: Cannot connect to host europeremotely.com:443 ssl:False [Connection reset by peer] |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2605 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 395 | 428469 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 130 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 298 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 43 | 200 | 1505 | Get job alerts; Get job alerts; English Teaching Jobs in Vietnam with VUS |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 1108 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 430 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 266 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 195 | 200 | 1647 | Openings; Search; WVI - World Vision International |
| ✅ ok | `html:impactpool-arabic` | 12 | 200 | 952 | Interpreter – Arabic/Sudanese Arabic


IRC - ; Interpreter (Arabic)


IOM - International Or; Consultants template


WHO - World Health Org |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 553 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 250 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1882 | Jobs in Jordan (45); Jobs in Saudi Arabia (4); Jobs in UAE (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 163 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 130 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 140 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 302 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 371 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 137 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15902 | timeout >15s |

## academic-editing-watchers  <sub>ok 3 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:cactus` | 18 | 200 | 2088 | Employer Brand Promise; Life at CACTUS; Open Positions |
| ✅ ok | `watch:enago` | 9 | 200 | 396 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 660 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 899 | 345017 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 143 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 303 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1520 | HTTP 404 |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 64 | 200 | 433 | Find Jobs; Senior Software Engineer; Design Engineer, Site |
| ⚪ empty | `google:jobs` | 0 | 200 | 210 | 93084 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 401 | 85 | HTTP 401 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 24 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 150 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 89 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 193 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 831 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 10 jobs
    ("Turing", "turing"),   # 21 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 103 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 19 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 51 jobs
    ("TransPerfect", "TransPerfect"),   # 18 jobs
```

```json
// source_registry.json additions
{"url": "https://weworkremotely.com/categories/all-other-remote-jobs.rss", "source_name": "wwr-all-other", "type": "rss"},
{"url": "https://www.workingnomads.com/api/exposed_jobs/", "source_name": "workingnomads-api", "type": "json"},
{"url": "https://www.themuse.com/api/public/jobs?page=1&category=Writing%20and%20Editing&level=Mid%20Level", "source_name": "writing-editing", "type": "json"},
{"url": "https://www.remote1stjobs.com/jobs.json", "source_name": "remote1stjobs", "type": "json"},
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
