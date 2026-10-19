# Source probe — 2026-10-19 09:11 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 46 | responded with parseable jobs → **can be added** |
| empty | 17 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 22 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 51 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 6 | DNS/TLS/timeout |

## Answer: **39 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 194 | Expansion Customer Success Manager (m/w/d); Senior Generative AI Engineer (m/w/d); Junior Customer Success Manager (m/w/d) |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 443 | Graduate Transport Planner; Key Account Manager Danish Market Native Spea; Technical Account Manager |
| ✅ ok | `baseline:wwr` | 89 | 200 | 427 | Expel: Technical Account Manager; Expel: Systems Engineer; Current: Senior Product Designer (Webflow) Te |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 172 | Conceptual Copywriter; Conceptual Art Director; Account Director |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 148 | Game Director; Creative Strategist UGC & Performance Ads (m/; MLOps Senior [Risk Team] |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 50 | Educational Lecture PowerPoint Design; Homepage CTA Button Integration; Korean Employment History Verification |
| ✅ ok | `baseline:remotive` | 12 | 200 | 108 | Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer; Remote Office Assistant |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 388 | Senior Software Engineer II Applied AI; Principal Software Engineer; Senior Sales Executive Central Region |
| ✅ ok | `precision:wwr-all-other` | 70 | 200 | 233 | Talkspace: Care Coordinator; Upstart: Compliance Manager, BSA/AML Program; Upstart: Capital Markets Manager |
| ✅ ok | `precision:workingnomads-api` | 42 | 200 | 359 | Video Creator (100% remote); Senior AI Engineer / Architect; Language specialist |
| ✅ ok | `precision:jobicy-teaching` | 22 | 200 | 481 | 1-on-1 Math Tutor for Grades 9-12; 1-on-1 Math Tutor for Grades 5-8; 1 on 1 High School Math Tutor |
| ✅ ok | `precision:remotive-translator` | 12 | 200 | 30 | Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer; Remote Office Assistant |
| ✅ ok | `precision:remotive-teacher` | 12 | 200 | 38 | Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer; Remote Office Assistant |
| ✅ ok | `precision:remotive-writer` | 12 | 200 | 59 | Software Engineer, AI Coding Tasks; Tech Lead Full-Stack Rails Engineer; Remote Office Assistant |
| ✅ ok | `precision:jobicy-translation` | 10 | 200 | 119 | Product Owner, Growth; Product Owner, Payments and Infrastructure; Strategic Sourcing Lead – Fulfillment - Mexic |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 225 | Captives Underwriter; Prompt-Response Writer US; Copywriter (Contract) |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 514 | Arabic Translator - Egyptian Dialect (Onsite); Machine Translation Post-Editor for Regional ; 葡萄牙语翻译 |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 512 | Multilingual Roles in Bulgaria (Up to €2,200/; Arabic Translator - Egyptian Dialect (Onsite); Arabic language communication Trainer |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 449 | English Language Instructor; English Language Teacher; Online English Teacher |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 446 | Editor; Editorial Associate; Proofreader |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 110 | YouTube Entertainment Video Editing ARABIC ED; Merge Excel Spreadsheets; AI Receptionist Kiosk Full-Stack Developer |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 129 | Southeast Asia Business Development Partnersh; Refine AI-Generated English Content; Cold Outreach Lead Generation Calls |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 130 | Bulk Vintage Photo Editing; Middle Grade Book Developmental Editor; Gender reveal video editing 90 seconds |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 159 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 95 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 49 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 147 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 833 | 200 | 192 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 112 | 200 | 90 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `html:dataannotation` | 112 | 200 | 498 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 29 | 200 | 55 | AI Engagement Lead; Chief of Staff (CEO's Office); Compliance Analyst |
| ✅ ok | `greenhouse:labelbox` | 7 | 200 | 95 | Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments; Forward Deployed Research Scientist |
| ⚪ empty | `ashby:deel` | 0 | 200 | 30 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 102 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 61 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 71 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 416 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 392 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 61 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 13 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 13 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 33 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 328 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 30 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 27 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 34 | 200 | 471 | シニア3D背景アーティスト; Technical Designer – Japan & Global Game Deve; Game Designer – Japan & Global Game Developme |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 420 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 438 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 420 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 407 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 118 | 4718 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 416 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 414 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 6208 | 133427 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 313 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 326 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 13 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 30 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 79 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 33 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 30 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 47 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 513 | ServerDisconnectedError: Server disconnected |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 430 | 177420 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 122 | 215096 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 80 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 379 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 143 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 415 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 701 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 30 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 98 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 191 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 52 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 81 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 374 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 9 | 200 | 92 | Business Development/ Sales Executive - EMEA ; Community & Support Intern - UAE Nationals; Internship Night - For Emirati Nationals |
| ❓ not_found | `lever:anghami` | 0 | 404 | 86 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 211 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 210 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 76 | HTTP 404 |

## remote-boards  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:remowork-arabic` | 197 | 200 | 559 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 635 | Part-Time Contract Video Producer (Line Produ; Part-Time Contract Video Producer (Line Produ; Business Analyst &#8211; AI Evaluator / AI Tr |
| ✅ ok | `html:jobgether` | 8 | 200 | 278 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 148 | 79755 bytes, text/html |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 79 | HTTP 403 + challenge page |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 488 | HTTP 403 |
| ⛔ blocked | `json:remote1stjobs` | 0 | 503 | 159 | HTTP 503 |
| 💥 error | `rss:euremotejobs` | 0 | 520 | 424 | HTTP 520 |
| 💥 error | `html:remote-co` | 0 |  | 15352 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 1871 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 154 | 387979 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 80 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 257 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 2140 | Get job alerts; Get job alerts; Head of Middle School Department &#8211; Chon |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 430 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 112 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 213 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 182 | 200 | 2340 | Openings; Search; WHO - World Health Organization |
| ✅ ok | `html:impactpool-arabic` | 14 | 200 | 702 | Arabic interpreter


IRC - International Resc; Lead Strategic Coordinator


IsDB - Islamic D; HR Administration Officer


ICRC - Internatio |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 188 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 183 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1108 | Jobs in Jordan (50); Jobs in Qatar (3); Jobs in UAE (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 54 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 88 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 135 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 143 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 310 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 83 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15146 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 0 · blocked 2 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 172 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 862 | Jobs; Jobs; Jobs |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 75 | HTTP 403 + challenge page |
| ⛔ blocked | `watch:prs` | 0 | 429 | 113 | HTTP 429 |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 362 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1658 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 126 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 63 | 200 | 609 | Find Jobs; Lead Web Designer &amp; Developer; Senior Software Engineer, AI |
| ⚪ empty | `google:jobs` | 0 | 200 | 117 | 92529 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 35 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 31 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 38 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 61 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 43 | HTTP 403 + challenge page |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 833 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 7 jobs
    ("Turing", "turing"),   # 29 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 112 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 9 jobs
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
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
