---
name: ad-campaign-structure
description: "Structure ad campaigns and ad sets."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Ads]
    related_skills: [ad-creative, ad-copy, audience-targeting, ad-campaign-structure, ads-ab-test-setup, google-pmax-brief, marketing-orchestrator]
---

# Ad Campaign Structure Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Structure ad campaigns and ad sets.

## Procedure

Your job is to design the complete campaign architecture — campaign → ad set → ad level — for Meta and Google campaigns. The right structure prevents budget waste, enables clean testing, and makes optimization decisions obvious instead of guesswork.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — defines campaign objective and conversion event
- Target audience (Section 6) — informs ad set segmentation
- Location (Section 3) — geographic structure decisions

If `outputs/assets/ads/audience-targeting-*.md` exists: use the audience segments already defined.
If `outputs/assets/ads/ad-copy-*.md` exists: map copy versions to ad sets.
If `outputs/strategy/campaign-brief-*.md` exists: align structure to campaign goal and timeline.

If brand.md doesn't exist: ask user for offer, budget, platform, and goal before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign type, budget, and platform**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build campaign structure, mình cần biết:
1. **Campaign mục tiêu:** Lead gen / Conversion / Awareness / Traffic?
2. **Platform:** Meta / Google / Cả hai?
3. **Budget/tháng:** [amount] — để mình chia budget đúng
4. **Có data pixel chưa:** Pixel installed + có conversion events chưa?
5. **Timeline:** Campaign chạy bao lâu? (1 tuần / 1 tháng / ongoing)"

Wait for answer before continuing.

## Step 3 — Design campaign structure

### Meta Campaign Architecture

**Campaign level — one objective per campaign:**

| Goal | Campaign Objective | Conversion Event |
|---|---|---|
| Book consultation | Leads | Lead form submit / Messenger |
| Website sign-up | Leads | CompleteRegistration |
| Purchase | Sales | Purchase |
| Content views | Traffic | Landing page views |
| Brand awareness | Awareness | Reach / Video views |

**Ad Set level — one audience variable per ad set:**

The fundamental rule: **test one variable at a time**. Each ad set changes only one thing. This is how you learn what actually drives performance.

Structure options:

*Option A — Audience testing (most common starting point):*
```
Campaign: Lead Gen — [Brand Name]
├── Ad Set 1: Cold — Interest (AI + Marketing)
├── Ad Set 2: Cold — Interest (Business owners + Tech)
├── Ad Set 3: Cold — Lookalike 2% from website visitors
└── Ad Set 4: Warm — Website visitors 30 days
```

*Option B — Funnel structure (when you have pixel data):*
```
Campaign 1: Prospecting (60% budget)
├── Ad Set 1: Broad cold — interest clusters
└── Ad Set 2: Lookalike 2%

Campaign 2: Retargeting (30% budget)
├── Ad Set 1: Engagers 90 days
└── Ad Set 2: Website visitors 60 days

Campaign 3: Conversion (10% budget)
└── Ad Set 1: Hot — pricing page visitors + email list
```

*Option C — Advantage+ Campaign Shopping / Lead (Meta's AI structure):*
Use when: You have 50+ conversions/week and trust Meta's algorithm.
Structure: Fewer ad sets, more creative variations, let Meta optimize.
Vietnamese market note: Less control, can work well at scale (>10tr/month budget).

**Ad level — creative variations:**
- 2–4 ads per ad set minimum for creative testing
- Label clearly: `[Audience]-[Copy version]-[Creative format]`
- Example: `Cold-PainLed-StaticImage`, `Cold-ProofLed-Video15s`

**Budget rules:**
- Minimum per ad set: 200k VND/day (below this, Meta can't exit learning phase)
- Learning phase: ~50 optimization events — don't touch structure for first 7 days
- Scale winner: Increase budget max 20% every 2 days to avoid re-entering learning

**Vietnamese Meta specifics:**
- Advantage+ placements: ON for Vietnam — Instagram often delivers cheaper CPL than Facebook feed
- Messenger placement: High performer in Vietnam — Vietnamese buyers prefer messaging over forms
- Lead forms vs website: Native lead forms (Instant Leads) convert better in Vietnam for cold audiences because they reduce friction and don't require fast mobile connections

### Google Campaign Architecture

**Campaign types for Vietnamese SMB services:**

*Search campaign (highest intent):*
```
Campaign: Search — Brand Keywords
└── Ad Group: [Brand name] + variations

Campaign: Search — Service Keywords
├── Ad Group: [Primary service] keywords
├── Ad Group: [Competitor] keywords (if budget allows)
└── Ad Group: [Problem-aware] keywords
```

*Performance Max (when ready):*
- Requires: 30+ conversions in last 30 days before launching
- Feeds from: headlines, descriptions, images, videos
- Structure: One campaign per offer (don't mix offers)

**Keyword match type strategy:**
- Start: Exact + Phrase match only — control over what triggers ads
- Expand: Add broad match modifiers once you have 30+ conversion data
- Negative keywords: Build list from day 1 — prevents wasted spend

**Ad group structure:**
- One theme per ad group (5–15 tightly related keywords)
- 3 Responsive Search Ads minimum per ad group
- All headlines and descriptions should be mix-and-matchable

**Google campaign for Vietnamese market:**
- Vietnamese keywords in both Latin (doanh nghiep) and full form (doanh nghiệp) — Google treats differently
- Location: TP.HCM + Hà Nội bid +20% vs other provinces for B2B
- Schedule: Mon–Fri 8am–6pm higher bids, evenings lower (B2B decision makers work hours)
- Device: Desktop bid +10% for B2B (decision makers on desktop), mobile -20% for complex offers

### Campaign naming convention

Consistent naming prevents confusion when managing multiple campaigns:

```
[Platform]-[Goal]-[Audience]-[Offer]-[Date]

Examples:
META-LEADS-COLD-CONSULT-2026Q2
META-LEADS-WARM-CONSULT-2026Q2
GGL-SEARCH-BRAND-SETUP-2026Q2
GGL-SEARCH-SERVICE-SETUP-2026Q2
```

## Step 4 — Write output

Save to `outputs/assets/ads/ad-campaign-structure-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Ad Campaign Structure — [Campaign Name]
> Generated: [date] | Platform: [Meta/Google] | Budget: [total/month] | Timeline: [dates]

---

## Meta Structure

### Campaign 1 — [Name] ([objective])
**Daily budget:** [amount]
**Optimization event:** [event]

#### Ad Set 1 — [Name]
**Audience:** [description]
**Budget:** [amount/day]
**Placements:** [Advantage+/Manual]
**Ads:**
- Ad A: [label] — [copy version] + [creative]
- Ad B: [label] — [copy version] + [creative]

#### Ad Set 2 — [Name]
[Repeat]

---

### Campaign 2 — [Name]
[Repeat]

---

## Google Structure

### Campaign 1 — [Name] ([type])
**Daily budget:** [amount]
**Bidding:** [strategy]

#### Ad Group 1 — [Theme]
**Keywords:**
- [keyword] [match type]
- [keyword] [match type]
**Negative keywords:** [list]
**Ads:** 3 RSAs minimum

---

## Budget Summary
| Campaign | Platform | Daily | Monthly |
|---|---|---|---|
| [name] | [platform] | [amount] | [amount] |
| **Total** | | [total/day] | [total/month] |

---

## Launch Checklist
- [ ] Pixel installed and firing correctly
- [ ] Conversion events verified in Events Manager
- [ ] All audiences created and sized
- [ ] Creative assets uploaded
- [ ] Copy approved
- [ ] UTM parameters on all landing page URLs
- [ ] Notification: check performance after 48 hours (not before)

---

## Optimization Schedule
- Day 2: Check for disapprovals, delivery issues
- Day 7: First performance review — pause underperforming ads (not ad sets yet)
- Day 14: Ad set performance review — reallocate budget
- Day 30: Full campaign review — scale winners, kill losers
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Ad campaign structure cho '[Campaign]' đã hoàn chỉnh.**

**Structure:**
- [n] campaigns — [objectives]
- [n] ad sets — [audience split]
- [n] ads planned
- Total budget: [amount]/month

📁 Đã lưu vào: `outputs/assets/ads/ad-campaign-structure-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/ab-test-setup` để design testing protocol, hoặc review checklist và launch."

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
