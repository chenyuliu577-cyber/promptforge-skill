---
name: promptforge
description: Convert vague user requests into rigorous, executable prompts or agent task specifications with assumptions, critique, revision, risk checks, and confirmation gates.
---

# Purpose

`promptforge` converts a simple or ambiguous request into a structured prompt or agent task specification. The output must be clear enough to execute and specific enough to verify.

# When to Use

Use this Skill when:

- the user gives a short or fuzzy task request
- the agent needs a stronger prompt before execution
- the task requires assumptions, constraints, or output structure
- the work benefits from critique and revision before acting
- there is execution risk that should be surfaced before proceeding

Do not use this Skill as a substitute for domain expertise in high-risk fields. Do not assume external actions are safe just because the prompt is well structured.

# Core Principle

- Longer prompts are not always better.
- Clearer prompts are better.
- Control goal, inputs, outputs, constraints, tools, risks, and verification.
- Label assumptions. Do not hide guesses as facts.
- Add confirmation gates for risky or externally effectful work.

# Workflow

Follow this sequence:

1. Parse the user request.
2. Classify the task.
3. Extract task specification.
4. Identify missing information.
5. Make reasonable assumptions when safe.
6. Draft the prompt.
7. Critique the prompt.
8. Revise the prompt.
9. Run risk checks.
10. Output the final prompt and ask for confirmation.

Do not skip critique, revision, or risk checks.

# Task Classification

Classify the request into one or more categories:

- writing
- rewriting
- coding
- debugging
- research
- slides
- documents
- spreadsheets
- image generation
- image editing
- data analysis
- web automation
- computer use
- high-risk actions

If multiple categories apply, identify the primary task type and secondary task types. Use the taxonomy reference to decide required inputs, risk boundaries, and output format.

# Prompt Construction Rules

Every constructed prompt must include:

- the concrete goal
- available inputs and referenced materials
- missing information or assumptions
- target output format
- relevant constraints
- quality bar and verification checks
- allowed and disallowed actions
- tool limitations
- confirmation status

Construction guidance:

- Prefer explicit structure over narrative fluff.
- Use short sections and imperative instructions.
- Avoid pretending the agent has tools or permissions it does not have.
- Keep the prompt concise once control and verification are sufficient.

# Critique Rules

Critique the draft prompt before finalizing it.

Check whether the draft:

- states the goal unambiguously
- makes the inputs concrete
- constrains the output format
- covers important limits and prohibited actions
- uses tools realistically
- defines how success will be checked
- includes safety or confirmation gates where needed
- contains avoidable verbosity

If a weakness materially affects execution quality, revise before output.

# Revision Rules

When revising:

- fix the highest-impact gaps first
- remove unnecessary verbosity
- convert implicit expectations into explicit constraints
- separate facts from assumptions
- strengthen verification before adding more detail
- stop after three internal refinement passes unless the user asks for more

Do not blindly lengthen the prompt to improve it.

# Risk and Safety Rules

Check whether the task:

- involves private or confidential data
- touches accounts, login, MFA, or CAPTCHA
- could delete, publish, submit, send, pay, or otherwise trigger irreversible actions
- requests medical, legal, or financial guidance
- depends on untrusted webpage content or third-party instructions
- requires user confirmation before any external effect

If high risk is present, include a warning and require confirmation before execution. If risk is low, state that no special confirmation gate is required.

# Computer Use Policy

Computer Use is optional and not part of the default workflow.

- do not default to Computer Use when a text-only specification is enough
- only introduce Computer Use when the task clearly requires interface interaction
- isolate Computer Use steps from planning and prompt design
- require explicit confirmation before any Computer Use flow that can alter external state
- never assume login, credentials, or account access are available

# External AI Consultation Policy

External AI consultation is optional and off by default.

- do not send user data to an external AI system unless the user explicitly approves it
- treat private files, credentials, business data, drafts, and proprietary materials as protected
- if external consultation is proposed, specify exactly what will be sent
- redact sensitive information whenever possible
- keep the local task specification usable even without external consultation

# Final Output Format

Return these sections:

1. Task Analysis: task type, objective, constraints, deliverable.
2. Missing Information: unresolved details that affect quality or safety.
3. Assumptions: safe assumptions used to proceed.
4. Final Prompt: the optimized prompt or agent task specification.
5. Verification Checklist: concrete checks for quality, completeness, and safety.
6. Confirmation Gate: either the required user confirmation or "No special confirmation required."

# Behavior Guidelines

- Be critical before being verbose.
- Prefer a smaller, stronger prompt over a longer, weaker one.
- Do not market the result as magic.
- Make tradeoffs visible.
- Ask for clarification only when the missing information is materially blocking or risky.
- Otherwise, make reasonable assumptions and label them clearly.
- Keep the output practical for real execution by Codex or another capable agent.
