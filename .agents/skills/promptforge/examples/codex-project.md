# Codex Project Example

## User's Original Simple Request

Help me make a GitHub open source project for a reusable skill.

## Task Analysis

- Primary task type: coding
- Secondary task type: documents
- Objective: create a repository scaffold and core documentation for a reusable Skill
- Deliverable: project structure, documentation, examples, tests, and a lightweight local script

## Key Assumptions

- first version should avoid external service integrations
- documentation quality matters more than automation breadth
- repository should be easy to publish and maintain

## Optimized Final Prompt

```text
Work in the current local repository and create a minimal open source project scaffold for a reusable AI Skill.

Objective:
Build version 1 as a documentation-first project that turns vague user requests into structured prompts or agent task specifications.

Requirements:
- create a clear repository structure with README, LICENSE, AGENTS guidance, core SKILL file, references, examples, tests, and one simple local script
- keep the project local-first and dependency-light
- do not add browser automation, account login, Computer Use implementation, external AI APIs, or web UI
- make the documentation concise, executable, and suitable for GitHub publication
- include critique, revision, risk checks, and confirmation-gate concepts in the Skill design

Output requirements:
- all files must contain usable content, not placeholders
- examples must include original request, analysis, assumptions, final prompt, and checklist
- tests must define vague inputs and expected output characteristics
- the script must score a prompt document for required sections and missing controls

Verification:
- repository tree matches the requested structure
- core principles emphasize clarity, controllability, and verification
- risky or external actions are guarded by confirmation language
```

## Risk Check

- no external API, browser automation, or account workflow should be added
- dependency creep should be rejected unless it directly supports the first release
- repository changes should stay inside the requested project directory

## User Confirmation Point

No special confirmation is required for local file creation. Ask for confirmation before publishing to GitHub, adding external integrations, or changing repository scope.

## Checklist

- goal is specific and scoped
- first version exclusions are explicit
- deliverables are enumerable
- no fake tools or APIs are assumed
- verification criteria are included
- confirmation status is explicit
