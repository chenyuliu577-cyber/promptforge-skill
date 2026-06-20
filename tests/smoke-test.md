# Smoke Test

This smoke test checks whether the `promptforge` Skill produces a structured, controllable, and verifiable result from a vague request.

## Manual Test Procedure

1. Open `skill/promptforge/SKILL.md`.
2. Use the workflow in the Skill against the vague input below.
3. Produce a final prompt or agent task specification.
4. Compare the result against the pass criteria.
5. Save the generated result as a temporary `.md` or `.txt` file if you want to run the linter.

## Test Input

```text
帮我让 Codex 修改我的网页
```

## Passing Output Must Include

- task analysis that classifies the request as coding or debugging
- missing information such as repository context, target page, desired change, and acceptance criteria
- safe assumptions that are clearly labeled
- an optimized final prompt with objective, inputs, requirements, prohibited actions, and output expectations
- quality standards or verification steps
- risk checks for scope creep, unrelated refactors, deployment, external services, and destructive changes
- a user confirmation point before broad rewrites, deployment, publication, or changes outside the requested scope

## Failing Output Examples

- gives only a generic prompt without task classification
- says "make the website better" without defining the target change
- assumes a framework, file path, deployment target, or external API without evidence
- allows broad redesign or unrelated refactoring without confirmation
- omits verification steps
- treats publishing, deployment, or production changes as automatic
- becomes long but still leaves the output format unclear

## Linter Check

Run the local linter on a generated prompt file:

```bash
python scripts/prompt_linter.py path/to/generated-prompt.md
```

For the built-in Codex example:

```bash
python scripts/prompt_linter.py skill/promptforge/examples/codex-project.md
```

A passing result should include a high score and no major missing sections. If the linter reports missing items, revise the generated prompt before treating it as ready.
