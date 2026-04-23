# ACCOUNT.md Format Specification

**Version:** 1.0
**Status:** Draft

---

## Core Principle

One file per account. Any team member or AI agent can read it and understand the account in under two minutes.

---

## Format at a Glance

```
YAML front matter (machine-readable):
  name, slug, health, tier, privacy          -- required
  aliases, contacts, external_ids, tags      -- recommended
  parent, children                           -- for nested accounts
  fiscal_year_end, budget_window             -- for outreach timing
  start_date, renewal_date, mrr, arr, seats  -- for revenue queries

Markdown body (three sections, in order):

  HEAD    -- who they are, why they use you, how they found you
  BODY    -- signal log (with verification tiers), renewal history, usage summary
  FOOTER  -- active threads, renewal status, open commitments, watch items

300-line cap. Sub-documents for overflow. One file per account.
```

---

## Overview

ACCOUNT.md is a plain-text format for describing a customer account relationship to both humans and AI agents. It combines structured YAML front matter (machine-readable account metadata) with a markdown body organized into three sections: HEAD, BODY, and FOOTER.

An ACCOUNT.md file is a single source of truth for one customer account. It lives in a repository, is version-controlled, and can be read directly by any AI agent as context before a customer interaction.

The format works for any team size: a solo founder with 15 clients, a 5-person startup with 80 accounts, or an enterprise team that wants portable account context alongside their CRM. It does not require a database or proprietary tooling. It does not replace a CRM. It gives every account a structured context file that travels with your codebase.

---

## File Structure

An ACCOUNT.md file contains:

1. **YAML front matter** (between `---` delimiters) with machine-readable account metadata
2. **Markdown body** with three required sections in order: HEAD, BODY, FOOTER

```
---
(YAML front matter: structured metadata)
---

## HEAD
(Static context: who they are, why they're here)

## BODY
(Living history: what has happened, what is happening now)

## FOOTER
(Forward-looking: what is next, what to watch)
```

### Document Cap

An ACCOUNT.md file should not exceed **300 lines of content**. This is a guideline, not a hard limit. The intent: an AI agent reading 300 lines gets full context in a single pass. An AI agent reading 3,000 lines gets noise.

**What counts toward the cap:** YAML front matter, HEAD content, BODY content (signal log, renewal history, usage summary), and FOOTER content (active threads, commitments, watch items).

**What does not count:** `### References` blocks at the end of each section. References are navigation, not content. They help a reader find deeper context but don't add information an agent needs for a 2-minute account read. Excluding them from the cap prevents teams from cutting useful references to stay under the line limit.

When a section grows beyond its useful length, archive older entries or summarize them. For accounts with extensive history, use sub-documents (see Document References).

### Document References

When an account needs more than 300 lines of context, split into sub-documents. The ACCOUNT.md file is always the primary file. Sub-documents live alongside it and are referenced explicitly.

```
accounts/
  acme-corp/
    ACCOUNT.md              -- primary file (under 300 lines)
    history.md              -- archived signal log entries older than 12 months
    verification-log.md     -- confidence change audit trail (optional, see below)
    contracts/              -- contract documents
    notes/                  -- call notes, meeting summaries, transcripts
    onboarding.md           -- onboarding record
```

**Rule:** The ACCOUNT.md file must be self-sufficient for the current state of the account. An AI agent reading only the ACCOUNT.md (without sub-documents) should be able to prepare for a customer call. Sub-documents provide depth, not essential context.

### Section References

Each section (HEAD, BODY, FOOTER) can include a `### References` block at the end linking to related documents. References act as footnotes: an inline marker `[^ref-name]` connects a specific statement to a specific document listed in the references block.

References are optional in every section. When present, they appear as the last block in the section. They do not count toward the 300-line cap.

**Footnote pattern:**

Use inline markers to connect specific statements to their source documents. The marker `[^ref-name]` appears in the prose, and the reference block at the end of the section provides the link.

```markdown
## HEAD

Pinnacle Logistics is a mid-size warehousing company based in Portland, OR, operating 11 facilities across the Pacific Northwest.[^onboarding]

**Why they use us:** "We were tracking shipment exceptions in spreadsheets and losing visibility every time someone went on vacation."[^original-call] (Laura Whitfield, June 2024)

**Configuration:** Team plan, 18 seats. SSO via Google Workspace. API integration with ShipStation.[^integration-spec]

### References
[^onboarding]: [Onboarding record](onboarding.md)
[^original-call]: [Sales call transcript, June 2024](notes/call-2024-06-10.md)
[^integration-spec]: [ShipStation integration spec](notes/shipstation-setup.md)

## BODY

(... signal log, renewal history ...)

API integration with ShipStation went down for 9 hours on March 12.[^incident-postmortem]

### References
[^incident-postmortem]: [March 12 incident post-mortem](notes/incident-2026-03-12.md)
[^signal-archive]: [Full signal history pre-2025](history.md)
[^qbr-q4]: [Q4 2025 QBR deck](notes/qbr-2025-q4.pdf)

## FOOTER

(... active threads, commitments ...)

Prepare retention package if competitive evaluation selects a finalist by May 15.[^retention-draft]

### References
[^retention-draft]: [Retention package draft](notes/retention-offer-draft.md)
[^comp-brief]: [Competitive evaluation brief](notes/comp-eval-2026-04.md)
```

**When to use footnotes vs. general references:** If a reference connects to a specific statement, use a footnote marker (`[^ref-name]`). If a reference is generally relevant to the whole section (like an archived signal log), list it in the references block without an inline marker.

**Pattern:** HEAD references tend to be static (contracts, onboarding, config). BODY references tend to be historical (archived signals, incident reports, QBR notes). FOOTER references tend to be forward-looking (competitive analysis, proposals, retention plans). This isn't a rule, just a natural pattern.

**Relationship to Active Threads:** Active threads already have a `Ref` column for linking to source material per thread. Section references are broader: they link to documents relevant to the entire section, not a single thread. Both can coexist.

---

## YAML Front Matter

The front matter contains fields that are machine-queryable across all accounts. These are the fields an AI agent or script reads when answering cross-account questions like "which accounts are at churn risk?" or "which renewals are coming up this quarter?"

### Required Fields

```yaml
---
version: "1.0"
name: "Acme Corp"
slug: acme-corp
health: green
tier: starter
privacy: full
```

| Field | Type | Description |
|---|---|---|
| `version` | string | Specification version. Currently `1.0`. |
| `name` | string | Display name of the account. |
| `slug` | string | URL-safe identifier. Used for file naming and cross-referencing. Lowercase, hyphens only. |
| `health` | enum | Account health status. Values: `green`, `yellow`, `red`. See Health Score section. |
| `tier` | string | Product tier or plan the account is on. Free-form string matching your pricing structure (e.g., `free`, `starter`, `team`, `enterprise`). |
| `privacy` | enum | Data visibility mode. Values: `full`, `masked`, `ids-only`. See Privacy Modes section. |

### Recommended Fields

```yaml
aliases:
  - ACME
  - Acme Logistics
  - AC
owner: james
website: acme-corp.com
city: Austin
state: TX
country: US
industry: logistics
source: referral
start_date: 2024-03-15
renewal_date: 2026-03-15
currency: USD
mrr: 49
arr: 588
seats: 12
contacts:
  - name: Sarah Chen
    role: decision-maker
    email: s.chen@acme.com
    last_contacted: 2026-04-15
  - name: Mike Torres
    role: champion
    email: m.torres@acme.com
    last_contacted: 2026-03-18
  - name: Priya Patel
    role: day-to-day
    email: p.patel@acme.com
    last_contacted: 2026-04-02
fiscal_year_end: "2026-06-30"
budget_window:
  - 3
  - 4
  - 5
parent: null
children:
  - acme-west-division
  - acme-east-division
external_ids:
  hubspot: "HS-28491"
  stripe: "cus_R4x8mKj2Lp"
  database: "acct-0047"
tags:
  - renewal-risk
  - feature-request-pending
```

| Field | Type | Description |
|---|---|---|
| `aliases` | list | Alternate names, acronyms, or shorthand for this account. Used for search and matching (e.g., a team member says "ACL" in a standup, the agent knows that's Acme Corp). |
| `owner` | string | Team member who owns this relationship. |
| `website` | string | Account's website domain. |
| `city` | string | Primary location city. |
| `state` | string | State, province, or region. |
| `country` | string | Country code (ISO 3166-1 alpha-2). Default: US. |
| `industry` | string | Industry or vertical. Free-form string. |
| `source` | string | How they found you. Values like `inbound`, `referral`, `outbound`, `event`, `content`. |
| `start_date` | date | When this account first became a customer. The origin date. ISO 8601 format (YYYY-MM-DD). |
| `renewal_date` | date | Next renewal date. ISO 8601 format. |
| `currency` | string | Currency for monetary values. ISO 4217 code (e.g., `USD`, `EUR`, `GBP`). Default: USD. |
| `mrr` | number | Monthly recurring revenue from this account. In the currency specified by `currency`. |
| `arr` | number | Annual recurring revenue. |
| `seats` | number | Number of seats, licenses, or users. |
| `fiscal_year_end` | date | End date of this account's fiscal year. ISO 8601 format. Determines when budget resets and when purchasing decisions happen. |
| `budget_window` | list of numbers | Months (1-12) when this account can approve new purchases or renewals. An AI agent generating outreach outside this window is wasting effort. Example: `[3, 4, 5]` for a spring budget cycle. |
| `parent` | string or null | Slug of the parent account, or `null` if this is a top-level account. See Account Hierarchy section. |
| `children` | list | Slugs of direct child accounts. See Account Hierarchy section. |
| `contacts` | list | Key contacts at this account. See Contact Fields below. |
| `external_ids` | map | Identifiers in external systems. Keys are system names, values are the ID strings. See External IDs section. |
| `tags` | list | Tags for filtering and grouping. See Standard Tags section. |

### Aliases

The `aliases` field captures every name a team might use to refer to this account. This matters because customer signals surface in conversation ("ACL mentioned renewal in the standup"), in CRM fields ("Acme Logistics"), and in contracts ("Acme Corp Logistics LLC"). An AI agent processing a transcript needs to know that all of these refer to the same account.

```yaml
aliases:
  - ACL
  - Acme Logistics
  - Acme Corp Logistics
```

### Account Hierarchy

Accounts can be nested. A parent account contains child accounts. A child account points to its parent. The hierarchy can be any depth: a holding company contains divisions, a division contains regional offices, a regional office contains individual locations. The spec does not limit the number of levels.

Each ACCOUNT.md file knows two things: its parent (one slug or null) and its direct children (a list of slugs). The full tree is built by walking the chain across files.

```yaml
# Top-level account (no parent)
parent: null
children:
  - acme-west-division
  - acme-east-division

# Child account (has parent, may have its own children)
parent: acme-corp
children:
  - acme-west-portland
  - acme-west-seattle
```

**Rules:**
- `parent` is a slug referencing another ACCOUNT.md file in the same repository, or `null` for top-level accounts.
- `children` is a list of slugs. Each slug should correspond to an ACCOUNT.md file that has this account as its `parent`.
- In `masked` or `ids-only` privacy modes, children may reference external IDs instead of slugs.
- An account with no parent and no children is a standalone account. Both fields can be omitted for standalone accounts.
- Health, revenue, and contacts belong to each account individually. A parent account's health is not automatically derived from its children. Teams may choose to roll up ARR or health across a hierarchy, but this is a tooling decision, not a format rule.

**Cross-account queries enabled:**
- "Show me all child accounts under Acme Corp" - filter by `parent: acme-corp`
- "Which parent accounts have a red child?" - walk children, check health
- "What is total ARR across this account and all its children?" - sum ARR down the tree

### Contact Fields

Each contact entry supports:

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Full name of the contact. |
| `role` | Yes | Relationship role. See Contact Roles. |
| `last_contacted` | No | Date of last meaningful interaction with this contact. ISO 8601 format. Enables "which contacts haven't been reached in 30 days?" queries. |
| `email` | No | Email address. Omit in `masked` or `ids-only` privacy modes. |
| `phone` | No | Phone number. Omit in `masked` or `ids-only` privacy modes. |
| `title` | No | Job title at the account. |
| `notes` | No | Brief context (e.g., "Was previously at Acme West, brought us in when she moved here"). |

### Contact Roles

The `role` field on contacts uses a fixed vocabulary:

| Role | Description |
|---|---|
| `decision-maker` | Signs contracts, approves budget. The person who says yes or no. |
| `champion` | Internal advocate for your product. Pushes for adoption and renewal. |
| `day-to-day` | Primary user or operational contact. Most frequent interaction. |
| `executive` | Senior stakeholder with visibility but not daily involvement. |
| `technical` | Handles implementation, integration, or technical questions. |

Custom roles are permitted. The five above are the standard vocabulary that tools should recognize.

### External IDs

The `external_ids` field maps this account to records in other systems. Keys are free-form system names. Values are string identifiers.

```yaml
external_ids:
  hubspot: "HS-28491"
  stripe: "cus_R4x8mKj2Lp"
  database: "acct-0047"
  salesforce: "001Dn00000Abc12"
  intercom: "usr_5f3a9b"
```

This field serves two purposes:
1. **Linking:** A script or agent can look up the full CRM record, billing history, or product usage data using these IDs.
2. **Privacy:** In `ids-only` mode, external IDs are the only account identifiers present. All other identifying information is omitted.

### Standard Tags

Tags are free-form, but the following standard tags are recognized by tooling and should be used when applicable:

**Account status tags:**

| Tag | When to use |
|---|---|
| `renewal-risk` | Account has active churn signals or renewal uncertainty |
| `renewal-confirmed` | Renewal explicitly confirmed by customer |
| `churned` | Account has not renewed or has canceled |
| `new-account` | Account is in first 90 days |
| `onboarding` | Account is in active onboarding |
| `expansion-opportunity` | Upsell or growth signal identified |

**Signal-based tags:**

| Tag | When to use |
|---|---|
| `champion-at-risk` | Champion contact is leaving or disengaging |
| `competitor-evaluation` | Account is actively evaluating competitors |
| `escalation-active` | Unresolved executive or formal escalation |
| `feature-request-pending` | Outstanding feature request that matters to this account |
| `usage-declining` | Usage metrics trending down for 2+ months |

**Segment tags:**

| Tag | When to use |
|---|---|
| `enterprise` | Enterprise tier account |
| `smb` | Small/medium business account |
| `pilot` | Account is in trial or pilot phase |

Custom tags are permitted. The standard tags above are the canonical vocabulary that cross-account queries and dashboards should recognize.

### Custom Fields

Additional YAML fields beyond those listed above are permitted. Consumers should accept unknown fields without error. This allows teams to extend the front matter for their specific needs (e.g., `warehouse_count`, `contract_type`, `csm_assigned`, `timezone`).

---

## Privacy Modes

ACCOUNT.md files may contain sensitive information: contact names, email addresses, deal values, internal relationship notes. The `privacy` field in the YAML front matter controls what data is included in the file.

### Three Modes

| Mode | What's included | What's omitted | Use case |
|---|---|---|---|
| `full` | Everything. Names, emails, phone numbers, revenue, signals, IDs. | Nothing. | Private repo, internal team use. The default for most teams. |
| `masked` | Roles instead of names ("decision-maker" instead of "Sarah Chen"). Revenue ranges instead of exact values ("$500-1000/mo" instead of "$588"). Signals reference roles, not people. External IDs included. | Real names, email addresses, phone numbers, exact revenue figures. | Shared repos, consulting contexts, or when ACCOUNT.md files may be visible to people outside the account team. |
| `ids-only` | External system IDs only. Slug, health, tier, tags, and IDs. No prose, no signals, no contacts, no revenue. | All PII, all narrative content, all signals. | Public or semi-public contexts. The file serves only as an index pointing to records in other systems. |

### How Privacy Modes Affect Each Section

| Section | `full` | `masked` | `ids-only` |
|---|---|---|---|
| YAML contacts | Name + role + email | Role only (no name, no email) | Omitted |
| YAML revenue | Exact numbers | Ranges or omitted | Omitted |
| YAML external_ids | Included | Included | Included |
| HEAD | Full narrative | Narrative with roles instead of names | Omitted |
| BODY signal log | Full signals with names | Signals with roles instead of names | Omitted |
| FOOTER | Full commitments and risks | Commitments with roles | Omitted |

### Example: Masked Mode

```yaml
---
version: "1.0"
name: "Acme Corp"
slug: acme-corp
health: yellow
tier: team
privacy: masked
contacts:
  - role: decision-maker
  - role: champion
  - role: day-to-day
external_ids:
  hubspot: "HS-28491"
  stripe: "cus_R4x8mKj2Lp"
tags:
  - champion-at-risk
---

## HEAD

Acme Corp is a 200-person logistics company in Texas. They use the product for shipment exception tracking.

## BODY

### Signal Log

| Date | Source | Category | Signal | Confidence |
|---|---|---|---|---|
| 2026-04-15 | standup | renewal | Decision-maker confirmed renewal but reducing seats. | verified |
| 2026-04-10 | standup | champion-change | Champion accepted a role at another organization. Departing end of June. | verified |

## FOOTER

### Renewal Status
**Status:** At risk. Champion departing. Decision-maker has not reconfirmed.
```

### Choosing a Mode

- **Default to `full`** unless you have a reason not to. Most teams work in private repos and need the full context.
- **Use `masked`** when files might be shared with contractors, consultants, or across teams that shouldn't see individual contact details.
- **Use `ids-only`** when you need a lightweight index that points to external systems without exposing any account detail.

Tools that read ACCOUNT.md files should check the `privacy` field and never expose data beyond what the mode permits. A `masked` file read by an AI agent should not prompt the agent to look up contact names from external IDs.

---

## HEAD Section

The HEAD section contains static context about the account: who they are, why they use your product, and how they got here. This section changes infrequently (roughly once per year or at major account events).

### Required Content

- **Who they are:** Company description, size, location, industry context. One to three sentences.
- **Why they use your product:** Their stated problem, in their own words if possible. Not your marketing copy. What they actually said when asked why they signed up or renewed.
- **How they found you:** The acquisition story. Referral from whom, which content piece, which event.

### Optional Content

- Key dates (contract signed, onboarding completed, first escalation)
- Product configuration notes (which features enabled, which integrations active)
- Relationship notes that rarely change (e.g., "Sarah was previously at Acme West, brought us in when she moved to Acme East")

### Example

```markdown
## HEAD

Acme Corp is a 200-person logistics company based in Austin, TX. They manage warehouse operations across Texas and Oklahoma for mid-size e-commerce brands.

**Why they use us:** "We were tracking shipment exceptions in spreadsheets and losing visibility every time someone went on vacation. We needed one place where the whole team could see what's stuck." (Sarah Chen, March 2024 onboarding call)

**How they found us:** Referral from Mike Torres, who used the product at his previous company. Sarah hired Mike in January 2024 and he brought the recommendation.

**Configuration:** Team plan, 12 seats. SSO enabled via Google Workspace. API integration with their warehouse management system (ShipStation).
```

---

## BODY Section

The BODY section is the living history of the account relationship. It is updated continuously as new information surfaces. This is where signals from conversations, product usage, and relationship events are recorded.

### Signal Log

The signal log is the core of the BODY section. Each entry is a short, dated record of something meaningful that happened or was said.

**Format:**

```markdown
### Signal Log

| Date | Source | Category | Signal | Confidence |
|---|---|---|---|---|
| 2026-04-15 | standup | renewal | Sarah confirmed renewal but reducing from 14 to 12 seats. Two people leaving. | verified |
| 2026-04-02 | support | bug | Reported PDF export broken on Chrome 124. Resolved same day. | verified |
| 2026-03-18 | call | expansion | Mike mentioned 3 new warehouse locations onboarding in fall. Potential +8 seats. | single-source |
| 2026-02-10 | usage | churn-risk | Active daily users dropped 60% month-over-month. No known cause. | single-source |
```

### Signal Categories

The signal taxonomy is adapted from established conversation intelligence platforms. Use these categories for the `Category` column:

| Category | What it captures |
|---|---|
| `renewal` | Renewal intent, timeline, seat changes, pricing discussions |
| `expansion` | Growth signals: new users, new departments, upsell interest |
| `churn-risk` | Disengagement, complaints, competitor mentions, usage drops |
| `champion-change` | Key contact leaving, new stakeholder, org restructuring |
| `feature-request` | Specific product requests with context on why they need it |
| `bug` | Product issues reported, severity, resolution status |
| `escalation` | Executive involvement, formal complaints, SLA issues |
| `competitor` | Mentions of competing products, evaluations, switching signals |
| `sentiment` | General relationship temperature: praise, frustration, neutrality |
| `commitment` | Promises made to this account (by your team, not theirs) |

Custom categories are permitted. The ten above are the standard vocabulary.

### Signal Sources

The `Source` column identifies where the signal came from. Common source values:

| Source | What it means |
|---|---|
| `call` | A scheduled call or meeting with the customer |
| `standup` | An internal team standup or sync where the account was mentioned |
| `email` | An email exchange with the customer or about the customer internally |
| `support` | A support ticket, help desk interaction, or bug report |
| `usage` | Product usage data, analytics, or dashboards |
| `qbr` | A quarterly business review or formal account review |
| `incident` | A system outage, downtime event, or data loss incident |
| `chat` | A Slack, Teams, or in-app chat message |
| `transcript` | An AI-transcribed meeting or call recording |

Custom sources are permitted. The key requirement is that the source is specific enough to trace back to the original context. "call" is better than "conversation." "standup-2026-04-15" is even better.

### Verification Tiers

Every signal has a confidence level. This is the mechanism that addresses the fundamental problem of customer intelligence: how do you know if something is accurate?

| Confidence | What it means | When to assign |
|---|---|---|
| `single-source` | One data point. A mention in a transcript, a metric from a dashboard, a comment in a ticket. It exists, but it has not been confirmed. | Default for any new signal from a single source. |
| `corroborated` | Two independent sources agree. The sources must be genuinely independent: a customer call and a usage dashboard, two separate conversations on different dates, a support ticket and a transcript mention. Two mentions in the same meeting are one source, not two. | Assign when a second independent source confirms the signal. |
| `verified` | Three independent sources confirm, or a human with direct knowledge of the account has explicitly reviewed and approved the signal as accurate. | Assign when high confidence is established. Health score changes should be based on verified signals. |

**A note on AI agents as sources:** An AI agent that processes a transcript and flags a signal counts as one source (the transcript). The agent is the mechanism, not an independent source. An agent that independently cross-references a transcript mention against CRM data and confirms a match is producing a `corroborated` signal (two sources: transcript + CRM). The distinction matters: the agent's confidence comes from the sources it reads, not from the agent itself.

**The rule:** Health score changes (in the YAML front matter) should only be triggered by `verified` or `corroborated` signals. A single `single-source` signal, no matter how alarming, does not change the health score. This prevents recency bias: one bad meeting does not turn a healthy account red.

**The sustained signal threshold:** Two signals in the same category within 90 days constitute a pattern. One churn-risk signal is a data point. Two churn-risk signals within 90 days are a pattern worth investigating. Three are a trend that should change the health score.

### Verification Change Tracking

When a signal's confidence changes (e.g., from `single-source` to `corroborated`), the reasoning behind that change should be recorded. Two approaches are supported, and teams can start with the default and adopt the sub-document approach as they grow.

**Default: Inline in the signal log.** Add a new row to the signal log documenting the upgrade:

```markdown
| 2026-04-02 | usage | churn-risk | Corroborated: Jan usage decline now confirmed by Laura's March 20 comment about shift leads not using the tool. Two independent sources. Upgrading from single-source. | corroborated |
```

The original signal row's confidence value is updated to `corroborated`. The new row captures the reasoning. The signal log is the audit trail. This is the simplest approach and is sufficient for most teams starting out.

**Recommended upgrade: Verification log sub-document.** As teams build confidence in the verification system and want to track patterns over time, maintain a `verification-log.md` alongside the ACCOUNT.md:

```markdown
# Verification Log

| Date | Original Signal Date | Category | Change | Reasoning | Sources |
|---|---|---|---|---|---|
| 2026-04-02 | 2026-01-08 | churn-risk | single-source → corroborated | Jan usage decline confirmed by Laura's March 20 call comment | usage-dashboard, [call-2026-03-20.md](notes/call-2026-03-20.md) |
| 2026-04-10 | 2026-04-02 | churn-risk | corroborated → verified | Derek's departure (verified independently) confirms pattern. Health changed to yellow. | [standup-2026-04-10.md](notes/standup-2026-04-10.md), usage-dashboard, [call-2026-03-20.md](notes/call-2026-03-20.md) |
```

The verification log serves three purposes:
1. **Troubleshooting:** "Why is this account yellow?" traces back through the log to the specific sources that triggered each confidence change.
2. **Calibration over time:** Reviewing verification logs across accounts reveals patterns in your signal quality. Which sources are most reliable? How often do single-source signals get corroborated? How long does corroboration take on average?
3. **Compliance and audit:** For teams in regulated industries (healthcare, finance, government), the verification log provides a documented chain of reasoning for account risk assessments.

**Progression:** Start with the inline default. When you find yourself wanting to answer "how good is our signal quality across all accounts?" or "how often do we change health scores and why?", adopt the sub-document. The inline approach captures reasoning per signal. The sub-document captures reasoning as a system you can learn from.

### Additional BODY Content

Beyond the signal log, the BODY section may include:

- **Renewal history:** One line per renewal cycle (date, outcome, seat count, notes).
- **Product usage summary:** Key metrics that indicate engagement (active users, feature adoption, login frequency). Updated monthly or quarterly, not daily. Use metrics that are meaningful for your product, not vanity numbers.
- **Support history summary:** Pattern-level view of support interactions. Not every ticket. "3 bugs in Q1, all resolved same day" or "2 escalations in 6 months, both integration-related." Captures whether this account is high-touch or low-touch on support.
- **NPS/CSAT scores:** If you collect them, one line per survey period with the score and any verbatim comment worth preserving.
- **Key relationship moments:** Major wins, escalations, hard conversations. The moments that shaped the relationship. Brief entries, not full narratives.

### Example

```markdown
## BODY

### Signal Log

| Date | Source | Category | Signal | Confidence |
|---|---|---|---|---|
| 2026-04-15 | standup | renewal | Sarah confirmed renewal but reducing from 14 to 12 seats. Two people leaving. | verified |
| 2026-04-02 | support | bug | PDF export broken on Chrome 124. Resolved same day. | verified |
| 2026-03-18 | call | expansion | Mike mentioned 3 new warehouse locations onboarding in fall. Potential +8 seats. | single-source |
| 2026-02-10 | usage | churn-risk | Active daily users dropped 60% month-over-month. No known cause. | single-source |
| 2025-12-05 | call | sentiment | Sarah: "This is the only tool the warehouse team doesn't complain about." | verified |
| 2025-09-15 | email | feature-request | Requested multi-language support for partner-facing reports. | single-source |

### Renewal History

| Cycle | Outcome | Seats | Notes |
|---|---|---|---|
| 2025-03 | Renewed | 14 | Added 2 seats. No pricing discussion. |
| 2024-03 | Renewed | 12 | First renewal. Smooth. |
| 2024-03 | New | 12 | Contract signed after 30-day trial. |

### Usage Summary (Q1 2026)

- Active users: 10 of 12 seats (83%)
- Shipments tracked: 1,247 (down from 1,890 in Q4 2025)
- Last login: April 14, 2026
```

---

## FOOTER Section

The FOOTER section is forward-looking. It answers the question a team member asks 10 minutes before a customer call: "What am I trying to accomplish, what's in flight, and what have we promised?"

This section is reviewed before every customer interaction and at every renewal cycle.

### Required Content

- **Renewal status:** Date and current status (on track, at risk, in negotiation, churned).
- **Active threads:** Parallel workstreams currently in progress with this account. Most real accounts have 2-4 things happening simultaneously: a renewal conversation, a support escalation, an expansion opportunity, an integration project. The active threads table captures all of them.
- **Open commitments:** Promises your team made to this account. Different from active threads: a thread is something being worked on now (has a next step), a commitment is a promise that may or may not have active work behind it. "We'll build multi-language support by Q3" is a commitment. "Scoping multi-language support with the product team" is an active thread. Both can exist for the same topic, but they serve different questions: threads answer "what am I working on right now?" and commitments answer "what did we promise?"

### Optional Content

- Expansion opportunities with estimated value
- Watch items and risks
- Scheduled touchpoints (next QBR, next check-in, onboarding milestone)

### Active Threads

Active threads are the parallel workstreams running on this account right now. Each thread has a name, status, the key people involved, the next concrete step, a deadline if one exists, and a reference to the source material (call notes, transcript, ticket, or document where this thread originated or was last discussed).

**Format:**

```markdown
### Active Threads

| Thread | Status | Key People | Next Step | Deadline | Ref |
|---|---|---|---|---|---|
| Renewal negotiation | In progress | Sarah, James | Sarah to confirm seat count after budget meeting | May 15 | [call-2026-04-15.md](notes/call-2026-04-15.md) |
| API integration fix | Resolved | Priya, Engineering | Monitor for 30 days post-fix | May 25 | [INC-4821](https://jira.example.com/INC-4821) |
| Expansion to new locations | Waiting | Mike, James | Follow up after Mike confirms location list | July 1 | [call-2026-03-18.md](notes/call-2026-03-18.md) |
```

**Thread status values:**

| Status | Meaning |
|---|---|
| `Not started` | Identified but no action taken yet |
| `In progress` | Actively being worked |
| `Waiting` | Blocked on the customer or an external dependency |
| `Resolved` | Complete. Remove from active threads after 30 days. |

Active threads are the most frequently updated part of the FOOTER. After every call, standup mention, or email exchange, check whether a thread's status or next step has changed.

**Why this matters:** Without active threads, the FOOTER is a list of facts. With active threads, it is a preparation tool. An AI agent reading the active threads before a call can say: "You have three things in flight with this account. The renewal is waiting on Sarah's budget meeting. The API fix is resolved but still in monitoring. Mike hasn't confirmed the location list yet."

### Example

```markdown
## FOOTER

### Renewal Status

**Next renewal:** 2027-03-15
**Status:** On track. Sarah confirmed April 15. Reducing to 12 seats (from 14). No pricing pushback.

### Active Threads

| Thread | Status | Key People | Next Step | Deadline | Ref |
|---|---|---|---|---|---|
| Renewal (seat reduction) | In progress | Sarah, James | Confirm final seat count after May budget meeting | May 15 | [call-2026-04-15.md](notes/call-2026-04-15.md) |
| Multi-language feature | Waiting | Sarah, Product | Product team scoping for Q3. Sarah asked about timeline twice. | Q3 2026 | [FEAT-312](https://jira.example.com/FEAT-312) |
| New location onboarding | Not started | Mike, James | Mike to confirm which 3 locations in July | July 1 | [call-2026-03-18.md](notes/call-2026-03-18.md) |

### Open Commitments

| Commitment | Made by | Date | Status |
|---|---|---|---|
| Multi-language support for partner reports | James | 2025-09-20 | Open. Scoped for Q3 2026. |
| Dedicated onboarding session for 3 new locations | James | 2026-03-18 | Open. Scheduled for August. |

### Expansion Opportunities

- **Fall 2026 warehouse onboarding:** Mike mentioned 3 new locations. If confirmed, +8 seats ($392/yr additional ARR). Follow up in July.

### Watch Items

- Usage drop in Q1 2026 (single-source, not yet corroborated). Monitor Q2 usage before raising with Sarah.
- Two staff departures reducing seats from 14 to 12. Normal attrition or early sign of deprioritization? Watch for further reductions.
```

---

## Health Score

The `health` field in the YAML front matter is a single-glance indicator of account status. It has exactly three values.

| Value | Meaning | Criteria |
|---|---|---|
| `green` | Healthy. Engaged, renewing, no significant risks. | No unresolved churn-risk signals. Usage stable or growing. Renewal confirmed or expected. |
| `yellow` | Needs attention. One or more signals suggest risk, but the account is not in immediate danger. | Corroborated or verified churn-risk signal, OR usage declining for 2+ months, OR champion change with no new champion identified. |
| `red` | At risk. Active churn signals, disengagement, or unresolved escalation. | Verified churn-risk pattern (2+ signals in 90 days), OR renewal explicitly at risk, OR escalation unresolved for 30+ days. |

**Rules:**
- Health changes require `corroborated` or `verified` signals. Never change health based on a single `single-source` signal.
- Health is reviewed at minimum once per quarter. More frequent review is encouraged for `yellow` and `red` accounts.
- When health changes, add a signal log entry documenting the change and the signals that triggered it.

---

## Cross-Account Queries

The structured format enables queries across all ACCOUNT.md files in a repository. These are examples of questions the format is designed to answer:

| Question | How to answer it |
|---|---|
| Which accounts are at churn risk? | Filter YAML: `health: red` or `health: yellow` |
| Which renewals are coming up this quarter? | Filter YAML: `renewal_date` within date range |
| Which accounts have open commitments? | Parse FOOTER: Open Commitments table where status = Open |
| Which accounts have had no activity in 60 days? | Parse BODY: Signal Log, find max date, compare to today |
| What is total ARR at risk? | Filter YAML: `health: red`, sum `arr` field |
| Which accounts mentioned a competitor? | Parse BODY: Signal Log where category = `competitor` |
| Who are our champions? | Parse YAML: `contacts` where role = `champion` |
| Find account by alias | Match YAML: `aliases` list contains search term |

An AI agent with access to a directory of ACCOUNT.md files can answer all of these questions by reading structured YAML and parsing markdown tables. No database required. No API required.

---

## File Naming and Directory Structure

### File Naming

Each account gets one file. The filename is the account slug:

```
accounts/
  acme-corp.md
  pinnacle-logistics.md
  chen-consulting.md
```

Alternatively, each account can be a directory with an ACCOUNT.md inside (recommended for accounts with sub-documents):

```
accounts/
  acme-corp/
    ACCOUNT.md
    history.md
    contracts/
    notes/
  pinnacle-logistics/
    ACCOUNT.md
```

### Repository Structure

A minimal setup:

```
accounts/
  acme-corp.md
  pinnacle-logistics.md
  chen-consulting.md
README.md
```

A team setup with tooling:

```
accounts/
  ACCOUNT.config.md          -- local configuration and context
  acme-corp/
    ACCOUNT.md
  pinnacle-logistics/
    ACCOUNT.md
tools/
  lint.py
  health-report.py
  query.py
README.md
LICENSE
```

---

## Configuration File (ACCOUNT.config.md)

When a team adopts ACCOUNT.md, they configure it for their business: custom tiers, industry-specific fields, additional signal categories, compliance requirements, and local conventions. This configuration lives in `ACCOUNT.config.md` at the root of the accounts directory.

The file follows the same two-layer architecture as ACCOUNT.md itself: YAML front matter for machine-readable settings, markdown body for human-readable context explaining why each customization exists.

### Why This File Exists

The ACCOUNT.md spec defines the universal structure. Every team's ACCOUNT.md files follow the same HEAD/BODY/FOOTER pattern with the same required fields. But every team also has context that's specific to their business:

- A healthcare company needs FERPA or HIPAA compliance flags
- A SaaS company with multiple products needs a `billing_model` field
- An agency uses different tier names than a B2B startup
- A team in a regulated industry tracks verification differently

Without a config file, this context lives in someone's head. With a config file, any team member or AI agent can read it and immediately understand how this team uses the format.

### Structure

```markdown
---
# ACCOUNT.config.md - Configuration for this team's ACCOUNT.md files

# Custom tiers (these are the valid values for the `tier` field in this team's files)
tiers:
  - free
  - starter
  - team
  - enterprise

# Custom signal categories (in addition to the standard 10)
custom_categories:
  - onboarding
  - training

# Custom contact roles (in addition to the standard 5)
custom_roles:
  - project-manager

# Custom tags (in addition to the standard vocabulary)
custom_tags:
  - high-touch
  - self-serve

# Custom YAML fields expected on ACCOUNT.md files in this directory
custom_fields:
  - field: billing_model
    type: string
    values: [centralized, distributed, direct]
    description: "How this account is billed. Determines expansion strategy."
  - field: onboarding_status
    type: string
    values: [not-started, in-progress, complete]
    description: "Current onboarding phase."

# Industry-specific compliance requirements
compliance: []

# Default privacy mode for new files
default_privacy: full

# Verification tracking approach
verification_tracking: inline    # inline | sub-document

# Default fiscal calendar for accounts that don't specify their own
default_fiscal_year_end: "2026-12-31"
default_budget_window: [1, 2, 3]
---

# Account Configuration

## About This Team

Brief description of who this team is, what product they sell, and how they manage customer relationships. An AI agent reading this file before reading any ACCOUNT.md should understand the business context.

## Tier Definitions

| Tier | What it means | Typical deal size |
|---|---|---|
| free | Self-serve, no contract | $0 |
| starter | Single user or small team, annual billing | $29-49/mo |
| team | 5-25 seats, annual contract | $200-500/mo |
| enterprise | 25+ seats, custom contract, dedicated support | $500+/mo |

## Custom Fields

### billing_model

How the account is billed. This determines how expansion conversations work:
- **centralized:** One invoice for the whole organization. Expansion means adding seats to the existing contract.
- **distributed:** Each department or location is billed separately. Expansion means signing new sub-accounts.
- **direct:** Individual billing. No organizational structure.

## Signal Category Additions

### onboarding
Signals related to the onboarding process: milestones completed, blockers, time-to-value metrics. Use during the first 90 days.

### training
Signals related to training sessions: attendance, feedback, follow-up requests. Use when training is a distinct activity from onboarding.

## Compliance Notes

Any industry-specific rules that affect how ACCOUNT.md files are written, stored, or processed. For example: "No student names in signal logs (FERPA). Use role descriptions instead."

## Conventions

Any team-specific conventions not covered by the spec. For example: "We review all yellow accounts every Monday. We archive signal log entries older than 18 months (not the default 12)."
```

### How Tools Use This File

An AI agent or script processing ACCOUNT.md files should read `ACCOUNT.config.md` first. The config tells the agent:

- What custom fields to expect (and what they mean)
- What tier values are valid for this team
- What additional signal categories exist
- What compliance rules to follow
- Whether verification tracking is inline or sub-document
- What the default privacy mode is

A linting tool checks each ACCOUNT.md against the config: are the custom required fields present? Are tier values from the allowed list? Are compliance rules being followed?

### When to Create This File

Create `ACCOUNT.config.md` when you first set up your accounts directory. It's optional for solo founders using the format out of the box. It becomes essential when:

- A team has more than one person writing ACCOUNT.md files (consistency)
- The business has industry-specific requirements (compliance)
- Custom fields are needed beyond the spec's standard fields (extensibility)
- An AI agent will process the files and needs to understand local context (agent readability)

---

## Section Ordering

The three sections must appear in this order: HEAD, BODY, FOOTER. This order reflects the natural reading pattern: context first (who is this?), then history (what happened?), then action (what's next?).

Sections may not be omitted. An empty section should contain a placeholder:

```markdown
## FOOTER

No forward-looking items at this time.
```

---

## Consumer Behavior

Rules for tools, scripts, and AI agents that read ACCOUNT.md files:

| Scenario | Behavior |
|---|---|
| Unknown YAML field | Accept without error. Custom fields are permitted. |
| Unknown signal category | Accept without error. Custom categories are permitted. |
| Unknown contact role | Accept without error. Custom roles are permitted. |
| Unknown tag | Accept without error. Custom tags are permitted. |
| Missing required YAML field | Warn. The file is valid but incomplete. |
| Missing section (HEAD, BODY, or FOOTER) | Warn. The file is valid but incomplete. |
| Duplicate section heading | Error. Reject the file. |
| File exceeds 300 lines | Warn. The file should be archived or summarized. |
| Unknown confidence tier | Accept without error. Treat as `single-source`. |
| Unknown privacy mode | Warn. Treat as `full` (most restrictive interpretation of unknown = show everything to the account owner). |
| `masked` or `ids-only` file | Never attempt to resolve masked data via external IDs. Respect the privacy mode. |

---

## Versioning

The `version` field in the YAML front matter tracks which specification version the file was written against. The current version is `1.0`. Breaking changes will increment the major version. Non-breaking additions will increment the minor version.

---

## How ACCOUNT.md Fits

ACCOUNT.md is one entry in a family of structured markdown formats designed for AI agent consumption:

| What the agent needs to know | Format |
|---|---|
| How to write code for this project | AGENTS.md / CLAUDE.md |
| What the design system looks like | DESIGN.md |
| How to perform a specific task | SKILL.md |
| Who the agent is | SOUL.md |
| What it needs to know about a customer | **ACCOUNT.md** |

Each format follows the same principle: structured data for machine consumption, prose for human reasoning, both in one portable file.
