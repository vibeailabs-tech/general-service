---
name: cro-sales-page
description: "Write long-form sales page copy."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, CRO]
    related_skills: [lp-builder, cta-optimization, cro-ab-test-setup, page-audit, cro-sales-page, marketing-orchestrator]
---

# Sales Page Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write long-form sales page copy.

## Procedure

Your job is to write a complete long-form sales page — the kind that takes a skeptical stranger and walks them all the way to "I want this." Every section earns the next. No filler. No corporate speak. Real copy that sells.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — the entire page must sound like this brand
- ICP and pain points (Section 6) — the page opens by speaking directly to them
- Positioning (Section 7) — the core promise lives here
- USP and proof points (Section 8) — use the before/after transformation and proof points
- Core offer and packages (Section 9) — the offer section is built from this
- Competitor table (Section 10) — for the comparison/differentiation section
- Key messages (Section 11) — the 3 core messages must appear in the page

If `outputs/strategy/offer-positioning-*.md` exists: read it — use the refined offer structure, guarantee, and value framing.
If `outputs/strategy/campaign-brief-*.md` exists: read it — use campaign-specific hooks and CTAs.

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified the offer or campaign**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Sales page này cho offer nào?
1. Toàn bộ service (tất cả packages)
2. Một package cụ thể (Starter / Growth / Full System)
3. Campaign đặc biệt (Labor Day / launch offer...)
4. Free consultation funnel (trang thu lead trước)

Và đây là trang dài (1,500–3,000 từ) hay ngắn (800–1,000 từ)?"

Wait for answer before continuing.

## Step 3 — Write the sales page

Use the Halbert copywriting structure — proven for high-ticket B2B sales in Vietnam:

### Section 1 — Headline + Subheadline
The most important part. Must stop the scroll.

**Headline formula options:**
- Pain + promise: "[Pain they feel right now] — [Promise of what changes]"
- Contrast: "[What they have] vs [What they could have]"
- Specific outcome: "[Specific result] trong [specific timeframe] — [risk removal]"
- Bold claim: "[Claim that challenges their current belief]"

Write 3 headline options. Mark the recommended one.

### Section 2 — The Opening Hook (Agitation)
First 150 words must make them feel seen.
- Describe their current situation in their own words
- Agitate the cost of the problem (time, money, emotional toll)
- Show you understand them — not selling yet

### Section 3 — The Turning Point
"Nhưng có một cách khác..."
- Introduce the idea that things don't have to be this way
- Not the product yet — the possibility

### Section 4 — The Mechanism
What makes this different from everything they've tried.
- Name the unique mechanism (from brand.md Section 8)
- Explain HOW it works — in simple, visual terms
- "It works because..." — the logic that makes it believable

### Section 5 — What You Get (The Offer)
Be exhaustive. Buyers need to feel the value before the price.
- List every deliverable with its value
- Use the "if you had to pay separately" framing to stack value
- Timeline: be specific ("Setup hoàn chỉnh trong 7–10 ngày")

### Section 6 — Proof Section
Stack multiple types of proof:
- Market data / stats (from brand.md Section 8)
- Testimonials or case study (if available — if not, use demo description)
- Logic proof: why the mechanism works
- Guarantee: state it in full — specific, measurable, no-questions-asked

### Section 7 — The Price Reveal
Never reveal price without anchoring first.
- Anchor 1: cost of the problem (what they're losing/paying now)
- Anchor 2: cost of alternatives
- Then: "[Brand]: [price] — một lần"
- Installment option if available
- Reframe: "$700 = less than 1 month agency retainer — and you own it forever"

### Section 8 — The Packages
If multiple tiers:
- Present all 3 clearly
- Each: name, who it's for, what's included, price, CTA
- Highlight recommended tier
- Include Labor Day bonus if campaign-specific

### Section 9 — Objection Handling
Address the top 5 objections directly — in a "You might be thinking..." format.
Use objections from brand.md Section 6 and competitor table Section 10.

### Section 10 — The Guarantee
Full guarantee statement — stand-alone section, not buried.
Make it specific: what exactly is guaranteed, by when, what happens if not met.

### Section 11 — Urgency + Scarcity
Only include if real.
- Real scarcity: "Chỉ 5 slots tháng 5 — mỗi setup cần thời gian thật để làm đúng"
- Real deadline: "Bonus hết hạn 1/5/2026"
- Never fake urgency

### Section 12 — Final CTA
- Restate the core promise in one sentence
- State what happens when they click/message
- Remove all remaining risk
- One clear action

### Copy rules
- Vietnamese register: "bạn/mình" throughout
- Specific numbers always: prices, timelines, agent counts, hours saved, % improvement
- Short paragraphs: 2–3 sentences max
- Bold key phrases — scannable for mobile readers
- Never: "giải pháp toàn diện", "đội ngũ chuyên nghiệp", AI hype language
- Yes: "$700 một lần", "16 agents", "tự chạy được hoặc setup lại miễn phí"

## Step 4 — Write output

Save to `outputs/assets/cro/sales-page.md`:

```markdown
# Sales Page — [Brand Name]
> Generated: [date] | Offer: [offer name] | Length: [word count]

---

## HEADLINE OPTIONS
1. [Option 1] ← Recommended
2. [Option 2]
3. [Option 3]

---

## OPENING HOOK
[Full section — ~150 words]

---

## THE TURNING POINT
[Full section]

---

## THE MECHANISM
[Full section — name the system, explain how it works]

---

## WHAT YOU GET
[Full deliverables list with value framing]

---

## PROOF
[Stats + testimonials/demo description + logic proof]

---

## THE PRICE
[Full price reveal with anchoring]

---

## PACKAGES
[All tiers with full details]

---

## OBJECTIONS
[5+ objections handled in "You might be thinking..." format]

---

## GUARANTEE
[Full guarantee statement — standalone]

---

## URGENCY / SCARCITY
[Only if real — deadline and slot count]

---

## FINAL CTA
[Full closing section]

---

## Page Metadata
- Recommended word count: [count]
- Primary keyword: [keyword for SEO if applicable]
- Mobile notes: [any adjustments for mobile]
- A/B test priority: [top element to test first]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Sales page cho [Brand Name] đã hoàn chỉnh.**

**Cấu trúc:**
- Headline (3 options): [preview of recommended]
- Offer presented: [packages or single offer]
- Proof elements: [count]
- Objections handled: [count]
- Guarantee: [guarantee statement summary]
- Word count: ~[count] từ

📁 Đã lưu vào: `outputs/assets/cro/sales-page.md`

**Bước tiếp theo:** Chạy `/page-audit` để score trang vừa viết và tìm điểm cải thiện, hoặc `/ab-test-setup` để test headline options."

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
