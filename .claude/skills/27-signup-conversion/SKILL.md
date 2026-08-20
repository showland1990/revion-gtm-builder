---
name: signup-conversion
description: Improve the transition from qualified visitor to started product experience by reducing unnecessary friction, aligning intent and preserving enough information for downstream activation and account identification.
---

# Signup conversion

> Signup is not the goal. Starting the right user's path to value is.

## Diagnose before removing friction

Ask:
- Who is trying to sign up?
- What intent brought them?
- What must happen before value?
- Which fields are actually required?
- Is signup necessary before first value?
- Does the product need a workspace, integration or code install first?

## Friction audit

Classify every step:
- required for product function
- required for security/legal
- useful for personalization
- useful only for marketing
- unnecessary

Remove or defer the last two unless evidence shows they improve downstream outcomes.

## Common patterns to consider

- no-signup sandbox
- OAuth/social auth
- magic links
- CLI-first install
- repo install
- SSO later, not first-run
- progressive profiling
- inferred company/account enrichment after signup

## Measure

Track:
- CTA click → signup start
- signup start → complete
- signup complete → first setup step
- time to signup
- errors
- abandonment step
- activation and retention by signup path

Never celebrate improved signup conversion if activation quality falls.

## Output

Document current path, friction inventory, target path, fields kept/deferred, hypotheses, instrumentation and experiment priority.
