---
name: transactional-email
description: "Write clear transactional email copy."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Email]
    related_skills: [email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email, marketing-orchestrator]
---

# Transactional Email Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write clear transactional email copy.

## Procedure

Your job is to write transactional emails — confirmations, receipts, onboarding triggers, notifications — that are clear, on-brand, and use every interaction as a trust-building moment. Transactional emails have the highest open rates of any email type. Most brands waste them.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand name and voice (Sections 1 + 5) — transactional emails must still sound like the brand
- Core offer (Section 9) — for upsell/cross-sell moments where appropriate
- Language (Section 4)

If brand.md doesn't exist: ask user for brand name, tone, and which transaction to write for before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified which transactional email to write**
Use what they gave. Go to Step 3.

**Path B — No specifics**
Ask:
"Loại transactional email nào bạn cần?
1. **Order confirmation** — xác nhận đơn hàng / thanh toán
2. **Welcome / onboarding** — sau khi đăng ký tài khoản hoặc mua lần đầu
3. **Delivery / fulfillment** — xác nhận giao hàng hoặc access
4. **Password reset / account** — security email
5. **Appointment confirmation** — xác nhận lịch hẹn / booking
6. **Invoice / receipt** — hóa đơn điện tử
7. **Notification** — trigger-based alert (payment due, expiry reminder, usage milestone)"

Wait for answer.

## Step 3 — Write the transactional email

### Transactional email principles

**The primary job: confirm and reassure**
Every transactional email must answer: "Did my action work?" within the first 2 lines. Don't make them search for the confirmation.

**The secondary job: build trust and move forward**
After confirming, use the email to:
- Reinforce the brand promise
- Set expectations for what happens next
- Provide one helpful resource or next step
- (Optional) plant the seed for the next action — without being pushy

**What NOT to do:**
- Don't bury the confirmation under a brand intro
- Don't put 3 CTAs — one secondary suggestion max
- Don't make it feel like a promotional email — people expect pure utility
- Don't skip branding entirely — a plain text receipt is a missed brand moment

### Transactional email structure

```
[Brand logo/name — minimal header]

[Confirmation statement — 1 sentence, bold or prominent]
"Đơn hàng của bạn đã được xác nhận." / "Lịch hẹn đã được đặt." / etc.

[Key details — the facts they need]
- What: [product/service/appointment]
- When: [date/time if applicable]
- Amount: [if financial transaction]
- Reference: [order number, booking ID]

[What happens next — 1–3 bullet points]
"Bạn sẽ nhận được [X] trong [timeframe]."

[One helpful resource or next step — optional but recommended]
Link to: FAQ / getting started guide / calendar add / contact support

[Support info — always include]
"Có câu hỏi? Nhắn Zalo [number] hoặc email [address]. Mình phản hồi trong [timeframe]."

[Sign-off — personal, not corporate]
```

### Vietnamese market specifics

**Payment confirmations:**
- Always include exact amount in VND (even if invoice is in USD — add VND equivalent)
- Include bank transfer reference if paid by bank transfer (phổ biến ở Việt Nam)
- Zalo support link > email for Vietnamese users — faster, more trusted channel

**Appointment/booking confirmations:**
- Include Zalo calendar link or Google Calendar link to add
- Include exact address with Google Maps link (Vietnamese users rely heavily on Maps)
- Include "Nếu cần đổi lịch: nhắn Zalo [number]" — flexible rescheduling builds trust

**Onboarding welcome:**
- First email after purchase is highest-read email in the relationship — use it fully
- Set clear expectations: "Trong 24 giờ tới bạn sẽ nhận được [X]"
- Introduce the human behind the brand: "Mình là [Tên] — người sẽ setup hệ thống cho bạn"

**Receipt/invoice:**
- Vietnamese businesses often need VAT invoice (hóa đơn VAT) — include note on how to request
- PDF attachment preferred over inline-only for record keeping

### Tone calibration for transactional emails

Transactional emails should be:
- **Clearer** than marketing emails (utility first)
- **Warmer** than generic system emails (it's still your brand)
- **Shorter** than newsletters (get to the point fast)

The "bạn/mình" register still applies. A confirmation email that says "Kính gửi Quý khách" when all your other emails say "bạn" breaks the brand experience.

## Step 4 — Write output

Save to `outputs/assets/email/transactional-[type]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Transactional Email — [Type]
> Generated: [date] | Type: [transaction type] | Trigger: [what sends this email]

## Trigger
[Exact event that sends this email — e.g., "Stripe payment confirmed", "Calendly booking created"]

## Email

**Subject:** [subject line — clear, not clever]
**From name:** [Brand name or "Tên từ Brand"]

---

[Full email content]

---

## Notes
- Dynamic fields: [list all {{variables}} used — name, order number, date, amount, etc.]
- Fallback for missing data: [what to show if variable is blank]
- Send timing: [immediately / delay X minutes / trigger condition]
- Reply-to: [support email or no-reply + Zalo]
- VAT invoice note: [include or not]

## Upsell / Cross-sell Opportunity
[If applicable: one low-friction next step to include — or "None — keep pure utility"]
```

## Step 5 — Confirm

After writing:

---
"✅ **Transactional email '[Type]' hoàn chỉnh.**

**Trigger:** [event]
**Primary job:** [confirmation statement]
**Secondary:** [one next step or resource]
**Dynamic fields:** [list]

📁 Đã lưu: `outputs/assets/email/transactional-[type]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/email-sequence` để viết onboarding sequence sau transactional email này, hoặc `/re-engagement` để build win-back cho customers đã lapsed."

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
