# Source probe — 2026-09-21 03:41 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 47 | responded with parseable jobs → **can be added** |
| empty | 18 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 22 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 50 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 5 | DNS/TLS/timeout |

## Answer: **40 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 250 | 200 | 124 | Enterprise Account Executive - DACH; Inside Sales Manager (m/w/d); (Senior) Talent Acquisition Manager (m/w/d) |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 483 | Senior .NET Software Engineer; Frontend Engineer; Backend Software Engineer |
| ✅ ok | `baseline:wwr` | 84 | 200 | 359 | Sezzle: Accountant; Legion: Enterprise Account Executive, West; Datadog: Developer Advocate - Service Managem |
| ✅ ok | `baseline:remotive` | 20 | 200 | 129 | Frontend Web Application Developer; Senior Shopify Developer; 🇩🇪 Kundenservice Mobilfunk Inbound - innerhal |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 647 | Norwegian Tech Linguistic Tester; Graduate Customer Success Manager; Early Childhood Teacher (PT) |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 133 | UK Public Relations Account Executive (UK Bas; Workers Compensation Claims Adjuster (Midwest; Business Operations Manager (Strategic Initia |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 65 | Casual Womenswear Copywriter Needed; Modern Curtains &amp; Drapes Design; High-End Bilingual Corporate Profile Design & |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 368 | Senior .NET Software Engineer; HR Operations Specialist; Marketing Student Assistant |
| ✅ ok | `precision:workingnomads-api` | 54 | 200 | 339 | Head of Engineering; Phone Sales Agent - Restock; Phone Sales Recovery Agent |
| ✅ ok | `precision:wwr-all-other` | 53 | 200 | 122 | Sezzle: Accountant; Sezzle: Accountant; LawnStarter: Analytics Engineering Manager, D |
| ✅ ok | `precision:jobicy-teaching` | 50 | 200 | 811 | AI Systems Engineering Expert; Early Childhood Teacher (PT); PreK Teacher |
| ✅ ok | `precision:jobicy-translation` | 36 | 200 | 728 | Translation Project Manager; Alliance Manager, Translational Medicine; Norwegian Tech Linguistic Tester |
| ✅ ok | `precision:remotive-translator` | 20 | 200 | 14 | Frontend Web Application Developer; Senior Shopify Developer; 🇩🇪 Kundenservice Mobilfunk Inbound - innerhal |
| ✅ ok | `precision:remotive-teacher` | 20 | 200 | 38 | Frontend Web Application Developer; Senior Shopify Developer; 🇩🇪 Kundenservice Mobilfunk Inbound - innerhal |
| ✅ ok | `precision:remotive-writer` | 20 | 200 | 13 | Frontend Web Application Developer; Senior Shopify Developer; 🇩🇪 Kundenservice Mobilfunk Inbound - innerhal |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 266 | Prompt-Response Writer; Underwriter - Ports & Terminals; Data Enterprise Reporter |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 353 | Arabic language translator/interpreter(Tour g; Translator; Translator |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 390 | AI Tutor - Bulgarian; Multilingual Roles in Bulgaria (Up to €2,200/; AI Tutor - Yoruba |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 364 | Certified English Language Teacher; Entry-Level English Teacher; Online English Instructor |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 382 | Copy Editor; Copy Editor; English Editor Novi Sad |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 136 | High-End Bilingual Corporate Profile Design –; English Documents Translation Needed; Translate Mystery Novel to German |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 135 | High-End Bilingual Corporate Profile Design –;  WordPress & WooCommerce Developer: Responsiv; English Documents Translation Needed |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 143 | Black-White Baby Sensory Animation; Precise After Effects Cleanup; Automated Video Creation System for YouTube |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 317 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 115 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 49 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 138 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 831 | 200 | 229 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 109 | 200 | 94 | Infrastructure Engineer ; Strategic Project Lead; Strategic Projects Lead, Deeptune |
| ✅ ok | `html:dataannotation` | 94 | 200 | 268 | Software EngineerCoding$75 – $150+ / hr312 hi; GeneralistGeneral$25 – $50 / hr452 hired rece; Data ScientistData &amp; ML$75 – $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 21 | 200 | 886 | AI Engagement Lead; Chief of Staff (CEO's Office); Client Director, Frontier Data - US |
| ✅ ok | `greenhouse:labelbox` | 10 | 200 | 102 | Accounts Payable, Spend Management Coordinato; Cyber Security Intern; Forward Deployed Engineering Manager |
| ⚪ empty | `ashby:deel` | 0 | 200 | 95 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 90 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 71 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 45 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 357 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 360 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 110 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 10 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 12 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 666 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 21 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 35 | 200 | 418 | シニア3D背景アーティスト; 3D 背景アーティスト; Game Designer – Japan & Global Game Developme |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 376 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 347 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 361 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 382 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 416 | 243547 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 358 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 331 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 2570 | 133286 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 319 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 805 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 334 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 11 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 83 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 33 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 29 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 29 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 23 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 113 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 15457 | timeout >15s |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 1 · not_found 16 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 658 | 176966 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 234 | 213024 bytes, text/html |
| ⛔ blocked | `personio:lingoda` | 0 | 429 | 824 | HTTP 429 |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 464 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 147 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 451 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 258 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 142 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 30 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 104 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 580 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 22 | 200 | 45 | Business Development/ Sales Executive - EMEA ; Community & Partnerships Manager; Community & Partnerships Manager |
| ❓ not_found | `lever:anghami` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 148 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 244 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 32 | HTTP 404 |

## remote-boards  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:remowork-arabic` | 199 | 200 | 802 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `json:remote1stjobs` | 50 | 200 | 1333 | Finance Manager (Corporate Finance); Senior Account Executive, Enterprise (Private; Senior Account Executive, Enterprise (Public  |
| ✅ ok | `html:jobgether` | 8 | 200 | 255 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 941 | 79755 bytes, text/html |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 447 | HTTP 202 + challenge page |
| ⛔ blocked | `rss:remotejobleads` | 0 | 403 | 103 | HTTP 403 + challenge page |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 107 | HTTP 403 + challenge page |
| 💥 error | `html:remote-co` | 0 |  | 15318 | timeout >15s |
| 💥 error | `html:europeremotely` | 0 |  | 361 | ClientConnectorError: Cannot connect to host europeremotely.com:443 ssl:False [Connection reset by peer] |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 1746 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 168 | 436120 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 103 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 286 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 44 | 200 | 1078 | Get job alerts; Get job alerts; English Teaching Jobs in Vietnam with VUS |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 374 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 95 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 152 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 168 | 200 | 1335 | Openings; Search; DRC - Danish Refugee Council |
| ✅ ok | `html:impactpool-arabic` | 12 | 200 | 730 | Interpreter – Arabic/Sudanese Arabic


IRC - ; Interpreter (Arabic and French)


IOM - Inter; Communications Specialist -Communications and |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 312 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 30 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 3 | 200 | 1846 | Jobs in Jordan (52); Jobs in Saudi Arabia (4); Jobs in UAE (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 165 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 31 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 111 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 220 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 294 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 91 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15803 | timeout >15s |

## academic-editing-watchers  <sub>ok 3 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:cactus` | 18 | 200 | 1919 | Employer Brand Promise; Life at CACTUS; Open Positions |
| ✅ ok | `watch:enago` | 9 | 200 | 279 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 552 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 542 | 345304 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 102 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 347 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1445 | HTTP 404 |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 64 | 200 | 376 | Find Jobs; Head of Cloud Infrastructure; Growth Product Manager |
| ⚪ empty | `google:jobs` | 0 | 200 | 94 | 92921 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 33 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 22 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 48 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 52 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 119 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 831 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 10 jobs
    ("Turing", "turing"),   # 21 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 109 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 22 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 35 jobs
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
