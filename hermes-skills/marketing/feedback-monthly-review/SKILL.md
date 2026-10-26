---
name: feedback-monthly-review
description: "Run this marketing skill."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Feedback]
    related_skills: [audience-update, messaging-refinement, positioning-evolution, feedback-monthly-review, marketing-orchestrator]
---

# Monthly Strategy Review (Feedback Layer) Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Run this marketing skill.

## Procedure

Your job is to close the feedback loop — run the full end-of-month review from the Feedback Agent's perspective. Unlike the Performance Agent's monthly review (which analyzes numbers), this skill synthesizes all updates from the Feedback Agent (audience, messaging, positioning) and writes a consolidated strategy brief for the next month. It is the last step before the cycle resets.

## Step 1 — Read ALL inputs

Read everything available:
- `outputs/profiles-output/brand.md` — current state after this month's updates
- `outputs/performance/monthly-review-[current month].md` — performance analysis
- `outputs/performance/audience-update-[current month].md` — audience changes
- `outputs/performance/messaging-refinement-[current month].md` — messaging changes
- `outputs/performance/positioning-evolution-[current month].md` — positioning changes
- `outputs/strategy/campaign-brief-*.md` — last month's strategy
- `outputs/research/` — any recent research

This skill requires all other feedback skills to have run first. If audience-update, messaging-refinement, or positioning-evolution files don't exist for this month, run those first.

## Step 2 — Synthesize and write next month's strategy

### The synthesis question

After all updates: what is the one most important thing the brand should do differently next month?

This is not a list of everything that changed. It is a strategic decision about priority — given everything learned this month, where should next month's energy go?

### Strategy brief structure

**1. This month in one paragraph:**
What happened, what was learned, what changed. Anyone reading this brief should be caught up in 60 seconds.

**2. Brand foundation updates summary:**
What changed in brand.md this month? Audience, messaging, positioning. List changes clearly so the execution agents know to work from the updated version.

**3. Strategic priority for next month:**
One primary strategic thrust — not a list of tactics.
- If conversion is the problem: priority is CRO + bottom-funnel content
- If reach is the problem: priority is distribution + paid acquisition
- If credibility is the problem: priority is case studies + thought leadership
- If retention is the problem: priority is email sequences + community

**4. Channel focus:**
Based on ROI data — which 2–3 channels to invest in next month, which to hold steady, which to reduce.

**5. Content calendar direction:**
What content themes to emphasize next month. Based on what worked, what audience questions came up, what's seasonal.

**6. Experiments to run:**
1–2 specific tests to run next month. Each with a clear hypothesis and success metric.

**7. What NOT to do next month:**
Explicitly state what to stop, pause, or deprioritize. This is as important as the priority list.

### Vietnamese business cycle context

**Monthly rhythm:**
- First week of month: execute on last month's plan
- Week 2–3: production and distribution
- Week 4: data collection, analysis
- Last 3 days of month: run this review, write next month's brief

**Quarterly considerations:**
- Q1 (Jan–Mar): Post-Tết recovery; March is the ramp-up month
- Q2 (Apr–Jun): Best B2B quarter; push campaigns hard here
- Q3 (Jul–Sep): Summer slowdown for B2B; good for relationship-building content
- Q4 (Oct–Dec): Year-end budget push; good time for ROI-focused campaigns

## Step 3 — Write output

Save to `outputs/strategy/campaign-brief-[YYYY-MM].md` (overwrites as next month's brief):

```markdown
# Campaign Brief — [Month YYYY]
> Generated: [date] | Based on: [previous month] learnings

## Month in Review (60-second catch-up)
[One paragraph: what happened, what was learned, what changed]

---

## Brand Foundation — Current State
*All execution agents should read brand.md before running any skill this month.*

**Audience (Section 6):** [Key update — or "no changes this month"]
**Messaging (Section 11):** [Key update]
**Positioning (Section 7):** [Key update]
**Offer (Section 9):** [Key update or "unchanged"]

---

## Strategic Priority for [Month YYYY]
**Primary thrust:** [One sentence — the main strategic direction]
**Why:** [Data that supports this priority]

---

## Channel Focus

| Channel | Investment | Direction | Reason |
|---|---|---|---|
| Facebook Ads | [budget] | Increase/Hold/Reduce | [Why] |
| Google Ads | [budget] | | |
| Email | [effort] | | |
| Organic Content | [effort] | | |
| Cold Outreach | [effort] | | |

---

## Content Themes for [Month]

**Must cover (based on what worked):**
1. [Theme] — [why: performance data]
2. [Theme]

**Must cover (based on audience questions):**
1. [Theme] — [why: common objection or question]

**Seasonal/topical:**
1. [Theme] — [why: Vietnamese calendar or market timing]

---

## Experiments to Run

### Experiment 1
**Hypothesis:** If we [change X], then [metric Y] will improve because [reason]
**Test:** [Specific A/B test or campaign]
**Success metric:** [Specific number]
**Duration:** [weeks]

### Experiment 2
[Same structure]

---

## What NOT to Do This Month
- **Stop:** [Specific activity to kill] — [Why: cost vs. result data]
- **Pause:** [Specific activity to hold] — [Why]
- **Don't start:** [Tempting thing to avoid right now] — [Why not yet]

---

## Quick Wins (do these in week 1)
1. [Specific action that will produce results fast]
2. [Second quick win]

---

## Monthly Goals

| KPI | Target | How we'll hit it |
|---|---|---|
| Revenue | [VND] | [Strategy] |
| Leads | [n] | |
| Demos booked | [n] | |
| CAC | [VND max] | |
| [Key channel metric] | | |

---

## Notes
[Seasonal factors, upcoming Vietnamese holidays, external market context]
```

## Step 4 — Confirm

After writing, reply:

---
"✅ **Monthly strategy review hoàn chỉnh. Hệ thống đã reset cho tháng [Next Month].**

**Tháng vừa rồi:** [One-sentence verdict]
**Thay đổi brand.md:** [What updated]
**Priority tháng [Next Month]:** [Strategic thrust]
**Mục tiêu chính:** [Key KPI target]

📁 Brief mới lưu tại: `outputs/strategy/campaign-brief-[YYYY-MM].md`
📁 brand.md đã được cập nhật với tất cả feedback từ tháng này

**Hệ thống sẵn sàng cho tháng mới:**
→ Execution agents sẽ đọc brand.md mới nhất
→ Strategy agents sẽ đọc campaign-brief mới nhất
→ Vòng lặp tiếp tục"

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
