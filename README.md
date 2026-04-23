# ACCOUNT.md

**One file per account. Any team member or AI agent can read it and understand the account in under two minutes.**

A format specification for describing a customer account relationship to both humans and AI agents. ACCOUNT.md gives teams a structured, portable, version-controlled way to capture everything they know about a customer: who they are, what has happened, and what comes next.

No database required. No CRM required. Works alongside your existing tools or replaces them entirely.

**Version:** 1.0

---

## Why

Customer intelligence is scattered. It lives in call transcripts nobody re-reads, CRM fields nobody updates, Slack threads that disappear, and meeting notes that never get filed. When someone asks "what's the status of this account?" the answer requires a scavenger hunt across five tools.

ACCOUNT.md fixes this by giving every piece of customer knowledge a standardized place to land.

---

## How It Works

An ACCOUNT.md file has two parts:

1. **YAML front matter** with machine-readable metadata (health status, tier, contacts, revenue, renewal date, external IDs, aliases)
2. **Three markdown sections** in order:
   - **HEAD** - Who they are, why they use your product, how they found you (changes ~once/year)
   - **BODY** - What has happened: signal log, renewal history, usage data (updated continuously)
   - **FOOTER** - What is next: active threads, renewal status, open commitments, risks (reviewed before every interaction)

```yaml
---
version: "1.0"
name: "Pinnacle Logistics"
slug: pinnacle-logistics
aliases:
  - PL
  - Pinnacle
health: yellow
tier: team
privacy: full
start_date: 2024-06-10
renewal_date: 2026-06-10
currency: USD
mrr: 82
seats: 18
contacts:
  - name: Laura Whitfield
    role: decision-maker
    last_contacted: 2026-04-15
  - name: Derek Nunez
    role: champion
    last_contacted: 2026-04-08
external_ids:
  hubspot: "HS-94721"
  stripe: "cus_Lk9m2Rp4Xv"
tags:
  - usage-declining
  - champion-at-risk
---
```

The structured front matter makes cross-account queries possible: "Which accounts are at churn risk?" "Which renewals are this quarter?" "What is total ARR at risk?" Questions that are impossible with free-form notes become trivial with a consistent format.

---

## Quick Start

1. Create a file called `ACCOUNT.md` (or `[slug].md`) for one customer
2. Add the YAML front matter with at least: `version`, `name`, `slug`, `health`, `tier`, `privacy`
3. Write the three sections: HEAD, BODY, FOOTER
4. Keep it under 300 lines of content. When it gets long, archive older entries into sub-documents.

That's it. No tooling required. Open a text editor and start writing.

See the [examples/](examples/) directory for complete files at different scales:
- [saas-startup/](examples/saas-startup/ACCOUNT.md) - 18-seat operations SaaS, health: yellow, champion departing
- [agency/](examples/agency/ACCOUNT.md) - 3-seat marketing agency, health: green, high engagement
- [enterprise-team/](examples/enterprise-team/ACCOUNT.md) - 45-seat healthcare enterprise, health: red, competitive evaluation in progress

---

## Key Concepts

### Signal Log

The BODY section contains a signal log: short, dated entries capturing meaningful customer signals. Each signal has a category, a source, and a confidence level.

**Ten standard categories:** `renewal`, `expansion`, `churn-risk`, `champion-change`, `feature-request`, `bug`, `escalation`, `competitor`, `sentiment`, `commitment`

### Verification Tiers

Not all signals are equally trustworthy. ACCOUNT.md tracks confidence:

| Tier | Meaning |
|---|---|
| `single-source` | One data point. Not yet confirmed. |
| `corroborated` | Two independent sources agree. |
| `verified` | Three sources confirm, or a human with direct knowledge approves. |

Health score changes require `corroborated` or `verified` signals. One bad meeting does not turn a healthy account red.

### Active Threads

The FOOTER tracks parallel workstreams in progress: a renewal negotiation, a feature request, an expansion conversation, a support escalation. Each thread has a status, key people, next step, deadline, and a reference to the source material. This is what a team member reads 10 minutes before a call.

### Privacy Modes

Control what data appears in the file:

| Mode | What's included |
|---|---|
| `full` | Everything. Names, emails, phone numbers, revenue, signals, IDs. Default for most teams. |
| `masked` | Roles instead of names. Revenue ranges instead of exact values. Signals reference roles, not people. External IDs included. |
| `ids-only` | Slug, health, tier, tags, and external system IDs. No PII, no narrative, no signals. |

### Account Hierarchy

Accounts can be nested: a holding company contains divisions, a division contains locations. Each file knows its parent and children (by slug). The hierarchy can be any depth. Useful for franchises, multi-location businesses, and enterprise org structures.

### Configuration (ACCOUNT.config.md)

When a team adopts the format, they create an `ACCOUNT.config.md` at the root of their accounts directory. Same two-layer architecture: YAML front matter defines custom tiers, fields, signal categories, and compliance requirements. Markdown body explains what each customization means and why it exists. An AI agent reads the config before reading any account file, so it understands the local context.

See [examples/ACCOUNT.config.md](examples/ACCOUNT.config.md) for a healthcare compliance team example.

### 300-Line Cap

ACCOUNT.md files should stay under 300 lines. The cap enforces discipline: an AI agent reading 300 lines gets full context. An AI agent reading 3,000 lines gets noise. Use sub-documents for archived history.

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

---

## Who This Is For

- A solo founder with 15 clients and no CRM
- A 5-person startup managing 80 accounts in a spreadsheet
- A sales team that wants structured account context their AI agent can read before every call
- An enterprise team migrating from HubSpot or Salesforce who wants portable, version-controlled account files
- Any team that wants one file per account that any team member, human or AI, can read in under two minutes

---

## Specification

The full format specification is in [docs/spec.md](docs/spec.md).

---

## License

Apache 2.0. See [LICENSE](LICENSE).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

Created by [Adam Russek-Sobol](https://www.linkedin.com/in/adamrusseksobol/) / [Lobos Innovation](https://lobosinnovation.com)
