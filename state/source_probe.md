# Source probe — 2026-10-12 03:48 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 46 | responded with parseable jobs → **can be added** |
| empty | 17 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 23 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 52 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 4 | DNS/TLS/timeout |

## Answer: **39 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 325 | 200 | 180 | Werkstudent: in im Einkauf / Materialbeschaff; Senior Systems & Application Engineer; Cloud Engineer (m/w/d) |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 849 | Technical Account Manager; Manager Clinical Data Management; Junior Sales Development Representative IT In |
| ✅ ok | `baseline:wwr` | 89 | 200 | 588 | Descript: Brand Design Lead; Stripe: Account Executive, Product Sales - Ta; Vercel: Software Engineer - Data Platform |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 77 | Analyste marketing, Attribution - ShareGate; Creatives/Performers/Artisans/Culinary/Experi; MedTech Co-Founder / CPO (100 % remote) (m/f/ |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 138 | Video Aur Content Creator ki Talash; Accurate Product Data Website; WinOLS Automation POC |
| ✅ ok | `baseline:remotive` | 18 | 200 | 102 | Inside Sales Contractor; Tier III Service Desk Engineer; Software Engineer / AI Code Trainer (Python,  |
| ✅ ok | `baseline:jobicy` | 15 | 200 | 248 | IT Associate; Enterprise Sales VP, Labor and Trust; International Audio/Video Remote Kurdish and  |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 652 | Academic Dean for MiaPrep Online Academy of O; Senior .NET Software Engineer; HR Operations Specialist |
| ✅ ok | `precision:wwr-all-other` | 71 | 200 | 773 | Descript: Applied Research Scientist, AI Rese; Upstart: Art Director, Performance; Sezzle: Chargeback Operations Intern |
| ✅ ok | `precision:workingnomads-api` | 51 | 200 | 1155 | Senior Backend Developer (Node.js / Nest.js); Senior Backend Developer (Python); Senior Business Central Developer |
| ✅ ok | `precision:remotive-translator` | 18 | 200 | 30 | Inside Sales Contractor; Tier III Service Desk Engineer; Software Engineer / AI Code Trainer (Python,  |
| ✅ ok | `precision:remotive-teacher` | 18 | 200 | 24 | Inside Sales Contractor; Tier III Service Desk Engineer; Software Engineer / AI Code Trainer (Python,  |
| ✅ ok | `precision:remotive-writer` | 18 | 200 | 22 | Inside Sales Contractor; Tier III Service Desk Engineer; Software Engineer / AI Code Trainer (Python,  |
| ✅ ok | `precision:jobicy-translation` | 15 | 200 | 203 | Regional Sales Operations Manager - EMEA; Strategic Sourcer – Fulfillment - Brazil; Strategic Sourcer – Fulfillment - Argentina |
| ✅ ok | `precision:jobicy-teaching` | 15 | 200 | 182 | Software Engineer, AI Enablement; Work from home as a Private Online German Tut; Content Engineer, Developer Relations |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 422 | Underwriter - Ports & Terminals; Data Enterprise Reporter; Production Supervisor - 12 Hour Weekend Shift |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 375 | Arabic Language Expert; Localization Specialist - Spanish EU; Project Associate (Cultural Mediator) |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 383 | Arabic Language Expert; AI Tutor - Khmer; Localization Specialist - Spanish EU |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 412 | Senior English Instructor; Corporate Czech and English Trainer; Elementary School Teacher |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 409 | Copy Editor; Proofreader (For Lecture Publications Limited; 文案编辑 |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 204 | SaaS Document Automation Platform Development; Research Oman Company Ownership; Promo video with Arabic-aware voice-over for  |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 215 | MBA Leads at ₹20-30 Each; Female Telemarketer for Subscription Sales; Dental Tutoring with English-Speaking Graduat |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 241 | Earthmoving Attachments Shopify SEO; AI-Enhanced Educational Video Editing; Energetic Country Mashup Creation |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 92 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 42 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 50 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 60 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 833 | 200 | 180 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 116 | 200 | 59 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `html:dataannotation` | 112 | 200 | 427 | Software EngineerCoding$40 – $150+ / hr312 hi; GeneralistGeneral$25 – $50 / hr452 hired rece; Data ScientistData &amp; ML$40 – $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 29 | 200 | 49 | AI Engagement Lead; Chief of Staff (CEO's Office); Community Manager |
| ✅ ok | `greenhouse:labelbox` | 8 | 200 | 47 | Cyber Security Intern; Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments |
| ⚪ empty | `ashby:deel` | 0 | 200 | 22 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 139 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 128 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 108 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 479 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 456 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 38 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 143 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 107 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 3288 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 40 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 40 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 1 · not_found 15 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 35 | 200 | 427 | シニア3D背景アーティスト; Technical Designer – Japan & Global Game Deve; Game Programmer – Japan & Global Game Develop |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 420 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 332 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 951 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 400 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 96 | 243555 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 412 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 395 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 3049 | 133429 bytes, text/html |
| ⛔ blocked | `html:futuregroup-careers` | 0 | 202 | 85 | HTTP 202 + challenge page |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 87 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 40 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 83 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 38 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 44 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 93 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 97 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 90 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 96 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 38 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 705 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 1961 | 177425 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 1740 | 215348 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 25 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 449 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 199 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 497 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 864 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 2381 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 213 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 97 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 39 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 88 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 1911 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 1106 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 22 | 200 | 179 | Business Development/ Sales Executive - EMEA ; Community & Partnerships Manager; Community & Partnerships Manager |
| ❓ not_found | `lever:anghami` | 0 | 404 | 24 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 188 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 438 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 96 | HTTP 404 |

## remote-boards  <sub>ok 3 · empty 1 · blocked 4 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 1609 | 200 | 715 | Account Manager - DACH; Regional Sales Director, East; Supply Category Lead, Services   |
| ✅ ok | `html:remowork-arabic` | 192 | 200 | 1020 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `html:jobgether` | 9 | 200 | 338 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 267 | 79755 bytes, text/html |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 674 | HTTP 202 + challenge page |
| ⛔ blocked | `rss:remotejobleads` | 0 | 403 | 119 | HTTP 403 + challenge page |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 70 | HTTP 403 + challenge page |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 700 | HTTP 403 |
| 💥 error | `html:remote-co` | 0 |  | 15450 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2392 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 412 | 399108 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 59 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 357 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 4766 | Get job alerts; Get job alerts; Teach English in Taiwan! (Tainan City) |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 172 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 484 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 208 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 218 | 200 | 1631 | Openings; Search; CHAI - Clinton Health Access Initiative |
| ✅ ok | `html:impactpool-arabic` | 13 | 200 | 981 | Part Time Arabic Language Teacher


UNOG - Un; Arabic editor individual contractor


UNEP - ; Job is closed:
Interpreter (Arabic-Turkish)

 |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 191 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 268 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 5 · not_found 1 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 3 | 200 | 1696 | Jobs in Jordan (55); Jobs in UAE (1); Jobs in Saudi Arabia (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 108 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 90 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 105 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 344 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 418 | HTTP 403 |
| ❓ not_found | `html:ureed-translation` | 0 | 404 | 1640 | HTTP 404 |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15626 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 0 · blocked 2 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 407 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 413 | Jobs; Jobs; Jobs |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 49 | HTTP 403 + challenge page |
| ⛔ blocked | `watch:prs` | 0 | 429 | 120 | HTTP 429 |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 457 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 992 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 229 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 66 | 200 | 443 | Find Jobs; Senior Site Reliability Engineer II; Director, Engineering (Platform) |
| ⚪ empty | `google:jobs` | 0 | 200 | 141 | 92794 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 25 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 36 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 40 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 38 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 69 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 833 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 8 jobs
    ("Turing", "turing"),   # 29 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 116 jobs
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
