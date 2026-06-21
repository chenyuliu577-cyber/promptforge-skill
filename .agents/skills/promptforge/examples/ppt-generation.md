# PPT Generation Example

## User's Original Simple Request

Help me make a premium PPT.

## Task Analysis

- Primary task type: slides
- Secondary task type: document generation
- Objective: convert a vague PPT request into executable file-based deliverables for a high-quality business presentation specification
- Current limitation: the user has not provided the topic, audience, use case, materials, brand rules, data sources, or delivery format
- Required output: structured Markdown files, not a `.pptx`, unless the user later confirms PPTX generation and provides the required assets

## Missing Information

### Blocking Information

These are required before making a formal client-facing or external deck:

- presentation topic
- target audience
- use case
- target decision or action
- real materials, data, brand assets, or template

### Strong-Impact Information

These can be defaulted, but quality will be materially affected:

- expected speaking time
- preferred slide count
- industry or business context
- presentation type: report, proposal, pitch, defense, or training
- chart and data needs
- speaker notes requirement

### Fine-Tuning Information

These can be supplied later:

- color preference
- font preference
- animation preference
- image style
- footer, page number, and logo placement

## Assumptions

- default type: Chinese-style senior business report deck
- default length: 10-12 slides
- default audience: management, clients, investors, or other non-technical decision-makers
- default goal: help the audience understand the issue, judge value, and choose the next action
- default style: restrained, professional, conclusion-first, moderate information density
- default visual direction: low-saturation colors, strong hierarchy, minimal decoration, structured diagrams and comparisons
- default data rule: missing data must be marked as `[待补充：data name]`; do not invent statistics, cases, market size, growth rates, or customer feedback

These assumptions are used because a business-report structure is the most reusable starting point when the actual scenario is unknown. They are placeholders, not facts.

## Final Prompt

```text
You are a rigorous presentation planning agent working in the current project directory.

Task:
Convert the vague request "Help me make a premium PPT" into a structured, executable, and reviewable business presentation production spec.

Do not generate a `.pptx` file yet. The user has not provided the topic, audience, materials, brand rules, template, or delivery format.

Create an `output/` directory and write these files:

1. `output/ppt_task_spec.md`
   Purpose: define the task goal, missing information, default assumptions, visual rules, risk boundaries, self-critique, acceptance criteria, and confirmation gate.

2. `output/page_by_page_plan.md`
   Purpose: provide a 10-12 slide page-level plan. Each slide must include:
   - page number
   - conclusion-style title
   - one core judgment
   - 3-5 short body points
   - main visual structure
   - data and material needs
   - speaker notes
   - production warning

3. `output/prompt_for_next_agent.md`
   Purpose: provide a copyable prompt for another AI, PPT producer, or Codex agent to continue the work.

Missing information handling:
- classify missing inputs as Blocking, Strong-Impact, or Fine-Tuning
- proceed with defaults only for a first draft
- never present assumptions as facts
- mark all unknown data as `[待补充：specific item]`

Definition of "premium PPT":
- sharp point of view
- compressed structure
- deliberate information selection
- visuals that support judgment
- no filler slides
- directly usable by a PPT producer

Anti-template rules:
- do not use generic slide titles such as "Background", "Pain Points", "Solution", "Core Advantages", "Market Analysis", "Implementation Path", "Risk Control", "Future Outlook", or "Summary"
- every title must contain a concrete judgment
- avoid empty terms such as "empowerment", "ecosystem", "matrix", "full-chain", "platform base", or "intelligent upgrade" unless the prompt defines the concrete meaning and actions

Self-Critique Before Finalizing:
Before writing the final files, critique the draft against these questions and revise once:
- does it still look like a generic AI template?
- does every slide have a clear judgment?
- are there any empty phrases that cannot be executed?
- are assumptions disguised as facts?
- can a PPT producer start making pages from the output?

Confirmation Gate:
The default plan may be used as a first-draft skeleton. Before creating a formal PPTX or external-facing deck, require user confirmation of:
- topic
- audience
- use case
- material scope
- delivery format
- brand rules
- real data sources
- public information boundaries

Quality constraints:
- do not answer only in chat
- do not create empty files
- do not write TODO-only placeholders
- do not invent data, customer cases, market size, or growth rates
- each slide must have exactly one core judgment
- each slide must specify a main visual structure
- each slide must include a production warning
```

## Verification Checklist

- output files are written under `output/`
- `output/ppt_task_spec.md` separates Blocking, Strong-Impact, and Fine-Tuning missing information
- `output/page_by_page_plan.md` contains 10-12 slides
- every slide has a conclusion-style title and one core judgment
- every slide includes body structure, main visual, material needs, speaker notes, and production warning
- missing data is marked with `[待补充：...]`
- no fake statistics, customer cases, market sizes, or growth rates are introduced
- generic slide titles and empty business jargon are avoided
- self-critique is included and the output is revised once before finalization

## Confirmation Gate

The default output can be used as a first-draft skeleton only. Before generating a formal PPTX or external-facing deck, ask the user to confirm topic, audience, use case, material scope, delivery format, brand rules, real data sources, and public information boundaries.

## Checklist

- task is specified as file-based delivery
- missing information is prioritized by severity
- default assumptions are labeled as assumptions
- anti-template rules are explicit
- formal delivery requires confirmation
