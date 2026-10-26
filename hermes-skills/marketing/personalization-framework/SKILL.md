---
name: personalization-framework
description: "Build outreach personalization frameworks."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Outreach]
    related_skills: [cold-email, linkedin-dm, follow-up-sequence, outreach-objection-handler, personalization-framework, marketing-orchestrator]
---

# Personalization Framework Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Build outreach personalization frameworks.

## Procedure

Your job is to build a repeatable system for personalizing cold outreach at scale — so every prospect gets a message that feels written specifically for them, without writing every message from scratch. Personalization is the single biggest lever in cold outreach response rates.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — the personalization must connect back to this
- Target audience (Section 6) — ICP segments that need different personalization approaches
- Brand voice (Section 5) — personalized messages must still sound like the brand

If `outputs/assets/outreach/cold-email-*.md` exists: apply the framework to existing email templates.
If `outputs/research/competitor-analysis-*.md` exists: check for company-specific signals to use.
If brand.md doesn't exist: ask user for offer, ICP, and outreach channel before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided a prospect list or specific prospects**
Build personalization for each prospect. Go to Step 3.

**Path B — User wants a reusable system**
Ask:
"Để build personalization framework, mình cần biết:
1. **ICP segments:** Bạn target mấy loại prospect khác nhau? (VD: Marketing Manager tại SaaS / Founder tại F&B / CMO tại retail)
2. **Volume:** Bạn outreach bao nhiêu prospects/tuần?
3. **Research time per prospect:** Bạn sẵn sàng dành bao lâu để research mỗi người? (2 phút / 5 phút / 10 phút)
4. **Data sources:** Bạn dùng LinkedIn, website, Facebook, hay nguồn nào khác?"

Wait for answer before continuing.

## Step 3 — Build the personalization framework

### Why personalization works (and why most people do it wrong)

**Bad personalization:** "Chào [Tên], mình thấy bạn là [Job Title] tại [Company]." This is mail merge, not personalization. Everyone knows you found this on LinkedIn.

**Good personalization:** References something specific they did, said, or created — something that shows you actually paid attention. "Mình đọc bài bạn đăng hôm thứ Ba về [specific topic] — đặc biệt phần về [specific point]. Điều đó khiến mình nghĩ đến..."

**The 1-3-1 rule:** 1 minute of research, 3 personalization signals found, 1 used per message. Don't use all 3 — it feels like surveillance.

### Personalization signal categories

**Tier 1 — High signal (use these first)**
These show genuine attention and generate the highest reply rates:
- Recent LinkedIn post or article they wrote
- Comment they left on someone else's post
- Company news: funding, new hire, product launch, expansion
- Job change: new role in last 90 days
- Content they shared with a specific opinion attached
- Award or recognition they or their company received

**Tier 2 — Medium signal**
Relevant but less specific:
- Industry they're in + current market trend affecting them
- Company size + typical challenges at that scale
- Tech stack they use (visible from job listings or website)
- Competitor they work with or mention publicly

**Tier 3 — Low signal (last resort)**
Generic but better than nothing:
- Their job title + common pain for that role
- Location + local market context
- Company founding year (speaks to their stage)

### Research process (5 minutes per prospect)

**Step 1 (1 min): LinkedIn profile scan**
- Recent posts (last 30 days) — look for opinions, not just shares
- "About" section — often reveals priorities and personality
- Recent job change flag

**Step 2 (1 min): Company LinkedIn page**
- Recent company updates
- Hiring patterns (tells you where they're investing)
- Recent announcements

**Step 3 (1 min): Their website**
- Homepage messaging (what problem they say they solve)
- Blog or news section (recent updates)
- Team page (size, growth signals)

**Step 4 (1 min): Google search: "[Name] [Company]"**
- Interviews, podcast appearances, articles written
- Awards or press mentions

**Step 5 (1 min): Write the personalization line**
One sentence. Specific. Genuine. Connects to your offer without forcing it.

### Personalization line formulas

**Formula 1 — Observation + Connection:**
"Mình đọc [specific thing they did/said] — [genuine observation]. Điều đó khiến mình nghĩ đến [connection to your offer]."

**Formula 2 — Shared context:**
"Mình thấy [Company] vừa [news/event] — [relevant observation]. Mình đang work với một vài công ty ở giai đoạn tương tự về [your offer area]."

**Formula 3 — Direct compliment + curiosity:**
"[Specific thing they made/said] là [genuine compliment — one word]. Tò mò về [specific aspect] — [connection to why you're reaching out]."

### Segment-specific personalization templates

Build a template bank per ICP segment. Each template has:
- **Research prompt:** What to look for (30 seconds of scanning)
- **Personalization slot:** The [PERSONALIZE HERE] placeholder in the template
- **Connection bridge:** How the personalization connects to the offer

**Example for Vietnamese SMB founder:**
- Research: Look for recent Facebook or LinkedIn post about marketing challenges
- Slot: "Mình vừa đọc bài bạn về [topic from post]"
- Bridge: "— điều đó relevant vì hầu hết founder mình nói chuyện đang gặp cùng vấn đề với [specific pain]"

**Example for Marketing Manager at mid-size company:**
- Research: Look for recent campaign they ran or tool they mentioned
- Slot: "Mình thấy [Company] vừa chạy [campaign type]"
- Bridge: "— curious bạn đang dùng gì để handle [content/automation/reporting] side của nó"

### Scaling personalization with templates

The framework outputs:
1. **Research checklist** per prospect type (what to look for, where, how long)
2. **Template bank** per ICP segment (3 templates per segment, each with personalization slot)
3. **Personalization line examples** (10 real examples they can pattern-match from)
4. **Quick-apply format** for high-volume outreach (for when you need to send 20+ per day)

## Step 4 — Write output

Save to `outputs/assets/outreach/personalization-framework-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Personalization Framework — [Brand Name]
> Generated: [date] | ICP segments: [n] | Volume: [prospects/week]

---

## Research Process (5 min per prospect)

| Step | Source | What to look for | Time |
|---|---|---|---|
| 1 | LinkedIn profile | Recent posts, opinions, job change | 1 min |
| 2 | Company LinkedIn | News, hiring, announcements | 1 min |
| 3 | Website | Homepage messaging, blog, team size | 1 min |
| 4 | Google | Interviews, press, awards | 1 min |
| 5 | Write the line | One specific, genuine sentence | 1 min |

---

## Signal Tiers

### Tier 1 — Use these (highest reply rate)
[List of high-signal personalization types for this brand's ICP]

### Tier 2 — Use if Tier 1 not available
[List]

### Tier 3 — Last resort
[List]

---

## Segment Templates

### Segment 1: [ICP Segment Name]

**Research prompt:** [What to look for in 30 seconds]

**Template A:**
Subject: [subject with personalization slot]
Opening: "[PERSONALIZE: specific observation] — [bridge to offer]"
[Rest of template]

**Template B:**
[Alternative angle]

**Template C:**
[Third option]

---

### Segment 2: [ICP Segment Name]
[Repeat]

---

## Personalization Line Examples (10 real examples)

1. "[Example — specific, genuine, connects to offer]"
2. "[Example]"
[...]

---

## High-Volume Quick-Apply Format

When sending 20+ emails/day, use this 2-minute research process:
1. [Fastest research step]
2. [What to prioritize]
3. [Minimum viable personalization]

---

## Quality Check

Before sending any personalized outreach, verify:
- [ ] The personalization is specific (not generic)
- [ ] It references something they actually did/said (not just their job title)
- [ ] The connection to the offer feels natural, not forced
- [ ] It doesn't feel like surveillance (one signal used, not all three)
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Personalization framework cho [Brand Name] đã hoàn chỉnh.**

**Segments covered:** [n] ICP segments
**Templates per segment:** 3
**Research process:** 5 min/prospect standard, 2 min high-volume

📁 Đã lưu vào: `outputs/assets/outreach/personalization-framework-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Apply framework to `/cold-email` or `/linkedin-dm` templates, hoặc build Agent 12 Sales Enablement để prepare for when prospects respond."

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
