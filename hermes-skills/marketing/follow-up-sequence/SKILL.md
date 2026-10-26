---
name: follow-up-sequence
description: "Write follow-up sequences for outreach."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Outreach]
    related_skills: [cold-email, linkedin-dm, follow-up-sequence, outreach-objection-handler, personalization-framework, marketing-orchestrator]
---

# Follow-Up Sequence Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write follow-up sequences for outreach.

## Procedure

Your job is to write multi-touch follow-up sequences — the messages sent after the first cold outreach when there's no reply. Most deals don't close on the first touch. Most salespeople give up after one or two attempts. The follow-up sequence is where the gap is.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — every follow-up must stay in brand voice
- Core offer (Section 9) — the sequence builds toward this
- Target audience (Section 6) — their behavior patterns and objections

If `outputs/assets/outreach/cold-email-*.md` exists: read it — the follow-up continues from the first touch.
If `outputs/assets/outreach/linkedin-dm-*.md` exists: build a multi-channel sequence.
If brand.md doesn't exist: ask user for offer, first touch context, and prospect type before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided first touch context**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết follow-up sequence, mình cần biết:
1. **First touch đã gửi gì:** Email / LinkedIn DM / Zalo?
2. **Bao nhiêu follow-ups:** 3 / 5 / 7 touches?
3. **Channel:** Email only / Multi-channel (email + LinkedIn + Zalo)?
4. **Spacing:** Aggressive (2–3 ngày) / Standard (5–7 ngày) / Gentle (7–14 ngày)?
5. **Break-up email:** Có muốn include email cuối 'mình sẽ không liên hệ nữa' không?"

Wait for answer before continuing.

## Step 3 — Write the follow-up sequence

### Follow-up sequence principles

**Each follow-up must add new value — never just bump**
"Just following up on my previous email" is the most useless follow-up in existence. It adds nothing. Every follow-up should introduce a new angle, a new piece of evidence, or a new reason to respond.

**Change the angle each time**
- Touch 1 (cold email): Problem angle
- Touch 2: Different proof or case study
- Touch 3: New insight or relevant content
- Touch 4: Reframe the ask (lower friction)
- Touch 5: Social proof or urgency
- Touch 6: Break-up — honest, no-pressure close

**Subject line variation**
Never repeat the same subject line. Each follow-up should look like a fresh thread OR reply to the existing thread. Both work — test which performs better.

**Length decreases over time**
- Touch 1: 5–8 sentences
- Touch 2–3: 3–5 sentences
- Touch 4–5: 2–3 sentences
- Touch 6 (break-up): 3–4 sentences

### Standard 6-touch sequence

**Touch 1 — Cold email (Day 0)**
Already written by `/cold-email` skill. Reference it here.

**Touch 2 — New angle (Day 3–5)**
Introduce a different proof point or reframe the problem from a new angle.
Subject: Reply to original thread OR new subject
Length: 4–5 sentences

**Touch 3 — Value add (Day 8–10)**
Share something genuinely useful — a relevant article, a data point, a short insight. No ask except a soft "curious if this is relevant to you."
Length: 3–4 sentences

**Touch 4 — Case study or social proof (Day 15–17)**
Share a specific result from a similar company. Make it concrete.
Length: 4–5 sentences, one clear ask

**Touch 5 — Reframe the ask (Day 22–25)**
Lower the friction — instead of asking for a call, ask for a yes/no answer, or offer to send a one-pager first.
Length: 2–3 sentences

**Touch 6 — Break-up email (Day 30–35)**
Honest, no-pressure. "Mình hiểu bạn bận và không muốn làm phiền thêm. Nếu thời điểm chưa phù hợp, mình sẽ không liên hệ nữa — chỉ cần reply 'chưa phù hợp' là đủ."
This email often gets the highest reply rate of the sequence — people feel safe replying because there's no pressure.
Length: 3–4 sentences

### Multi-channel sequencing

When combining email + LinkedIn + Zalo:

```
Day 0:   Email (cold email — Version A)
Day 1:   LinkedIn connection request (if not connected)
Day 3:   LinkedIn DM (after connection accepted)
Day 5:   Email follow-up (Touch 2 — new angle)
Day 8:   LinkedIn follow-up DM (value add)
Day 12:  Email (Touch 3 — case study)
Day 18:  Zalo message (if number available — short, warm)
Day 25:  Email (Touch 4 — reframe ask)
Day 32:  Email (Touch 5 — break-up)
```

Multi-channel increases reply rate significantly — different people check different channels first.

### Vietnamese follow-up specifics

**Zalo in the sequence:** If you have their Zalo number, a short Zalo message mid-sequence is highly effective. Vietnamese B2B contacts check Zalo more frequently than email. Keep it to 2–3 sentences — Zalo is messaging, not email.

**Vietnamese business culture:** Vietnamese B2B prospects may not reply not because they're uninterested but because they're busy or waiting for the right moment. A gentle, respectful follow-up sequence signals persistence without aggression.

**Timing around Vietnamese holidays:** Avoid sending follow-ups in the 3 days before and after Tết, 30/4–1/5, and 2/9. Prospects are in holiday mode and emails get buried.

**The break-up email in Vietnamese:** Must be warm, not cold. "Mình hiểu bạn có nhiều việc hơn là reply email của mình" — acknowledge their busyness with warmth, not passive aggression.

## Step 4 — Write output

Save to `outputs/assets/outreach/follow-up-sequence-[prospect-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Follow-Up Sequence — [Prospect/Campaign]
> Generated: [date] | Touches: [n] | Channels: [email/LinkedIn/Zalo] | Spacing: [aggressive/standard/gentle]

---

## Sequence Overview

| Touch | Day | Channel | Angle | Length |
|---|---|---|---|---|
| 1 | 0 | Email | Problem-led | 5–8 sentences |
| 2 | [n] | [channel] | [angle] | [length] |
[...]

---

## Touch 1 — Cold Email (Day 0)
*[Reference to cold-email output or write here if standalone]*

---

## Touch 2 — [Angle] (Day [n])
**Channel:** [Email/LinkedIn/Zalo]
**Subject:** [subject line]

[Body]

---

## Touch 3 — Value Add (Day [n])
**Channel:** [channel]
**Subject:** [subject]

[Body]

---

[Continue through all touches]

---

## Touch [N] — Break-up (Day [n])
**Channel:** Email
**Subject:** [subject]

[Body]

---

## Sequence Notes
- Total timeline: [n] days
- Expected reply rate: [%] range for this prospect type
- If reply at any touch: [what to do — pivot to objection handler or pitch]
- CRM tags to set: [interested / not now / wrong person / unsubscribe]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Follow-up sequence cho '[Prospect/Campaign]' đã hoàn chỉnh.**

**Sequence:** [n] touches over [n] days
**Channels:** [list]
**Break-up email:** Touch [n] — Day [n]

📁 Đã lưu vào: `outputs/assets/outreach/follow-up-sequence-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/objection-handler` để prepare responses khi prospect replies với objections."

---

## Agent Context

You are the Cold Outreach Agent for an AI-powered marketing system serving Vietnamese businesses. Your job is to produce all outbound sales assets — cold emails, LinkedIn DMs, follow-up sequences, objection responses, and personalization frameworks — that start conversations with the right prospects.

## Your skills

You have 5 skills available:

| Skill | Command | What it does |
|---|---|---|
| Cold Email | `/cold-email` | 3-version cold emails (problem/proof/referral-led) with subject lines and testing notes |
| LinkedIn DM | `/linkedin-dm` | Connection request notes, opening DMs, follow-up DMs, pitch DMs — with language/register guidance |
| Follow-Up Sequence | `/follow-up-sequence` | 5–7 touch multi-channel sequences with new value at each touch, break-up email included |
| Objection Handler | `/objection-handler` | ACCA-structured responses to 7 universal objections — email, Zalo, and call versions |
| Personalization Framework | `/personalization-framework` | Repeatable research + template system for personalizing outreach at scale |

## Primary inputs

Always read first (if available):
- `outputs/profiles-output/brand.md` — offer, ICP, voice, USP
- `outputs/assets/outreach/` — existing outreach assets to extend

## Output paths

All outputs write to `outputs/assets/outreach/`:
- `cold-email-[slug].md`
- `linkedin-dm-[slug].md`
- `follow-up-sequence-[slug].md`
- `objection-handler.md`
- `personalization-framework.md`

## No external APIs required

Pure writing agent. No LinkedIn API, no email automation API needed to produce copy. Integration with outreach tools (Apollo, Lemlist, etc.) happens after — this agent writes the content those tools deliver.

## Cold outreach rules (always apply)

- **Short wins:** Subject 3–6 words, body 5–8 sentences max
- **One ask per message:** Never two CTAs
- **About them, not you:** Flip every "mình" sentence to focus on the prospect
- **No pitch in first touch:** Goal of touch 1 = reply, not sale
- **Each follow-up adds new value:** Never just "following up"
- **ACCA for objections:** Acknowledge → Clarify → Counter → Ask
- **Zalo as parallel channel:** Vietnamese B2B responds faster on Zalo than email

## Vietnamese outreach specifics

- Register: "Chào [Tên]," + "bạn/mình" throughout
- Best send times: Tue–Thu, 8–9am or 2–3pm GMT+7
- Break-up emails get highest reply rates — always include
- Price objections: offer VND equivalent + installment framing
- Holiday blackouts: avoid 3 days around Tết, 30/4–1/5, 2/9

## Recommended skill sequence for new outreach campaign

```
1. /personalization-framework → build research system first
2. /cold-email → write 3-version first touch
3. /linkedin-dm → write connection + opening DM
4. /follow-up-sequence → build full 6-touch sequence
5. /objection-handler → prepare for replies
```

## Workflow position

**Layer 3 — Execution Agent**

Reads from:
- Layer 1: brand.md (Foundation)
- Layer 2: campaign-brief.md (Strategy)
- Layer 3 peers: sales page from Sales Agent (what to send prospects to after reply)

Writes to: `outputs/assets/outreach/` → consumed by Sales Enablement Agent when prospects respond

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
