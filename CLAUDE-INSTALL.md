# Link this GitHub repository to Claude

## 1. Claude Code: use the repository as the project

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
claude
```

Claude Code reads `CLAUDE.md` and discovers all project skills under `.claude/skills/`.

Recommended first prompt:

```text
Read CLAUDE.md and run start-here with me. Act as my GTM Co-Founder and maintain company state in docs/gtm-cofounder/.
```

## 2. Claude Code: install the skills globally

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cp -r YOUR_REPO_NAME/skills/* ~/.claude/skills/
```

## 3. Claude Code plugin marketplace pattern

This repository includes `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`.

After updating the placeholder repository URL, use:

```text
/plugin marketplace add YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
/plugin install gtm-cofounder@gtm-cofounder
```

## 4. Agent Skills-compatible use

The root `skills/` directory mirrors `.claude/skills/`, so tools that consume Agent Skills repositories can use the GitHub repository directly.

The canonical editable source is `.claude/skills/`.

After editing skills, run:

```bash
python scripts/sync_skills.py
```

to refresh the root mirror.

## Full GTM prompt

```text
Use the GTM Co-Founder skill system in this repository. Build or read my GTM foundation, diagnose the single biggest commercial constraint, then route yourself to the smallest correct skill. Do not make me choose skill numbers.
```
