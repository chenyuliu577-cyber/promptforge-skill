# Contributing

Thank you for helping improve `promptforge-skill`. This project is intentionally small, local-first, and documentation-led.

## Project Goal

PromptForge turns vague user requests into structured, executable, and verifiable prompts or agent task specifications. The focus is task specification, critical review, risk control, and final prompts that another agent can actually follow.

Do not present the project as a universal prompt machine or magic prompt generator.

## Welcome Contributions

- clearer Skill rules
- better examples for common task types
- stronger risk and confirmation checks
- improved prompt quality tests
- small standard-library scripts that improve local validation
- documentation fixes that make the project easier to use

## Unwelcome Contributions

- broad feature expansion without a clear design
- experimental features mixed into the core Skill
- complex dependencies without a strong reason
- claims that longer prompts are always better
- turning Computer Use into the default workflow
- external API dependencies without a design document and safety boundary
- browser automation, login flows, or account-based workflows in the core project

## Documentation Rules

- Write clear, direct, executable documentation.
- Prefer concrete rules and examples over abstract advice.
- Keep marketing language out of the project.
- Explain safety boundaries whenever a workflow can affect external systems or private data.

## Skill Modification Rules

- Keep `.agents/skills/promptforge/SKILL.md` concise and directive.
- Preserve the core workflow: parse, classify, extract, identify gaps, assume safely, draft, critique, revise, check risk, output with confirmation.
- If `SKILL.md` changes, review `examples`, `references`, and `tests` in the same pull request.
- Do not add Computer Use as a default path.
- Do not introduce external AI API usage unless the design explicitly covers privacy, consent, and what data is sent.

## Example Modification Rules

Every example should include:

- original vague request
- task analysis
- key assumptions
- optimized final prompt
- risk check
- user confirmation point
- checklist

Examples should show practical control, not prompt bloat.

## Test Requirements

- Update `tests/vague-tasks.md` when adding a new task family.
- Update `tests/expected-outputs.md` when Skill behavior changes.
- Keep `tests/smoke-test.md` aligned with the current workflow.
- Run the linter before opening a pull request.

## Pull Request Checklist

- The change keeps the project local-first and dependency-light.
- No external API, secret, or account requirement was added without a written safety design.
- `SKILL.md`, examples, references, and tests remain consistent.
- Computer Use remains optional and non-default.
- The project is not described as a magic or universal prompt generator.
- `python scripts/lint_all.py` passes locally, or the PR explains why it could not be run.
