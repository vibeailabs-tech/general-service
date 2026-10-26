---
name: re-engagement
description: "Write re-engagement campaigns for cold lists."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Email]
    related_skills: [email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email, marketing-orchestrator]
---

# Re-engagement Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write re-engagement campaigns for cold lists.

## Procedure

Your job is to write a re-engagement sequence for inactive subscribers or lapsed customers — win them back or clean them from the list. No passive "we miss you" emails. Every email has a real reason to re-engage.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5)
- Core offer (Section 9) — what you're ultimately trying to get them back to
- Target audience (Section 6) — understand why they might have gone cold

If brand.md doesn't exist: ask user for brand, offer, and inactive segment description before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described the inactive segment**
Use what they gave. Go to Step 3.

**Path B — No info provided**
Ask:
"Để viết re-engagement sequence, mình cần biết:
1. **Ai là người nhận?** Subscribers chưa mở email bao lâu? Khách hàng cũ chưa mua lại bao lâu?
2. **Lý do có thể họ đã cold:** Không relevant? Quá nhiều email? Đã tìm được giải pháp khác? Chưa đến thời điểm mua?
3. **Có gì mới để offer?** New feature, new content, new offer, hay giảm giá?
4. **End state:** Nếu không re-engage sau sequence này — unsubscribe hay giữ lại?"

Wait for answer.

## Step 3 — Write the re-engagement sequence

### Re-engagement psychology

People go cold for 3 main reasons:
1. **Irrelevance** — content stopped matching their situation
2. **Timing** — they weren't ready when they joined, might be ready now
3. **Overload** — too many emails, they tuned out

The re-engagement sequence must address the actual reason — not just say "we miss you."

### 3-email re-engagement structure

**Email 1 — The Pattern Interrupt**
Don't pretend everything is fine. Acknowledge they've been quiet — but frame it as useful information, not guilt. Offer something genuinely valuable (insight, tool, resource) with no ask attached.

Goal: Get an open and a read. Nothing more.

Subject approach: Surprising statement, direct question, or a specific thing that's changed since they last engaged.

**Email 2 — The Reason to Come Back**
Introduce what's new or what's changed. New case study, new feature, new angle on the problem they care about. Give them a real reason to re-engage — not a coupon (unless that's right for this brand).

If applicable: include a soft offer or invitation (book a call, take a quiz, reply with their situation).

Goal: Click or reply.

**Email 3 — The Honest Ask**
The final email. Be direct: "Mình sẽ xóa bạn khỏi danh sách sau email này — nếu bạn vẫn muốn ở lại, nhấn vào đây."

This email has two wins: either they re-engage (active subscriber back), or they don't (list is cleaner). Both are good outcomes.

Subject: Direct — "Đây là email cuối mình gửi bạn" or "Mình sẽ xóa địa chỉ của bạn ngày [date]"

### Vietnamese market notes on re-engagement

- Vietnamese subscribers respond well to **directness** — "Mình thấy bạn chưa đọc email gần đây" outperforms vague "we miss you"
- **Zalo alternative:** For Vietnamese businesses, if email re-engagement fails, a personal Zalo message often works better. Include a Zalo option in Email 3.
- **Guilt framing doesn't work** — don't make them feel bad for going cold. Make them feel like there's a real reason to return.
- **Sunset window:** 90–180 days inactive = re-engagement worthy. 180+ days = sunset immediately.

### Sunset policy (after sequence)

If subscriber doesn't engage after 3 emails:
- Remove from active list
- Move to suppression list (don't delete — prevents future re-subscribe confusion)
- Do NOT keep sending — deliverability damage from inactive subscribers hurts the whole list

## Step 4 — Write output

Save to `outputs/assets/email/re-engagement-[segment]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Re-engagement Sequence — [Segment Name]
> Generated: [date] | Segment: [description] | Emails: 3 | Goal: [re-engage or sunset]

## Segment Description
- Who they are: [description]
- Inactive since: [timeframe]
- Likely reason cold: [hypothesis]
- What's changed: [new offer/content/reason to return]

---

## Email 1 — Pattern Interrupt
**Send:** Day 1
**Subject:** [subject]
**Preview:** [preview]

---

[Email body]

---

## Email 2 — Reason to Return
**Send:** Day 4
**Subject:**
**Preview:**

---

[Email body]

---

## Email 3 — The Honest Ask
**Send:** Day 8
**Subject:**
**Preview:**

---

[Email body]

---

## Post-Sequence Action
- If opens Email 1–2 but doesn't click: [action]
- If clicks any email: [move to which sequence]
- If no engagement after Email 3: [sunset — move to suppression list]

## Sunset Note
Subscribers who don't engage after this sequence should be removed from active list on [date]. Estimated list cleanup: [n]% of inactive segment.
```

## Step 5 — Confirm

After writing:

---
"✅ **Re-engagement sequence cho '[Segment]' hoàn chỉnh.**

**3 emails:**
1. [Subject 1] — Pattern interrupt
2. [Subject 2] — Reason to return
3. [Subject 3] — Honest ask / sunset

**Post-sequence:** Non-engagers moved to suppression after Day 8.

📁 Đã lưu: `outputs/assets/email/re-engagement-[segment]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/email-sequence` để write welcome sequence cho new subscribers, hoặc `/subject-line-ab` để optimize subject lines trong sequence này."

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
