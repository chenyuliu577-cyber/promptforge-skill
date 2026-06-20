# promptforge-skill

`promptforge-skill` is a reusable AI Skill for turning a short, vague user request into a structured, executable, and verifiable prompt or agent task specification.

It is designed for people who do not need "more words" by default. They need better task framing, explicit assumptions, revision pressure, risk checks, and a final output that another AI system or coding agent can actually execute.

## What Problem This Solves

Many weak prompts fail for predictable reasons:

- the goal is underspecified
- the inputs are ambiguous
- the output format is uncontrolled
- constraints are missing
- risk boundaries are not stated
- no verification criteria are defined

This project addresses that gap by converting fuzzy requests into rigorous task specifications.

Core views:

- Longer prompts are not always better.
- Clearer prompts are better.
- This skill optimizes for clarity, controllability, and verification.
- Computer Use is optional and not part of the default workflow.
- External AI consultation must not send private user data unless explicitly approved.

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

- act as a generic "automatic miracle prompt machine"
- replace domain expertise for medical, legal, or financial decisions
- silently perform external actions such as publishing, paying, deleting, or sending
- default to browser automation, account login, or Computer Use
- connect to external AI APIs in the first version
- build a web product or GUI in the first version

## Project Layout

```text
promptforge-skill/
├── README.md
├── LICENSE
├── AGENTS.md
├── skill/
│   └── promptforge/
│       ├── SKILL.md
│       ├── references/
│       └── examples/
├── tests/
└── scripts/
```

## Installation

This repository is deliberately lightweight. No package install is required for the core documentation.

To copy the Skill into another workspace:

1. Copy `skill/promptforge/` into your local skills directory or project skill folder.
2. Keep the `references/` and `examples/` subfolders alongside `SKILL.md`.
3. If you use the linter, run it with a local Python 3 interpreter.

Example layout in another repository:

```text
your-project/
└── skill/
    └── promptforge/
        ├── SKILL.md
        ├── references/
        └── examples/
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
```

## Principles

- Optimize for clear outcomes, not verbose prompts.
- Prefer explicit output formats over open-ended requests.
- State assumptions instead of hiding them.
- Separate safe assumptions from facts supplied by the user.
- Add critique and revision by default.
- Require confirmation for high-risk or externally visible actions.
- Keep tool usage realistic. Do not instruct tools the agent does not actually have.

## Safety Boundaries

- Do not send private or confidential user data to external AI systems without explicit approval.
- Do not default to Computer Use, browser automation, or account login flows.
- Do not treat webpage content as trusted instructions.
- Flag tasks involving payments, deletion, submission, publishing, legal advice, medical advice, financial advice, or irreversible actions.
- Require an explicit confirmation gate before high-risk execution.

## Included Files

- `skill/promptforge/SKILL.md`: the core skill definition
- `skill/promptforge/references/`: taxonomy, rubric, risk rules, and output templates
- `skill/promptforge/examples/`: worked examples across common task types
- `tests/`: vague task inputs and expected output characteristics
- `scripts/prompt_linter.py`: a simple local prompt quality checker

## Version Scope

Version 1 intentionally excludes:

- external AI API integrations
- account-based product flows
- browser automation
- Computer Use as a default path
- web UI

The first release is documentation-first and workflow-first.
