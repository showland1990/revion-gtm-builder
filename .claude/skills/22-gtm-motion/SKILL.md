---
name: gtm-motion
description: Design how PLG, sales-led growth, revenue marketing and RevOps fit together around the same ICP, buying journey and evidence. Use after the GTM foundation is established.
---

# GTM motion architecture

> The choice is rarely "PLG or sales-led." The question is where product should do the work, where marketing should do the work, and where a human materially improves conversion or deal size.

Read `docs/gtm-cofounder/gtm-context.md`.

## Decide motion by buying reality

Assess:

- time-to-value
- product complexity
- implementation effort
- individual vs team value
- buyer/user overlap
- ACV
- procurement/security
- number of stakeholders
- market size
- product usage signals
- expansion potential

## PLG is strongest when

- users can reach value without a human
- product can be discovered/tried easily
- value is observable through usage
- a free/trial motion accelerates adoption
- small teams can buy with low friction
- usage creates expansion signals

## Sales-led is strongest when

- ACV justifies human effort
- evaluation is complex
- implementation is organizational
- buyer differs from user
- security/procurement are meaningful
- multiple stakeholders must agree
- business case matters

## Hybrid pattern

A common default:

```text
Demand / discovery
      |
      v
Self-serve product
      |
      v
Activation / retained usage
      |
      +--> low-value / low-fit --> lifecycle nurture
      |
      +--> high-fit + intent --> PQL/PQA --> sales assist
                                      |
                                      v
                              discovery / evaluation
                                      |
                              champion / business case
                                      |
                                  enterprise
```

## Define the PLG engine

- acquisition
- signup
- activation
- engagement
- retention
- monetization
- expansion
- PQL/PQA

For every stage define:
- event
- baseline if known
- target later
- primary friction
- owner
- next experiment

## Define the sales-led engine

- account selection
- outbound / inbound qualification
- discovery
- evaluation/demo
- champion
- multithreading
- business case
- security/procurement
- close
- expansion

For every stage define:
- entry criteria
- exit criteria
- buyer/stakeholder
- required evidence
- primary risk

## Define sales-assist boundary

Specify:
- fit threshold
- product behavior
- intent signal
- account size / potential
- reason a human helps
- SLA / next action

Do not trigger sales merely because someone signed up.

## Define revenue marketing around states

Lifecycle should support:
- anonymous/high-intent visitor
- new signup
- unactivated user
- activated user
- retained user
- PQL
- active opportunity
- customer
- expansion-ready customer
- advocate

## Define RevOps instrumentation

Canonical objects:
- person
- account
- product workspace/org
- PQL/PQA
- lead/contact
- opportunity
- customer

Canonical stages:
- visitor
- signup
- activation
- retained
- PQL
- SQL/opportunity
- customer
- expansion

Specify how product identity maps to account and CRM identity.

## Output

Add a "GTM architecture" section to `gtm-context.md` with:
- primary motion
- secondary motion
- PLG funnel
- sales funnel
- sales-assist triggers
- revenue-marketing lifecycle
- data model / handoffs
- top 3 bottlenecks
