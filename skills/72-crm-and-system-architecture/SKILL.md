---
name: crm-and-system-architecture
description: Design the CRM and GTM systems architecture, including systems of record, field ownership, sync logic, automation, routing and data governance.
---

# CRM and system architecture

> The CRM should reflect the commercial model, not become the commercial model.

## Map systems

Possible systems:
- product database
- analytics
- CDP/event pipeline
- marketing automation
- CRM
- billing
- support
- enrichment
- data warehouse
- BI
- customer success

## For each field/object decide

- system of record
- source
- owner
- sync direction
- update frequency
- historical requirement
- overwrite rules

## Automation categories

- identity enrichment
- account matching
- lifecycle updates
- routing
- SLA alerts
- PQL sync
- opportunity updates
- renewal/expansion
- attribution capture

## Guardrails

Avoid:
- circular syncs
- hidden field transformations
- automation with no owner
- stale enrichment silently overwriting first-party data
- excessive mandatory fields
- stage automation that outruns human judgment

## Output

Write:
`docs/gtm-cofounder/revops-systems.md`
