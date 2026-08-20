---
name: pql-pqa-model
description: Define product-qualified leads/accounts using ICP fit, realized product value, intent and expansion potential, then create explainable scoring and sales-assist thresholds.
---

# PQL / PQA model

> A PQL is not "someone used the product a lot." It is an account where fit + realized value + buying/expansion signal make human help economically useful.

Prefer account-level qualification for B2B: PQA, even if the operational label remains PQL.

## Four signal families

### 1. Fit
Company size, segment, industry, technical environment, geography, estimated spend/ACV potential.

### 2. Value
Activation, retained usage, repeated core behavior, multiple use cases, team adoption.

### 3. Intent
Pricing views, enterprise feature attempts, plan-limit reached, security docs, procurement/security questions, demo/contact requests.

### 4. Expansion
Multiple users, multiple teams, rapid usage growth, strategic integration, additional workspace/project creation.

## Negative signals

Student/personal, tiny anti-ICP company, one-off usage, internal/test, activation failure, churned/inactive, unsupported geography/use case.

## Scoring principles

Keep the model explainable. Example:

```text
Fit:       0-40
Value:     0-30
Intent:    0-20
Expansion: 0-10
Penalties: 0 to -50
```

Weights are hypotheses, not universal truths.
Calibrate with historical opportunities, meetings, conversion, ACV and win rate where possible.

## Thresholds

Define states such as nurture, product lifecycle, marketing assist, sales assist and urgent sales action.
For each state define threshold, reason, owner, SLA, action and suppression rules.

## PQL reason codes

Never send sales a naked score. Attach:
- why now
- product behavior
- account fit
- likely use case
- likely champion
- suggested outreach hypothesis

## Output

Write `docs/gtm-cofounder/pql-model.md` using the template.
