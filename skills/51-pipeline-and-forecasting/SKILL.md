---
name: pipeline-and-forecasting
description: Build stage definitions, pipeline math, coverage, conversion analysis and evidence-based forecasting for a sales-led motion.
---

# Pipeline and forecasting

> Forecasting is not asking reps for confidence percentages. It is estimating outcomes from process evidence and historical conversion.

## Stage architecture

Each stage requires:
- entry criteria
- exit criteria
- expected customer action
- seller action
- required fields
- typical risk

Never stage by seller activity alone, such as "demo completed."

## Funnel metrics

Track:
- target → engaged
- engaged → qualified conversation
- conversation → opportunity
- opportunity → evaluation
- evaluation → business case/decision
- decision → procurement
- procurement → won
- win rate
- sales cycle
- ACV
- pipeline created
- pipeline coverage
- slippage
- no-decision rate

Segment by:
- source
- ICP tier
- ACV
- product-led vs outbound vs inbound
- rep
- use case
- geography where relevant

## Coverage

Required coverage depends on stage conversion and timing.

Do not impose universal 3x/4x coverage.
Derive:
`needed open pipeline = target bookings / expected win rate`, adjusted for time and stage mix.

## Forecast categories

Example:
- Pipeline
- Best case
- Commit
- Closed

Define objective criteria for each.

## Forecast inspection

Check:
- stage age
- next step
- close-date movement
- missing buyer
- missing champion
- procurement timing
- historical conversion
- cohort/source quality

## Output

Write `docs/gtm-cofounder/sales-scorecard.md` and update roadmap.
