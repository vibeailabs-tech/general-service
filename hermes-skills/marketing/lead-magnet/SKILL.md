---
name: lead-magnet
description: "Design lead magnets that capture contacts."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Strategy]
    related_skills: [campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning, marketing-orchestrator]
---

# Lead Magnet Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Creates 3 lead magnet concepts tailored to the brand's audience and offer. Use this skill when the user wants to grow their email list, capture leads, or create a free offer to attract potential customers. Trigger whenever the user mentions lead magnet, free offer, freebie, email capture, or list building.

Slash command: load this skill and follow its Procedure. Short summary: Design lead magnets that capture contacts.

## Procedure

Your job is to design 3 lead magnet concepts that attract the exact right buyers — not tire-kickers — and move them toward the core offer. In Vietnam, the best lead magnets solve a specific, immediate problem and can be consumed quickly.

## Step 1 — Read inputs

Read:
- `outputs/profiles-output/brand.md` — ICP pain points (Section 6), core offer (Section 9), USP (Section 8), content pillars (Section 12)
- `outputs/research/keyword-research-*.md` — "People Also Ask" questions (if exists)
- `outputs/research/competitor-analysis-*.md` — what competitors are giving away (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a type or topic**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bạn muốn lead magnet phục vụ mục đích gì?
1. Thu thập email/số điện thoại từ người lạ
2. Warm up khách hàng đang cân nhắc
3. Kích hoạt lại khách hàng cũ
4. Tất cả — đề xuất 3 loại khác nhau"

Wait for answer before continuing.

## Step 3 — Design 3 lead magnet concepts

### Lead magnet principles for Vietnam market

**What works:**
- Solves ONE specific, named pain point (not "improve your marketing")
- Immediately actionable — consumer can use it today
- Quick to consume — checklist, template, calculator, short guide (not 50-page ebook)
- Creates "aha" moment that makes the paid offer feel obvious
- Vietnamese language, with specific numbers and examples
- Delivery via Zalo or email (not gated PDF nobody downloads)

**What doesn't work:**
- Generic "ultimate guide to X" — too broad, no urgency
- Anything requiring too much setup before seeing value
- Content that competes with what they can Google in 30 seconds
- Ebooks longer than 10 pages

### Lead magnet formats ranked by conversion rate (Vietnam context):
1. **Calculator / quiz** — interactive, personalized result ("Chi phí thật của bạn là...")
2. **Checklist** — quick scan, immediate value ("10 điều cần check trước khi...")
3. **Template** — copy-paste ready ("Template [X] cho doanh nghiệp Việt Nam")
4. **Mini video / screen-record** — show don't tell (demo, walkthrough, behind-the-scenes)
5. **Cheat sheet** — condensed reference ("Tất cả bạn cần biết về X trong 1 trang")
6. **Free consultation / audit** — highest intent, lowest volume (for high-ticket offers)
7. **Case study / result breakdown** — proof + education combined

### For each of the 3 concepts, define:

**Concept structure:**
- **Name** — specific, benefit-driven title (not "Free Guide")
- **Format** — checklist / calculator / template / video / consultation
- **Specific problem it solves** — one sentence, exact language the ICP uses
- **What's inside** — 3–5 bullet points of what they get
- **The "aha" moment** — what insight makes them think "I need the paid offer"
- **Delivery method** — Zalo / email / direct download / Facebook Messenger
- **CTA to paid offer** — how it naturally leads to the next step
- **Estimated conversion** — how qualified are the leads this attracts?

### Lead magnet ladder:
Design the 3 concepts at different funnel stages:
- **Concept 1 — Top of funnel** (broad audience, low commitment, high volume)
- **Concept 2 — Middle of funnel** (problem-aware, moderate commitment, qualified)
- **Concept 3 — Bottom of funnel** (solution-aware, high commitment, highest intent)

## Step 4 — Write output

Save to `outputs/strategy/lead-magnets-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Lead Magnet Concepts — [Brand Name]
> Generated: [date]

## Concept 1 — [Name] (Top of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** Low-medium (volume play)

---

## Concept 2 — [Name] (Middle of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** Medium-high (intent qualified)

---

## Concept 3 — [Name] (Bottom of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** High (ready to buy)

---

## Recommended First Build
[Which of the 3 to build first and why — based on current stage, audience size, and fastest path to revenue]

## Promotion Plan
[How to get the lead magnet in front of the right people — organic posts, paid ads, Zalo broadcast, etc.]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **3 lead magnet concepts cho [Brand Name] đã hoàn chỉnh.**

**Đề xuất build trước:**
- [Concept name] — [format] — [why this one first]

**Tóm tắt 3 concepts:**
1. [Name] — [one line description]
2. [Name] — [one line description]
3. [Name] — [one line description]

📁 Đã lưu vào: `outputs/strategy/lead-magnets-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/campaign-brief` để đóng gói toàn bộ strategy thành brief cho execution agents."

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
