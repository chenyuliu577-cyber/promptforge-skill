# Image Editing Example

## User's Original Simple Request

帮我把图片 P 得更好看。

## Task Analysis

- Primary task type: image editing
- Objective: turn a subjective request into precise editing instructions
- Missing data: source image, target style, what should remain unchanged, realism tolerance

## Key Assumptions

- the user likely wants tasteful improvement rather than heavy alteration
- preserving subject identity is usually a default requirement
- realistic retouching is safer than dramatic transformation unless requested

## Optimized Final Prompt

```text
Edit the provided image to improve its overall visual quality.

Objective:
Make the image look more polished while preserving the original subject and intent.

Requirements:
- improve lighting, contrast, color balance, and overall clarity where beneficial
- preserve the subject identity, core composition, and important objects
- keep the result natural unless the user explicitly requests a stylized edit
- if the image contains text, logos, or product details, do not distort them
- if the user has not specified a style, prefer clean, realistic enhancement

Do not:
- change facial identity
- remove important content without permission
- over-smooth, over-sharpen, or apply obvious beauty-filter artifacts

Verification Checklist:
- the image is visibly improved
- preserved elements remain intact
- the edit looks intentional rather than artificial
```

## Risk Check

- preserve identity and important source details unless the user requests a specific change
- avoid edits that could misrepresent a person, product, document, or event
- do not publish or share the edited image externally without approval

## User Confirmation Point

No special confirmation is required for a local edit preview. Ask for confirmation before identity-changing edits, public use, or edits that could mislead viewers.

## Checklist

- preservation rules are explicit
- the vague word "better" is operationalized
- over-editing is prohibited
- quality checks are concrete
- confirmation status is explicit
