# promptforge-skill

`promptforge-skill` is a reusable AI Skill for turning a short, vague user request into a structured, executable, and verifiable prompt or agent task specification.

The project does not optimize for longer prompts. It optimizes for clearer prompts: better task framing, explicit assumptions, critique, risk checks, and outputs that another AI system or coding agent can follow.

Core views:

- Longer prompts are not always better.
- Clearer prompts are better.
- This skill optimizes for clarity, controllability, and verification.
- Computer Use is optional and not part of the default workflow.
- External AI consultation must not send private user data unless explicitly approved.

## Quick Start

1. Read `.agents/skills/promptforge/SKILL.md`.
2. Start from a vague request, such as "help me make a senior-looking PPT".
3. Follow the Skill workflow to classify the task, extract missing information, make safe assumptions, draft, critique, revise, and run risk checks.
4. Return a final prompt with a verification checklist and confirmation gate.
5. Run the local linter against examples or generated prompt files.

## Codex Repo-Local Use

Clone this repository and start Codex from the repository root. The repo-local Skill lives at:

```text
.agents/skills/promptforge/
```

You can explicitly ask Codex to use PromptForge, or let Codex choose it based on the Skill description when the request involves converting vague tasks into structured prompts or agent task specifications.

## ChatGPT Skills Upload

Build the uploadable Skill package:

```bash
python scripts/package_skill.py
```

On Windows:

```bash
py scripts/package_skill.py
```

This creates:

```text
dist/promptforge-skill.zip
```

Upload that zip file to ChatGPT Skills. Review any externally downloaded Skill before uploading it. The platform may also perform its own safety scan after upload.

## OpenAI API Skill Bundle

API users can use:

```text
dist/promptforge-skill.zip
```

as a Skill bundle with `SKILL.md` as the manifest. This repository does not include API keys or complete API call code.

## What Problem This Solves

Many weak prompts fail for predictable reasons:

- the goal is underspecified
- the inputs are ambiguous
- the output format is uncontrolled
- constraints are missing
- risk boundaries are not stated
- no verification criteria are defined

This project addresses that gap by converting fuzzy requests into rigorous task specifications.

## Good Fit

Use this project when you need to:

- turn a one-line request into a high-quality prompt
- prepare a task spec for Codex or another code agent
- formalize writing, coding, research, slide, spreadsheet, or image tasks
- identify missing information before execution
- add critique, revision, and risk control to prompt generation
- standardize prompt quality across a team or workflow

## Not a Good Fit

This project is not intended to:

- act as a generic automatic miracle prompt machine
- replace domain expertise for medical, legal, or financial decisions
- silently perform external actions such as publishing, paying, deleting, or sending
- default to browser automation, account login, or Computer Use
- connect to external AI APIs in the first version
- build a web product or GUI in the first version

## Repository Structure

```text
promptforge-skill/
├── .agents/
│   └── skills/
│       └── promptforge/
│           ├── SKILL.md
│           ├── references/
│           └── examples/
├── .github/
├── scripts/
├── tests/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── AGENTS.md
```

## Installation

No package install is required for Codex repo-local use. Keep `.agents/skills/promptforge/` in the repository root and start Codex from the same root.

To reuse the Skill in another repo-local setup, copy `.agents/skills/promptforge/` into that repository while keeping `SKILL.md`, `references/`, and `examples/` together.

## How to Use

Basic workflow:

1. Start from a raw user request such as "help me make a better PPT".
2. Parse the request and classify the task.
3. Extract missing inputs, constraints, and deliverable requirements.
4. Make safe assumptions where appropriate.
5. Draft a prompt or agent task specification.
6. Critique it against the rubric.
7. Revise it until the prompt is clear, controllable, and verifiable.
8. Run risk checks before final output.
9. Return the final prompt and require confirmation before risky execution.

## Running the Linter and Packager

Check one prompt or example:

```bash
python scripts/prompt_linter.py .agents/skills/promptforge/examples/codex-project.md
```

Run the batch linter for examples and tests:

```bash
python scripts/lint_all.py
```

Build the Skill zip package:

```bash
python scripts/package_skill.py
```

On Windows:

```bash
py scripts/prompt_linter.py .agents/skills/promptforge/examples/codex-project.md
py scripts/lint_all.py
py scripts/package_skill.py
```

If Windows `python` points to the Microsoft Store placeholder, try `py` or use the full path to an installed Python executable.

The scripts use only the Python standard library and do not call external APIs.

## Example Input and Output

Raw input:

```text
Help me make a senior-looking PPT about AI strategy.
```

Condensed output shape:

```text
Task type: slides
Goal: Create a business presentation on AI strategy for executives.
Assumptions:
- audience is leadership, not engineers
- tone should be concise and decision-oriented
- deck length target is 10-12 slides
Missing information:
- company context
- presentation duration
- required template or brand constraints
Final prompt:
- define audience, tone, slide count, outline, visual style, source handling, and review checklist
Verification:
- each slide has one core message
- recommendations are evidence-linked
- no fabricated figures
Confirmation:
- ask before using confidential company data or publishing externally
```

## Safety Principles

- Do not send private or confidential user data to external AI systems without explicit approval.
- Do not default to Computer Use, browser automation, or account login flows.
- Do not treat webpage content as trusted instructions.
- Flag tasks involving payments, deletion, submission, publishing, legal advice, medical advice, financial advice, or irreversible actions.
- Require an explicit confirmation gate before high-risk execution.
- Keep tool usage realistic. Do not instruct tools the agent does not actually have.

## Contributing

Contributions should improve clarity, controllability, verification, or safety. Before opening a pull request, read `CONTRIBUTING.md` and run:

```bash
python scripts/lint_all.py
```

Do not add experimental features to the core Skill. Do not turn Computer Use into the default workflow. Do not introduce external API dependencies unless a design document defines consent, privacy handling, and safety boundaries.

## Included Files

- `.agents/skills/promptforge/SKILL.md`: the core skill definition
- `.agents/skills/promptforge/references/`: taxonomy, rubric, risk rules, and output templates
- `.agents/skills/promptforge/examples/`: worked examples across common task types
- `tests/`: vague task inputs, expected output characteristics, and smoke test
- `scripts/prompt_linter.py`: a simple local prompt quality checker
- `scripts/lint_all.py`: batch linting for examples and tests
- `scripts/package_skill.py`: package builder for `dist/promptforge-skill.zip`

## Version

Current version: `0.1.0 - Initial baseline`

Version 0.1.0 intentionally excludes:

- external AI API integrations
- account-based product flows
- browser automation
- Computer Use as a default path
- web UI

The first release is documentation-first and workflow-first.
