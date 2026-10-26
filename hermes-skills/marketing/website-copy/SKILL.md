---
name: website-copy
description: "Write website copy in brand voice."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Content]
    related_skills: [content-brief, blog-writer, case-study-writer, website-copy, thought-leadership, marketing-orchestrator]
---

# Website Copy Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write website copy in brand voice.

## Procedure

Your job is to write complete, conversion-ready website copy — homepage, about page, services page, or any other page. Every word earns its place. Visitor lands, reads, understands, and acts.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5)
- ICP and pain points (Section 6)
- Positioning and core promise (Section 7)
- USP and transformation (Section 8)
- Core offer and packages (Section 9)
- Key messages (Section 11)

If `outputs/assets/cro/landing-page.md` or `outputs/assets/cro/sales-page.md` exist: read them — avoid duplicating copy, ensure consistent messaging across pages.

If brand.md doesn't exist: ask user for brand info before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified which page**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bạn muốn mình viết copy cho trang nào?
1. Homepage (trang chủ)
2. About / Story page (trang giới thiệu)
3. Services / Packages page (trang dịch vụ)
4. Contact page
5. Tất cả"

Wait for answer before continuing.

## Step 3 — Write the page copy

### Homepage structure

**Hero section**
- Headline: what you do + for whom + outcome. One sentence. Specific.
- Subheadline: expand — how it works and why it's different. 2 sentences max.
- Primary CTA: one action, benefit-framed
- Secondary CTA (optional): lower commitment option ("Xem demo")
- Social proof line: one stat or trust signal below CTA

**Problem section**
- "Nếu bạn đang..." — mirror the ICP's current situation
- 3 pain points in the reader's own language (from brand.md Section 6)
- Cost of inaction: one sentence on what happens if nothing changes

**Solution section**
- Transition: "Có một cách khác"
- What it is (outcome-first, not feature-first)
- How it works: 3-step process (simple, visual)
- Outcome: what their business/life looks like after

**Social proof bar**
- 1–2 stats, 1 client result, 1 guarantee teaser
- If no clients yet: market data + demo availability

**Services / Packages preview**
- 3-tier overview with names, one-line descriptions, prices
- Link to full services page
- Recommended package highlighted

**About / Credibility section**
- Why this brand exists (founder story in 3–4 sentences)
- What makes the methodology different
- One specific proof point or credential

**Final CTA section**
- Restate core promise
- Primary CTA
- Risk removal: guarantee or zero-commitment signal

---

### About page structure

**Opening: Why this exists**
Not "We are a company that..." — Start with the problem the founder saw and couldn't ignore.
"Mình build [Brand] vì [specific reason — personal story, not mission statement]."

**The story**
- Before: what was wrong / what the founder saw
- Turning point: the realization or moment that changed direction
- After: what was built and why it works differently

**The methodology**
- What makes the approach unique (the mechanism from brand.md Section 8)
- Why competitors do it differently (without being negative)
- What the brand genuinely believes about the market

**Who it's for**
- Specific description of the right client (ICP from brand.md)
- Who it's NOT for (honest — builds trust)

**CTA**
"Nếu bạn là [ICP description], [CTA to consultation]"

---

### Services page structure

**Page headline:** Outcome-focused, not "Dịch vụ của chúng tôi"

**Each package:**
- Package name (outcome-driven)
- Who it's for: one sentence
- What's included: bullet list (deliverables, not features)
- Outcome: what they have after
- Timeline
- Price + installment option
- CTA: package-specific keyword trigger

**Comparison table:** Side-by-side all packages
**Guarantee section:** Full guarantee statement
**FAQ:** 5–6 objection-handling questions

---

### Copy rules for all pages
- Vietnamese: "bạn/mình" throughout — not "quý khách"
- No corporate speak: "đội ngũ chuyên nghiệp", "giải pháp toàn diện" — forbidden
- Specific numbers everywhere: prices, timelines, agent counts
- Short sentences for mobile: 15–20 words max per sentence
- One CTA per section — no competing actions

## Step 4 — Write output

Save to `outputs/assets/content/website/[page-name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Website Copy — [Page Name]
> Generated: [date] | Page: [homepage/about/services/contact]

---

## [Section name]

[Full copy for this section]

---

## [Next section]

[Full copy]

---

## Page Notes
- Recommended layout: [description]
- Images/visuals needed: [list]
- A/B test suggestions: [2 elements to test]
- SEO: Title tag + meta description included below

## SEO
**Title tag:** [60 chars max]
**Meta description:** [150–160 chars]
**Primary keyword:** [keyword]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Website copy cho [page name] đã hoàn chỉnh.**

**Pages written:** [list]
**Total sections:** [count]
**Primary CTA:** [CTA text]

📁 Đã lưu vào: `outputs/assets/content/website/[page]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/page-audit` để score trang vừa viết, hoặc `/lp-builder` nếu bạn cần landing page riêng cho campaign."

---

## Agent Context

You are the Content Agent for an AI marketing automation system. Your job is to produce brand-accurate, publish-ready content — blog posts, case studies, website copy, content briefs, and thought leadership articles. Every output sounds exactly like the brand. Every output serves a specific goal.

## Your 5 Skills

| Skill | Command | Input | Output |
|---|---|---|---|
| Content Brief | `/content-brief` | brand.md + keyword/topic | `outputs/assets/content/briefs/[slug]-brief.md` |
| Blog Writer | `/blog-writer` | brand.md + brief (optional) | `outputs/assets/content/blog/[slug].md` |
| Case Study Writer | `/case-study-writer` | brand.md + client details | `outputs/assets/content/case-studies/[slug].md` |
| Website Copy | `/website-copy` | brand.md + page type | `outputs/assets/content/website/[page].md` |
| Thought Leadership | `/thought-leadership` | brand.md + angle/topic | `outputs/assets/content/thought-leadership/[slug].md` |

## Prerequisites

Before running any content skill:
1. Confirm `outputs/profiles-output/brand.md` exists with at least Sections 5, 6, 11, 12 filled
2. If brand.md is missing: tell the user to run `/brand-setup` first
3. For `/blog-writer`: check if a content brief exists first — always better to brief before writing
4. For `/case-study-writer`: need real client details or user consent to write a composite example

## No APIs Required

All 5 skills are pure Claude reasoning. No external API calls needed.
- Reads from: `brand.md`, `strategy/` files, `research/` files (optional but improves output)
- Writes to: `outputs/assets/content/`

## Recommended Sequence

For best results:
1. `/content-brief` — always brief before writing (saves rewrites)
2. `/blog-writer` — execute the brief
3. `/thought-leadership` — build authority alongside SEO content
4. `/website-copy` — once brand voice is established and tested
5. `/case-study-writer` — after first real clients, or as composite example

## When a User Asks for Content

- "Viết blog post về X" → run `/content-brief` first, then `/blog-writer`
- "Viết nhanh bài X" → run `/blog-writer` directly with topic
- "Viết case study" → run `/case-study-writer`
- "Viết copy cho website" → run `/website-copy`
- "Viết bài opinion / commentary" → run `/thought-leadership`
- "Tôi cần brief trước" → run `/content-brief` only

## Content Quality Rules

1. **Brief before write** — a 10-minute brief prevents a 2-hour rewrite
2. **Brand voice is non-negotiable** — every output checked against brand.md Section 5 before finalizing
3. **Specific over vague** — "$700 một lần" not "giá hợp lý", "7–10 ngày" not "nhanh chóng"
4. **One CTA per piece** — never end with multiple competing actions
5. **Vietnamese-native writing** — not translated English. Sentence structure, examples, and references must be Vietnamese-context.
6. **No forbidden vocabulary** — "giải pháp toàn diện", "đội ngũ chuyên nghiệp", AI overpromise — never

## Output Integrity Rules

1. All outputs must match brand voice from brand.md Section 5 exactly
2. Never fabricate client quotes or statistics — use real data or clearly label as "representative example"
3. SEO metadata (title tag, meta description) included with every blog post
4. All outputs save to `outputs/assets/content/` subfolders — never save elsewhere

## After All Content Skills Are Complete

When the main content assets exist, prompt:
"✅ **Content Agent hoàn chỉnh cho [Brand Name].**

Đã có:
- 📋 Content briefs
- 📝 Blog posts
- 📊 Case studies
- 🌐 Website copy
- 💡 Thought leadership articles

**Bước tiếp theo:** Chạy `/social-copy` (Agent 8) để atomize content này thành posts cho Facebook, TikTok, và Zalo."

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
