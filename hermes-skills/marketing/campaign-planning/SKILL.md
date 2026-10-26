---
name: campaign-planning
description: "Plan a full marketing campaign end to end."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Strategy]
    related_skills: [campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning, marketing-orchestrator]
---

# Campaign Planning Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Builds a full 90-day marketing campaign plan for a Vietnamese business. Use this skill when the user wants to plan a campaign, map out a marketing timeline, or structure their marketing activities. Trigger whenever the user mentions campaign planning, 90-day plan, marketing roadmap, or wants to know what to do next in their marketing.

Slash command: load this skill and follow its Procedure. Short summary: Plan a full marketing campaign end to end.

## Procedure

Your job is to build a focused, actionable 90-day marketing campaign — not a vague strategy document. Every week should have a clear goal, content theme, and measurable output.

## Step 1 — Read inputs

Read the following files:
- `outputs/profiles-output/brand.md` — brand positioning, ICP, USP, core offer
- `outputs/research/market-research-*.md` — market size, opportunities, threats (if exists)
- `outputs/research/competitor-analysis-*.md` — competitor gaps to exploit (if exists)
- `outputs/research/keyword-research-*.md` — keyword priorities (if exists)
- `outputs/research/trend-monitoring-*.md` — trends to ride (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.
If research files don't exist: proceed with brand.md data only, note the gap.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign goal or focus**
Use their goal. Go to Step 3.

**Path B — No goal provided**
Ask:
"Chiến dịch 90 ngày này hướng đến mục tiêu nào?
1. Tăng nhận diện thương hiệu (brand awareness)
2. Tạo leads và khách hàng mới (lead generation)
3. Ra mắt sản phẩm/dịch vụ mới (product launch)
4. Tái kích hoạt khách hàng cũ (re-engagement)
5. Kết hợp (mixed — brand + leads)"

Wait for answer before continuing.

## Step 3 — Build the 90-day campaign structure

### Campaign Architecture

**Month 1 — Awareness & Trust (Weeks 1–4)**
Goal: Get the right people to know this brand exists and trust it enough to engage.
- Lead with educational content that addresses top pain points
- Build SEO foundation with Tier 3 keywords
- Establish social presence rhythm (consistency > volume)
- No hard selling in Month 1 — build credibility first

**Month 2 — Consideration & Engagement (Weeks 5–8)**
Goal: Move warm audience from "interesting" to "I want this."
- Introduce comparison content (us vs alternatives)
- Publish proof: case studies, testimonials, before/after
- Capture leads with a lead magnet offer
- Start retargeting anyone who engaged in Month 1

**Month 3 — Conversion & Retention (Weeks 9–12)**
Goal: Turn interested prospects into paying customers.
- Direct offer content: pricing, packages, CTA-forward
- Run a limited-time incentive (bonus, discount, free consultation)
- Email sequence for leads captured in Month 2
- Referral or review ask for new customers

### For each month, define:
- **Theme:** The single narrative thread for the month
- **Primary platform:** Where most energy goes (Facebook / TikTok / Zalo / Blog / LinkedIn)
- **Content mix:** Ratio of educational : proof : promotional content
- **Key milestones:** What must be live by end of month
- **Success metric:** The one number that proves this month worked

### Weekly breakdown (for Month 1 as example):
- Week 1: [specific theme] → [content type] → [platform] → [CTA]
- Week 2: [specific theme] → [content type] → [platform] → [CTA]
- Week 3: [specific theme] → [content type] → [platform] → [CTA]
- Week 4: [specific theme] → [content type] → [platform] → [CTA]

Use brand.md content pillars to assign weekly themes. Use keyword-research.md to assign SEO targets per week. Use trend-monitoring.md to inject timely angles.

### Budget allocation framework (if user has a budget):
- 40% — content production (writing, design, video)
- 35% — paid distribution (Facebook/TikTok ads, boosted posts)
- 15% — tools and automation
- 10% — testing and experimentation

## Step 4 — Define campaign KPIs

Set measurable targets for the 90-day period. Base on industry benchmarks for Vietnam:

| Metric | Conservative | Realistic | Aggressive |
|---|---|---|---|
| Organic reach/month | — | — | — |
| Leads generated | — | — | — |
| Email subscribers | — | — | — |
| Conversion rate | — | — | — |
| Revenue target | — | — | — |

Fill in numbers based on the brand's current stage, audience size, and market data from research files.

## Step 5 — Write output

Save to `outputs/strategy/campaign-plan-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# 90-Day Campaign Plan — [Brand Name]
> Generated: [date] | Goal: [campaign goal] | Market: Vietnam

## Campaign Overview
- Goal: 
- Primary audience: 
- Core message for this campaign:
- Platforms: 
- Budget range (if provided):

---

## Month 1 — [Theme Name] (Weeks 1–4)
**Goal:** 
**Content ratio:** X% educational / X% proof / X% promotional
**Primary platform:**
**Key milestone:**
**Success metric:**

### Week-by-Week
| Week | Theme | Content Type | Platform | CTA |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

---

## Month 2 — [Theme Name] (Weeks 5–8)
[same structure]

---

## Month 3 — [Theme Name] (Weeks 9–12)
[same structure]

---

## 90-Day KPI Targets
| Metric | Target |
|---|---|
| | |

---

## Quick Wins (Do in Week 1)
[3–5 actions to take immediately that cost nothing but time]

---

## Risks & Contingencies
[What could go wrong and what to do about it]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Kế hoạch chiến dịch 90 ngày cho [Brand Name] đã hoàn chỉnh.**

**Tóm tắt:**
- Tháng 1: [theme] — [primary action]
- Tháng 2: [theme] — [primary action]
- Tháng 3: [theme] — [primary action]
- Quick win đầu tiên: [top action for week 1]

📁 Đã lưu vào: `outputs/strategy/campaign-plan-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/content-calendar` để lập lịch nội dung chi tiết từng tuần."

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
