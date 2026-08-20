---
name: revenue-data-model
description: Define the canonical cross-system data model connecting anonymous visitors, users, workspaces, accounts, leads/contacts, PQL/PQA, opportunities, customers, subscriptions and expansion.
---

# Revenue data model

> Revenue teams cannot share a funnel if they do not share the same objects and relationships.

## Canonical objects

At minimum consider:
- anonymous visitor
- person
- product user
- workspace/org/team
- company/account
- subscription
- lead/contact
- PQL/PQA
- campaign/program
- opportunity
- customer
- contract
- expansion opportunity

## For each object define

- system of record
- unique key
- creation event
- merge rules
- parent/child relationship
- ownership
- retention/history needs
- sensitive fields

## Critical joins

Document how to connect:

```text
anonymous visitor
→ known person
→ product user
→ workspace
→ company/account
→ CRM contact
→ PQL/PQA
→ opportunity
→ contract/subscription
→ expansion
```

## Identity pitfalls

Watch for:
- one person in multiple workspaces
- one company with multiple domains
- consultants using customer domains
- freemail vs corporate email
- subsidiaries
- merged/acquired accounts
- historical membership
- shared workspaces
- duplicate CRM records

## Output

Write:
`docs/gtm-cofounder/revenue-data-model.md`
