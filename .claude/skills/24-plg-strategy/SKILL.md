---
name: plg-strategy
description: Design the complete product-led growth system from acquisition through activation, retention, monetization, expansion and sales assist. Use after the GTM foundation is coherent and PLG is a primary or supporting motion.
---

# PLG strategy

> PLG is not "put a free tier on it." Product-led growth means the product carries meaningful work across acquisition, evaluation, activation, retention, monetization and expansion.

Read first:
1. `docs/gtm-cofounder/gtm-context.md`
2. `docs/gtm-cofounder/foundation-review.md` if available
3. `docs/gtm-cofounder/plg-model.md` if it exists
4. current product analytics / event definitions if available

If the foundation is weak on ICP, pain, value or motion architecture, route back before scaling PLG.

## First decide whether PLG is actually appropriate

Score each as strong / medium / weak:
- product can be tried without a salesperson
- time-to-value is short
- user can experience value before procurement
- user and buyer overlap at least for smaller accounts
- adoption can spread bottom-up
- product behavior can signal value and intent
- marginal cost of trial/free usage is tolerable
- pricing can support self-serve or sales-assist
- product has a repeatable retained behavior

PLG can still support a sales-led business if product evaluation/adoption happens before purchase.

## Define the PLG equation

```text
Qualified Acquisition
× Signup Conversion
× Activation
× Retention
× Monetization
× Expansion
= Product-led revenue growth
```

Do not optimize a stage in isolation.

## Define canonical states

Write concrete behavioral definitions for:
- Visitor
- Qualified visitor
- Signup
- Setup complete
- Activated user
- Activated account/workspace
- Engaged user
- Retained account
- Monetized account
- Expansion-ready account
- PQL / PQA
- Sales-assisted account
- Advocate

A state cannot be "logged in." It must represent progress toward customer value.

## Choose the unit of analysis

Explicitly define:
- person/user
- account/company
- workspace/org/team
- paid subscription
- opportunity

Then decide which unit owns activation, retention, PQL and expansion.

## Identify the North Star behavior

Ask:
1. What repeated behavior is closest to delivered value?
2. Does it predict retention?
3. Does it predict expansion/revenue?
4. Can the user influence it?
5. Can the business instrument it reliably?

Do not choose revenue as the product North Star if it gives no behavioral guidance.

## Build the model

For each stage capture:
- event definition
- unit
- baseline
- segment split
- target later
- primary friction
- hypotheses
- experiments
- owner
- downstream effect

## Diagnostic order

Always diagnose in this order:
1. Is acquisition reaching the right ICP?
2. Can they start?
3. Do they activate?
4. Do activated users retain?
5. Does retained usage monetize?
6. Do good accounts expand?
7. Can high-fit/high-intent accounts be handed to sales?

Do not scale acquisition before activation/retention are credible.

## Output

Write `docs/gtm-cofounder/plg-model.md` using `plg-model.template.md`.
Then route to the stage with the largest evidence-backed constraint.
