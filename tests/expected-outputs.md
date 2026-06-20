# Expected Output Characteristics

For each vague task in `vague-tasks.md`, a qualified `promptforge` output should include task analysis, missing information, assumptions, a final prompt, and a verification checklist. Additional safety or confirmation language is required when risk is present.

## 1. 帮我做一个高级 PPT

- must classify the task as slides
- must ask or assume audience, topic, and slide count
- must define structure and success criteria
- must avoid empty style-only guidance

## 2. 帮我让 Codex 修改我的网页

- must classify as coding or debugging depending on context
- must mention repository or file context
- must constrain scope and ask for acceptance criteria
- must require realistic tool and codebase assumptions

## 3. 帮我把图片 P 得更好看

- must classify as image editing
- must define preservation constraints
- must turn "better" into concrete edit goals
- must include quality checks against over-editing

## 4. 帮我写论文

- must classify as writing or documents
- must ask for topic, audience, format, and citation expectations
- must prohibit fabrication of claims or references
- must define the expected structure

## 5. 帮我分析股票

- must flag financial-risk considerations
- must distinguish analysis from investment advice
- must ask for ticker, time horizon, and objective
- must include caveats and likely confirmation or caution language

## 6. 帮我自动操作网页 AI

- must classify as web automation and likely high-risk
- must surface login, account, submission, and trust-boundary risks
- must require confirmation before external effects
- should prefer planning over immediate execution

## 7. 帮我整理 Excel

- must classify as spreadsheets
- must ask for workbook structure and desired transformation
- must define preservation rules for raw data
- must include output sheet or cleanup criteria

## 8. 帮我写实验报告

- must classify as writing or documents
- must require experiment details and evidence inputs
- must prohibit invented results
- must define a standard report structure

## 9. 帮我做 GitHub 开源项目

- must classify as coding plus documentation
- must ask for project scope, language, and first-version boundary
- must define concrete deliverables
- must avoid unrealistic platform integrations unless requested

## 10. 帮我生成一套提示词

- must clarify what those prompts are for
- must classify the underlying task domain rather than staying generic
- must define prompt count, target use cases, and output structure
- must include review criteria so the prompt set is testable
