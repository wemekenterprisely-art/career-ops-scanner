# Source probe — 2026-11-09 11:56 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 46 | responded with parseable jobs → **can be added** |
| empty | 19 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 18 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 52 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 7 | DNS/TLS/timeout |

## Answer: **39 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 375 | Werkstudent (m/w/d) - Karriereberatung, Coach; Mitarbeiter in der Kundenberatung (m/w/d) - o; Social Media Manager:in (Werkstudium oder Pra |
| ✅ ok | `baseline:wwr` | 100 | 200 | 1066 | Midi Health: Nurse Practitioner - Arizona (AZ; True Talent Solutions Partners: Strategic Pro; Dimont &amp; Associates, LLC: Hazard Claims A |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 733 | Account Executive Enterprise; AI Developer; Junior Market Analyst |
| ✅ ok | `baseline:jobicy` | 20 | 200 | 557 | Devices & IOT Field Engineering Manager; Early Childhood Teacher; Senior Product Designer, Design Systems |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 268 | Account Development; Senior Director of Experience Design; Sr. Engineer - Packaging Execution (CA Based  |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 107 | Collaboration Opportunity &ndash; Revenue Sha; Editor Video Pendek Sosial Media; Filipino High-Ticket Sales Closer |
| ✅ ok | `baseline:remotive` | 12 | 200 | 197 | Tier III Service Desk Engineer; US Remote Patient Care Advocate (Customer Ser; Freelance Writer |

## precision-queries  <sub>ok 8 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 2286 | AI Content Reviewer Video Annotation; Paid Media Manager US ; Senior Software Engineer II Applied AI |
| ✅ ok | `precision:wwr-all-other` | 99 | 200 | 337 | Midi Health: Nurse Practitioner - Arizona (AZ; Photon Medical Group: Remote Nurse Practition; NM MITCHELL CONSULTANCY LTD: Remote Schedulin |
| ✅ ok | `precision:jobicy-translation` | 50 | 200 | 1129 | Talent Pool: Romansh Speakers (Switzerland); Spanish Patent Language Lead; Spanish (Spain) to English Pharmacovigilance  |
| ✅ ok | `precision:jobicy-teaching` | 23 | 200 | 784 | Manager of Implementations, High Touch - EMEA; Senior Application Security Analyst; Product Support Analyst |
| ✅ ok | `precision:workingnomads-api` | 18 | 200 | 508 | New Business Manager; AI Content Reviewer, Video Annotation; Technical Operations Lead |
| ✅ ok | `precision:remotive-translator` | 12 | 200 | 60 | Tier III Service Desk Engineer; US Remote Patient Care Advocate (Customer Ser; Freelance Writer |
| ✅ ok | `precision:remotive-teacher` | 12 | 200 | 176 | Tier III Service Desk Engineer; US Remote Patient Care Advocate (Customer Ser; Freelance Writer |
| ✅ ok | `precision:remotive-writer` | 12 | 200 | 55 | Tier III Service Desk Engineer; US Remote Patient Care Advocate (Customer Ser; Freelance Writer |

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
| ⛔ blocked | `themuse:writing-editing` | 0 | 403 | 171 | HTTP 403 + challenge page |

## linkedin  <sub>ok 4 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 358 | Site Mandarin Translator; 华星-翻译类（本硕）; Indonesian-Mandarin Translator |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 371 | Junior/ Middle Specialist with Portuguese &am; Subject Matter Expert Manager, Domain Expert ; Associate Language Specialist – Spanish IRC30 |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 519 | English Instructor; Online Evening English Language Teacher; Entry-Level ESL Online Tutor (Ref:EDU911/26) |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 373 | Telugu Proofreader; Proofreader; Redaktor / Korektor |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 180 | Amharic to English Legal Translation - 09/11/; Oromo Interview Audio Transcription; Technical SEO Audit & Fixes for Salla E-comme |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 191 | Amharic to English Legal Translation - 09/11/; Filipino High-Ticket Sales Closer; Review : Green Synthesis Nanomaterials and it |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 190 | Video editing; Professional Social Media Video Editor - 09/1; Long-Term Sports Reels Editor |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 233 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 120 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 177 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 133 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 827 | 200 | 253 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `html:dataannotation` | 133 | 200 | 178 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `ashby:mercor` | 91 | 200 | 95 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `greenhouse:turing` | 47 | 200 | 59 | Account Director, Enterprise AI - Consumer Pa; Account Executive, Frontier AI; AI Engagement Lead |
| ✅ ok | `greenhouse:labelbox` | 10 | 200 | 83 | Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments; Forward Deployed Research Scientist |
| ⚪ empty | `ashby:deel` | 0 | 200 | 121 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 192 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 121 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 131 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 491 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 461 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 34 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 165 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 114 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 95 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 34 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 38 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 262 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 36 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 36 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 31 | 200 | 470 | Rendering Engineer; シニア3D背景アーティスト; Technical Designer – Japan & Global Game Deve |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 446 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 513 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 903 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 425 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 323 | 5576 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 371 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 434 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 6170 | 133427 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 104 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 32 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 92 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 56 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 38 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 18 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 110 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 97 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 102 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 97 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 36 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 36 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 488 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 406 | ServerDisconnectedError: Server disconnected |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 2450 | 163019 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 1862 | 220902 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 39 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 180 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 552 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 34 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 246 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 528 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 804 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 34 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 1456 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 261 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 95 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 35 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 105 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 98 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 508 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 10 | 200 | 126 | AI Artist; AI Artist; Community & Support Intern - UAE Nationals |
| ❓ not_found | `lever:anghami` | 0 | 404 | 20 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 294 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 607 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 117 | HTTP 404 |

## remote-boards  <sub>ok 5 · empty 1 · blocked 0 · not_found 0 · needs_key 0 · error 3</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 34776 | 200 | 3599 | Business Development Manager, Custom Assay Se; Business Development Manager, Immunoassays & ; Business Development Manager, Immunoassays &  |
| ✅ ok | `html:remowork-arabic` | 212 | 200 | 921 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 632 | Digital Designer; Cloud Network Engineer; Python/GenAI Engineer |
| ✅ ok | `html:jobgether` | 6 | 200 | 339 | Job search playbook; Jobseekers guide; Review Jobgether &nbsp;→ |
| ✅ ok | `html:dailyremote` | 2 | 200 | 260 | Job Application Tracker; Search Jobs by Job Title |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 794 | 79774 bytes, text/html |
| 💥 error | `rss:euremotejobs` | 0 | 520 | 359 | HTTP 520 |
| 💥 error | `html:remote-co` | 0 |  | 15580 | timeout >15s |
| 💥 error | `html:europeremotely` | 0 |  | 530 | ClientConnectorError: Cannot connect to host europeremotely.com:443 ssl:False [Connection reset by peer] |

## translation-boards  <sub>ok 1 · empty 1 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2344 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 455 | 387747 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 145 | HTTP 403 + challenge page |
| ⛔ blocked | `html:translatorscafe` | 0 | 403 | 424 | HTTP 403 |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 42 | 200 | 2615 | Get job alerts; Get job alerts; Director of Studies needed for language schoo |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 469 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 406 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 450 | HTTP 404 |

## un-ngo  <sub>ok 2 · empty 0 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:impactpool-arabic` | 18 | 200 | 1001 | Arabic interpreter


IRC - International Resc; Administration Associate


UNOPS - United Nat; Diaspora Engagement Project Associate


UNV - |
| ✅ ok | `html:idealist-arabic` | 4 | 200 | 218 | Find a Job; Jobs; Find a Job |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 57 | HTTP 403 + challenge page |
| ⛔ blocked | `html:untalent-arabic` | 0 | 403 | 138 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 1 · blocked 4 · not_found 1 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 2412 | Jobs in Jordan (53); Jobs in Saudi Arabia (6); Jobs in Qatar (3) |
| ⚪ empty | `html:mostaql-writing-translation` | 0 | 202 | 451 | 2387 bytes, text/html |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 214 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 198 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 129 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 695 | HTTP 403 |
| ❓ not_found | `html:ureed-translation` | 0 | 404 | 3300 | HTTP 404 |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15121 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 585 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 491 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 383 | 383270 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 120 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 470 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 1011 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 205 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 66 | 200 | 391 | Find Jobs; Software Engineer - Embedded Systems (Cleared; Software Engineer - Embedded Systems |
| ⚪ empty | `google:jobs` | 0 | 200 | 132 | 94233 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 47 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 35 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 44 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 74 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 80 | HTTP 403 + challenge page |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 827 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 10 jobs
    ("Turing", "turing"),   # 47 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 91 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 10 jobs
```

```python
# SMARTRECRUITERS_COMPANIES additions — 2 boards
    ("Keywords Studios", "KeywordsStudios"),   # 31 jobs
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
