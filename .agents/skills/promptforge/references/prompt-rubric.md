# Prompt Rubric

Use this rubric to score a drafted prompt before releasing the final version.

## Scoring Scale

Score each dimension from `0.0` to `10.0`. Use half-point increments when needed.

- `9.0-10.0`: strong and release-ready
- `8.5-8.9`: good enough to output as the final version
- `7.0-8.0`: usable but should be improved
- below `7.0`: not ready

If the total prompt quality is below `8.5`, revise it before output.

Default maximum internal iterations: `3`.

Do not blindly lengthen the prompt to raise the score. Better prompts are often shorter and more controlled.

## Dimensions

### 1. goal clarity

- Is the objective explicit and singular enough to execute?
- Are success and task boundaries understandable?

### 2. input clarity

- Does the prompt specify what materials, context, files, or assumptions are available?
- Are missing inputs surfaced rather than silently guessed?

### 3. output controllability

- Is the expected deliverable format defined?
- Can the output be checked against concrete structure requirements?

### 4. execution readiness

- Does the prompt specify concrete deliverables, file paths, output format, and acceptance checks?
- For Codex or document-generation tasks, can the agent act without guessing where to write results?

### 5. constraint coverage

- Does the prompt include relevant limits, priorities, exclusions, and scope boundaries?
- Are important tradeoffs made visible?

### 6. tool realism

- Does the prompt use only tools, permissions, and workflows that are realistically available?
- Does it avoid pretending the agent can browse, log in, or call tools it does not have?

### 7. safety

- Does the prompt account for privacy, external effects, sensitive data, and risky domains?
- Are approval gates included where appropriate?

### 8. verification

- Are there clear quality checks, acceptance criteria, or review steps?
- Can another reviewer tell whether the task was done well?

### 9. anti-template strength

- Does the prompt prevent generic AI templates, vague section titles, and empty business jargon?
- For slides and reports, does it require concrete judgments instead of category labels?

### 10. decision sharpness

- For slides, reports, and proposals, does the prompt require conclusion-style titles, one core judgment per section, and deliberate information selection?
- Does it prevent filler pages or unsupported claims?

### 11. confirmation quality

- Does the prompt distinguish a default draft from formal delivery?
- Are confirmations specific, such as topic, audience, materials, brand rules, data sources, or external publication boundaries?

### 12. concision

- Is the prompt as short as possible without losing control?
- Has unnecessary wording been removed?

## Release Rule

Output the final version only if the prompt is at least `8.5/10` overall and has no major safety or realism failure.

If a dimension is weak in a way that would predictably cause failure, revise the prompt even if the average score looks acceptable.

## Revision Guidance

When revising:

- first fix ambiguity in the goal
- then fix missing inputs and output format
- then fix safety and external-action boundaries
- finally remove unnecessary verbosity

The rubric is a control mechanism, not an invitation to produce bloated prompts.
