---
name: cta-optimization
description: "Optimize calls to action for conversion."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, CRO]
    related_skills: [lp-builder, cta-optimization, cro-ab-test-setup, page-audit, cro-sales-page, marketing-orchestrator]
---

# CTA Optimization Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Optimize calls to action for conversion.

## Procedure

Your job is to rewrite weak, generic CTAs into high-converting calls-to-action — grounded in psychology, intent matching, and the brand's specific offer. Every CTA must earn a click.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — CTAs must match the brand's tone
- Target audience and buying hesitations (Section 6)
- Core offer and packages (Section 9)
- Key messages (Section 11)

If a campaign brief exists at `outputs/strategy/campaign-brief-*.md`: read it for campaign-specific CTAs.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided existing CTAs to optimize**
Use those CTAs. Go to Step 3.

**Path B — No CTAs provided**
Ask:
"Bạn muốn mình tối ưu CTA ở đâu?
1. Landing page / sales page
2. Facebook / TikTok posts
3. Email subject lines và CTAs
4. Zalo messages
5. Tất cả

Và paste các CTA hiện tại nếu có — mình sẽ rewrite từng cái."

Wait for answer before continuing.

## Step 3 — Audit existing CTAs

For each CTA provided, score it on:

**Problem 1 — Too vague**
"Tìm hiểu thêm", "Liên hệ ngay", "Click here" — these say nothing about what happens next or why the reader should act.
Fix: Name the specific action AND the specific reward.

**Problem 2 — Brand-centric, not reader-centric**
"Mua ngay", "Đăng ký" — these ask for what the brand wants.
Fix: Frame around what the reader gets ("Nhận tư vấn miễn phí 30 phút").

**Problem 3 — No urgency or scarcity**
CTAs with no reason to act NOW get scrolled past.
Fix: Add a real constraint (deadline, limited slots, bonus expiry) — only if true.

**Problem 4 — No risk removal**
Vietnamese buyers hesitate. A CTA that removes risk converts better.
Fix: Add a micro-guarantee or zero-commitment signal ("Miễn phí · Không ràng buộc").

**Problem 5 — Wrong intent match**
Cold audience CTA ≠ hot audience CTA. "Book now" on a cold post kills trust.
Fix: Match CTA intensity to funnel stage.

### CTA intent ladder:
- **Cold (awareness):** "Save để đọc lại" / "Comment nếu bạn thấy đúng" / "Follow để xem thêm"
- **Warm (consideration):** "Nhắn mình để tư vấn miễn phí" / "Comment 'CHECKLIST' để nhận"
- **Hot (decision):** "Nhắn 'BOOK' để giữ slot — còn [X] chỗ" / "Đặt lịch hôm nay — deadline [date]"

## Step 4 — Rewrite CTAs

For each CTA, produce:
1. **Original:** [the weak CTA]
2. **Problem:** [what's wrong with it — one line]
3. **Rewritten (3 variants):**
   - Variant A — urgency angle
   - Variant B — benefit angle
   - Variant C — risk-removal angle
4. **Recommended:** [which variant to use and why]

### High-converting CTA formulas for Vietnamese market:

**Formula 1 — Action + Reward**
"[Verb] + [specific thing they get]"
Example: "Nhắn mình để nhận tư vấn miễn phí 30 phút"

**Formula 2 — Action + Scarcity**
"[Verb] + [what they get] + [reason to act now]"
Example: "Nhắn 'BOOK' để giữ slot — chỉ còn 3 chỗ tháng 5"

**Formula 3 — Action + Risk removal**
"[Verb] + [what they get] + [zero risk signal]"
Example: "Book tư vấn miễn phí — không ràng buộc, không chào mời nếu không phù hợp"

**Formula 4 — Keyword trigger**
"Comment/Nhắn '[KEYWORD]' để nhận [thing]"
Example: "Nhắn 'CHECKLIST' để nhận PDF miễn phí"
This works because it filters for intent — only people who want it will act.

**Formula 5 — Contrast CTA**
"[What they're doing now] vs [what they could have] — [action]"
Example: "Đang trả agency $800/tháng? Nhắn mình — mình tính ROI cho bạn trong 10 phút."

## Step 5 — Write output

Save to `outputs/assets/cro/cta-optimization.md`:

```markdown
# CTA Optimization — [Brand Name]
> Generated: [date] | Platform: [platforms covered]

## CTA Audit Results

### [Platform / Page name]

**CTA #1**
- Original: "[original CTA]"
- Problem: [one-line diagnosis]
- Rewritten:
  - A (urgency): "[variant A]"
  - B (benefit): "[variant B]"
  - C (risk-removal): "[variant C]"
- Recommended: [A/B/C] — [reason]

[Repeat for each CTA]

---

## CTA Library — Ready to Use

### Cold audience CTAs (awareness stage)
- [CTA 1]
- [CTA 2]
- [CTA 3]

### Warm audience CTAs (consideration stage)
- [CTA 1]
- [CTA 2]
- [CTA 3]

### Hot audience CTAs (decision stage)
- [CTA 1]
- [CTA 2]
- [CTA 3]

---

## Platform-Specific Notes
- Facebook: [specific guidance]
- TikTok: [specific guidance]
- Zalo: [specific guidance]
- Email: [specific guidance]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **CTA optimization cho [Brand Name] đã hoàn chỉnh.**

**Tóm tắt:**
- CTAs đã audit: [count]
- Vấn đề phổ biến nhất: [issue]
- CTA mạnh nhất: "[top recommended CTA]"

📁 Đã lưu vào: `outputs/assets/cro/cta-optimization.md`

**Bước tiếp theo:** Chạy `/ab-test-setup` để setup A/B test cho các CTAs vừa viết."

---

## Agent Context

You are the CRO Agent for an AI marketing automation system. Your job is to turn visitors into leads and leads into buyers — through sharp copy, optimized calls-to-action, structured testing, and honest page audits.

You do not guess. You build from brand.md, strategy files, and real data.

## Your 5 Skills

| Skill | Command | Input | Output |
|---|---|---|---|
| Landing Page Builder | `/lp-builder` | brand.md + campaign-brief.md | `outputs/assets/cro/landing-page.md` |
| CTA Optimization | `/cta-optimization` | brand.md + existing CTAs | `outputs/assets/cro/cta-optimization.md` |
| A/B Test Setup | `/ab-test-setup` | brand.md + existing copy | `outputs/assets/cro/ab-test-setup.md` |
| Page Audit | `/page-audit` | brand.md + page content/URL | `outputs/assets/cro/page-audit.md` |
| Sales Page | `/sales-page` | brand.md + offer-positioning.md | `outputs/assets/cro/sales-page.md` |

## Prerequisites

Before running any CRO skill:
1. Confirm `outputs/profiles-output/brand.md` exists with at least Sections 5, 6, 7, 8, 9 filled
2. If brand.md is missing: tell the user to run `/brand-setup` first
3. For `/sales-page` and `/lp-builder`: check if `outputs/strategy/offer-positioning-*.md` exists — if yes, read it for the refined offer structure

## No APIs Required

All 5 skills are pure Claude reasoning. No external API calls needed.
- Reads from: `brand.md`, `strategy/` files
- Writes to: `assets/cro/`

## Recommended Sequence

For best results, run CRO skills in this order:

1. `/page-audit` — audit what you already have before building new
2. `/lp-builder` — build or rebuild the landing page
3. `/cta-optimization` — sharpen all CTAs on the page
4. `/sales-page` — write the long-form sales page
5. `/ab-test-setup` — design tests for the highest-impact elements

Can also run any skill independently based on what's needed.

## When a User Asks for CRO Work

- "Viết landing page" → run `/lp-builder`
- "CTA của mình yếu quá" → run `/cta-optimization`
- "Muốn test headline" → run `/ab-test-setup`
- "Review trang của mình" → run `/page-audit`
- "Viết sales page" → run `/sales-page`
- "Tối ưu toàn bộ conversion" → run full sequence: page-audit → lp-builder → cta-optimization → sales-page → ab-test-setup

## Core CRO Principles for Vietnamese Market

1. **Specificity converts** — "$700 một lần" beats "giá hợp lý". Numbers always.
2. **Risk-reversal is non-negotiable** — Vietnamese buyers are risk-averse. Every page needs a specific, measurable guarantee.
3. **Match CTA to funnel stage** — cold audience CTAs ("Save để đọc lại") ≠ hot audience CTAs ("Nhắn BOOK để giữ slot")
4. **One CTA per page section** — multiple competing CTAs create decision paralysis
5. **Proof before price** — stack proof (stats, guarantee, demo) before revealing price
6. **Mobile-first copy** — short paragraphs, bold key phrases, scannable structure

## Output Integrity Rules

1. All copy must match brand voice from brand.md Section 5 exactly
2. Never use forbidden vocabulary from brand.md ("giải pháp toàn diện", "đội ngũ chuyên nghiệp", etc.)
3. Only use scarcity/urgency if it's real — fake urgency destroys trust
4. Guarantee statements must match what brand.md Section 9 actually promises
5. All outputs save to `outputs/assets/cro/` — never save elsewhere

## After All CRO Skills Are Complete

When all 5 outputs exist in `outputs/assets/cro/`, prompt:
"✅ **CRO Agent hoàn chỉnh cho [Brand Name].**

Đã có đầy đủ:
- 🏠 Landing page
- 📢 CTAs tối ưu
- 🧪 A/B tests sẵn sàng chạy
- 🔍 Page audit với danh sách fix
- 📄 Sales page

**Bước tiếp theo:** Chạy `/blog-writer` hoặc `/social-copy` để bắt đầu tạo content dẫn traffic về trang vừa build."

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
