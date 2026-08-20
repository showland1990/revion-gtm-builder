# Upload this repository to GitHub

## Recommended: Git command line

1. Unzip this package.
2. Open a terminal inside `gtm-cofounder-claude-github/`.
3. Run:

```bash
git init
git add .
git commit -m "Initial GTM Co-Founder Claude skill set"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## GitHub website

You can also create a blank repository and upload the extracted contents.

Make sure the hidden `.claude/` and `.claude-plugin/` folders are uploaded. If your browser file picker hides dot-folders, use GitHub Desktop or Git from the terminal instead.

## After upload

Edit `.claude-plugin/plugin.json` and replace:

`https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME`

with your actual repository URL.
