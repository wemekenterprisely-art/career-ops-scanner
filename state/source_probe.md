# Source probe — 2026-11-02 11:31 UTC

_Ran from: github-actions · 150 candidates · concurrency 6 · timeout 15s_

| status | count | meaning |
|---|---:|---|
| ok | 45 | responded with parseable jobs → **can be added** |
| empty | 22 | 200 but nothing parsed → wrong parser or no jobs right now |
| blocked | 18 | 403/429/999/captcha → do not scrape from this IP; use an aggregator or ATS route |
| not_found | 51 | 404/410 → slug or endpoint is wrong |
| needs_key | 8 | add the secret and re-run |
| error | 6 | DNS/TLS/timeout |

## Answer: **38 new sources responded with jobs** (+7 baseline references)

## baseline  <sub>ok 7 · empty 0 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `baseline:arbeitnow` | 300 | 200 | 201 | Senior Customer Success Manager (m/f/d); Netzwerkadministrator / IT-Systemadministrato; Senior Artist Manager / Influencer Manager (m |
| ✅ ok | `baseline:wwr` | 100 | 200 | 512 | LOTARO: Head of Lead Generation \| Remote (m/w; Smartsheet: Senior Channel Account Manager; Upgrade: Dealer Development Manager (Portland |
| ✅ ok | `baseline:remoteok` | 99 | 200 | 471 | Virtual Destination Wedding Coordinator; Virtual Scheduling Assistant; Partner Operations Manager |
| ✅ ok | `baseline:himalayas` | 20 | 200 | 161 | Director, Application Development Engineering; CX Named Account Manager \| Thailand (Virtual,; Associate Director US Oncology Marketing Pati |
| ✅ ok | `baseline:freelancer-rss` | 20 | 200 | 54 | Food Brand Social Media Photography; Comprehensive Offline Product Price Compariso; Record POV Videos for AI Training |
| ✅ ok | `baseline:remotive` | 12 | 200 | 86 | Full-Stack Developer; Senior Back-end Developer; Head of Engineering |
| ✅ ok | `baseline:jobicy` | 3 | 200 | 315 | Director of Creative Strategy; Multigres Engineer; Cloud Support Engineer |

## precision-queries  <sub>ok 6 · empty 2 · blocked 0 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `precision:remoteok-writing` | 100 | 200 | 409 | Accounting & Finance Manager; Senior Software Engineer II Applied AI; Principal Software Engineer |
| ✅ ok | `precision:wwr-all-other` | 85 | 200 | 584 | Upgrade: Dealer Development Manager (Portland; Upgrade: Dealer Development Manager (Las Vega; Glossier: Director of Co-Manufacturing &amp;  |
| ✅ ok | `precision:workingnomads-api` | 35 | 200 | 274 | Senior Magento Developer; Senior Back-end Developer; Looking For Online ESL Teachers - Remote- Joi |
| ✅ ok | `precision:remotive-translator` | 12 | 200 | 26 | Full-Stack Developer; Senior Back-end Developer; Head of Engineering |
| ✅ ok | `precision:remotive-teacher` | 12 | 200 | 25 | Full-Stack Developer; Senior Back-end Developer; Head of Engineering |
| ✅ ok | `precision:remotive-writer` | 12 | 200 | 50 | Full-Stack Developer; Senior Back-end Developer; Head of Engineering |
| ⚪ empty | `precision:jobicy-translation` | 0 | 200 | 289 | 567 bytes, application/json |
| ⚪ empty | `precision:jobicy-teaching` | 0 | 200 | 252 | 564 bytes, application/json |

## aggregator-keyed  <sub>ok 1 · empty 0 · blocked 0 · not_found 0 · needs_key 8 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `themuse:writing-editing` | 20 | 200 | 215 | Blending Control Technician; Captives Underwriter; Prompt-Response Writer US |
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
| ✅ ok | `linkedin:guest-arabic-translator` | 10 | 200 | 440 | MANDARIN TRANSLATOR; 华星-翻译类（本硕）; Mandarin Translator |
| ✅ ok | `linkedin:guest-arabic-linguist` | 10 | 200 | 431 | Content Moderator – Arabic Speaking (Open to ; 华星-翻译类（本硕）; Korean Linguistic Expert |
| ✅ ok | `linkedin:guest-esl` | 10 | 200 | 435 | Entry-Level ESOL Online Tutor (Ref:EDU0211/26; English Language teacher KS3 \| IGCSE \| A Leve; Specialista Linguistico da Remoto |
| ✅ ok | `linkedin:guest-proofreader` | 10 | 200 | 405 | Copy Editor (Remote); Copy Editor (Remote); Authored Works Review (Editor) |

## freelance  <sub>ok 3 · empty 1 · blocked 3 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `freelancer:api-arabic` | 20 | 200 | 126 | Urgent One-Page Japanese Translation required; Saudi Arabic Marketing Translator; CSV Import & Translation |
| ✅ ok | `freelancer:api-esl` | 20 | 200 | 138 | Prague Instagram Content & Meta Ads; Urgent Business Writing & Data Support; Retype Photo Pages Into PDF |
| ✅ ok | `freelancer:api-proofreading` | 20 | 200 | 115 | Retype Photo Pages Into PDF; Brand Design & Web Content; AI-Powered B2B Video Creator |
| ⚪ empty | `pph:search-arabic` | 0 | 202 | 109 | 2371 bytes, text/html |
| ⛔ blocked | `guru:arabic-translation` | 0 | 403 | 86 | HTTP 403 |
| ⛔ blocked | `workana:writing-translation` | 0 | 403 | 30 | HTTP 403 + challenge page |
| ⛔ blocked | `truelancer:arabic` | 0 | 429 | 72 | HTTP 429 |

## ats-language-ai  <sub>ok 5 · empty 6 · blocked 0 · not_found 11 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `greenhouse:agency` | 827 | 200 | 197 | 3D Modeling & Python Specialist - Freelance A; Accounting Specialist - Freelance AI Trainer ; Actuarial Science Specialist - Freelance AI T |
| ✅ ok | `html:dataannotation` | 112 | 200 | 156 | Software EngineerCodingUp to $150+ / hr312 hi; GeneralistGeneralUp to $50 / hr452 hired rece; Data ScientistData &amp; MLUp to $150+ / hr92 |
| ✅ ok | `ashby:mercor` | 108 | 200 | 78 | Software Engineer, Systems & Platform Applied; Infrastructure Software Engineer ; Strategic Project Lead |
| ✅ ok | `greenhouse:turing` | 40 | 200 | 132 | Account Director - Consumer Packaged Goods - ; AI Engagement Lead; Client Director, Financial Services (BFSI) |
| ✅ ok | `greenhouse:labelbox` | 10 | 200 | 109 | Forward Deployed Engineering Manager; Forward Deployed Engineer, RL Environments; Forward Deployed Research Scientist |
| ⚪ empty | `ashby:deel` | 0 | 200 | 65 | 28 bytes, application/json |
| ⚪ empty | `workable:prolific` | 0 | 200 | 81 | 46 bytes, application/json |
| ⚪ empty | `workable:superannotate` | 0 | 200 | 72 | 53 bytes, application/json |
| ⚪ empty | `workable:toloka` | 0 | 200 | 63 | 46 bytes, application/json |
| ⚪ empty | `smartrecruiters:TELUSInternational` | 0 | 200 | 385 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:Welocalize` | 0 | 200 | 400 | 52 bytes, application/json |
| ❓ not_found | `greenhouse:joinhandshake` | 0 | 404 | 54 | HTTP 404 |
| ❓ not_found | `greenhouse:surgeai` | 0 | 404 | 46 | HTTP 404 |
| ❓ not_found | `ashby:surgeai` | 0 | 404 | 116 | HTTP 404 |
| ❓ not_found | `greenhouse:mercor` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `ashby:micro1` | 0 | 404 | 37 | HTTP 404 |
| ❓ not_found | `ashby:pareto` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `greenhouse:superannotate` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `greenhouse:clickworker` | 0 | 404 | 40 | HTTP 404 |
| ❓ not_found | `lever:welocalize` | 0 | 404 | 296 | HTTP 404 |
| ❓ not_found | `greenhouse:welocalize` | 0 | 404 | 71 | HTTP 404 |
| ❓ not_found | `greenhouse:centific` | 0 | 404 | 44 | HTTP 404 |

## ats-lsp  <sub>ok 4 · empty 5 · blocked 0 · not_found 15 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `smartrecruiters:KeywordsStudios` | 35 | 200 | 400 | Rendering Engineer; シニア3D背景アーティスト; Technical Designer – Japan & Global Game Deve |
| ✅ ok | `smartrecruiters:TransPerfect` | 18 | 200 | 371 | Account Manager - Client Services; Spanish Quality Manager & Tester; Project Coordinator |
| ✅ ok | `html:tarjama-careers` | 5 | 200 | 547 | 07
Careers; Open on LinkedIn; View all open positions |
| ✅ ok | `html:torjoman-careers` | 2 | 200 | 508 | العربية; Careers |
| ⚪ empty | `smartrecruiters:Acolad` | 0 | 200 | 356 | 52 bytes, application/json |
| ⚪ empty | `html:transperfect-careers` | 0 | 200 | 124 | 4718 bytes, text/html |
| ⚪ empty | `smartrecruiters:Lionbridge` | 0 | 200 | 351 | 52 bytes, application/json |
| ⚪ empty | `smartrecruiters:RWS` | 0 | 200 | 369 | 52 bytes, application/json |
| ⚪ empty | `html:saudisoft-careers` | 0 | 200 | 2717 | 133429 bytes, text/html |
| ❓ not_found | `lever:unbabel` | 0 | 404 | 295 | HTTP 404 |
| ❓ not_found | `greenhouse:unbabel` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `lever:lilt` | 0 | 404 | 408 | HTTP 404 |
| ❓ not_found | `ashby:lilt` | 0 | 404 | 49 | HTTP 404 |
| ❓ not_found | `greenhouse:phrase` | 0 | 404 | 41 | HTTP 404 |
| ❓ not_found | `greenhouse:crowdin` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `lever:crowdin` | 0 | 404 | 67 | HTTP 404 |
| ❓ not_found | `greenhouse:keywordsstudios` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `greenhouse:acclaro` | 0 | 404 | 48 | HTTP 404 |
| ❓ not_found | `workable:argosmultilingual` | 0 | 404 | 52 | HTTP 404 |
| ❓ not_found | `workable:alconost` | 0 | 404 | 61 | HTTP 404 |
| ❓ not_found | `workable:straker` | 0 | 404 | 51 | HTTP 404 |
| ❓ not_found | `workable:getblend` | 0 | 404 | 48 | HTTP 404 |
| ❓ not_found | `greenhouse:languageline` | 0 | 404 | 43 | HTTP 404 |
| ❓ not_found | `greenhouse:propio` | 0 | 404 | 44 | HTTP 404 |
| 💥 error | `html:lionbridge-careers` | 0 |  | 179 | ClientResponseError: 400, message='Got more than 8190 bytes when reading: b"default-src \'self\' \'unsafe-inlin |
| 💥 error | `html:futuregroup-careers` | 0 |  | 597 | ServerDisconnectedError: Server disconnected |

## ats-edtech  <sub>ok 0 · empty 2 · blocked 0 · not_found 17 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ⚪ empty | `html:nagwa-careers` | 0 | 200 | 746 | 163016 bytes, text/html |
| ⚪ empty | `html:almentor-careers` | 0 | 200 | 1740 | 220902 bytes, text/html |
| ❓ not_found | `greenhouse:preply` | 0 | 404 | 47 | HTTP 404 |
| ❓ not_found | `lever:preply` | 0 | 404 | 1912 | HTTP 404 |
| ❓ not_found | `greenhouse:babbel` | 0 | 404 | 51 | HTTP 404 |
| ❓ not_found | `teamtailor:babbel` | 0 | 404 | 445 | HTTP 404 |
| ❓ not_found | `greenhouse:busuu` | 0 | 404 | 50 | HTTP 404 |
| ❓ not_found | `recruitee:lingoda` | 0 | 404 | 229 | HTTP 404 |
| ❓ not_found | `teamtailor:lingoda` | 0 | 404 | 513 | HTTP 404 |
| ❓ not_found | `personio:lingoda` | 0 | 404 | 513 | HTTP 404 |
| ❓ not_found | `greenhouse:cambly` | 0 | 404 | 42 | HTTP 404 |
| ❓ not_found | `lever:cambly` | 0 | 404 | 540 | HTTP 404 |
| ❓ not_found | `recruitee:novakid` | 0 | 404 | 228 | HTTP 404 |
| ❓ not_found | `workable:novakid` | 0 | 404 | 75 | HTTP 404 |
| ❓ not_found | `greenhouse:openenglish` | 0 | 404 | 45 | HTTP 404 |
| ❓ not_found | `greenhouse:engoo` | 0 | 404 | 44 | HTTP 404 |
| ❓ not_found | `workable:abwaab` | 0 | 404 | 51 | HTTP 404 |
| ❓ not_found | `lever:noonacademy` | 0 | 404 | 69 | HTTP 404 |
| ❓ not_found | `html:edraak-careers` | 0 | 404 | 509 | HTTP 404 |

## ats-mena  <sub>ok 1 · empty 0 · blocked 0 · not_found 4 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `workable:tamatem` | 11 | 200 | 60 | Business Development / Sales Executive; Community & Support Intern - UAE Nationals; Freelance Marketing Artist: Video Editor, Mot |
| ❓ not_found | `lever:anghami` | 0 | 404 | 68 | HTTP 404 |
| ❓ not_found | `recruitee:tamatem` | 0 | 404 | 231 | HTTP 404 |
| ❓ not_found | `html:mawdoo3-careers` | 0 | 404 | 266 | HTTP 404 |
| ❓ not_found | `workable:sarwa` | 0 | 404 | 46 | HTTP 404 |

## remote-boards  <sub>ok 5 · empty 1 · blocked 1 · not_found 0 · needs_key 0 · error 2</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `json:remote1stjobs` | 30281 | 200 | 2518 | Strategic Account Manager; GTM Associate; Founding Enterprise Account Executive, DACH |
| ✅ ok | `html:remowork-arabic` | 205 | 200 | 696 | Jobs; Job Tracker; Browse Job Categories |
| ✅ ok | `rss:remotejobleads` | 16 | 200 | 427 | Medical Coder / CDI Specialist &#8211; AI Eva; AI Recruiter (AIR); AI Recruiter (AIR) |
| ✅ ok | `html:jobgether` | 7 | 200 | 313 | Job search playbook; Job search playbook; Jobseekers guide |
| ✅ ok | `html:dailyremote` | 2 | 200 | 317 | Job Application Tracker; Search Jobs by Job Title |
| ⚪ empty | `html:dynamitejobs` | 0 | 200 | 146 | 79755 bytes, text/html |
| ⛔ blocked | `html:europeremotely` | 0 | 403 | 535 | HTTP 403 |
| 💥 error | `rss:euremotejobs` | 0 | 520 | 176 | HTTP 520 |
| 💥 error | `html:remote-co` | 0 |  | 15993 | timeout >15s |

## translation-boards  <sub>ok 1 · empty 2 · blocked 1 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:translationdirectory` | 2 | 200 | 2245 | Need More Linguistic Jobs?; Do you work for these translation agencies?  |
| ⚪ empty | `html:translatorscafe` | 0 | 200 | 528 | 0 bytes, text/html |
| ⚪ empty | `html:gotranscript` | 0 | 200 | 189 | 386155 bytes, text/html |
| ⛔ blocked | `html:proz-translation-jobs` | 0 | 403 | 65 | HTTP 403 + challenge page |

## esl-boards  <sub>ok 2 · empty 0 · blocked 0 · not_found 2 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:eslbase` | 40 | 200 | 2511 | Get job alerts; Get job alerts; Head of Middle School Department &#8211; Chon |
| ✅ ok | `html:eslcafe-international` | 12 | 200 | 332 | Job Center; International Job Board; Korean Job Board |
| ❓ not_found | `html:tefl-online` | 0 | 404 | 197 | HTTP 404 |
| ❓ not_found | `html:teachaway-online` | 0 | 404 | 125 | HTTP 404 |

## un-ngo  <sub>ok 2 · empty 0 · blocked 2 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:impactpool-arabic` | 11 | 200 | 1350 | Arabic interpreter


IRC - International Resc; Lead Strategic Coordinator


IsDB - Islamic D; ICLA Project Manager Palestine Gaza


NRC - N |
| ✅ ok | `html:idealist-arabic` | 8 | 200 | 298 | Find a Job; Jobs; Communications |
| ⛔ blocked | `html:unjobs-translation` | 0 | 403 | 216 | HTTP 403 + challenge page |
| ⛔ blocked | `html:untalent-arabic` | 0 | 403 | 243 | HTTP 403 + challenge page |

## mena-boards  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `html:akhtaboot-translator` | 4 | 200 | 1947 | Jobs in Jordan (55); Jobs in Qatar (3); Jobs in UAE (1) |
| ⚪ empty | `html:mostaql-writing-translation` | 0 | 202 | 375 | 2387 bytes, text/html |
| ⛔ blocked | `html:bayt-translator` | 0 | 403 | 116 | HTTP 403 + challenge page |
| ⛔ blocked | `html:wuzzuf-translator` | 0 | 403 | 80 | HTTP 403 + challenge page |
| ⛔ blocked | `html:gulftalent-translator` | 0 | 403 | 174 | HTTP 403 + challenge page |
| ⛔ blocked | `html:tanqeeb-translator` | 0 | 403 | 480 | HTTP 403 |
| ⛔ blocked | `html:ureed-translation` | 0 | 403 | 57 | HTTP 403 + challenge page |
| 💥 error | `html:naukrigulf-translator` | 0 |  | 15961 | timeout >15s |

## academic-editing-watchers  <sub>ok 2 · empty 1 · blocked 1 · not_found 2 · needs_key 0 · error 1</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `watch:enago` | 9 | 200 | 206 | Academic Editor; Reviewer and Journal Expert; Senior Scientific Editor |
| ✅ ok | `watch:papertrue` | 3 | 201 | 567 | Jobs; Jobs; Jobs |
| ⚪ empty | `watch:prs` | 0 | 200 | 813 | 369903 bytes, text/html |
| ⛔ blocked | `watch:scribbr` | 0 | 403 | 55 | HTTP 403 + challenge page |
| ❓ not_found | `watch:scribendi` | 0 | 404 | 377 | HTTP 404 |
| ❓ not_found | `watch:wordvice` | 0 | 404 | 894 | HTTP 404 |
| 💥 error | `watch:cactus` | 0 |  | 77 | ClientConnectorDNSError: Cannot connect to host www.cactusglobal.com:443 ssl:False [Name or service not known] |

## major-platforms-blocked  <sub>ok 1 · empty 1 · blocked 5 · not_found 0 · needs_key 0 · error 0</sub>

| status | id | items | http | ms | sample / detail |
|---|---|---:|---:|---:|---|
| ✅ ok | `wellfound:html` | 67 | 200 | 307 | Find Jobs; Senior Software Engineer (Rust + Python) — Cl; Senior Backend Software Engineer — Medical Da |
| ⚪ empty | `google:jobs` | 0 | 200 | 123 | 93923 bytes, text/html |
| ⛔ blocked | `indeed:html` | 0 | 403 | 25 | HTTP 403 + challenge page |
| ⛔ blocked | `indeed:rss` | 0 | 403 | 27 | HTTP 403 + challenge page |
| ⛔ blocked | `glassdoor:html` | 0 | 403 | 48 | HTTP 403 |
| ⛔ blocked | `ziprecruiter:html` | 0 | 403 | 26 | HTTP 403 + challenge page |
| ⛔ blocked | `upwork:search` | 0 | 403 | 31 | HTTP 403 + challenge page |

## Ready-to-paste config (only boards that answered with jobs)

```python
# GREENHOUSE_COMPANIES additions — 3 boards
    ("Invisible Technologies", "agency"),   # 827 jobs
    ("Labelbox / Alignerr", "labelbox"),   # 10 jobs
    ("Turing", "turing"),   # 40 jobs
```

```python
# ASHBY_COMPANIES additions — 1 boards
    ("Mercor", "mercor"),   # 108 jobs
```

```python
# WORKABLE_COMPANIES additions — 1 boards
    ("Tamatem Games", "tamatem"),   # 11 jobs
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
{"url": "https://www.remotejobleads.com/feed/", "source_name": "remotejobleads", "type": "rss"},
{"url": "https://www.remote1stjobs.com/jobs.json", "source_name": "remote1stjobs", "type": "json"},
```

## Secrets to add for the keyed aggregators

Settings → Secrets and variables → Actions → New repository secret: `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `CAREERJET_AFFID`, `JOOBLE_API_KEY`, `RAPIDAPI_KEY`, `REED_API_KEY_B64`, `RELIEFWEB_APPNAME`
