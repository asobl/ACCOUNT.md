---
# ACCOUNT.config.md - Example configuration for a healthcare compliance SaaS team

tiers:
  - pilot
  - clinic
  - network
  - enterprise

custom_categories:
  - compliance-deadline
  - credentialing
  - audit

custom_roles:
  - compliance-officer
  - medical-director

custom_tags:
  - hipaa-sensitive
  - state-audit-risk
  - multi-facility
  - joint-commission

custom_fields:
  - field: facility_count
    type: number
    description: "Number of facilities covered under this account's contract."
  - field: compliance_framework
    type: string
    values: [joint-commission, state-only, cms, custom]
    description: "Which compliance framework this account follows. Determines calendar templates and alert rules."
  - field: ehr_integration
    type: string
    values: [epic, cerner, athena, allscripts, none]
    description: "Which EHR system is integrated. Affects onboarding and support complexity."

compliance:
  - hipaa

default_privacy: full

verification_tracking: sub-document

default_fiscal_year_end: "2026-09-30"
default_budget_window: [7, 8, 9]
---

# Account Configuration: MedTrack Compliance Platform

## About This Team

MedTrack is a compliance tracking platform for healthcare networks. Our customers are hospitals, clinic networks, and long-term care facilities that need to track staff credentialing, license renewals, and regulatory deadlines. We sell annual contracts priced by facility count.

Most of our accounts are multi-facility healthcare networks (10-50 facilities). Our biggest accounts are regional health systems with 100+ facilities. Our smallest are independent clinics.

## Tier Definitions

| Tier | What it means | Typical deal size | Account structure |
|---|---|---|---|
| pilot | 60-day trial at a single facility. No contract. | $0 | Standalone |
| clinic | Single facility, annual contract | $200-400/mo | Standalone |
| network | 5-25 facilities, annual contract, dedicated onboarding | $1,000-3,000/mo | Parent + children |
| enterprise | 25+ facilities, multi-year contract, custom compliance calendar, SLA | $5,000+/mo | Parent + children |

## Custom Fields

### facility_count

Number of facilities covered under this account's contract. This is the primary scaling unit for pricing and support allocation. A 12-facility network needs different support than a single clinic, even at the same tier.

### compliance_framework

Which regulatory framework governs this account's compliance requirements:
- **joint-commission:** Follows Joint Commission accreditation standards. Requires quarterly self-assessments.
- **state-only:** State licensing only, no national accreditation. Requirements vary by state.
- **cms:** Centers for Medicare/Medicaid Services conditions of participation. Federal requirements.
- **custom:** Custom compliance calendar built during onboarding (rare, usually large enterprise accounts).

### ehr_integration

Which Electronic Health Records system is integrated with our platform. Determines:
- Onboarding complexity (Epic integrations take 6-8 weeks, Athena takes 2 weeks)
- Support ticket patterns (Cerner API changes cause recurring sync issues)
- Expansion potential (facilities on the same EHR system onboard faster)

## Signal Category Additions

### compliance-deadline
Signals related to upcoming regulatory deadlines: license expirations, accreditation renewals, state survey windows. These are time-sensitive and often trigger health score changes if unresolved.

### credentialing
Signals related to staff credentialing: credential expirations caught, near-misses, bulk renewal periods. High credentialing signal volume is a positive indicator (the system is being used as intended).

### audit
Signals related to external audits: state survey results, Joint Commission visits, CMS reviews. An audit finding that our system should have caught is a critical escalation.

## Compliance Notes

**HIPAA applies to all accounts.** Signal log entries must never contain patient names, medical record numbers, or protected health information. Use role descriptions and facility names only. Example:

- Good: "Clinic B had 3 expired nursing licenses flagged in March."
- Bad: "Nurse Jane Smith at Clinic B has an expired RN license, patient load of 40."

AI agents processing these ACCOUNT.md files must respect HIPAA constraints. The `hipaa` compliance flag in this config signals to any tool: do not output, store, or transmit PHI, even if it appears in a linked transcript or note.

## Conventions

- **Quarterly health reviews:** All network and enterprise accounts are reviewed quarterly. Clinic accounts are reviewed at renewal only.
- **Fiscal year:** Most healthcare networks run on a September 30 fiscal year end (following the federal fiscal year). Budget windows are typically July-September.
- **Verification tracking:** We use the sub-document approach (`verification-log.md`) for all network and enterprise accounts. Clinic accounts use inline verification.
- **Archive cadence:** Signal log entries older than 24 months are archived to `history.md`. Healthcare compliance history is retained longer than the default 12 months because audit lookback periods can extend to 3 years.
