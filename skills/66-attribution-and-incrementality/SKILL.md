---
name: attribution-and-incrementality
description: Build a practical revenue attribution system combining first-party touch data, self-reported attribution, account journeys, experiments and confidence levels without claiming false causal precision.
---

# Attribution and incrementality

> Attribution is evidence about contribution. Causality requires stronger proof than a CRM touch.

## Data layers

Use together:

### First-party journey
- source/referrer
- campaign
- content
- product
- account
- opportunity

### Self-reported attribution
"How did you first hear about us?"
Keep free text when possible.

### Sales/customer evidence
Discovery notes:
- how they found you
- what influenced evaluation
- who shared it internally

### Experiments
- holdouts
- geo/account tests
- time-based tests
- budget changes
where feasible

## Attribution views

Maintain separate views:
- first touch
- lead/signup creation
- opportunity creation
- last meaningful touch
- self-reported
- influenced journey

Do not collapse them into one magic model.

## Confidence

Tag contribution:
- high confidence
- medium confidence
- weak/directional

Examples:
High:
tracked high-intent campaign → opportunity, confirmed by buyer

Medium:
multiple known touches + self-report supports channel

Weak:
cookie touch among many with no corroboration

## Incrementality

Ask:
"Would this outcome likely have happened without the program?"

For material spend, seek stronger evidence through:
- holdout
- matched accounts
- geography
- cohort comparison
- before/after with confounder checks

## Output

Write:
`docs/gtm-cofounder/attribution-model.md`
