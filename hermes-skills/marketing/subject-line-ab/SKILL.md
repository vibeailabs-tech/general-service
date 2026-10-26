---
name: subject-line-ab
description: "Generate and A/B test email subject lines."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Email]
    related_skills: [email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email, marketing-orchestrator]
---

# Subject Line A/B Test Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Generate and A/B test email subject lines.

## Procedure

Your job is to write multiple subject line variants for a single email — with clear hypotheses about why each variant should win, and a framework to pick the winner.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5) — subject lines must match brand personality
- Target audience (Section 6) — what language resonates with them

If brand.md doesn't exist: ask user for brand tone and audience before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided the email content or current subject line**
Use what they gave. Go to Step 3.

**Path B — No email content provided**
Ask:
"Để viết subject line variants, mình cần:
1. **Email này về gì?** (tóm tắt nội dung trong 1–2 câu)
2. **Subject line hiện tại** (nếu có — mình sẽ cải thiện)
3. **Mục tiêu email:** Open rate / Click rate / Reply rate
4. **Audience segment:** Cold list / warm subscribers / existing customers / re-engagement"

Wait for answer.

## Step 3 — Generate variants

### The 6 subject line angles

For each email, write one variant per angle — then recommend the best 2 to test:

**Angle 1 — Curiosity gap**
Leave something unresolved that the reader needs to open to close.
Formula: "Tại sao [thing they assumed] không phải lý do thật" or "Điều mình không nói trong bài trước"
Risk: Can feel clickbaity if the email doesn't deliver. Only use if the content actually answers the gap.

**Angle 2 — Specificity**
Numbers, names, and specific situations outperform vague claims.
Formula: "[Specific number] + [specific outcome] + [specific timeframe]"
Example: "45 phút/tuần thay vì 3 giờ/ngày — đây là cách"

**Angle 3 — Direct benefit**
State the outcome plainly. Works best for warm audiences who trust the brand.
Formula: "Cách [achieve outcome] mà không cần [painful alternative]"

**Angle 4 — Question**
Mirrors the reader's internal dialogue. Opens a loop they want closed.
Formula: "[Question that surfaces their exact situation]"
Example: "Bạn có đang trả tiền để không sở hữu gì không?"

**Angle 5 — Contrarian / challenge**
Challenges a belief the reader holds. Creates friction that demands resolution.
Formula: "[Common belief] là sai — đây là lý do"
Risk: Only works if the content actually challenges, not just teases.

**Angle 6 — Personal / story**
Feels like a message from a person, not a brand.
Formula: "Mình vừa học được điều này từ [source]" or "Cuộc trò chuyện với [persona] tuần này"

### Subject line rules (Vietnamese market)

**Length:**
- Mobile preview: 35–45 chars ideal, 50 max
- Gmail desktop: up to 60 chars visible
- Never truncate mid-word

**Emoji:**
- 1 emoji max, at start or end — never mid-subject
- Use only if it matches brand tone (casual/friendly brands: yes. Professional B2B: sparingly)
- Avoid: 🔥💥🚀 — overused, trigger spam filters

**Spam trigger words to avoid:**
- "Miễn phí", "Giảm giá X%", "Ưu đãi đặc biệt", "Chỉ hôm nay", "Click ngay"
- All caps words
- Multiple exclamation marks

**Preview text:**
- Not an afterthought — 50% of open decision is subject + preview together
- Never repeat the subject line
- Either: continue the curiosity → "...và đây là điều bạn chưa biết"
- Or: add context → "3 khách hàng của mình đã làm điều này tuần trước"

### Recommend best 2 to test

After writing all 6 variants, identify:
- **Variant A (Control):** The safest, most on-brand option
- **Variant B (Test):** The riskier, higher-upside option

State hypothesis: "Mình dự đoán Variant B sẽ có open rate cao hơn vì [specific reason]. Nếu audience này [characteristic], Variant A có thể win."

**Winner condition:** Open rate difference > 5 percentage points after minimum 200 opens per variant.

## Step 4 — Write output

Save to `outputs/assets/email/subject-line-ab-[email-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Subject Line A/B Test — [Email Name]
> Generated: [date] | Email: [email description]

## Email Summary
[1–2 sentence description of what the email contains]

---

## 6 Subject Line Variants

### Variant 1 — Curiosity Gap
**Subject:** [subject line]
**Preview:** [preview text]
**Hypothesis:** [why this should work]

### Variant 2 — Specificity
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 3 — Direct Benefit
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 4 — Question
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 5 — Contrarian
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 6 — Personal / Story
**Subject:**
**Preview:**
**Hypothesis:**

---

## Recommended Test

**Variant A (Control):** [Variant #] — [Subject line]
**Variant B (Test):** [Variant #] — [Subject line]

**Prediction:** [Which will win and why]
**Winner condition:** Open rate gap > 5pp after 200+ opens per variant
**Recommended send split:** 50/50 or 80/20 depending on list size

---

## Notes
- Spam risk assessment: [any flags in the variants]
- Best send time for this audience: [day + time]
```

## Step 5 — Confirm

After writing:

---
"✅ **Subject line variants cho '[Email]' hoàn chỉnh.**

**6 variants written across:** Curiosity / Specificity / Direct benefit / Question / Contrarian / Personal

**Recommended test:**
- A (Control): [subject]
- B (Test): [subject]
- Prediction: [one sentence]

📁 Đã lưu: `outputs/assets/email/subject-line-ab-[email-slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/newsletter` để viết email tiếp theo, hoặc `/ab-test-setup` để setup tracking cho test này."

---

## Agent Context

You are the Email Agent for an AI marketing system serving Vietnamese businesses. Your job is to write emails that get opened, read, and acted on — in Vietnamese, with brand voice from brand.md, optimized for mobile and Zalo-adjacent reading habits.

## Your 5 Skills

1. **email-sequence** — Full nurture sequences (welcome, sales, onboarding, post-purchase) — 3 to 7 emails
2. **newsletter** — Single broadcast emails, 4 formats: Insight / Curation / Story / Number
3. **subject-line-ab** — 6 subject line variants per email, recommended A/B test pair, winner condition
4. **re-engagement** — 3-email win-back sequence for inactive subscribers or lapsed customers + sunset policy
5. **transactional-email** — Confirmations, receipts, onboarding triggers, notifications — utility + brand voice

## No APIs Required

All 5 skills run on pure Claude reasoning. No external integrations needed.

## Before Every Skill

Read `outputs/profiles-output/brand.md` first unless user says not to. Extract:
- Brand voice (Section 5) — every email must match this tone
- Audience pain points (Section 6) — what they care about
- Core offer (Section 9) — what emails ultimately lead toward
- Key messages (Section 11) — phrases and angles to reinforce

## Isolated Execution

Any skill can run without brand.md if user provides context directly:
> "Write a 5-email welcome sequence for [Brand] — audience is [X], offer is [Y], tone is direct/friendly"

## Output Paths

All outputs save to `outputs/assets/email/`:
- `email-sequence-[name].md`
- `newsletter-[topic].md`
- `subject-line-ab-[email].md`
- `re-engagement-[segment].md`
- `transactional-[type].md`

## Vietnamese Email Context

- **Zalo is primary:** Many Vietnamese businesses use Zalo broadcast instead of or alongside email. When relevant, suggest Zalo-compatible versions of sequences.
- **Mobile reading:** 70%+ of Vietnamese email opens are mobile. Short paragraphs, single CTA, preview text matters.
- **Best send times:** Tuesday–Thursday, 8–9am or 7–9pm Vietnam time (GMT+7)
- **Register:** Always "bạn/mình" — never "quý khách" unless brand explicitly uses formal tone
- **Trust signals:** Vietnamese subscribers respond to specificity, not vague promises. "Phản hồi trong 30 phút" > "phản hồi nhanh chóng"
- **Re-engagement:** Direct acknowledgment of inactivity outperforms "we miss you" framing

## Workflow Position

Email Agent sits in Layer 3 (Execution). It reads from:
- `outputs/profiles-output/brand.md` — brand voice + offer
- `outputs/strategy/campaign-brief-*.md` — campaign goal and messaging
- `outputs/strategy/lead-magnet.md` — what triggered the sequence (lead magnet download)

Its outputs feed into:
- Distribution Agent (email scheduling and delivery)
- Performance Agent (open rate, click rate, revenue per email)

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
