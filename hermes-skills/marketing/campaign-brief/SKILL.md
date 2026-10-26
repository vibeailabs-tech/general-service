---
name: campaign-brief
description: "Write a complete campaign brief document."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Strategy]
    related_skills: [campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning, marketing-orchestrator]
---

# Campaign Brief Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Creates a structured campaign brief that all execution agents read before producing any content. Use this skill when the user wants to brief content writers, social media agents, or email agents on a specific campaign. Trigger whenever the user mentions campaign brief, briefing, creative brief, or wants to kick off a specific campaign.

Slash command: load this skill and follow its Procedure. Short summary: Write a complete campaign brief document.

## Procedure

Your job is to produce a single, structured brief that every execution agent reads before creating any content for this campaign. Think of it as the "single source of truth" for a specific campaign — just like brand.md is the source of truth for the brand.

## Step 1 — Read inputs

Read:
- `outputs/profiles-output/brand.md` — voice, audience, positioning, key messages
- `outputs/strategy/campaign-plan-*.md` — campaign goals, monthly themes (if exists)
- `outputs/strategy/content-calendar-*.md` — specific content pieces planned (if exists)
- `outputs/strategy/lead-magnets-*.md` — lead magnet being promoted (if exists)
- `outputs/research/competitor-analysis-*.md` — angles to counter (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described the campaign**
Use their description. Go to Step 3.

**Path B — No campaign described**
Ask:
"Brief này cho chiến dịch nào?
1. Mô tả ngắn: tên chiến dịch, mục tiêu, thời gian chạy
2. Sản phẩm/dịch vụ đang quảng bá trong chiến dịch này?
3. Có offer đặc biệt không? (giảm giá, bonus, deadline)
4. Kênh chính: Facebook / TikTok / Email / Zalo / Tất cả?"

Wait for answers before continuing.

## Step 3 — Build the campaign brief

A campaign brief has 8 components:

### 1. Campaign Overview
- Campaign name (memorable, internal use)
- Campaign goal (one primary goal — awareness / leads / conversion)
- Duration (start date → end date)
- Budget range (if known)

### 2. The Offer
- What exactly is being promoted
- Price + any special incentive
- Deadline or scarcity (if applicable)
- Guarantee or risk-reversal

### 3. Target Audience (from brand.md + campaign-specific)
- Primary segment for this campaign
- Where they are in the buying journey (cold / warm / hot)
- Their #1 pain point this campaign addresses
- Their biggest objection to buying

### 4. Core Message
- The single sentence this campaign comes back to
- Tone direction for this campaign (urgent / educational / inspirational / proof-driven)
- What NOT to say (off-brand angles for this campaign)

### 5. Proof Points
- 2–3 specific stats, results, or testimonials to reference
- The strongest single proof point — the one that closes skeptics

### 6. Content Direction
- Hook angles to test (3 different opening lines/hooks)
- Content formats for each platform
- Emotional arc: awareness → interest → desire → action
- CTAs at each stage

### 7. Platform-Specific Instructions
For each active platform:

**Facebook:**
- Post frequency
- Format mix (text / image / video / carousel)
- Targeting notes (if running ads)
- Boosting budget recommendation

**TikTok:**
- Video length and style
- Hook structure (first 3 seconds)
- Trending sounds or formats to use
- Hashtag strategy

**Zalo:**
- Broadcast timing
- Message tone (more personal)
- ZNS or OA notes if applicable

**Email:**
- Sequence length
- Subject line direction
- Send timing

### 8. Success Metrics
- Primary KPI (the one number that defines success)
- Secondary metrics to track
- What "good" looks like vs "needs adjustment"
- Review checkpoint: when to evaluate and optimize

## Step 4 — Write output

Save to `outputs/strategy/campaign-brief-[campaign-name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Campaign Brief — [Campaign Name]
> Brand: [Brand Name] | Created: [date] | Status: Active

---

## 1. Campaign Overview
- **Name:** 
- **Goal:** 
- **Duration:** [start] → [end]
- **Budget:** 

---

## 2. The Offer
- **What:** 
- **Price:** 
- **Incentive:** 
- **Deadline:** 
- **Guarantee:** 

---

## 3. Target Audience
- **Segment:** 
- **Funnel stage:** Cold / Warm / Hot
- **Primary pain point:** 
- **Primary objection:** 

---

## 4. Core Message
- **Campaign headline:** 
- **One-sentence core message:** 
- **Tone:** 
- **Do NOT say:** 

---

## 5. Proof Points
- 
- 
- **Strongest single proof:** 

---

## 6. Content Direction

**3 Hook angles to test:**
1. 
2. 
3. 

**Emotional arc:**
- Awareness → [emotion/insight to trigger]
- Interest → [what makes them lean in]
- Desire → [what makes them want it]
- Action → [what removes final hesitation]

**CTAs by stage:**
- Cold audience: 
- Warm audience: 
- Hot audience: 

---

## 7. Platform Instructions

### Facebook
- Frequency: 
- Format mix: 
- Targeting: 
- Boost budget: 

### TikTok
- Video length: 
- Hook structure: 
- Hashtags: 

### Zalo
- Broadcast timing: 
- Tone: 

### Email
- Sequence: 
- Subject direction: 
- Send timing: 

---

## 8. Success Metrics
- **Primary KPI:** 
- **Secondary metrics:** 
- **Review checkpoint:** 
- **"Good" benchmark:** 
- **"Needs adjustment" signal:** 
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Campaign brief cho '[Campaign Name]' đã hoàn chỉnh.**

**Overview:**
- Goal: [goal]
- Duration: [dates]
- Core message: [one sentence]
- Primary platform: [platform]

📁 Đã lưu vào: `outputs/strategy/campaign-brief-[name]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chia sẻ file này với execution agents:
- `/blog-writer` — để viết bài blog theo brief này
- `/social-copy` — để viết caption Facebook/TikTok
- `/email-sequence` — để viết chuỗi email"

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
