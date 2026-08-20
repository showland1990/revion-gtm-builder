---
name: plg-lifecycle
description: Design behavior-triggered lifecycle communication across signup, activation, retention, monetization, PQL, customer and expansion states, coordinated across in-product, email and human touch.
---

# PLG lifecycle

> Lifecycle is not a drip campaign. It is the right intervention for the user's current product state.

## State model

Design separately for:
- visitor / started signup
- signed up, not set up
- setup, not activated
- activated
- engaged
- at-risk
- retained
- monetization-ready
- PQL/PQA
- paid
- expansion-ready
- advocate

## For each state define

- desired next behavior
- barrier
- value reminder
- proof
- channel
- trigger
- delay
- exit condition
- suppression
- measurement

## Intervention hierarchy

Prefer:
1. product UX
2. contextual in-product guidance
3. triggered email/message
4. human assistance

Do not use email to compensate permanently for broken product UX.

## Behavioral triggers

Examples: setup stalled, integration failed, activation incomplete, first value reached, collaborator invited, inactivity after prior value, limit reached, enterprise feature attempted, rapid account growth, paid milestone, renewal/expansion signal.

## Message principle

Each message contains context, one value and one next action.
Avoid generic feature education.

## Coordination

Suppress marketing nurture during active sales opportunities, support incidents, unsubscribe or inappropriate account state.
Define ownership between product, lifecycle marketing, customer success and sales.

## Output

Write `docs/gtm-cofounder/plg-lifecycle.md` using the template.
