---
name: funnel-and-pipeline-math
description: Build funnel math from traffic and product usage through pipeline and bookings, including stage conversion, velocity, coverage and source/segment decomposition.
---

# Funnel and pipeline math

> Revenue planning is conversion math plus timing. If assumptions are invisible, plans become wishful thinking.

## Build the model

Examples:

PLG:
```text
Qualified visitors
× signup rate
× activation rate
× retained rate
× paid/PQL rate
× ACV
```

Sales:
```text
Target accounts
× engagement rate
× qualified conversation rate
× opportunity rate
× win rate
× ACV
```

Pipeline:
```text
Pipeline created
× win rate
÷ sales-cycle timing
= expected bookings contribution
```

## Decompose

Always split where meaningful by:
- source
- segment
- ACV band
- motion
- geography
- rep/team
- product-led vs sales-led

## Velocity

Track:
- stage age
- median days per stage
- full sales cycle
- slippage
- reopen/regression

## Coverage

Do not use universal coverage multiples.

Derive required pipeline:
- target bookings
- expected win rate
- time remaining
- stage mix
- creation rate

## Output

Write/update:
`docs/gtm-cofounder/revenue-model.md`
