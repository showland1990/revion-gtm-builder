---
name: plg-experimentation
description: Prioritize and design PLG experiments with explicit hypotheses, guardrails, segment analysis and learning logs so growth work compounds instead of becoming random A/B tests.
---

# PLG experimentation

> Experiments exist to reduce uncertainty and move a constrained metric, not to keep a growth team busy.

## Start from the bottleneck

Read roadmap and PLG model. Choose one constrained stage.

## Experiment brief

Every experiment must state:
- Observation
- Problem
- Hypothesis
- Segment
- Change
- Primary metric
- Guardrail metrics
- Expected direction
- Minimum runtime/sample logic if known
- Decision rule
- Owner
- Result
- Learning

## Prioritization

Score:
- expected impact
- confidence
- effort
- speed to learn
- reversibility
- strategic learning

Prefer experiments that both improve performance and reveal something about user behavior.

## Guardrails

Possible guardrails include downstream activation, retention, support load, revenue, refund/churn, latency/reliability and acquisition quality.
Never optimize signup conversion at the expense of activation quality without noticing.

## Segment effects

Check ICP, use case, company size, channel, plan and new vs existing user. A global average can hide the strategy.

## Learning log

Write experiments to `docs/gtm-cofounder/plg-experiments.md`.
Update foundational evidence when an experiment materially validates or disproves a belief.
