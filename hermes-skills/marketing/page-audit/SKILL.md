---
name: page-audit
description: "Audit a page for conversion weaknesses."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, CRO]
    related_skills: [lp-builder, cta-optimization, cro-ab-test-setup, page-audit, cro-sales-page, marketing-orchestrator]
---

# Page Audit Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Audit a page for conversion weaknesses.

## Procedure

Your job is to score an existing page — landing page, sales page, Facebook page, or any marketing asset — and deliver a prioritized list of specific fixes. Not vague advice. Exact changes with expected impact.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — to check if page matches
- Target audience and pain points (Section 6) — to check if page speaks to them
- Core offer (Section 9) — to check if offer is presented clearly
- USP (Section 8) — to check if differentiation is visible
- Competitors (Section 10) — to check if positioning is distinct

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided page content or URL**
Use what they gave. Go to Step 3.

**Path B — No page provided**
Ask:
"Bạn muốn mình audit trang nào?
- Paste nội dung trang vào đây, hoặc
- Cho mình URL để mình scrape, hoặc
- Mô tả trang (Facebook page / landing page / Zalo OA profile...)

Và mục tiêu của trang này là gì? (thu lead / bán trực tiếp / build trust)"

Wait for answer before continuing.

## Step 3 — Run the audit

Score the page across 6 dimensions (1–10 each):

### Dimension 1 — Clarity (Rõ ràng)
**Question:** Trong 5 giây, người lạ có biết (1) trang này là của ai, (2) họ làm gì, (3) tại sao mình nên quan tâm không?
- 9–10: Tất cả 3 câu trả lời rõ ngay trong hero
- 7–8: 2/3 rõ, 1 cái phải đọc xuống
- 5–6: Phải đọc 30 giây mới hiểu
- 1–4: Vẫn không rõ sau khi đọc hết

### Dimension 2 — Relevance (Đúng người)
**Question:** Người đọc có thấy "đây là dành cho mình" không?
- Check: ICP language, pain points, specific audience signals
- Red flags: "phục vụ mọi đối tượng", vague audience, no pain point articulation

### Dimension 3 — Value Proposition (Giá trị rõ ràng)
**Question:** Lợi ích cụ thể là gì? Có số liệu không? Có outcome không?
- Check: specific numbers, before/after, timeline, price anchoring
- Red flags: "tăng trưởng mạnh mẽ", "hiệu quả vượt trội", features without outcomes

### Dimension 4 — Trust (Tin tưởng)
**Question:** Có lý do để tin không?
- Check: testimonials, guarantees, social proof, credentials, specific results
- Red flags: no proof, vague guarantees ("hài lòng 100%"), stock photos

### Dimension 5 — CTA Strength (Hành động rõ ràng)
**Question:** Có một CTA rõ ràng, compelling, và đúng lúc không?
- Check: CTA text specificity, placement, number of CTAs (too many = confusion)
- Red flags: "Liên hệ ngay", multiple competing CTAs, CTA buried below fold

### Dimension 6 — Friction (Rào cản)
**Question:** Có điều gì đang chặn người đọc hành động không?
- Check: page load speed signals, form length, commitment level of CTA, objections not addressed
- Red flags: long forms, asking for too much info, no FAQ, no risk reversal

### Overall score: (sum of 6 dimensions) / 6

### Score interpretation:
- 8–10: Strong page — optimize details
- 6–7: Decent foundation — 3–4 targeted fixes needed
- 4–5: Significant gaps — rebuild 2–3 major sections
- 1–3: Needs full rebuild — start from brand.md

## Step 4 — Prioritize fixes

For each issue found, assign:
- **Impact:** High / Medium / Low (on conversion rate)
- **Effort:** Easy (30 min) / Medium (2–3 hrs) / Hard (full rebuild)
- **Priority:** Fix immediately / Fix this week / Fix this month

### Fix prioritization matrix:
- High impact + Easy effort → **Do first** (quick wins)
- High impact + Hard effort → **Plan and schedule**
- Low impact + Easy effort → **Do when time allows**
- Low impact + Hard effort → **Skip for now**

## Step 5 — Write output

Save to `outputs/assets/cro/page-audit.md`:

```markdown
# Page Audit — [Brand Name]
> Generated: [date] | Page: [page name/URL] | Goal: [page goal]

---

## Overall Score: [X]/10

| Dimension | Score | Grade |
|---|---|---|
| Clarity | [X]/10 | [A/B/C/D/F] |
| Relevance | [X]/10 | |
| Value Proposition | [X]/10 | |
| Trust | [X]/10 | |
| CTA Strength | [X]/10 | |
| Friction | [X]/10 | |

---

## What's Working
- [strength 1]
- [strength 2]
- [strength 3]

---

## Critical Issues (Fix Immediately)

### Issue #1 — [Issue name]
- **Dimension:** [which dimension]
- **What's wrong:** [specific description]
- **Current:** "[current copy or element]"
- **Fix:** "[exact replacement or action]"
- **Expected impact:** [what will improve]

[Repeat for each critical issue]

---

## High-Impact Fixes (This Week)

### Fix #1 — [Fix name]
- **Current:** [what exists now]
- **Recommended:** [specific change]
- **Why:** [reason]

[Repeat]

---

## Quick Wins (30 Minutes Each)
1. [Quick win 1] — [exact change]
2. [Quick win 2] — [exact change]
3. [Quick win 3] — [exact change]

---

## Lower Priority (This Month)
- [Issue] — [recommendation]
- [Issue] — [recommendation]

---

## Rewritten Elements
Key sections that need complete rewrites (with new copy):

### Hero (rewritten)
[New headline + subheadline + CTA]

### [Other section if needed]
[New copy]

---

## A/B Test Suggestions
Based on this audit, the highest-value things to test:
1. [Test suggestion] — hypothesis: [what you expect]
2. [Test suggestion]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Page audit cho [Brand Name] đã hoàn chỉnh.**

**Điểm tổng:** [X]/10

**3 vấn đề nghiêm trọng nhất:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]

**Quick win ngay hôm nay:** [top quick win]

📁 Đã lưu vào: `outputs/assets/cro/page-audit.md`

**Bước tiếp theo:** Fix critical issues trước, sau đó chạy `/ab-test-setup` để test các thay đổi."

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
