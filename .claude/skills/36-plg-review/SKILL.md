---
name: plg-review
description: Run a recurring operating review of the PLG funnel, diagnose the current constraint, distinguish measurement problems from product problems, and route the next highest-leverage work.
---

# PLG operating review

> Review the system as a chain. The weakest meaningful stage sets the pace.

Read `gtm-context.md`, `plg-model.md`, instrumentation, PQL model, lifecycle and experiment log.

## Scorecard

Review by segment and cohort where possible:

| Stage | Definition | Baseline | Trend | Segment issue | Confidence |
|---|---|---:|---|---|---|
| Qualified acquisition | | | | | |
| Signup | | | | | |
| Activation | | | | | |
| Time-to-value | | | | | |
| Retention | | | | | |
| Monetization | | | | | |
| Expansion | | | | | |
| PQL/PQA | | | | | |
| Sales-assist conversion | | | | | |

## Diagnose

Ask in order:
1. Is the data trustworthy?
2. Is the traffic/account mix changing?
3. Where is the biggest downstream-consequential loss?
4. Is that loss universal or segment-specific?
5. Is the root cause positioning, product, pricing, lifecycle or sales handoff?
6. What evidence would change our diagnosis?

## Avoid local optimization

Examples:
- more signups + worse activation = not a win
- more PQLs + lower opportunity conversion = scoring degraded
- higher monetization + worse retention = possible over-gating
- faster activation + no retention change = aha may be shallow

## Output

Update `plg-model.md`, roadmap, experiment priorities and evidence ledger.
Choose one primary constraint, then route to the relevant PLG skill.
