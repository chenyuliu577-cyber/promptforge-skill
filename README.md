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

1. Read `skill/promptforge/SKILL.md`.
2. Start from a vague request, such as "help me make a senior-looking PPT".
3. Follow the Skill workflow to classify the task, extract missing information, make safe assumptions, draft, critique, revise, and run risk checks.
4. Return a final prompt with a verification checklist and confirmation gate.
5. Run the local linter against examples or generated prompt files.

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
|-- README.md
|-- LICENSE
|-- AGENTS.md
|-- CONTRIBUTING.md
|-- CHANGELOG.md
|-- scripts/
|   |-- prompt_linter.py
|   `-- lint_all.py
|-- skill/
|   `-- promptforge/
|       |-- SKILL.md
|       |-- references/
|       `-- examples/
|-- tests/
`-- .github/
    `-- workflows/
        `-- lint.yml
```

## Installation

No package install is required for the core Skill.

To copy the Skill into another workspace:

1. Copy `skill/promptforge/` into your local skills directory or project skill folder.
2. Keep the `references/` and `examples/` subfolders alongside `SKILL.md`.
3. Run the linter with Python 3 when validating prompt files.

Example layout in another repository:

```text
your-project/
`-- skill/
    `-- promptforge/
        |-- SKILL.md
        |-- references/
        `-- examples/
```

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

## Running the Linter

Check one prompt or example:

```bash
python scripts/prompt_linter.py skill/promptforge/examples/codex-project.md
```

Run the batch linter for examples and tests:

```bash
python scripts/lint_all.py
```

On Windows, if `python` points to the Windows Store placeholder, try:

```bash
py scripts/prompt_linter.py skill/promptforge/examples/codex-project.md
py scripts/lint_all.py
```

The linter uses only the Python standard library and does not call external APIs.

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

- `skill/promptforge/SKILL.md`: the core skill definition
- `skill/promptforge/references/`: taxonomy, rubric, risk rules, and output templates
- `skill/promptforge/examples/`: worked examples across common task types
- `tests/`: vague task inputs, expected output characteristics, and smoke test
- `scripts/prompt_linter.py`: a simple local prompt quality checker
- `scripts/lint_all.py`: batch linting for examples and tests

## Version

Current version: `0.1.0 - Initial baseline`

Version 0.1.0 intentionally excludes:

- external AI API integrations
- account-based product flows
- browser automation
- Computer Use as a default path
- web UI

The first release is documentation-first and workflow-first.
