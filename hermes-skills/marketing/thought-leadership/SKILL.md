---
name: thought-leadership
description: "Write thought-leadership content pieces."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Content]
    related_skills: [content-brief, blog-writer, case-study-writer, website-copy, thought-leadership, marketing-orchestrator]
---

# Thought Leadership Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write thought-leadership content pieces.

## Procedure

Your job is to write opinion articles and industry commentary that position this brand as the sharpest, most trustworthy voice in the space. Not content marketing dressed as opinion. Real perspective. A clear point of view. Something worth disagreeing with.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — bold, pragmatic, trustworthy — this is where bold matters most
- Positioning and competitive angle (Section 7) — what does this brand genuinely believe?
- Key messages (Section 11) — each thought leadership piece should reinforce one of these
- Content pillars (Section 12) — which pillar does this piece serve?
- USP (Section 8) — the mechanism and belief system behind the brand

If `outputs/research/trend-monitoring-*.md` exists: read it — use current trends as the hook or counterpoint.
If `outputs/research/market-research-*.md` exists: use market data to support the argument.

If brand.md doesn't exist: ask user for brand info before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User has a topic or angle**
Use their angle. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bài thought leadership này muốn nói điều gì?
1. Quan điểm về ngành (industry commentary — điều mà mọi người đang làm sai)
2. Dự đoán (prediction — điều sắp xảy ra mà ít người thấy)
3. Phản biện (contrarian take — quan điểm ngược với số đông)
4. Bài học rút ra (lessons from experience — điều mình học được)
5. Framework / mental model (cách nhìn mới về vấn đề quen thuộc)

Và topic cụ thể?"

Wait for answer before continuing.

## Step 3 — Write the thought leadership piece

### What makes thought leadership different from a blog post

A blog post informs. Thought leadership challenges.

A blog post answers "how to." Thought leadership answers "why this matters" or "why everyone else is wrong."

A blog post is safe. Thought leadership has a point of view someone can disagree with.

**Test:** If you removed the author's name and replaced it with any other brand in the space — would it still make sense? If yes, it's not thought leadership. It's content.

### Structure for a thought leadership piece

**Opening: The provocation (100–150 words)**
Start with the controversial claim, the uncomfortable truth, or the prediction. Don't bury the lede.

Not: "Trong thời đại AI phát triển nhanh chóng, doanh nghiệp cần thích ứng..."
Yes: "73% doanh nghiệp Việt Nam đã dùng AI — và phần lớn trong số đó đang làm sai hoàn toàn."

**The argument (body)**
- H2s as arguments, not topics
- Each section advances the central thesis
- Use: personal observation, market data, specific examples, logical consequence
- Acknowledge the strongest counterargument — then refute it. This builds credibility.
- Avoid: vague claims, unverifiable statements, generic advice

**The implication**
What does this mean for the reader specifically? If the argument is true — what should they do differently starting today?

**The close**
- Restate the central claim — stronger, with more evidence behind it now
- One specific, actionable conclusion
- CTA that flows naturally from the argument

### Tone calibration for Vietnamese B2B thought leadership
- Direct, but not arrogant — "Mình tin rằng..." not "Rõ ràng là..."
- Back every claim with a specific example or number
- Acknowledge uncertainty where it exists — "Dữ liệu chưa đủ để chắc chắn, nhưng mình thấy pattern này..."
- Vietnamese readers respond to: concrete stories, specific numbers, honest admission of limits
- Avoid: moralizing, lecturing, overpromising

### Formats
- **Long form (1,000–1,500 words):** LinkedIn article, blog post, Medium
- **Short form (400–600 words):** Facebook long post, newsletter section
- **Thread format:** 8–12 points, each 2–3 sentences — for Facebook/LinkedIn

## Step 4 — Write output

Save to `outputs/assets/content/thought-leadership/[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# [Title — The Claim, Not the Topic]
> Generated: [date] | Format: [long/short/thread] | Pillar: [content pillar] | Platform: [primary platform]

---

[Full article content]

---

## Repurposing Notes
- TikTok angle: [how to turn this into a 60s video]
- Zalo version: [shortened 150-word version for broadcast]
- Facebook short version: [hook + 3 key points + CTA]

## Follow-up content ideas
1. [Related piece this argument leads to]
2. [Counterargument piece to write next]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Thought leadership piece '[Title]' đã hoàn chỉnh.**

**Central claim:** [one sentence — the argument]
**Format:** [long/short/thread]
**Content pillar:** [pillar]
**Strongest point:** [the section that will generate most discussion]

📁 Đã lưu vào: `outputs/assets/content/thought-leadership/[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/social-copy` để atomize bài này thành Facebook post + TikTok script + Zalo message."

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
