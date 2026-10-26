# Source probe — 2026-10-26 09:14 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 47 | responded with parseable jobs → **can be added** |
| empty | 18 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 20 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 51 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 6 | DNS/TLS/timeout |

## Answer: **40 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 183 | Sales Manager Maklersoftware (m/w/d); Praktikum Social Media & Marketing (m/w/d); Senior Software Engineer \| Agentic Engineerin |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 620 | Field Phlebotomy Supervisor Northern Californ; Solutions Engineer; Sales Development Representative German Speak |
| ✅ ok | `baseline:wwr` | 96 | 200 | 809 | Reddit: Frontend Engineer, Ads; Mercury: Customer Support Manager - Risk; Mercury: Customer Support Specialist |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 543 | Senior Software Engineer, Backend (Money Move; Linux Software Engineer - Ubuntu for Next-Gen; Software Engineer - Branching |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 121 | Shopify Operations Specialist for a U.S. Jewe; CHIEF OF STAFF (M/F/D); AI Speech & Audio Specialist – ASR \| TTS \| Vo |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 172 | Basic sa Star Instagram Poster; Best-Selling Product Analysis; Automation Anywhere Excel Bot |
| ✅ ok | `baseline:remotive` | 10 | 200 | 99 | AI Trainer - Video Annotation; Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 424 | Accounting & Finance Manager; Senior Software Engineer II Applied AI; Principal Software Engineer |
| ✅ ok | `precision:wwr-all-other` | 83 | 200 | 334 | Datadog: Key Accounts Executive; Gemini: Lead, Technical Compliance; Talkspace: Clinical Quality Specialist |
| ✅ ok | `precision:workingnomads-api` | 39 | 200 | 319 | Senior Angular Developer; Senior DevOps Engineer; Quality Assurance Rater - Spanish speakers in |
| ✅ ok | `precision:jobicy-translation` | 20 | 200 | 1065 | LQA Game Tester (European Spanish) - Freelanc; Solution Architect; Sr. Clinical Research Associate (Romania) |
| ✅ ok | `precision:jobicy-teaching` | 20 | 200 | 1075 | Enterprise Sales Executive, Banking, Financia; Customer Success Manager (Higher Education); Senior Strategic Implementation Specialist -  |
| ✅ ok | `precision:remotive-translator` | 10 | 200 | 16 | AI Trainer - Video Annotation; Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer |
| ✅ ok | `precision:remotive-teacher` | 10 | 200 | 18 | AI Trainer - Video Annotation; Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer |
| ✅ ok | `precision:remotive-writer` | 10 | 200 | 16 | AI Trainer - Video Annotation; Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 274 | Prompt-Response Writer US; Copywriter (Contract); Financial Writer (Ghostwriter) Specialist |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 484 | Tercüman; Localization Specialist, Castilian Spanish; Russian Interpreter |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 586 | Search Operations Specialist - Arabic Speakin; Postdoctoral Research Fellow in Arabic Philos; Tercüman |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 496 | Virtual English as an Additional Language/Dia; Specialista Linguistico da Remoto; English Tutor |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 458 | Senior Copy Editor; Proofreader; Dual Proofreader/Document Processor (Legal Se |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 157 | Pakistani Truck-Art Triptych Design; English/German to Russian Texts; Legal Contract Drafting for Car Wash Machine  |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 154 | English/German to Russian Texts; excel dashboard developers; Legal Contract Drafting for Car Wash Machine  |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 194 | Launch Furniture Sales on Meta; Finance Scenario Tool UI/UX; Social Media Promo Editing |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 188 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 149 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 70 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 170 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 833 | 200 | 378 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 112 | 200 | 69 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `html:dataannotation` | 112 | 200 | 233 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 31 | 200 | 83 | AI Engagement Lead; Director, Investor Relations & Corporate Deve; Engagement Manager |
| ✅ ok | `greenhouse:labelbox` | 8 | 200 | 132 | Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments; Forward Deployed Research Scientist |
| ⚪ empty | `ashby:deel` | 0 | 200 | 64 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 165 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 140 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 108 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 474 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 496 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 70 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 89 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 110 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 59 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 49 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 55 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 50 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 279 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 47 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 34 | 200 | 489 | シニア3D背景アーティスト; Technical Designer – Japan & Global Game Deve; Game Designer – Japan & Global Game Developme |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 396 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 594 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 824 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 380 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 206 | 4718 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 351 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 370 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 6791 | 133429 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 222 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 57 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 218 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 49 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 53 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 50 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 89 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 49 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 59 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 90 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 65 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 91 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 49 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 275 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 486 | ServerDisconnectedError: Server disconnected |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 1018 | 162839 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 1760 | 220902 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 77 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 51 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 416 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 52 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 271 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 411 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 587 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 145 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 55 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 258 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 57 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 52 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 58 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 346 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 7 | 200 | 103 | Business Development / Sales Executive; Community & Support Intern - UAE Nationals; Internship Night - For Emirati Nationals |
| ❓ not_found | `lever:anghami` | 0 | 404 | 326 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 243 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 429 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 67 | HTTP 404 |

## remote-boards  <sub>ok 4 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:remowork-arabic` | 201 | 200 | 602 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 542 | Senior ASIC Design Engineer — AI Evaluation &; Transaction Monitoring Analyst / Financial Fr; Transaction Monitoring Analyst / Financial Fr |
| ✅ ok | `json:remote1stjobs` | 10 | 200 | 3832 | Senior Product Owner; Senior Product Marketing Manager  \| US \| Remo; GTM Enablement - Global Onboarding & Operatio |
| ✅ ok | `html:jobgether` | 8 | 200 | 281 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 213 | 79755 bytes, text/html |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 100 | HTTP 403 + challenge page |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 648 | HTTP 403 |
| 💥 error | `rss:euremotejobs` | 0 | 520 | 552 | HTTP 520 |
| 💥 error | `html:remote-co` | 0 |  | 15979 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 1915 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 291 | 385260 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 87 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 379 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 43 | 200 | 2438 | Get job alerts; Get job alerts; Head of Middle School Department &#8211; Chon |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 451 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 230 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 241 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 182 | 200 | 1465 | Openings; Search; Mercy Corps Afghanistan |
| ✅ ok | `html:impactpool-arabic` | 16 | 200 | 1160 | Arabic interpreter


IRC - International Resc; Lead Strategic Coordinator


IsDB - Islamic D; HR Administration Officer


ICRC - Internatio |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 209 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 89 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1604 | Jobs in Jordan (56); Jobs in Qatar (3); Jobs in UAE (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 131 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 112 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 181 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 249 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 369 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 81 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15627 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 421 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 654 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 683 | 372624 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 97 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 426 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 945 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 103 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 66 | 200 | 3092 | Find Jobs; Software Development Engineer in Test; Software Engineer - Embedded Systems |
| ⚪ empty | `google:jobs` | 0 | 200 | 191 | 94236 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 401 | 97 | HTTP 401 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 18 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 78 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 87 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 52 | HTTP 403 + challenge page |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 833 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 8 jobs
    ("Turing", "turing"),   # 31 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 112 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 7 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 34 jobs
    ("TransPerfect", "TransPerfect"),   # 18 jobs
```

```json
// source_registry.json additions
{"url": "https://weworkremotely.com/categories/all-other-remote-jobs.rss", "source_name": "wwr-all-other", "type": "rss"},
{"url": "https://www.workingnomads.com/api/exposed_jobs/", "source_name": "workingnomads-api", "type": "json"},
{"url": "https://www.themuse.com/api/public/jobs?page=1&category=Writing%20and%20Editing&level=Mid%20Level", "source_name": "writing-editing", "type": "json"},
{"url": "https://www.remotejobleads.com/feed/", "source_name": "remotejobleads", "type": "rss"},
{"url": "https://www.remote1stjobs.com/jobs.json", "source_name": "remote1stjobs", "type": "json"},
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
