# AGENTS.md

This repository is maintained for reusable Skill design, not for feature sprawl.

## Maintenance Rules

- Do not add dependencies without a concrete maintenance or quality reason.
- Do not mix experimental features into the core Skill workflow.
- If `skill/promptforge/SKILL.md` changes, update the examples and tests in the same change.
- Keep all documentation clear, concise, and executable.
- Do not describe this project as an "automatic万能提示词神器" or an all-purpose magic prompt generator.
- The core focus is task specification, critical review, risk control, and final executable prompts.

## Repository Priorities

- Preserve the documentation-first architecture.
- Keep the default workflow tool-agnostic and local-first.
- Treat Computer Use as optional and separated from the baseline flow.
- Treat external AI consultation as opt-in and privacy-gated.
- Prefer explicit templates, rules, and examples over vague guidance.

## Editing Standards

- Favor direct language over marketing language.
- Avoid adding framework or product scaffolding unless the scope explicitly changes.
- Keep example prompts realistic about tools, permissions, and deliverables.
- Ensure any new example includes analysis, assumptions, final prompt, and checks.
- Ensure tests describe what a good output must contain, not just what it should sound like.

## Release Discipline

- New capabilities should first land as documentation, policy, or examples before automation.
- High-risk workflows must include confirmation gates and risk notes.
- If a change weakens clarity, controllability, or verification, it should be reconsidered.
