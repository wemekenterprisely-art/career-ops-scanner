# Source probe — 2026-10-05 03:44 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 46 | responded with parseable jobs → **can be added** |
| empty | 18 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 24 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 50 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 4 | DNS/TLS/timeout |

## Answer: **39 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 325 | 200 | 265 | Senior Concept & Strategy (Mensch); Senior Customer Success Manager - Germany; IT Systemadministrator (all genders welcome) |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 484 | Head of Operations; Junior Crypto Analyst & Trader; Enterprise Sales Development Representative |
| ✅ ok | `baseline:wwr` | 89 | 200 | 411 | AssemblyAI: Senior Research Engineer; Descript: Account Executive; AssemblyAI: Senior GTM AI Engineer |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 135 | Clinical Hub Lead; Scientific Director - Oncology; Junior Full Stack Developer (Ruby on Rails /  |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 67 | PDF Form Data Extraction; Full-Service Wedding Planning; Gesti&oacute;n Google &amp; Meta Ads |
| ✅ ok | `baseline:remotive` | 18 | 200 | 75 | Freelance Copywriter; Senior React Full-stack Developer; Senior back-end Engineer |
| ✅ ok | `baseline:jobicy` | 14 | 200 | 667 | Solutions Architect for Automotive; Large Enterprise Account Executive; Open Source Enterprise Sales / Alliances |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 370 | Senior .NET Software Engineer; HR Operations Specialist; Marketing Student Assistant |
| ✅ ok | `precision:wwr-all-other` | 67 | 200 | 134 | Jumio: Identity Strategist, EMEA; Jumio: Identity Strategist; Clover Health: Commercial Partnerships &amp;  |
| ✅ ok | `precision:workingnomads-api` | 54 | 200 | 429 | Live Photo Collection Study in India; Content Reviewer United States - English-spea; Quality Assurance Rater - Spanish (ES) |
| ✅ ok | `precision:remotive-translator` | 18 | 200 | 13 | Freelance Copywriter; Senior React Full-stack Developer; Senior back-end Engineer |
| ✅ ok | `precision:remotive-teacher` | 18 | 200 | 27 | Freelance Copywriter; Senior React Full-stack Developer; Senior back-end Engineer |
| ✅ ok | `precision:remotive-writer` | 18 | 200 | 12 | Freelance Copywriter; Senior React Full-stack Developer; Senior back-end Engineer |
| ✅ ok | `precision:jobicy-teaching` | 16 | 200 | 700 | Senior Solutions Architect - ACE; Senior Data Scientist (German-speaking); Senior Manager of AI Practice, Claude Corps |
| ✅ ok | `precision:jobicy-translation` | 12 | 200 | 757 | International SEO/AEO Manager; Freelance Paid Search Strategist Japanese - E; Marketing Operations Manager |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 328 | Underwriter - Ports & Terminals; Data Enterprise Reporter; Blending Control Technician |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 372 | Translator; Russian Interpreter; Language Assistant to Resident Twinning Advis |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 387 | Afrikaans Linguist CAT III; Jr. Language-Enabled OSINT Collector (CONUS); General Qualifications Examiner - Internation |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 381 | IGCSE English Teacher; English Online teacher; English Second Language Instructor |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 375 | Senior Copy Editor; Proofreader; Sub editor |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 152 | AI-Powered WhatsApp B2B Marketplace; Dual-Brand Rebranding  - Arabic/ English; English to Spanish Website Translation - 04/1 |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 142 | International Freelancer Lead Generation; AI-Powered WhatsApp B2B Marketplace; Dual-Brand Rebranding  - Arabic/ English |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 182 | Land Launch Event Videography; D&D Comedy Clip Editor; Audiobook Narration Editing |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 273 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 25 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 97 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 56 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 833 | 200 | 203 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 114 | 200 | 60 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `html:dataannotation` | 107 | 200 | 335 | Software EngineerCoding$40 – $150+ / hr312 hi; GeneralistGeneral$25 – $50 / hr452 hired rece; Data ScientistData &amp; ML$40 – $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 30 | 200 | 30 | AI Engagement Lead; Chief of Staff (CEO's Office); Community Manager |
| ✅ ok | `greenhouse:labelbox` | 9 | 200 | 48 | Cyber Security Intern; Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments |
| ⚪ empty | `ashby:deel` | 0 | 200 | 87 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 146 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 124 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 106 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 453 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 428 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 124 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 9 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 27 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 390 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 20 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 1 · not_found 15 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 35 | 200 | 410 | Technical Designer – Japan & Global Game Deve; Game Programmer – Japan & Global Game Develop; Game Designer – Japan & Global Game Developme |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 368 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 418 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 498 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 348 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 271 | 243556 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 323 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 343 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 2804 | 133428 bytes, text/html |
| ⛔ blocked | `html:futuregroup-careers` | 0 | 202 | 282 | HTTP 202 + challenge page |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 317 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 860 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 9 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 22 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 8285 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 23 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 31 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 21 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 19 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 206 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 1 · not_found 16 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 608 | 177423 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 55 | 214595 bytes, text/html |
| ⛔ blocked | `personio:lingoda` | 0 | 429 | 679 | HTTP 429 |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 19 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 84 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 468 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 131 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 386 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 26 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 81 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 241 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 28 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 246 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 391 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 22 | 200 | 45 | Business Development/ Sales Executive - EMEA ; Community & Partnerships Manager; Community & Partnerships Manager |
| ❓ not_found | `lever:anghami` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 257 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 246 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 36 | HTTP 404 |

## remote-boards  <sub>ok 3 · empty 1 · blocked 4 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 1609 | 200 | 451 | Account Manager - DACH; Regional Sales Director, East; Supply Category Lead, Services   |
| ✅ ok | `html:remowork-arabic` | 193 | 200 | 921 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `html:jobgether` | 8 | 200 | 258 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 219 | 79755 bytes, text/html |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 155 | HTTP 202 + challenge page |
| ⛔ blocked | `rss:remotejobleads` | 0 | 403 | 51 | HTTP 403 + challenge page |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 51 | HTTP 403 + challenge page |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 645 | HTTP 403 |
| 💥 error | `html:remote-co` | 0 |  | 15570 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2148 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 216 | 399107 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 105 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 256 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 539 | Get job alerts; Get job alerts; Head of Middle School Department &#8211; Chon |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 379 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 181 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 346 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 199 | 200 | 1368 | Openings; Search; FAO - Food and Agriculture Organization of th |
| ✅ ok | `html:impactpool-arabic` | 14 | 200 | 814 | Part Time Arabic Language Teacher


UNOG - Un; Interpreter – Arabic/Sudanese Arabic


IRC - ; Interpreter (Arabic-Turkish)


UNV - United N |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 325 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 147 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 3 | 200 | 1264 | Jobs in Jordan (61); Jobs in Saudi Arabia (2); Jobs in UAE (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 126 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 101 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 186 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 189 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 250 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 118 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15544 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 149 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 593 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 565 | 353573 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 99 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 256 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 693 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 69 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 66 | 200 | 405 | Find Jobs; Security Engineer; Senior Data Scientist, Audio |
| ⚪ empty | `google:jobs` | 0 | 200 | 86 | 93045 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 29 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 14 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 94 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 94 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 73 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 833 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 9 jobs
    ("Turing", "turing"),   # 30 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 114 jobs
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
