---
version: "1.0"
name: "Northstar Health Partners"
slug: northstar-health-partners
aliases:
  - NHP
  - Northstar
  - Northstar Health
health: red
tier: enterprise
privacy: full
owner: rachel
website: northstarhp.com
city: Pittsburgh
state: PA
country: US
industry: healthcare
source: outbound
start_date: 2023-01-15
renewal_date: 2026-07-15
currency: USD
mrr: 416
arr: 4992
seats: 45
fiscal_year_end: "2026-09-30"
budget_window:
  - 7
  - 8
  - 9
parent: null
children:
  - northstar-western-pa-clinics
  - northstar-central-pa-clinics
contacts:
  - name: Dr. Rachel Ong
    role: executive
    email: r.ong@northstarhp.com
    last_contacted: 2026-04-14
    title: Chief Medical Officer
    notes: Has not responded to the post-mortem email. Kevin says route through Diana, not directly.
  - name: Kevin Marshall
    role: decision-maker
    email: k.marshall@northstarhp.com
    last_contacted: 2026-04-20
    title: VP of Operations
    notes: Supportive but cannot block the board-mandated competitive evaluation.
  - name: Diana Reeves
    role: champion
    email: d.reeves@northstarhp.com
    last_contacted: 2026-04-19
    title: Compliance Manager
  - name: Carlos Fuentes
    role: day-to-day
    email: c.fuentes@northstarhp.com
    last_contacted: 2026-03-25
    title: Compliance Analyst
  - name: Anil Sharma
    role: technical
    email: a.sharma@northstarhp.com
    last_contacted: 2026-03-12
    title: IT Director
    notes: Primary contact for the API integration. Handled the March 12 outage response on their side.
external_ids:
  hubspot: "HS-10284"
  stripe: "cus_Wx7nPq3Km8"
  database: "acct-0009"
  jira: "NHP"
tags:
  - enterprise
  - healthcare
  - renewal-risk
  - escalation-active
  - competitor-evaluation
---

## HEAD

Northstar Health Partners is a regional healthcare network operating 12 clinics and 2 hospitals across western Pennsylvania. 430 employees. They use the product for compliance tracking and staff credentialing workflows across all facilities.

**Why they use us:** "We had three compliance violations in 2022 because credentials expired and nobody caught it. The state audit was a wake-up call. We needed a system that tracks deadlines and sends alerts without someone babysitting a spreadsheet." (Kevin Marshall, December 2022 sales call)

**How they found us:** Outbound. Rachel cold-emailed Kevin after seeing a state compliance bulletin listing Northstar. Kevin took a demo within a week. Champion (Diana) was assigned during onboarding and has been the internal driver since.

**Configuration:** Enterprise plan, 45 seats (12 clinic managers + 28 department leads + 5 compliance team). SSO via Okta. API integration with their HRIS (ADP Workforce Now). Custom compliance calendar built during onboarding.

---

## BODY

### Signal Log

| Date | Source | Category | Signal | Confidence |
|---|---|---|---|---|
| 2026-04-20 | call | competitor | Kevin: "The board asked us to evaluate two other vendors before renewal. I'm not driving it, but I can't block it." | verified |
| 2026-04-20 | call | escalation | Kevin raised the API outage from March 12 again. "That one cost us a full day of manual work across 4 clinics. Rachel heard about it." | verified |
| 2026-04-14 | email | escalation | Diana forwarded an internal email chain. Dr. Ong (CMO) wrote: "I need to understand why this system went down during credentialing week. Get me a root cause by Friday." | verified |
| 2026-03-12 | incident | bug | API integration with ADP went down for 9 hours. Credentialing sync failed across all facilities. Root cause: our API rate limiter triggered on bulk sync. Resolved same day. Post-mortem sent March 14. | verified |
| 2026-03-01 | usage | sentiment | February active users: 42 of 45 (93%). Highest engagement month in 12 months. Compliance audit season drives usage. | verified |
| 2026-01-22 | call | renewal | Kevin: "Renewal should be fine. Budget is approved for next year. Diana will handle the paperwork." (Pre-outage.) | single-source |
| 2025-11-10 | call | feature-request | Diana requested automated state-specific compliance calendar updates. "Every time Pennsylvania changes a deadline, someone has to manually update the system." | corroborated |
| 2025-09-15 | qbr | expansion | Diana presented internally to add dental clinics (3 locations, ~15 seats). Board deferred to 2026 budget cycle. | corroborated |
| 2025-07-15 | call | renewal | Renewed. Kevin: "You've saved us from two potential violations. That's worth more than the contract." | verified |
| 2025-03-20 | call | sentiment | Diana: "The compliance team doesn't know how we lived without this." | verified |

### Renewal History

| Cycle | Outcome | Seats | Notes |
|---|---|---|---|
| 2025-07 | Renewed | 45 | Added 10 seats (from 35). Diana drove expansion to department leads. Kevin signed without negotiation. |
| 2024-01 | Renewed | 35 | Added 5 seats. Smooth renewal. |
| 2023-01 | New | 30 | 60-day pilot. Converted after catching an expired credential that would have triggered state audit. |

### Usage Summary (Q1 2026)

- Active users: 42 of 45 seats (93%)
- Compliance items tracked: 1,247 (up 18% YoY)
- Last login by Diana: April 19, 2026
- Last login by Kevin: April 20, 2026
- API calls (ADP integration): 12,400/month average

### Support History

- Q1 2026: 1 critical incident (API outage, 9 hours, resolved same day). Post-mortem delivered.
- 2025: 4 tickets total. All resolved within 48 hours. No critical incidents.
- Lifetime: generally low-touch except for the March 2026 incident.

---

## FOOTER

### Renewal Status

**Next renewal:** 2026-07-15
**Status:** At risk. Board-mandated competitive evaluation in progress. API outage on March 12 escalated to CMO (Dr. Ong). Kevin is supportive but cannot block the evaluation.

**Health changed to red** on April 20, 2026. Triggers: confirmed competitor evaluation (verified) + unresolved executive escalation (verified) + two escalation signals within 40 days (sustained pattern).

### Active Threads

| Thread | Status | Key People | Next Step | Deadline | Ref |
|---|---|---|---|---|---|
| Competitive evaluation response | In progress | Kevin, Diana, Rachel | Ask Diana what vendors are being evaluated. Understand competitive set. | May 1 | [call-2026-04-20.md](notes/call-2026-04-20.md) |
| Dr. Ong escalation response | Waiting | Kevin, Rachel | Kevin to confirm whether Rachel should email Dr. Ong directly or route through Diana. Draft ready. | April 25 | [email-2026-04-14.md](notes/email-2026-04-14.md) |
| Auto compliance calendar feature | Waiting | Diana, Product | On roadmap for Q3 2026. Diana's top feature request. | Q3 2026 | [FEAT-267](https://jira.example.com/FEAT-267) |
| Dental clinic expansion | Waiting | Diana, Kevin | Board deferred to 2026. Now complicated by competitive evaluation. Do not pitch until renewal is secure. | Post-renewal | [qbr-2025-09-15.md](notes/qbr-2025-09-15.md) |

### Open Commitments

| Commitment | Made by | Date | Status |
|---|---|---|---|
| Root cause analysis for March 12 API outage | Engineering | 2026-03-14 | Delivered. Post-mortem sent. Kevin acknowledged. Dr. Ong has not responded. |
| Rate limiter fix to prevent recurrence | Engineering | 2026-03-20 | Delivered. Deployed March 25. Monitoring confirms no recurrence. |
| Automated state compliance calendar updates | Product team | 2025-11-15 | Open. On roadmap for Q3 2026. Diana's top feature request. |
| Formal response to Dr. Ong's root cause request | Rachel | 2026-04-14 | Open. Draft ready. Waiting for Kevin to confirm routing. |

### Expansion Opportunities

- **Dental clinics (3 locations, ~15 seats):** Board deferred to 2026 budget. Now complicated by competitive evaluation. Do not pitch until renewal is secure.

### Watch Items

- **Critical (renewal blocker):** The competitive evaluation is board-driven, not Kevin-driven. Kevin and Diana are allies but cannot override the board. The March 12 outage is the catalyst. Even if the technical fix is deployed, Dr. Ong's confidence must be restored.
- **Action needed by April 25:** Get Kevin's guidance on the Dr. Ong response. Either (a) email Dr. Ong directly with a formal incident summary + prevention measures, or (b) give Diana the materials to present internally. Kevin decides the routing.
- **Action needed by May 1:** Ask Diana what vendors are being evaluated. Understanding the competitive set determines the retention strategy.
- **Monitor:** If competitive evaluation selects a finalist other than us by May 15, prepare a retention package: 12-month price lock + dedicated CSM + SLA guarantee on API uptime.
