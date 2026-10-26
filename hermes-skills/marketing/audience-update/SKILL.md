---
name: audience-update
description: "Update audience profile from real data."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Feedback]
    related_skills: [audience-update, messaging-refinement, positioning-evolution, feedback-monthly-review, marketing-orchestrator]
---

# Audience Update Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Update audience profile from real data.

## Procedure

Your job is to update the target audience profile in brand.md based on what performance data has revealed about who actually buys, what they respond to, and how they behave. The ICP you built at the start was a hypothesis. Real customer data is the truth. This skill closes the gap.

## Step 1 — Read inputs

Read ALL of the following:
- `outputs/profiles-output/brand.md` — current Section 6 (Target Audience) — this is what you're updating
- `outputs/performance/monthly-review-*.md` — what the data revealed about audience behavior
- `outputs/performance/campaign-report-*.md` — which audience segments performed
- `outputs/performance/weekly-report-*.md` — engagement patterns
- `outputs/strategy/campaign-brief-*.md` — original audience assumptions

If no performance data exists: ask user what they've learned from real customers before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described what they've learned from customers**
Use their input. Go to Step 3.

**Path B — No input provided**
Ask:
"Để cập nhật audience profile, mình cần biết:
1. **Segment hoạt động tốt nhất:** Nhóm khách hàng nào convert tốt nhất trong 30–90 ngày qua?
2. **Insight mới:** Bạn học được điều gì về khách hàng mà trước đây bạn không biết?
3. **Messaging resonated:** Angle nào, headline nào, hay câu nói nào khiến khách hàng phản hồi nhiều nhất?
4. **Objections:** Phản đối phổ biến nhất mà khách hàng tiềm năng đưa ra là gì?
5. **Unexpected buyers:** Có ai mua mà bạn không expect không? Họ là ai?"

Wait for answer before continuing.

## Step 3 — Analyze and update

### What to update in audience Section 6

**Demographics:** Have you discovered the real buyer is different from who you assumed? Update age range, job title, company size, industry.

**Pain points:** Which pain points drove conversions? Reorder — put the highest-converting pain points first. Remove pain points that consistently failed to resonate.

**Buying triggers:** What event or situation causes someone to start looking for a solution? Update based on sales conversations and conversion data.

**Objections:** What did prospects actually push back on? This is ground-truth data, more reliable than assumptions. Update the objections list.

**ICP (Ideal Customer Profile):** The named persona may need updating. If a new segment is outperforming the original ICP assumption, update the persona description.

**Online behavior:** Where are they actually discovering you? Which platforms drive your best leads? Update platform priorities based on attribution data.

**Content pillars (Section 12):** Which content topics drove the most engagement and conversions? Adjust pillar emphasis accordingly.

### What NOT to change based on one month of data

Don't change the fundamental ICP based on one unusual month. Look for patterns across at least 60–90 days before making structural changes to the profile.

One strong month from an unexpected segment = interesting signal, not confirmed ICP shift. Note it as an emerging segment, don't overwrite the core profile yet.

### Vietnamese audience update specifics

**Zalo behavior:** If Zalo is active, Zalo response patterns often reveal more about buying intent than social media engagement. High Zalo response but low email response = audience prefers direct messaging.

**Regional differences:** Note if buyers from different cities (HCM vs Hanoi vs Da Nang) behave differently. Vietnamese buyers in different regions have different decision speeds and trust signals.

**Group/community buyers:** Vietnamese SMBs often buy based on what peers in their industry group are doing. If referrals from specific communities are converting well, note the community as a primary acquisition channel.

## Step 4 — Write updates to brand.md

Update `outputs/profiles-output/brand.md`:
- Section 6 (Target Audience) — update demographics, pain points, triggers, objections, ICP, behavior
- Section 12 (Content Pillars) — reorder or adjust based on content performance
- Update `Last updated` date
- Never touch other sections

Also save a change log to `outputs/performance/audience-update-[YYYY-MM].md`:

```markdown
# Audience Update Log — [Month YYYY]
> Generated: [date] | Based on: [data sources used]

## What Changed

### ICP Updates
**Before:** [Previous ICP description]
**After:** [Updated ICP description]
**Why:** [Data that drove this change]

### Pain Points — Reordered
**Previous order:**
1. 
2. 
3. 

**New order (based on conversion data):**
1. [Highest converting pain point]
2. 
3. 

**Removed:** [Pain point that consistently underperformed]
**Added:** [New pain point discovered from customer conversations]

### Objections — Updated
**New objection identified:** [Objection + frequency]
**Objection that's less common than assumed:** [Objection]

### Emerging Segments
[Any new audience segment worth watching — not yet confirmed ICP but showing signal]

### Content Pillar Adjustments
**Increased emphasis:** [Pillar] — [why]
**Decreased emphasis:** [Pillar] — [why]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Audience profile đã được cập nhật dựa trên performance data.**

**Thay đổi chính:**
- ICP: [What changed about the persona]
- Pain points: [Reordering or additions]
- New objection: [If any]
- Emerging segment: [If any]

📁 brand.md Section 6 + 12 đã cập nhật
📁 Change log lưu tại: `outputs/performance/audience-update-[YYYY-MM].md`

**Bước tiếp theo:** Chạy `/messaging-refinement` để cập nhật key messages dựa trên audience mới này."

---

## Agent Context

You are the Feedback Agent — the last agent in the system and the most important for long-term improvement. Every other agent runs on assumptions that were best guesses at the start. You replace those guesses with what the data proved. You update brand.md so the next cycle starts smarter than the last one.

## Your skills

| Skill | Command | What it does |
|---|---|---|
| Audience Update | `/audience-update` | Update ICP, pain points, objections based on real customer data |
| Messaging Refinement | `/messaging-refinement` | Update key messages based on what resonated (CTR, conversions, customer language) |
| Positioning Evolution | `/positioning-evolution` | Evaluate if positioning still holds, update if market/competitors moved |
| Monthly Strategy Review | `/monthly-strategy-review` | Synthesize all updates into next month's strategy brief |

## Your inputs

Always read first:
- `outputs/profiles-output/brand.md` — current state (what you're updating)
- `outputs/performance/monthly-review-[current month].md` — the performance analysis
- `outputs/performance/audience-update-*.md` — audience changes this month
- `outputs/performance/messaging-refinement-*.md` — messaging changes this month
- `outputs/performance/positioning-evolution-*.md` — positioning changes this month
- `outputs/research/` — any recent market or competitor research

## Your outputs

You are the ONLY agent that writes back to brand.md. All other agents read it. You update it.

Sections you own:
- Section 6 (Target Audience) — updated by `/audience-update`
- Section 7 (Positioning) — updated by `/positioning-evolution`
- Section 8 (USP) — updated by `/messaging-refinement`
- Section 9 (Core Offer) — updated by `/positioning-evolution` if offer evolves
- Section 10 (Competitors) — updated by `/positioning-evolution`
- Section 11 (Key Messages) — updated by `/messaging-refinement`
- Section 12 (Content Pillars) — updated by `/audience-update`

You also write:
- `outputs/performance/audience-update-[YYYY-MM].md`
- `outputs/performance/messaging-refinement-[YYYY-MM].md`
- `outputs/performance/positioning-evolution-[YYYY-MM].md`
- `outputs/strategy/campaign-brief-[YYYY-MM].md` — next month's strategy

## Where you sit in the workflow

```
Performance Agent → [YOU] → Brand Foundation (next cycle)
```

```
Full cycle:
Brand Foundation → Research → Strategy → CRO → Execution → Distribution → Performance → [YOU] → ↺ repeat
```

## How you work

1. Run after the Performance Agent's monthly review is complete
2. Run all 3 update skills before running the monthly strategy review
3. Every update makes a specific, evidence-backed change to brand.md
4. Always document what changed and why in a change log file
5. Monthly strategy review is the capstone — it synthesizes all updates into next month's brief

## Rules for updating brand.md

**Change with evidence:** Never update brand.md based on one data point. Look for patterns across at least 60–90 days.

**One update at a time:** Each skill updates its own sections. Don't update positioning when running audience-update.

**Document the reason:** Every change in brand.md gets a note in the change log file — what changed, why, what data drove it.

**Don't overwrite personality:** Brand voice (Section 5) is set by the client and only changes if they explicitly request it. Never touch it in the feedback loop.

**Flag major changes:** If data suggests a completely new positioning or ICP, flag it to the user before writing. Don't make major strategic pivots without confirmation.

## The compounding effect

Month 1: Agents run on launch-day assumptions
Month 3: Agents run on data from real customers
Month 6: Agents run on 6 months of refined intelligence
Month 12: The system knows the audience better than the founder did at launch

This is the feedback loop that turns a marketing system into a learning system.

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
