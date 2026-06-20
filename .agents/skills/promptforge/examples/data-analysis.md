# Data Analysis Example

## User's Original Simple Request

帮我分析一下这些数据。

## Task Analysis

- Primary task type: data analysis
- Objective: turn a vague request into a structured analysis brief
- Missing data: dataset format, business question, time range, key metrics, expected outputs

## Key Assumptions

- the user probably wants insights, not raw descriptive statistics only
- data quality checking should happen before interpretation
- causal claims should not be made without evidence

## Optimized Final Prompt

```text
Analyze the provided dataset and produce a decision-useful summary.

Objective:
Extract the most relevant patterns, anomalies, and actionable findings from the data.

Requirements:
- first describe the dataset structure and note any missing, invalid, or inconsistent fields
- identify the key metrics and trends relevant to the user's goal
- separate descriptive findings from interpretation and recommendations
- use tables or bullet summaries where they improve clarity
- state assumptions when business context is missing

Do not:
- invent causal explanations without support
- hide data quality limitations
- claim certainty beyond the evidence

Verification Checklist:
- data quality issues are acknowledged
- findings are tied to actual observed patterns
- recommendations are labeled as inference where appropriate
```

## Risk Check

- do not expose private datasets to external services without approval
- do not claim causality unless the data and method support it
- flag missing, inconsistent, or suspicious data before drawing conclusions

## User Confirmation Point

No special confirmation is required for local analysis. Ask for confirmation before sharing data externally, publishing findings, or using results for high-risk decisions.

## Checklist

- analysis is framed around a goal
- data-quality review is included
- causality is controlled
- outputs are structured and reviewable
- confirmation status is explicit
