---
name: revops-review
description: Audit the entire revenue operations system for conflicting definitions, unreliable data, broken handoffs, stage inflation, reporting gaps and operational debt.
---

# RevOps review

> Operational debt accumulates quietly until nobody trusts the funnel.

## Review areas

Score Red / Amber / Green:
- identity/account matching
- lifecycle definitions
- CRM object model
- product→CRM sync
- PQL routing
- inbound routing
- stage criteria
- required fields
- pipeline math
- forecast
- attribution
- unit economics
- renewal/expansion
- dashboard consistency
- operating cadence

## Tests

- Can two teams independently define the same stage?
- Can a user/account be traced across systems?
- Can a PQL become an opportunity without manual archaeology?
- Can a closed-won account map back to source and product behavior?
- Can forecast assumptions be explained?
- Can revenue plan assumptions be recomputed?
- Are stale fields driving decisions?
- Are dashboards using the same formulas?

## Output

Write:
`docs/gtm-cofounder/revops-review.md`

Then route the highest-risk issue.
