---
name: lifecycle-and-stage-definitions
description: Create one canonical lifecycle across product, marketing, sales and customer teams with objective entry/exit criteria and no conflicting definitions.
---

# Lifecycle and stage definitions

> A lifecycle stage is a state with meaning, not a label a team can reinterpret.

## Suggested lifecycle

Adjust to business model:

```text
Anonymous
→ Known
→ Signup
→ Activated
→ Retained
→ PQL/PQA
→ Sales accepted / Qualified
→ Opportunity
→ Evaluation
→ Decision
→ Procurement
→ Customer
→ Expansion-ready
→ Expansion
→ Renewal
→ Advocate
```

## For every stage define

- unit: person/account/workspace/opportunity
- entry criteria
- exit criteria
- owner
- SLA
- required fields
- allowed regressions
- terminal outcomes
- reporting logic

## Rules

- Do not use activity alone as stage.
- Do not allow reps to advance without evidence.
- Do not let marketing create stages that sales ignores.
- Keep product lifecycle and account lifecycle distinct where needed.
- Preserve historical state transitions.

## Output

Write:
`docs/gtm-cofounder/lifecycle-definitions.md`
