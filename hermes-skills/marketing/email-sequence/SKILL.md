---
name: email-sequence
description: "Write multi-email nurture and sales sequences."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Email]
    related_skills: [email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email, marketing-orchestrator]
---

# Email Sequence Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write multi-email nurture and sales sequences.

## Procedure

Your job is to write a complete email nurture sequence — from first contact to conversion. Every email has one job. No filler emails.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5) — every email must sound like this brand
- Target audience and pain points (Section 6)
- Core offer and pricing (Section 9)
- Key messages (Section 11)
- USP (Section 8)

Check if `outputs/strategy/campaign-brief-*.md` exists — if so, align sequence to campaign goal.

If brand.md doesn't exist: ask user for brand name, offer, audience, and tone before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified sequence type and goal**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết email sequence, mình cần biết:
1. **Loại sequence:** Welcome / Lead nurture / Post-purchase onboarding / Sales / Re-engagement
2. **Trigger:** Người đăng ký nhận được email này sau khi làm gì? (đăng ký form, download lead magnet, mua hàng...)
3. **Mục tiêu cuối:** Conversion mong muốn là gì? (book call, mua sản phẩm, upgrade, để lại review...)
4. **Số email:** 3 / 5 / 7 emails?
5. **Khoảng cách:** Gửi hàng ngày, cách 2 ngày, hay theo trigger?"

Wait for answer.

## Step 3 — Write the sequence

### Email sequence principles

**One email = one job**
Each email does exactly one thing: introduce, educate, overcome an objection, share proof, or ask for the sale. Never combine jobs.

**The job order for a 5-email sales sequence:**
1. Welcome + set expectations (what's coming, why it matters)
2. Educate on the problem (make them feel understood)
3. Introduce the solution (not the pitch — the concept)
4. Social proof (case study, testimonial, specific result)
5. The offer (clear ask, urgency if real, risk-reversal)

**For a 7-email sequence:** add objection handling (email 5) and a soft follow-up (email 7 = "last chance" or value recap).

### Vietnamese email writing rules

**Subject lines:**
- 35–50 characters (mobile preview)
- Curiosity or specificity — not both
- No ALL CAPS, no excessive punctuation
- Test: would you open this if you didn't write it?

**Preview text (50–90 chars):**
- Continues the subject line, doesn't repeat it
- Completes the curiosity gap or adds context

**Opening line:**
- Never start with "Chào [Tên]," on its own — add immediate value in the same sentence or next line
- First line = reason to keep reading
- Mirror their situation: "Nếu bạn đang [pain point]..."

**Body:**
- Short paragraphs: 1–3 sentences
- One bold key sentence per email (the thing you want them to remember)
- No walls of text — Vietnamese mobile readers scroll fast
- Conversational, not corporate: "bạn/mình", not "quý khách"

**CTA:**
- One CTA per email — never two
- Specific and action-oriented: "Book 30 phút miễn phí" not "Liên hệ với chúng tôi"
- CTA as a text link or button — not buried in a paragraph

**Timing (Vietnamese market):**
- Best open times: Tuesday–Thursday, 8–9am or 7–9pm
- Avoid Monday morning and Friday afternoon
- If using Zalo broadcast: same timing applies

### Sequence structure per email:

```
Subject: [35–50 chars]
Preview: [50–90 chars]

[Opening — 1–2 sentences, immediate value or mirror]

[Body — 3–5 short paragraphs, one idea each]

[Transition sentence leading to CTA]

[CTA — one, clear, specific]

[Sign-off]
[P.S. — optional, adds one more hook or addresses an objection]
```

## Step 4 — Write output

Save to `outputs/assets/email/email-sequence-[name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Email Sequence — [Sequence Name]
> Generated: [date] | Type: [sequence type] | Emails: [n] | Goal: [conversion goal]

## Sequence Overview
- Trigger: [what starts this sequence]
- Goal: [desired end action]
- Cadence: [timing between emails]
- Total length: [n] emails over [x] days

---

## Email 1 — [Job: e.g., Welcome]
**Send:** Immediately after trigger
**Subject:** [subject line]
**Preview:** [preview text]

---

[Email body]

---

## Email 2 — [Job]
**Send:** Day [n]
**Subject:**
**Preview:**

---

[Email body]

---

[Repeat for all emails]

---

## Sequence Notes
- A/B test opportunities: [which subjects or CTAs to test]
- Personalization tokens: [first name, company name, etc.]
- Segmentation: [if applicable — who gets which version]
```

## Step 5 — Confirm

After writing:

---
"✅ **Email sequence '[Name]' hoàn chỉnh.**

**Sequence stats:**
- [n] emails over [x] days
- Goal: [conversion goal]
- Trigger: [trigger event]

**Subjects:**
1. [Email 1 subject]
2. [Email 2 subject]
...

📁 Đã lưu: `outputs/assets/email/email-sequence-[name]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/subject-line-ab` để test subject lines, hoặc `/newsletter` để viết broadcast email cho list hiện có."

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
