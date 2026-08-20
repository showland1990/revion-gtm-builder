# GTM Co-Founder — Full Claude Skill Set

A complete Claude-ready GTM operating system for developer tools, AI products and technical B2B companies.

## 85 modular GTM skills

This repository covers:

- GTM foundation and customer discovery
- ICP, segmentation, category, positioning and messaging
- PLG acquisition, activation, retention, monetization and expansion
- PQL / PQA and product-led sales
- account selection and trigger-based outbound
- enterprise discovery and qualification
- demos, evaluations and pilots
- champion building and multithreading
- business case / ROI
- security, procurement and negotiation
- pipeline, forecasting and opportunity inspection
- revenue marketing
- content, inbound, search, ABM, events and partnerships
- customer and expansion marketing
- attribution and incrementality
- RevOps
- revenue data models and lifecycle definitions
- unit economics
- capacity and revenue planning
- executive dashboards
- weekly, monthly and quarterly GTM operating reviews

## Architecture

```text
START HERE
    |
    v
GTM FOUNDATION
    |
 +--+------------------+
 |                     |
 v                     v
PLG                  SALES
 |                     |
 +------ PQL/PQA ------>|
 |                     |
 +----------+----------+
            |
            v
   REVENUE MARKETING
            |
            v
          REVOPS
            |
            v
   OPERATING CADENCE
            |
            v
         ROADMAP
```

## Repository structure

```text
CLAUDE.md

.claude/
  gtm-routing.md
  gtm-artifacts.md
  SKILL-CATALOG.md
  skills/
    00-start-here/
    ...
    84-gtm-orchestrator/

skills/
  00-start-here/
  ...
  84-gtm-orchestrator/

templates/
docs/gtm-cofounder/
tests/
scripts/

.claude-plugin/
  plugin.json
  marketplace.json
```

`.claude/skills/` is the Claude Code project skill source.

Root `skills/` is an exact mirror for GitHub-link / Agent Skills installation workflows.

## Skill ranges

| Range | System |
|---|---|
| 00–17 | Original GTM core |
| 18–23 | GTM foundation expansion |
| 24–36 | PLG engine |
| 37–52 | Sales-led + enterprise |
| 53–68 | Revenue marketing |
| 69–83 | RevOps + GTM management |
| 84 | Intelligent GTM orchestrator |

## Start with Claude Code

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
claude
```

Then:

```text
Run start-here with me.
```

Or:

```text
Act as my GTM Co-Founder. Read the project instructions, diagnose the single biggest commercial constraint, and route yourself to the correct skill. Do not make me choose from the skill catalog.
```

See `CLAUDE-INSTALL.md` for global skill and plugin-style installation.

## Intelligent routing

Users describe symptoms, not skill numbers.

### "We have 8,000 signups but almost no revenue."

```text
acquisition quality
→ activation
→ retention
→ monetization
→ PQL/PQA
→ product-led sales
```

### "We need more pipeline."

```text
foundation
→ demand capture
→ product signals
→ account selection
→ outbound
→ opportunity conversion
```

### "Enterprise deals keep slipping."

```text
qualification
→ discovery
→ champion
→ economic buyer
→ evaluation
→ business case
→ security/procurement
→ commercials
```

## Persistent company state

Claude maintains live GTM working state under:

```text
docs/gtm-cofounder/
```

including the founder brief, GTM context, roadmap, PLG model, PQL model, sales model, opportunity files, revenue marketing model, RevOps model, forecast and operating reviews.

## Validate the repository

```bash
python tests/validate_skills.py
python tests/validate_root_skills.py
```

Expected:

- 85 project skills
- continuous `00–84` numbering
- unique metadata
- root `skills/` exactly mirrors `.claude/skills/`
- 23 canonical templates

## License

MIT. See `LICENSE`.
