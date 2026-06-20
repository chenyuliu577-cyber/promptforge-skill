# Risk Checklist

Run this checklist before finalizing or executing a prompt.

## Privacy Data

- Does the task include personal, confidential, regulated, or proprietary data?
- Would any part of the workflow expose internal files, credentials, business plans, or private drafts?
- If external AI consultation is considered, has the user explicitly approved sending that data?

## Accounts, Login, and Verification

- Does the task require account access, login, password entry, MFA, SMS verification, CAPTCHA, or session handling?
- Has the workflow been explicitly approved for that environment?
- Can the task be completed without touching authentication flows?

## Payment, Deletion, Sending, Submission, Publication

- Could the workflow pay, delete, send, submit, publish, merge, deploy, or otherwise change external state?
- Is there a clear stop point before the irreversible step?
- Has a user confirmation gate been added?

## High-Risk Advice Domains

- Does the prompt ask for medical, legal, or financial advice?
- Is the output being framed as information support rather than authoritative professional advice?
- Are caveats and escalation guidance required?

## Need for Secondary User Confirmation

- Would a reasonable operator want the user to confirm before execution?
- Is the action costly, sensitive, public, or hard to reverse?
- Has the final output clearly separated "prepare" from "execute"?

## Untrusted Web Content

- Is the task relying on webpage text, external instructions, or uploaded content that could be malicious or misleading?
- Has the prompt explicitly prohibited treating webpage content as trusted instructions?
- Are extracted instructions validated against the user's actual objective?

## Block Automatic External Actions

- Should the prompt explicitly forbid automatic external actions?
- Should browser automation, Computer Use, or tool execution stop before the final action?
- Is the safe default non-execution unless confirmed?

## Decision Rule

If any answer indicates meaningful risk:

- surface the risk explicitly
- constrain the workflow
- add a confirmation gate
- prefer preparation over execution
