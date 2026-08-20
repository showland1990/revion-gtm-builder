---
name: segmentation
description: Turn the GTM context into a prioritized market segmentation and a sharp primary ICP. Use after gtm-foundation, before messaging, PLG targeting, outbound account selection or ABM.
---

# Segmentation and ICP

> Segmentation is not slicing a TAM into demographics. It is finding groups that behave differently enough to require a different GTM decision.

Read `docs/gtm-cofounder/gtm-context.md` first.

## Segment only on variables that change something

A segmentation variable matters if it changes one or more of:
- pain intensity
- urgency
- product fit
- time-to-value
- willingness to pay
- buying process
- sales cycle
- retention
- expansion
- reachability

Candidate variables:
- company stage / size
- engineering-team size
- industry
- regulatory burden
- technical stack / architecture
- team topology
- workflow maturity
- deployment model
- data / usage scale
- trigger event
- geography

## Process

1. Generate 3 to 7 plausible segments from observed differences.
2. For each segment, summarize:
   - problem
   - trigger
   - fit
   - buyer
   - economics
   - reachability
   - evidence
3. Score qualitatively: strong / medium / weak on:
   - pain
   - urgency
   - product fit
   - ability to pay
   - reachability
   - proof
   - expansion
4. Force a primary segment.
5. Define a secondary segment only if meaningfully distinct.
6. Define anti-ICP.
7. Write explicit disqualifiers.
8. Update `gtm-context.md`.

## ICP test

A strong ICP lets a stranger answer:
- Is this account in or out?
- What probably just happened?
- Who likely cares?
- What pain likely exists?
- Why is our product unusually suited?
- Why might they buy now?

If not, sharpen it.

## Output

Write:

### Primary ICP
- company shape
- team shape
- technical context
- trigger
- pain
- buyer
- budget logic
- why we win
- disqualifiers
- evidence status

### Secondary ICP
Only if justified.

### Anti-ICP
Who to avoid and why.

### Targeting implications
- PLG acquisition
- PQL fit
- outbound account criteria
- ABM eligibility
