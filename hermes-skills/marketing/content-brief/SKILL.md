---
name: content-brief
description: "Write briefs that guide content production."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Content]
    related_skills: [content-brief, blog-writer, case-study-writer, website-copy, thought-leadership, marketing-orchestrator]
---

# Content Brief Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write briefs that guide content production.

## Procedure

Your job is to write a research-backed content brief before any content is created. No writer — human or AI — should produce a blog post, article, or website copy without a brief. This is the brief.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5)
- Target audience and pain points (Section 6)
- Content pillars (Section 12)
- Key messages (Section 11)
- Positioning (Section 7)

If `outputs/research/keyword-research-*.md` exists: read it — use Tier 1–3 keywords and PAA questions.
If `outputs/strategy/campaign-brief-*.md` exists: read it — align brief to campaign goals.

If brand.md doesn't exist: ask user for brand info before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a topic or keyword**
Use their topic. Go to Step 3.

**Path B — No topic provided**
Ask:
"Bạn muốn mình viết brief cho loại content nào?
1. Blog post (SEO — target keyword cụ thể)
2. Thought leadership article (opinion / industry commentary)
3. Website copy (homepage / about / services)
4. Case study (customer success story)

Và topic hoặc keyword cụ thể là gì?"

Wait for answer before continuing.

## Step 3 — Build the brief

### Brief components (fill all of them)

**1. Content goal**
What should this piece accomplish? Pick one primary:
- Rank for a keyword (SEO)
- Build trust with cold audience (awareness)
- Convert warm leads (consideration/decision)
- Establish thought leadership (authority)

**2. Target audience**
Not "SMB owners" — the specific person reading this piece right now. What's their situation? What brought them to this article? What do they already believe?

**3. Target keyword (for SEO pieces)**
- Primary keyword: [exact phrase]
- Secondary keywords: 2–3 related terms
- Search intent: informational / commercial / navigational
- Estimated difficulty: low / medium / high (based on keyword-research.md or content of SERP)

**4. Headline options (3)**
- Option 1: SEO-optimized (keyword in headline)
- Option 2: Curiosity/emotion angle
- Option 3: Specific outcome/number angle
Mark the recommended one.

**5. Article structure**
- Hook (first 2–3 sentences — what makes them keep reading)
- H2 sections (4–6 sections with specific subheading copy — not "Introduction", "Conclusion")
- For each section: what argument/point is made, what evidence supports it
- CTA placement: where and what

**6. Key argument**
One sentence: what is the single most important thing this piece proves or argues?

**7. Proof points to include**
- Statistics (from research files or brand.md)
- Examples or case studies
- Comparisons or analogies

**8. What NOT to include**
- Topics that distract from the main argument
- Competitor mentions that don't serve the piece
- Generic advice anyone could give

**9. SEO requirements**
- Primary keyword in: title, H1, first 100 words, at least 2 H2s, meta description
- Meta description: 150–160 characters, includes keyword + benefit
- Internal link suggestions: which other pages/posts to link to
- Recommended word count: [based on what ranks for this keyword]

**10. CTA**
What should the reader do after finishing this piece? One specific action.

## Step 4 — Write output

Save to `outputs/assets/content/briefs/[topic-slug]-brief-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Content Brief — [Title]
> Generated: [date] | Type: [blog/article/website copy] | Keyword: [keyword]

## Goal
[Primary goal — one sentence]

## Target Reader
[Specific person — situation, what they already know, what they're looking for]

## Keyword Strategy
- Primary: [keyword]
- Secondary: [keyword 1], [keyword 2]
- Intent: [informational/commercial/navigational]
- Word count target: [count]

## Headline Options
1. [Option 1] — SEO angle ← Recommended
2. [Option 2] — Curiosity angle
3. [Option 3] — Outcome angle

## Key Argument
[One sentence: what this piece proves]

## Article Structure

### Hook
[What the opening 2–3 sentences accomplish]

### H2: [Exact subheading copy]
- Point: [what's argued]
- Evidence: [stat, example, or analogy to use]

### H2: [Exact subheading copy]
- Point:
- Evidence:

[Repeat for 4–6 sections]

### CTA Section
[Where it goes + what it says]

## Proof Points
- [Stat or data point]
- [Example or case study]
- [Comparison or analogy]

## Do NOT Include
- [Topic to avoid]
- [Framing to avoid]

## SEO Checklist
- [ ] Primary keyword in title
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least 2 H2s
- [ ] Meta description written (150–160 chars)
- [ ] Internal links suggested

## Meta Description
[150–160 character meta description with keyword]

## Internal Link Suggestions
- Link to: [page/post] — anchor text: [text]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Content brief cho '[Title]' đã hoàn chỉnh.**

**Summary:**
- Keyword: [primary keyword]
- Key argument: [one sentence]
- Structure: [count] sections
- Word count target: [count] từ
- CTA: [CTA text]

📁 Đã lưu vào: `outputs/assets/content/briefs/[slug]-brief-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/blog-writer` với brief này để viết bài hoàn chỉnh."

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
