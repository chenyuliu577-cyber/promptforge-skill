# Vague Task Test Set

Goal: use these inputs to test whether `promptforge` can produce structured, safe, and executable outputs from minimal requests.

Input context: each item below is intentionally vague and should be treated as the full user request.

Output format: for each input, the Skill should return task analysis, missing information, assumptions, final prompt, verification checklist, risk controls, and confirmation status.

Constraints:

- preserve the user's likely intent without inventing private facts
- make safe assumptions only when clearly labeled
- keep the final prompt controlled and executable

Do not:

- treat vague requests as fully specified
- skip risk checks
- add Computer Use, web automation, or external API usage unless the task explicitly requires it and includes confirmation boundaries

Quality standards:

- task type is classified
- missing information is surfaced
- output is specific enough to verify
- risky or external actions include a confirmation gate

Checklist:

- goal is clear
- output format is defined
- assumptions are labeled
- risk control is present

1. 帮我做一个高级 PPT
2. 帮我让 Codex 修改我的网页
3. 帮我把图片 P 得更好看
4. 帮我写论文
5. 帮我分析股票
6. 帮我自动操作网页 AI
7. 帮我整理 Excel
8. 帮我写实验报告
9. 帮我做 GitHub 开源项目
10. 帮我生成一套提示词
