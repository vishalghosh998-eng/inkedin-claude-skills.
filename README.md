# LinkedIn Claude Skills

Claude Code skills for LinkedIn content research and strategy.

## Included skills

- `icp-research-agent` — researches the ideal customer profile and produces an ICP Brief.
- `outlier-agent` — identifies posts that materially outperform a creator's baseline and extracts reusable patterns.
- `newsjacking-agent` — finds and verifies recent industry news and develops newsjacking angles.

## Structure

```text
.claude/
└── skills/
    ├── icp-research-agent/
    │   ├── SKILL.md
    │   └── references/
    ├── outlier-agent/
    │   ├── SKILL.md
    │   ├── references/
    │   └── scripts/
    └── newsjacking-agent/
        ├── SKILL.md
        └── references/
```

## Claude Code usage

Clone this repository into a project and Claude Code can use the skills from `.claude/skills/`.

The intended workflow is:

1. Run `icp-research-agent` first to establish the ICP and buyer-content context.
2. Use `outlier-agent` to study what is outperforming among relevant creators.
3. Use `newsjacking-agent` to identify timely stories and angles relevant to the ICP.

These files are preserved from the supplied skill packages; no substantive skill instructions were rewritten.
