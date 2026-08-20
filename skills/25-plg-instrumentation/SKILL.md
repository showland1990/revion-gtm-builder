---
name: plg-instrumentation
description: Define the product analytics event model, identities, funnel states, cohorts and properties needed to operate PLG and connect product usage to CRM, revenue and sales assist.
---

# PLG instrumentation

> If product, marketing and sales cannot agree what an activated account is, PLG is not measurable.

Read `gtm-context.md` and `plg-model.md`.

## Start from decisions, not events

Before naming events ask:
- What decision will this metric change?
- What behavior represents value?
- At user or account level?
- What segmentation is required?
- What downstream system needs the signal?

Do not instrument every click.

## Canonical identity model

Define:
- `user_id`
- `anonymous_id`
- `workspace_id` / `org_id`
- `account_id`
- `subscription_id`
- `crm_account_id`
- `crm_contact_id`
- `opportunity_id`

Specify merge/association logic.

Critical problem: how does anonymous web behavior become a product user, then a company/account, then a CRM opportunity?

## Event taxonomy

Use consistent verbs and objects, for example:
- `account_created`
- `workspace_created`
- `integration_connected`
- `project_created`
- `first_value_completed`
- `member_invited`
- `core_action_completed`
- `limit_reached`
- `upgrade_viewed`
- `plan_upgraded`
- `enterprise_feature_attempted`

For each event document:
- definition
- firing condition
- unit
- properties
- exclusions
- owner
- data source

## Core derived metrics

Define formulas for:
- visitor → signup
- signup → setup
- signup → activation
- median time-to-value
- activated → retained
- free → paid
- PQL rate
- expansion rate
- activation by acquisition source
- retention by activation path
- monetization by segment

## Cohorts

Minimum cuts:
- signup week/month
- acquisition source
- ICP segment
- company size
- primary use case
- plan
- activation path

## Data quality checks

- event fires once where expected
- bot/test/internal traffic excluded
- identity merges are correct
- account membership is historical, not only current
- event semantics are stable
- timestamps/timezones are consistent
- backfills are documented

## Output

Write `docs/gtm-cofounder/plg-instrumentation.md` using the template.
