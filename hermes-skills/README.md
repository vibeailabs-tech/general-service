# AI Marketing Agent Team — Hermes Edition

Converted from the Claude Code system in `../.claude/` (16 agents + 75 commands)
to the [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
skill standard (agentskills.io): 76 skills under one `marketing/` category.

## What changed vs. the Claude version

| Claude Code | Hermes |
|---|---|
| `.claude/agents/agent-XX-*.md` (subagents, `model:`, `memory:`) | Folded into each skill as `## Agent Context`; `orchestrator` → `marketing-orchestrator` skill |
| `.claude/commands/<cat>/<skill>.md` | `marketing/<skill>/SKILL.md` |
| Long `description:` in frontmatter | `description:` ≤ 60 chars (Hermes hardline); full triggers moved to `## When to Use` |
| Duplicate skill names (`ab-test-setup`, `video-script`...) | Prefixed: `cro-ab-test-setup`, `ads-ab-test-setup`, `social-video-script`, `sales-page-writer`... |
| Mixed paths (`/profiles/brand.md`, `/outputs/...`) | Single standard: `outputs/profiles-output/brand.md`, outputs under `outputs/` |
| API keys in `.claude/settings.local.json` | `required_environment_variables` (Hermes prompts securely on load) |
| `.claude/commands/.../references/brand-md-schema.md` | `references/brand-md-schema.md` inside the 5 brand skills |

Each `SKILL.md` follows the Hermes body order: When to Use → Procedure →
Agent Context → Pitfalls → Verification.

## Install

Hermes must be installed first (`hermes --version`). Then:

```bash
./install.sh
# = cp -R marketing/ ~/.hermes/skills/marketing/
```

Alternative — external skill dir (no copying, edit in place):

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /Users/henryle/Desktop/general-service/hermes-skills
```

## Use

Every skill becomes a slash command in Hermes CLI / messaging:

```
/marketing-orchestrator     # check system state, route work
/brand-setup                # FIRST: builds outputs/profiles-output/brand.md
/market-research            # then research, strategy, execution...
/blog-writer viết bài về ...
```

Rule (enforced by the orchestrator): no execution skill runs before
`outputs/profiles-output/brand.md` exists. Run `/brand-setup` first.

## API keys (Research/SEO skills only)

Set in `~/.hermes/.env` or let Hermes prompt on skill load:
`OPENROUTER_API_KEY`, `FIRECRAWL_API_KEY`, `SERPAPI_KEY`.
Core brand/content/social/email skills need no keys.

## Regenerate

After editing the Claude sources in `../.claude/`, rebuild with:

```bash
python3 convert.py
./install.sh
```
