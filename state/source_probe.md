# Source probe — 2026-09-28 03:42 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 45 | responded with parseable jobs → **can be added** |
| empty | 19 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 23 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 50 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 5 | DNS/TLS/timeout |

## Answer: **38 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 325 | 200 | 331 | Group Product Manager [Klaxoon]; Backend Engineer - (Kotlin, Spring, AWS) - Be; Softwareentwickler Automatisierungstechnik /  |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 685 | Director Payment Integrity; Danish Speaking Solutions Consultant Work Sof; MecÃ¡nico Automotriz DiagnÃ³stico y Presupues |
| ✅ ok | `baseline:wwr` | 79 | 200 | 513 | Fivetran : Compensation &amp; Analytics Partn; JFrog: Strategic Account Executive; Fivetran : Analyst, GTM Analytics |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 796 | Cloud Support Engineer; Senior Software Engineer, Backend (Money Move; Engineering Manager - MLOps & Analytics |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 205 | Advisory \| Accounting \| Audit \| Tax \| Payroll; Senior Software Engineer- DSP/Wireless commun; Blockchain Developer |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 208 | Lead Generation for Accounting &amp; GST Fili; Hybrid Online Bookstore Website Build; Hens Party Photo Shoot |
| ✅ ok | `baseline:remotive` | 17 | 200 | 165 | Content Reviewer - United States; Frontend Web Application Developer; Senior Shopify Developer |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 543 | Senior .NET Software Engineer; HR Operations Specialist; Marketing Student Assistant |
| ✅ ok | `precision:wwr-all-other` | 59 | 200 | 252 | Fivetran : Compensation &amp; Analytics Partn; Fivetran : Analyst, GTM Analytics; Expel: Associate SOC Analyst |
| ✅ ok | `precision:workingnomads-api` | 54 | 200 | 724 | Beekman Social - Account Manager; Stack .NET Developer / Algorithm Engineer – B; Senior back-end Engineer |
| ✅ ok | `precision:jobicy-teaching` | 50 | 200 | 1269 | 1 on 1 High School Math Tutor (Remote in US); 1 on 1 AMC Tutor (Remote in US); 1 on 1 High School Math Tutor |
| ✅ ok | `precision:jobicy-translation` | 35 | 200 | 1122 | Alliance Manager, Translational Medicine; Translation Project Manager; Backend Engineer |
| ✅ ok | `precision:remotive-translator` | 17 | 200 | 61 | Content Reviewer - United States; Frontend Web Application Developer; Senior Shopify Developer |
| ✅ ok | `precision:remotive-teacher` | 17 | 200 | 40 | Content Reviewer - United States; Frontend Web Application Developer; Senior Shopify Developer |
| ✅ ok | `precision:remotive-writer` | 17 | 200 | 62 | Content Reviewer - United States; Frontend Web Application Developer; Senior Shopify Developer |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 275 | Data Partner - Creative Writer -  Remote - As; Prompt-Response Writer; Underwriter - Ports & Terminals |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 439 | Mandarin Translator; Business Support &amp; Translation Associate; Associate Localization Specialist - Japanese |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 486 | Tenured/Tenure-track Position in the Departme; Department of Linguistics and Asian/Middle Ea; Mandarin Translator |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 453 | English Language Instructor; Profesor De Inglés; Entry-Level English Teacher |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 351 | Proofreader, Editorial Team; Editor; English Editor (Cover Letter Required) |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 198 | German Manuals Translation & Adaptation; Complete Online Presence: Site, Logo, Content; Arabic Text Entry Specialist |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 268 | US Admin & Support Assistant; Senior Data Analytics / Digital Analytics Exp; JioMart Beauty Product Listing & Copywriter N |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 254 | Indian philosophy Research & Editing; YouTube Brand Awareness Videos; Informative Instagram Reels Creation |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 157 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 97 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 165 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 230 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 832 | 200 | 268 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `ashby:mercor` | 114 | 200 | 164 | Member of Technical Staff, Applied AI Backend; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `html:dataannotation` | 107 | 200 | 534 | Software EngineerCoding$40 – $150+ / hr312 hi; GeneralistGeneral$25 – $50 / hr452 hired rece; Data ScientistData &amp; ML$40 – $150+ / hr92 |
| ✅ ok | `greenhouse:turing` | 34 | 200 | 91 | AI Engagement Lead; Chief of Staff (CEO's Office); Client Director, Frontier Data - US |
| ✅ ok | `greenhouse:labelbox` | 10 | 200 | 165 | Cyber Security Intern; Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments |
| ⚪ empty | `ashby:deel` | 0 | 200 | 275 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 228 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 206 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 148 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 493 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 449 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 119 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 64 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 222 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 209 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 69 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 69 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 66 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 193 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 87 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 71 | HTTP 404 |

## ats-lsp  <sub>ok 3 · empty 5 · blocked 1 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 35 | 200 | 423 | シニア3D背景アーティスト; 3D 背景アーティスト; Game Designer – Japan & Global Game Developme |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 424 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 595 | 07
Careers; Open on LinkedIn; View all open positions |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 430 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 403 | 243557 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 435 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 403 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 3156 | 133287 bytes, text/html |
| ⛔ blocked | `html:futuregroup-careers` | 0 | 202 | 269 | HTTP 202 + challenge page |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 215 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 72 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 170 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 73 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 82 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 64 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 77 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 72 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 89 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 136 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 65 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 69 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 286 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:torjoman-careers` | 0 | 502 | 252 | HTTP 502 |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 1 · not_found 16 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 1602 | 177424 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 1814 | 214542 bytes, text/html |
| ⛔ blocked | `personio:lingoda` | 0 | 429 | 1018 | HTTP 429 |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 81 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 70 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 585 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 70 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 382 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 975 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 70 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 252 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 90 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 69 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 73 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 715 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 21 | 200 | 154 | Business Development/ Sales Executive - EMEA ; Community & Partnerships Manager; Community & Partnerships Manager |
| ❓ not_found | `lever:anghami` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 235 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 542 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 75 | HTTP 404 |

## remote-boards  <sub>ok 2 · empty 2 · blocked 3 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:remowork-arabic` | 198 | 200 | 877 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `html:jobgether` | 8 | 200 | 340 | Job search playbook; Job search playbook; Job search playbook |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 211 | 79755 bytes, text/html |
| ⚪ empty | `json:remote1stjobs` | 0 | 200 | 327 | 560 bytes, application/feed+json |
| ⛔ blocked | `rss:euremotejobs` | 0 | 202 | 277 | HTTP 202 + challenge page |
| ⛔ blocked | `rss:remotejobleads` | 0 | 403 | 149 | HTTP 403 + challenge page |
| ⛔ blocked | `html:dailyremote` | 0 | 403 | 146 | HTTP 403 + challenge page |
| 💥 error | `html:remote-co` | 0 |  | 15329 | timeout >15s |
| 💥 error | `html:europeremotely` | 0 |  | 370 | ClientConnectorError: Cannot connect to host europeremotely.com:443 ssl:False [Connection reset by peer] |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2417 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 368 | 436689 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 164 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 309 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 961 | Get job alerts; Get job alerts; Head of Middle School Department &#8211; Chon |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 402 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 355 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 317 | HTTP 404 |

## un-ngo  <sub>ok 3 · empty 0 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:untalent-arabic` | 185 | 200 | 1505 | Openings; Search; IOM - UN Migration |
| ✅ ok | `html:impactpool-arabic` | 12 | 200 | 1092 | Interpreter – Arabic/Sudanese Arabic


IRC - ; Interpreter (Arabic and French)


IOM - Inter; Partnerships Specialist


UNOPS - United Nati |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 403 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 127 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 0 · blocked 6 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 3 | 200 | 1818 | Jobs in Jordan (51); Jobs in UAE (1); Jobs in Saudi Arabia (1) |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 172 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 149 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 156 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 265 | HTTP 403 |
| ⛔ blocked | `html:mostaql-writing-translation` | 0 | 403 | 442 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 146 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15561 | timeout >15s |

## academic-editing-watchers  <sub>ok 3 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:cactus` | 18 | 200 | 1155 | Employer Brand Promise; Life at CACTUS; Open Positions |
| ✅ ok | `watch:enago` | 9 | 200 | 386 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 712 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 837 | 352894 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 156 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 308 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1298 | HTTP 404 |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 69 | 200 | 484 | Find Jobs; Senior Data Scientist, Audio; Director, Text-to-Speech Synthesis Research |
| ⚪ empty | `google:jobs` | 0 | 200 | 248 | 92577 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 95 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 111 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 123 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 106 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 190 | HTTP 403 |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 832 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 10 jobs
    ("Turing", "turing"),   # 34 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 114 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 21 jobs
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
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
