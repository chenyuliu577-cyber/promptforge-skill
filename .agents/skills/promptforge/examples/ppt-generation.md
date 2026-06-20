# PPT Generation Example

## User's Original Simple Request

帮我做一个高级 PPT。

## Task Analysis

- Primary task type: slides
- Objective: produce a presentation specification instead of a vague design request
- Missing data: audience, topic, duration, language, brand style, desired slide count

## Key Assumptions

- "高级" likely means polished, executive-facing, and concise
- the user probably wants a business-quality deck rather than a decorative one
- a safe default is to request or assume a 10-12 slide structure unless specified otherwise

## Optimized Final Prompt

```text
Create a presentation plan for an executive-style PPT.

Objective:
Turn the user's topic into a concise, polished deck suitable for decision-makers.

Assumptions:
- audience is business stakeholders unless stated otherwise
- slide count target is 10-12
- tone is professional, concise, and insight-led

Requirements:
- define the audience, deck objective, and one-line core message
- propose a slide-by-slide outline with one key point per slide
- recommend suitable visuals, charts, or diagrams for each slide
- specify title style, narrative flow, and final recommendation slide
- if important context is missing, list it clearly before finalizing

Do not:
- create decorative filler slides
- add unsupported statistics
- confuse visual polish with strategic clarity

Verification Checklist:
- every slide has a clear takeaway
- the deck builds toward a decision or recommendation
- unnecessary text density is avoided
```

## Risk Check

- do not invent statistics, sources, client facts, or business results
- do not use confidential company context unless the user provides it
- do not treat visual polish as a substitute for a clear argument

## User Confirmation Point

No special confirmation is required for a draft outline. Ask for confirmation before creating a final client-facing deck, using private company data, or publishing/exporting externally.

## Checklist

- audience and objective are surfaced
- slide count and structure are controlled
- visual guidance is included
- unsupported claims are prohibited
- final review criteria are explicit
- confirmation status is explicit
