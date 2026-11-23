# Source probe — 2026-11-23 13:26 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 49 | responded with parseable jobs → **can be added** |
| empty | 19 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 16 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 53 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 5 | DNS/TLS/timeout |

## Answer: **42 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 171 | Working Student, Export Control/ Internationa; Senior Sales Manager, Regional Enterprise; Business Development Representative (German s |
| ✅ ok | `baseline:remoteok` | 100 | 200 | 429 | Product Manager, Developer Ecosystem; Manager, Technical Accounting and Equity Repo; Senior SRE, Site Experience |
| ✅ ok | `baseline:wwr` | 100 | 200 | 582 | Affirm: Analytics Lead, Full Stack; Oportun: Senior Manager, Risk Strategy (R1434; Coinbase: Compliance, Senior Associate |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 1472 | Business Development Representative; Business Services Team Manager; Cloud Platform Engineer |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 83 | Hematology Physician; Medical Oncologist; Pediatric Hematology/Oncology Physician |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 75 | Money and work; Promote Global Export Accelerator Program; LIANZA &mdash; Sito web multilingue e piattaf |
| ✅ ok | `baseline:remotive` | 16 | 200 | 59 | Content Reviewer - United States; Tech Lead Full-Stack Rails Engineer; Content Creator - YouTube |

## precision-queries  <sub>ok 7 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:wwr-all-other` | 118 | 200 | 343 | Oportun: Senior Manager, Risk Strategy (R1434; Coinbase: Compliance, Senior Associate; Talkspace: General Application for Clinical a |
| ✅ ok | `precision:remoteok-writing` | 40 | 200 | 368 | Business Development Specialist Arabic speake; Technical Lead Norm Compliance; Research Engineer Privacy and Anonymization |
| ✅ ok | `precision:workingnomads-api` | 37 | 200 | 97 | Looking For Online ESL Teachers - Remote- Joi; Case Manager (Philippines); Content Reviewer - United States |
| ✅ ok | `precision:jobicy-translation` | 28 | 200 | 164 | Sr. Clinical Research Associate (Brazil); English to Belarusian Review Lead for UI, Mar; Sr. Marketing Designer |
| ✅ ok | `precision:remotive-translator` | 16 | 200 | 14 | Content Reviewer - United States; Tech Lead Full-Stack Rails Engineer; Content Creator - YouTube |
| ✅ ok | `precision:remotive-teacher` | 16 | 200 | 26 | Content Reviewer - United States; Tech Lead Full-Stack Rails Engineer; Content Creator - YouTube |
| ✅ ok | `precision:remotive-writer` | 16 | 200 | 44 | Content Reviewer - United States; Tech Lead Full-Stack Rails Engineer; Content Creator - YouTube |
| ⛔ blocked | `precision:jobicy-teaching` | 0 | 429 | 184 | HTTP 429 |

## aggregator-keyed  <sub>ok 0 · empty 0 · blocked 0 · not_found 1 · needs_key 8 · error 0</sub>

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
| ❓ not_found | `themuse:writing-editing` | 0 | 404 | 125 | HTTP 404 |

## linkedin  <sub>ok 4 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 464 | Mediatrice/mediatore linguistico culturale ar; Junior Project Support Specialist with Foreig; Translator |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 462 | Junior Project Support Specialist with Foreig; Mediatrice/mediatore linguistico culturale ar; CAT II Spanish Linguist |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 437 | English Instructors; Specialista Linguistico da Remoto; English Tutor |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 493 | Copy Editor – English Books; Content Editor; Chief Sub Editor (News)- English |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 124 | Spanish lawyer to file monitorio opposition, ; Website Copy Audit & Rewrite; Bilingual Web Developer Partner Needed |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 147 | shree ji handicraf; Food Review Reels Editor; 2d ai music video |
| ✅ ok | `workana:writing-translation` | 2 | 200 | 224 | Freelance Jobs; Writing &amp; Translation |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 116 | 2371 bytes, text/html |
| ⛔ blocked | `freelancer:api-arabic` | 0 | 200 | 112 | HTTP 200 + challenge page |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 44 | HTTP 403 |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 133 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 827 | 200 | 234 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `html:dataannotation` | 133 | 200 | 125 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `ashby:mercor` | 108 | 200 | 90 | Strategic Project Lead; Strategic Projects Lead, Deeptune; Administrative Generalist |
| ✅ ok | `greenhouse:turing` | 31 | 200 | 47 | AI Engagement Lead; Client Director, Financial Services (BFSI); Client Engagement Lead - Pharma & Life Scienc |
| ✅ ok | `greenhouse:labelbox` | 13 | 200 | 92 | Director of Marketing; Forward Deployed Engineer, Enterprise Account; Forward Deployed Engineering Manager |
| ⚪ empty | `ashby:deel` | 0 | 200 | 59 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 81 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 80 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 70 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 378 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 359 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 50 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 49 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 789 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 24 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 28 | 200 | 375 | Rendering Engineer; シニア3D背景アーティスト; 3D 背景アーティスト |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 382 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 123 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 484 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 349 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 150 | 5576 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 383 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 353 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 5326 | 133428 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 318 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 314 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 14 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 285 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 39 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 24 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 25 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 531 | ServerDisconnectedError: Server disconnected |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 1073 | 166619 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 192 | 220847 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 149 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 340 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 126 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 400 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 500 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 181 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 33 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 30 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 81 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 207 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 8 | 200 | 40 | AI Artist; AI Artist; AI Artist |
| ❓ not_found | `lever:anghami` | 0 | 404 | 91 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 132 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 157 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 31 | HTTP 404 |

## remote-boards  <sub>ok 5 · empty 1 · blocked 1 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 34274 | 200 | 3530 | Medical Editor - Market Access Marketing; Account Executive, Healthcare and Pharmaceuti; Digital Onboarding Specialist I - Lisbon / Ma |
| ✅ ok | `html:remowork-arabic` | 208 | 200 | 937 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 442 | Legal Expert (Employment &#038; Labor); Paralegal (General); STEM / Quant Bachelor |
| ✅ ok | `html:jobgether` | 8 | 200 | 298 | Job search playbook; Job search playbook; Job search playbook |
| ✅ ok | `html:dailyremote` | 2 | 200 | 125 | Job Application Tracker; Search Jobs by Job Title |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 181 | 79774 bytes, text/html |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 484 | HTTP 403 |
| 💥 error | `rss:euremotejobs` | 0 | 520 | 186 | HTTP 520 |
| 💥 error | `html:remote-co` | 0 |  | 15404 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 1807 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 124 | 391820 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 52 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 276 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 2211 | Get job alerts; Get job alerts; Teachers Needed in Budapest for Pre-School, P |
| ✅ ok | `html:eslcafe-international` | 8 | 200 | 404 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 134 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 179 | HTTP 404 |

## un-ngo  <sub>ok 4 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 186 | 200 | 1127 | Openings; Search; WVI - World Vision International |
| ✅ ok | `html:impactpool-arabic` | 14 | 200 | 848 | Arabic Language Interpreter


IRC - Internati; Interpreter (Arabic-French)


IOM - Internati; Closing today:
Global Roving and Emergency Re |
| ✅ ok | `html:unjobs-translation` | 4 | 200 | 1105 | Roster - Conference Interpreter, Geneva, Swit; Linguist Talent Pool, London, United Kingdom; Register as a Conference and Language Service |
| ✅ ok | `html:idealist-arabic` | 4 | 200 | 260 | Find a Job; Jobs; Find a Job |

## mena-boards  <sub>ok 1 · empty 1 · blocked 4 · not_found 1 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1874 | Jobs in Jordan (36); Jobs in Saudi Arabia (6); Jobs in Qatar (3) |
| ⚪ empty | `html:mostaql-writing-translation` | 0 | 202 | 628 | 2387 bytes, text/html |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 96 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 60 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 163 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 158 | HTTP 403 |
| ❓ not_found | `html:ureed-translation` | 0 | 404 | 2412 | HTTP 404 |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15934 | timeout >15s |

## academic-editing-watchers  <sub>ok 4 · empty 1 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:cactus` | 18 | 200 | 1387 | Employer Brand Promise; Life at CACTUS; Open Positions |
| ✅ ok | `watch:enago` | 9 | 200 | 221 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:scribbr` | 7 | 200 | 79 | Jobs; Jobs; Jobs |
| ✅ ok | `watch:papertrue` | 3 | 201 | 505 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 397 | 386364 bytes, text/html |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 373 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1372 | HTTP 404 |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 68 | 200 | 302 | Find Jobs; Senior Security Engineer - Corporate Security; Senior Security Platform Engineer - Secure De |
| ⚪ empty | `google:jobs` | 0 | 200 | 114 | 93784 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 26 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 18 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 23 | HTTP 403 + challenge page |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 63 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 56 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 827 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 13 jobs
    ("Turing", "turing"),   # 31 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 108 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 8 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 28 jobs
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
