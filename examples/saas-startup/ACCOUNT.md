---
version: "1.0"
name: "Pinnacle Logistics"
slug: pinnacle-logistics
aliases:
  - PL
  - Pinnacle
  - Pinnacle Ops
health: yellow
tier: team
privacy: full
owner: james
website: pinnaclelogistics.com
city: Portland
state: OR
country: US
industry: logistics
source: referral
start_date: 2024-06-10
renewal_date: 2026-06-10
currency: USD
mrr: 82
arr: 984
seats: 18
fiscal_year_end: "2026-12-31"
budget_window:
  - 10
  - 11
parent: null
children: []
contacts:
  - name: Laura Whitfield
    role: decision-maker
    email: l.whitfield@pinnaclelogistics.com
    last_contacted: 2026-04-15
    title: VP of Operations
  - name: Derek Nunez
    role: champion
    email: d.nunez@pinnaclelogistics.com
    last_contacted: 2026-04-08
    title: Director of Warehouse Operations
    notes: Leaving June 30 for a VP role at another company. Was our internal driver since day one.
  - name: Amy Liu
    role: day-to-day
    email: a.liu@pinnaclelogistics.com
    last_contacted: 2026-04-02
    title: Operations Coordinator
  - name: Tom Bakker
    role: technical
    email: t.bakker@pinnaclelogistics.com
    last_contacted: 2026-02-20
    title: IT Manager
external_ids:
  hubspot: "HS-94721"
  stripe: "cus_Lk9m2Rp4Xv"
  database: "acct-0118"
tags:
  - usage-declining
  - champion-at-risk
  - renewal-risk
---

## HEAD

Pinnacle Logistics is a mid-size warehousing and fulfillment company based in Portland, OR, operating 11 facilities across the Pacific Northwest. They manage last-mile delivery for approximately 40 e-commerce brands.

**Why they use us:** "We were doing exception tracking on paper and in spreadsheets. By the time someone flagged a stuck shipment, the customer had already called to complain. We needed one place where the whole team could see what's stuck in real time." (Laura Whitfield, June 2024 onboarding call)

**How they found us:** Referral from Derek Nunez, who used the product at his previous company (Cascade Fulfillment). Derek joined Pinnacle as Director of Warehouse Operations in March 2024 and brought the recommendation to Laura.

**Configuration:** Team plan, 18 seats (11 facility managers + 5 shift leads + 2 ops coordinators). SSO via Google Workspace. API integration with ShipStation for automated exception imports. No custom integrations.

---

## BODY

### Signal Log

| Date | Source | Category | Signal | Confidence |
|---|---|---|---|---|
| 2026-04-10 | standup | champion-change | Derek accepted a VP role at another company. Last day is June 30. No successor named for his role. | verified |
| 2026-04-02 | usage | churn-risk | March active users: 8 of 18 (44%). Down from 14 of 18 (78%) in November. Decline steady over 4 months. | corroborated |
| 2026-03-20 | call | sentiment | Laura: "Honestly, I'm not sure the shift leads are using it the way Derek set it up. He was the one who kept everyone on track." | single-source |
| 2026-03-05 | support | bug | Amy reported PDF export formatting broken on Safari. Resolved in 2 days. Amy thanked support team by name. | verified |
| 2026-02-14 | call | renewal | Laura mentioned budget season starting. No concerns raised about renewal, but did not explicitly confirm. "We'll figure it out when we get there." | single-source |
| 2026-01-08 | usage | churn-risk | December usage: 9 of 18 active. First month below 50% since onboarding. | single-source |
| 2025-10-15 | call | expansion | Derek asked about adding 4 regional managers. "If we can show the exec team the Q3 data, I think we can justify expanding." | single-source |
| 2025-09-03 | email | feature-request | Laura requested a company-wide dashboard showing exception counts by facility. "The exec team keeps asking and I have to pull it manually." | single-source |
| 2025-06-10 | call | renewal | Renewed. Laura: "This is a no-brainer. Derek runs it and nobody complains." | verified |

### Renewal History

| Cycle | Outcome | Seats | Notes |
|---|---|---|---|
| 2025-06 | Renewed | 18 | Added 4 seats (from 14). Derek drove expansion. No pricing discussion. |
| 2024-06 | New | 14 | 30-day trial converted. Derek ran onboarding for all facility managers. |

### Usage Summary (Q1 2026)

- Active users: 8 of 18 seats (44%)
- Exceptions tracked: 2,847 (down from 4,120 in Q1 2025)
- Last login by Laura: March 28, 2026
- Last login by Derek: April 8, 2026
- 6 facility managers have not logged in since January

### Support History

- Q1 2026: 1 bug (PDF export, resolved in 2 days). Low-touch account on support.
- Q4 2025: 0 tickets.
- Lifetime: 3 total tickets, all resolved within 3 days.

---

## FOOTER

### Renewal Status

**Next renewal:** 2026-06-10
**Status:** At risk. Derek (champion) is leaving June 30. Usage declining for 4 months. Laura has not confirmed renewal. Budget season in progress.

**Health changed to yellow** on April 10, 2026. Triggers: Derek departure (verified champion-change) + sustained usage decline (corroborated, 4 consecutive months).

### Active Threads

| Thread | Status | Key People | Next Step | Deadline | Ref |
|---|---|---|---|---|---|
| Renewal confirmation | In progress | Laura, James | Schedule call with Laura before May 15 to discuss renewal and Derek's successor | May 15 | [call-2026-02-14.md](notes/call-2026-02-14.md) |
| Champion transition | Not started | Laura, James | Identify who replaces Derek as internal owner of the tool | June 15 | [standup-2026-04-10.md](notes/standup-2026-04-10.md) |
| Facility dashboard feature | Waiting | Laura, Product | Product team has it on roadmap for Q3. Laura asked twice. No ETA shared. | Q3 2026 | [FEAT-489](https://jira.example.com/FEAT-489) |

### Open Commitments

| Commitment | Made by | Date | Status |
|---|---|---|---|
| Company-wide exception dashboard for exec reporting | Product team | 2025-09-10 | Open. On roadmap for Q3 2026. Laura asked about this twice. |
| Follow-up on regional manager expansion | James | 2025-10-15 | Stale. Derek drove this. Revisit with Laura post-departure. |

### Expansion Opportunities

- **Regional manager expansion (4 seats):** Originally Derek's initiative. Uncertain without him. Do not pitch until new operations director is hired and relationship is established.

### Watch Items

- **Critical:** Derek leaving June 30. He was the champion, the trainer, and the internal enforcer of adoption. Without a successor who owns the tool, renewal risk is high even if Laura approves budget.
- **Action needed:** Schedule a call with Laura before May 15 to understand: (1) who replaces Derek, (2) whether the new person will own the tool, (3) whether Laura wants us to re-train facility managers directly.
- **Monitor:** If May active users drop below 6 of 18 (33%), escalate to red and prepare a retention offer.
