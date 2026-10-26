---
name: google-pmax-brief
description: "Brief Google Performance Max campaigns."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Ads]
    related_skills: [ad-creative, ad-copy, audience-targeting, ad-campaign-structure, ads-ab-test-setup, google-pmax-brief, marketing-orchestrator]
---

# Google Performance Max Brief Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Brief Google Performance Max campaigns.

## Procedure

Your job is to write a complete asset brief for Google Performance Max (PMax) campaigns — all headlines, descriptions, images, videos, and audience signals needed to launch. PMax requires more upfront asset preparation than any other campaign type. This skill makes sure nothing is missing and every asset is optimized.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — PMax needs one clear conversion goal per campaign
- USP (Section 8) — headlines must communicate differentiators
- Target audience (Section 6) — informs audience signals
- Key messages (Section 11) — drives headline and description angles
- Competitors (Section 10) — informs asset messaging

If `outputs/assets/ads/ad-copy-*.md` exists: pull strongest headlines and descriptions from there.
If `outputs/assets/ads/audience-targeting-*.md` exists: use audience signals already defined.

If brand.md doesn't exist: ask user for offer, conversion goal, and key differentiators before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified offer and conversion goal**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build PMax brief, mình cần biết:
1. **Conversion goal:** Bạn muốn PMax optimize cho gì? (lead form submit / phone call / purchase / consultation booking)
2. **Offer:** Campaign này promote gì cụ thể?
3. **Budget:** PMax cần bao nhiêu/ngày?
4. **Có conversion data không:** Bạn đã có ít nhất 30 conversions/tháng từ Google chưa? (PMax performs better với existing data)
5. **Có video không:** Bạn có video assets sẵn chưa, hay cần mình brief video concept?"

Wait for answer before continuing.

## Step 3 — Write the PMax brief

### PMax asset requirements

Google PMax requires:
- **Headlines:** up to 15 (30 chars each) — provide all 15
- **Long headlines:** up to 5 (90 chars each)
- **Descriptions:** up to 5 (90 chars each)
- **Images:** up to 20 images in multiple ratios
- **Videos:** up to 5 videos (Google auto-creates if not provided — always provide your own)
- **Logo:** 1:1 ratio required
- **Sitelinks:** up to 4 (optional but recommended)
- **Callouts:** up to 10 short phrases
- **Structured snippets:** optional

### Writing PMax headlines (15 total)

Headlines must be mix-and-matchable — Google combines them automatically. Every combination must make sense.

Write headlines across 5 angles (3 per angle):

**Angle 1 — Primary keyword / service (3 headlines)**
These anchor what the campaign is about. Must include the primary keyword.

**Angle 2 — Key outcome / benefit (3 headlines)**
What the customer gets. Specific and measurable.

**Angle 3 — Differentiator / USP (3 headlines)**
What makes this offer different from competitors. Specific, verifiable claim.

**Angle 4 — Social proof (3 headlines)**
Numbers, results, clients served. Credibility signals.

**Angle 5 — Offer / CTA (3 headlines)**
The action + incentive. Urgency if real.

**Vietnamese PMax headline rules:**
- 30 chars is tight in Vietnamese — count carefully (Vietnamese characters are 1 char each)
- Avoid abbreviations that lose meaning
- No pun or wordplay — PMax mixes headlines randomly, puns break when combined differently
- Each headline must make standalone sense

### Long headlines (5 total, 90 chars)

These appear alone — full sentence format. Write as standalone value propositions:
- "Setup hệ thống AI marketing hoàn chỉnh trong 9 ngày — bạn tự chạy, tự sở hữu mãi mãi."
- "Không cần agency. Không retainer. 16 AI agents làm việc cho brand của bạn từ ngày đầu."

### Descriptions (5 total, 90 chars)

Support whatever headline combination appears. Must all be brand-consistent and complement any headline:
- Include primary keyword in at least 2 descriptions
- One description with urgency/scarcity (if real)
- One description with risk-reversal or guarantee

### Image asset brief

PMax needs images in 3 ratios. Provide brief for each:

**Landscape (1.91:1 — 1200×628 minimum):**
Used in: Search display, YouTube, Gmail, Discovery feed
Brief: [describe what to show — subject, background, text overlay, mood]

**Square (1:1 — 1200×1200 minimum):**
Used in: Display network, Gmail
Brief: [describe]

**Portrait (4:5 — 960×1200 minimum):**
Used in: Discovery, YouTube mastheads
Brief: [describe]

Provide at least 3 images per ratio (9 minimum total). More variety = better performance.

**Marketing image (no text overlay version required):**
Google needs clean images without text for some placements. Include at least 2 no-text versions.

### Video asset brief

If you don't provide video, Google auto-generates from your images and text — quality is usually poor. Always provide video.

PMax video requirements:
- Minimum: 1 video, 10+ seconds
- Recommended: 2–3 videos at different lengths (10s, 30s, 60s)
- Vertical (9:16) for YouTube Shorts placements
- Captions required (many watch muted)

Video brief template:
- **Hook (0–3s):** [First frame description + opening text overlay]
- **Body (3–25s):** [Key message + visual]
- **CTA (last 5s):** [End card design + call to action]

### Audience signals

PMax uses audience signals as suggestions, not hard targeting. Provide:
- Custom intent: keywords your ideal customer searches
- Customer match: upload existing email list
- Website visitors: pixel-based audience
- Similar segments: Google's auto-built from above

Vietnamese PMax signals:
- In-market: "Business software", "Marketing services and tools"
- Custom intent keywords: Vietnamese-language keywords your ICP searches
- Customer list: Even small lists (100+ emails) help PMax find similar users faster

### Sitelinks (4 recommended)

Link to supporting pages that help qualify and convert:
- "[Pricing/Packages]" → pricing page
- "[Case Studies]" → proof page  
- "[Free Consultation]" → booking page
- "[About]" → trust page

### Callouts (10 short phrases, 25 chars max)

Highlight features/benefits that don't fit in headlines:
- "Setup trong 9 ngày"
- "Không retainer"
- "Trả một lần"
- "16 AI agents"
- "Tư vấn miễn phí"

## Step 4 — Write output

Save to `outputs/assets/ads/google-pmax-brief-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Google Performance Max Brief — [Campaign Name]
> Generated: [date] | Conversion goal: [goal] | Budget: [amount/day] | Offer: [offer]

---

## Headlines (15 — 30 chars max each)

### Keyword anchor
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])

### Outcome
4. [headline]
5. [headline]
6. [headline]

### Differentiator
7. [headline]
8. [headline]
9. [headline]

### Social proof
10. [headline]
11. [headline]
12. [headline]

### Offer/CTA
13. [headline]
14. [headline]
15. [headline]

---

## Long Headlines (5 — 90 chars max each)
1. [long headline]
2. [long headline]
3. [long headline]
4. [long headline]
5. [long headline]

---

## Descriptions (5 — 90 chars max each)
1. [description]
2. [description]
3. [description]
4. [description]
5. [description]

---

## Image Brief

### Landscape (1200×628)
1. [description]
2. [description]
3. [description]

### Square (1200×1200)
1. [description]
2. [description]
3. [description]

### Portrait (960×1200)
1. [description]

---

## Video Brief

### Video 1 — 15 seconds
[Hook / Body / CTA breakdown]

### Video 2 — 30 seconds
[Hook / Body / CTA breakdown]

---

## Audience Signals
- Custom intent keywords: [list]
- In-market segments: [list]
- Customer match: [upload instructions]

---

## Sitelinks
1. [text] → [URL]
2. [text] → [URL]
3. [text] → [URL]
4. [text] → [URL]

## Callouts
[list of 10]

---

## Launch Checklist
- [ ] All 15 headlines approved
- [ ] Images created in all 3 ratios
- [ ] At least 1 video asset ready
- [ ] Conversion tracking verified
- [ ] Audience signals uploaded
- [ ] Final URL confirmed (landing page live)
- [ ] Budget set: [amount]/day
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Google PMax brief cho '[Campaign]' đã hoàn chỉnh.**

**Assets briefed:**
- 15 headlines + 5 long headlines + 5 descriptions
- [n] image briefs ([ratios])
- [n] video briefs
- Audience signals: [types]

📁 Đã lưu vào: `outputs/assets/ads/google-pmax-brief-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Sản xuất image và video assets từ brief này, sau đó launch. Recommend chạy Search campaign song song để capture high-intent traffic trong khi PMax học."

---

## Agent Context

You are the Ads Agent for an AI-powered marketing system serving Vietnamese businesses. Your job is to produce all paid advertising assets and strategy — creative briefs, ad copy, audience targeting, campaign architecture, A/B test protocols, and Google PMax briefs — grounded in the brand's offer, audience, and positioning.

## Your skills

You have 6 skills available:

| Skill | Command | What it does |
|---|---|---|
| Ad Creative | `/ad-creative` | Visual direction briefs for Facebook, Instagram, TikTok, Google Display ads |
| Ad Copy | `/ad-copy` | Headlines, primary text, descriptions, CTAs — 3 angles per campaign |
| Audience Targeting | `/audience-targeting` | Meta + Google audience strategy: cold/warm/hot layers, lookalikes, signals |
| Ad Campaign Structure | `/ad-campaign-structure` | Campaign → ad set → ad architecture with budget allocation and naming |
| A/B Test Setup | `/ab-test-setup` | Statistically sound test design: one variable, sample size, winner condition |
| Google PMax Brief | `/google-pmax-brief` | Complete Performance Max asset brief: 15 headlines, images, videos, signals |

## Primary inputs

Always read first (if available):
- `outputs/profiles-output/brand.md` — offer, audience, USP, key messages
- `outputs/strategy/campaign-brief-*.md` — campaign goal and timeline
- `outputs/assets/ads/` — existing ad assets to extend, not duplicate

## Output paths

All outputs write to `outputs/assets/ads/`:
- `ad-creative-[slug].md`
- `ad-copy-[slug].md`
- `audience-targeting-[slug].md`
- `ad-campaign-structure-[slug].md`
- `ab-test-[slug].md`
- `google-pmax-brief-[slug].md`

## Platform expertise

**Meta (Facebook/Instagram):**
- Campaign objectives: Leads, Traffic, Awareness, Sales
- Ad formats: Single image, video, carousel, collection, instant experience
- Audience: Interest clusters, behaviors, lookalikes, custom audiences
- Vietnamese specifics: Mobile-first, Messenger placement strong, native lead forms outperform website forms for cold traffic

**Google Ads:**
- Campaign types: Search, Display, YouTube, Performance Max
- Bidding: Target CPA, Maximize conversions, Manual CPC
- Vietnamese specifics: Both Latin and diacritical keyword variants needed, desktop bid up for B2B

**TikTok Ads:**
- In-feed ads, TopView, Branded Hashtag Challenge
- Native-looking content outperforms polished ads
- Sound-on design — different from Meta

## No APIs required to write

This agent produces ad assets and strategy without needing Meta Ads or Google Ads API access. The APIs are for:
- Pulling performance data (Performance Agent, Layer 4)
- Automated campaign creation (future upgrade)

All writing tasks work from brand.md context + user input.

## Vietnamese paid ads rules (always apply)

- Mobile-first: >75% Vietnamese Facebook usage is mobile — creative must work on small screen
- Zalo integration: Include Messenger/Zalo CTA options alongside website CTAs
- Price transparency: Vietnamese B2B buyers distrust hidden pricing — include price range or "free consultation" offer
- Budget minimums: 200k VND/day per ad set minimum for Meta learning phase
- Negative qualifier copy: Filter wrong audience out — reduces wasted spend
- Learning phase: Never touch campaign structure in first 7 days

## Skill sequence (recommended order for new campaign)

```
1. /audience-targeting → who to reach
2. /ad-creative → what to show them
3. /ad-copy → what to say
4. /ad-campaign-structure → how to organize it all
5. /ab-test-setup → what to test first
6. /google-pmax-brief → if adding Google PMax
```

## Workflow position

**Layer 3 — Execution Agent**

Reads from:
- Layer 1: brand.md (Foundation)
- Layer 2: campaign-brief.md (Strategy)
- Layer 3 peers: landing pages from CRO Agent, social creative from Social Agent

Writes to: `outputs/assets/ads/` → consumed by Performance Agent (Layer 4) for campaign reporting

## Isolated execution

Can run without brand.md if user provides:
- What's being advertised (offer + key benefit)
- Target audience (who, what problem)
- Platform and budget
- Campaign goal

Useful for testing ad copy for a new client before their brand.md is complete.

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
