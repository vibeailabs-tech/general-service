---
name: messaging-refinement
description: "Refine messaging from performance data."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Feedback]
    related_skills: [audience-update, messaging-refinement, positioning-evolution, feedback-monthly-review, marketing-orchestrator]
---

# Messaging Refinement Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Refine messaging from performance data.

## Procedure

Your job is to update the brand's key messages and USP based on what's actually resonating with customers. Messaging that was written before launch was a hypothesis. What people click on, respond to, and buy from is the truth. This skill updates the hypothesis with reality.

## Step 1 — Read inputs

Read ALL of the following:
- `outputs/profiles-output/brand.md` — current Section 8 (USP) and Section 11 (Key Messages)
- `outputs/performance/monthly-review-*.md` — what messaging resonated vs. flopped
- `outputs/performance/campaign-report-*.md` — which ad copy, headlines, CTAs performed
- `outputs/assets/social/` — top performing social posts
- `outputs/assets/email/` — best performing subject lines and email bodies
- `outputs/assets/ads/` — best performing ad copy

If no performance data exists: ask user which messages have gotten the strongest response from customers before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided messaging feedback or performance data**
Use their input. Go to Step 3.

**Path B — No input provided**
Ask:
"Để refine messaging, mình cần biết:
1. **Top performing:** Content, ad, hay email nào có CTR / engagement / conversion cao nhất?
2. **Resonating phrases:** Câu nói nào khiến khách hàng nói 'đúng rồi, đó chính xác là vấn đề của tôi'?
3. **Flopped messages:** Angle nào hoàn toàn không có phản hồi?
4. **Customer language:** Khách hàng dùng từ gì để mô tả vấn đề của họ? (exact words, not your words)
5. **Objections that messaging didn't overcome:** Khách hàng vẫn nói gì dù đã xem marketing của bạn?"

Wait for answer before continuing.

## Step 3 — Analyze and refine

### Messaging analysis framework

**What resonated (high CTR, engagement, conversions):**
- What angle was used? (pain / proof / fear / desire / contrarian)
- What exact language was used?
- Was it specific or vague? (specific almost always beats vague)
- What emotion did it trigger?

**What flopped (low CTR, no engagement, no conversion):**
- Was the message too generic?
- Was it solving the wrong pain?
- Was it too early in the funnel for a conversion message?
- Was the language too formal / informal for the audience?

**Customer language mining:**
The most valuable source of messaging data is the exact words customers use. From sales calls, comments, Zalo messages, reviews:
- What words do they use to describe their problem?
- What do they say they want?
- What do they say they're afraid of?
Incorporate this language directly into key messages — don't translate it.

### Messaging refinement rules

**Rule 1 — Specific beats vague, always**
"Giảm 3 giờ mỗi ngày" beats "tiết kiệm thời gian"
"80% khách hàng thấy kết quả trong 30 ngày" beats "kết quả nhanh chóng"

**Rule 2 — Customer language beats your language**
If customers say "mình không biết bắt đầu từ đâu", your message should say "không biết bắt đầu từ đâu" — not "thiếu lộ trình marketing rõ ràng"

**Rule 3 — Pain before solution**
Messages that name the problem before offering the solution consistently outperform solution-first messages for cold audiences.

**Rule 4 — Proof in the headline, not the footnote**
Social proof embedded in headlines converts better than social proof buried in body copy.

### What to update in brand.md

**Section 8 — USP:**
- Is the unique mechanism still the right frame?
- Is the transformation promise (before/after) matching what customers actually experience?
- Are the proof points the strongest available? (update with new case study data)

**Section 11 — Key Messages:**
- Remove messages that consistently underperformed
- Add messages that proved effective in the field
- Update the language to match what customers actually say
- Reorder — put highest-converting messages first

## Step 4 — Write updates

Update `outputs/profiles-output/brand.md`:
- Section 8 (USP) — update mechanism name, transformation promise, proof points
- Section 11 (Key Messages) — update, reorder, and refine all 3 messages
- Update `Last updated` date

Also save a change log to `outputs/performance/messaging-refinement-[YYYY-MM].md`:

```markdown
# Messaging Refinement Log — [Month YYYY]
> Generated: [date] | Based on: [data sources]

## Performance Data Summary
**Top performing message/angle:** [Description + metric]
**Lowest performing message/angle:** [Description + metric]

---

## USP Updates

### Before
[Previous USP text]

### After
[Updated USP text]

### Why changed
[Data or customer feedback that drove this change]

---

## Key Messages — Before vs. After

### Message 1
**Before:** [Previous message]
**After:** [Updated message]
**Why:** [What data supported this change]

### Message 2
[Same structure]

### Message 3
[Same structure]

---

## New Language Discovered (Customer Voice)
Exact phrases from customers to use in future messaging:
- "[Exact customer phrase]" — source: [sales call / comment / review]
- "[Exact customer phrase]"
- "[Exact customer phrase]"

---

## Messages to Retire
- [Message that consistently underperformed] — reason: [why it didn't work]

---

## Hypotheses to Test Next Month
Messages that showed partial signal and should be A/B tested:
1. [Message hypothesis]
2. [Message hypothesis]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Key messages đã được cập nhật dựa trên performance data.**

**Thay đổi chính:**
- USP: [What changed]
- Message 1: [New version]
- Retired: [Message removed]
- Customer language added: [Examples]

📁 brand.md Section 8 + 11 đã cập nhật
📁 Change log lưu tại: `outputs/performance/messaging-refinement-[YYYY-MM].md`

**Bước tiếp theo:** Chạy `/positioning-evolution` để xem xét liệu positioning có cần update không, hoặc push messaging mới vào content calendar."

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
