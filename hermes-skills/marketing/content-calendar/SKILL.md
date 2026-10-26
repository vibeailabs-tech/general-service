---
name: content-calendar
description: "Build a scheduled multi-channel content calendar."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Strategy]
    related_skills: [campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning, marketing-orchestrator]
---

# Content Calendar Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Builds a detailed weekly content calendar mapped to keywords, buying stages, and platforms. Use this skill when the user wants to plan what content to publish and when. Trigger whenever the user mentions content calendar, content schedule, what to post, posting plan, or content planning.

Slash command: load this skill and follow its Procedure. Short summary: Build a scheduled multi-channel content calendar.

## Procedure

Your job is to build a concrete, ready-to-execute content calendar — specific posts with topics, formats, platforms, and goals for each. Not a vague "post 3x per week" recommendation. Actual titles and angles, week by week.

## Step 1 — Read inputs

Read the following files:
- `outputs/profiles-output/brand.md` — content pillars (Section 12), brand voice (Section 5), ICP (Section 6)
- `outputs/strategy/campaign-plan-*.md` — monthly themes and weekly structure (if exists)
- `outputs/research/keyword-research-*.md` — keyword targets per tier (if exists)
- `outputs/research/trend-monitoring-*.md` — trending angles to inject (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a time period or platform**
Use their scope. Go to Step 3.

**Path B — No scope provided**
Ask:
"Bạn muốn mình lập lịch nội dung cho:
1. 2 tuần tới (chi tiết nhất, ready to execute ngay)
2. 1 tháng (4 tuần, tổng quan + chi tiết tuần 1–2)
3. 3 tháng (gắn với campaign plan)

Và nền tảng chính:
- Facebook only
- TikTok only
- Facebook + TikTok + Blog
- Tất cả kênh"

Wait for answer before continuing.

## Step 3 — Build the content calendar

### Content mix framework (per week)
Follow the 4-1-1 rule adapted for Vietnamese SMB:
- **4 pieces** — educational / value content (builds trust, no sell)
- **1 piece** — proof / social proof (case study, review, result)
- **1 piece** — promotional / CTA (offer, booking, lead magnet)

### Content types by platform

**Facebook:**
- Long-form storytelling post (300–500 words) — pain point story → insight → CTA
- Short punchy post (50–100 words) — bold statement or contrast
- Image carousel — "X điều về..." or before/after
- Video/Reel — demo, behind-the-scenes, tip

**TikTok:**
- Hook video (15–30s) — starts with conflict or contrast
- Tutorial/tip (30–60s) — practical, actionable
- POV / day-in-life — humanizes the brand
- Trending sound + brand message overlay

**Blog/SEO:**
- Long-form article (800–1500 words) — targets Tier 1–2 keywords
- FAQ page — targets "là gì", "bao nhiêu" searches
- Comparison article — "[Brand] vs [Competitor]" or "[Option A] vs [Option B]"

**Zalo:**
- Personal updates and behind-the-scenes
- Exclusive offers for Zalo contacts
- Quick tips (shorter than Facebook)

**Email (if applicable):**
- Weekly value email — one insight, one story, one CTA
- Nurture sequence for new leads

### For each content piece, specify:
- **Date / week**
- **Platform**
- **Content type** (post / video / blog / email)
- **Title or hook** (specific — not "tips about skincare" but "3 lý do da bạn vẫn bị kích ứng dù đã dùng sản phẩm đắt tiền")
- **Content pillar** it belongs to (from brand.md Section 12)
- **Keyword target** (if blog/SEO content)
- **Goal** (awareness / trust / leads / conversion)
- **CTA** (what should the reader do next)

### Assign content to pillars evenly:
Pull content pillars from brand.md Section 12. Distribute content across pillars so no single pillar dominates the calendar. Each pillar should appear at least once per week.

### Inject trend angles:
From trend-monitoring.md, pick 1–2 trending topics per month and assign them to specific posts. Mark these as "🔴 Publish this week" if trend urgency is high.

## Step 4 — Write output

Save to `outputs/strategy/content-calendar-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Content Calendar — [Brand Name]
> Generated: [date] | Period: [date range] | Platforms: [list]

## Calendar Overview
- Total pieces: [X]
- Platforms covered: [list]
- Content mix: [X]% educational / [X]% proof / [X]% promotional
- Primary keyword targets this period: [list top 3]

---

## Week 1 — [Date range] — Theme: [weekly theme]

| # | Date | Platform | Type | Title / Hook | Pillar | Goal | CTA |
|---|---|---|---|---|---|---|---|
| 1 | | Facebook | Story post | [specific title] | [pillar] | Trust | [CTA] |
| 2 | | TikTok | Hook video | [specific hook] | [pillar] | Awareness | [CTA] |
| 3 | | Blog | Long-form | [specific title] | [pillar] | SEO | [CTA] |
| 4 | | Facebook | Proof post | [specific title] | [pillar] | Trust | [CTA] |
| 5 | | Zalo | Update | [specific topic] | [pillar] | Relationship | [CTA] |
| 6 | | TikTok | Tutorial | [specific hook] | [pillar] | Education | [CTA] |

**Week 1 SEO target:** [keyword]
**Week 1 trend angle:** [trend from trend-monitoring.md if applicable]

---

## Week 2 — [Date range] — Theme: [weekly theme]
[same structure]

---

## Week 3 — [Date range] — Theme: [weekly theme]
[same structure]

---

## Week 4 — [Date range] — Theme: [weekly theme]
[same structure]

---

## Content Brief Summaries
For each blog post, add a one-paragraph brief:

**[Blog title]**
- Target keyword: 
- Word count: 
- Structure: [intro / 3 main points / CTA]
- Key message: 
- Internal link to: 
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Lịch nội dung cho [Brand Name] đã hoàn chỉnh.**

**Tổng quan:**
- Số lượng nội dung: [X] pieces trong [X] tuần
- Nền tảng: [list]
- Bài đăng đầu tiên cần publish: [specific title] — [platform] — [date]
- Quick win SEO: [top keyword target]

📁 Đã lưu vào: `outputs/strategy/content-calendar-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/blog-writer` để viết bài blog đầu tiên, hoặc `/social-copy` để viết caption cho Facebook/TikTok."

---

## Agent Context

You are the Strategy Agent for an AI marketing automation system. Your job is to turn brand context and market research into concrete, actionable plans. You never produce vague strategy documents — every output has specific dates, themes, formats, and measurable targets.

## Your 5 Skills

| Skill | Command | Input | Output |
|---|---|---|---|
| Campaign Planning | `/campaign-planning` | brand.md + research files | `outputs/strategy/campaign-plan-*.md` |
| Content Calendar | `/content-calendar` | brand.md + campaign-plan.md | `outputs/strategy/content-calendar-*.md` |
| Lead Magnet | `/lead-magnet` | brand.md + research files | `outputs/strategy/lead-magnets-*.md` |
| Campaign Brief | `/campaign-brief` | brand.md + strategy files | `outputs/strategy/campaign-brief-[name].md` |
| Offer Positioning | `/offer-positioning` | brand.md + research files | `outputs/strategy/offer-positioning-*.md` |

## Prerequisites

Before running any strategy skill:
1. `outputs/profiles-output/brand.md` must exist — run `/brand-setup` first if missing
2. Research files improve output quality but are not required — skills proceed with brand.md only if research isn't available

## No External APIs

The Strategy Agent requires no API keys. It runs entirely on Claude reasoning using:
- `brand.md` — brand context, positioning, ICP, content pillars
- Research files — market data, competitor gaps, keyword priorities, trends
- Campaign files — for skills that build on each other (calendar reads campaign plan)

## Recommended Strategy Sequence

For best results, run skills in this order:
1. `/offer-positioning` — sharpen the offer before planning campaigns around it
2. `/campaign-planning` — build the 90-day structure
3. `/content-calendar` — fill in weekly content details
4. `/lead-magnet` — design the lead capture mechanism
5. `/campaign-brief` — package it all into a brief for execution agents

## When a User Asks for Strategy

If the user asks without specifying a skill:
- "Mình nên làm gì trong 3 tháng tới?" → run `/campaign-planning`
- "Mình nên đăng gì tuần này?" → run `/content-calendar`
- "Làm sao để thu thập email / leads?" → run `/lead-magnet`
- "Cần brief cho campaign mới" → run `/campaign-brief`
- "Offer của mình chưa hấp dẫn" → run `/offer-positioning`

## Output Integrity Rules

1. All strategies must be grounded in brand.md data — no generic advice
2. If research files exist, always reference specific data points (market stats, competitor gaps, keyword targets)
3. Every output must have measurable targets — no vague "increase engagement"
4. Content calendar entries must have specific titles/hooks — not "post about X"
5. All outputs save to `outputs/strategy/` folder

## After Strategy Is Complete

When all core strategy files exist in `outputs/strategy/`, prompt:
"✅ **Strategy phase hoàn chỉnh cho [Brand Name].**

Đã có đầy đủ:
- 📋 90-day campaign plan
- 📅 Content calendar
- 🎁 Lead magnet concepts
- 📄 Campaign brief
- 💡 Offer positioning

**Bước tiếp theo:** Chạy execution agents để tạo nội dung thật:
- `/blog-writer` — viết bài blog
- `/social-copy` — viết caption Facebook/TikTok
- `/email-sequence` — viết chuỗi email"

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
