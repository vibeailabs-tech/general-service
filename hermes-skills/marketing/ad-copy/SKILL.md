---
name: ad-copy
description: "Write paid ad copy for Meta and Google."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Ads]
    related_skills: [ad-creative, ad-copy, audience-targeting, ad-campaign-structure, ads-ab-test-setup, google-pmax-brief, marketing-orchestrator]
---

# Ad Copy Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write paid ad copy for Meta and Google.

## Procedure

Your job is to write all ad copy components — headlines, primary text, descriptions, and CTAs — for Facebook/Instagram ads, TikTok ads, and Google Search ads. Every word is tested against one criterion: does it make the right person click and the wrong person scroll past?

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — ad copy must match brand tone exactly
- Target audience (Section 6) — pain points, language they use, what they're afraid of
- Core offer (Section 9) — what you're selling and how it's framed
- USP (Section 8) — the one claim no competitor can make
- Key messages (Section 11) — messages to reinforce

If `outputs/strategy/campaign-brief-*.md` exists: read it — use campaign goal and offer framing.
If `outputs/assets/ads/ad-creative-*.md` exists: align copy to the creative concept.

If brand.md doesn't exist: ask user for offer, audience pain point, and unique claim before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign, offer, or angle**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết ad copy, mình cần biết:
1. **Offer:** Bạn đang quảng cáo gì cụ thể? (VD: tư vấn miễn phí, gói $700, lead magnet)
2. **Platform:** Facebook / Instagram / TikTok / Google Search?
3. **Mục tiêu:** Awareness / Lead / Purchase?
4. **Audience stage:** Cold (chưa biết brand) / Warm (đã tương tác) / Hot (đã xem sales page)?
5. **CTA action:** Điền form / Nhắn Zalo / Đọc bài / Xem video / Mua ngay?"

Wait for answer before continuing.

## Step 3 — Write all ad copy components

### Facebook/Instagram Ad Copy

**Primary text (body copy above the image):**
- Cold audience: 100–150 words — enough to qualify the reader and create desire
- Warm/retargeting: 50–80 words — they already know you, remind and convert
- Structure: Pain → Agitate → Solution → Proof → CTA
- Hook line (first sentence): this is what shows before "see more" — make it earn the click
- Never start with the brand name — start with the reader's problem

**Headline (below image, 40 chars max):**
- Most important copy real estate after the hook
- Formula options:
  - Outcome: "Hệ thống AI marketing chạy không cần agency"
  - Question: "Bạn đang trả bao nhiêu cho content không sở hữu?"
  - Direct: "Setup AI marketing team trong 9 ngày"
  - Number: "16 agents — $80/tháng — bạn sở hữu toàn bộ"

**Description (under headline, 30 chars max):**
- Support the headline — add urgency, specificity, or risk-reversal
- Examples: "Còn 5 slots tháng 5" / "Tư vấn miễn phí 30 phút" / "Không retainer, không lock-in"

**CTA button:**
- Match to funnel stage: "Tìm hiểu thêm" (cold) / "Đăng ký ngay" (warm) / "Liên hệ ngay" (hot)
- Vietnamese-specific: "Nhắn tin" performs well for Zalo-native audiences

### TikTok Ad Copy

**On-screen text (overlay, first 3 seconds):**
- Max 8 words — readable at a glance
- States the hook before voiceover begins
- High contrast against video background

**Caption (below video):**
- 80–120 words max
- First sentence = hook restatement
- Hashtags: 5–8, end of caption
- CTA: one action — "Link bio" or "Comment [keyword]"

### Google Search Ad Copy

**Headlines (up to 15, 30 chars each — Google picks best combo):**
Write at least 10 headlines covering:
- Primary keyword match (2–3 headlines)
- Benefit/outcome (3–4 headlines)
- Social proof (1–2 headlines)
- Urgency or offer (1–2 headlines)
- Brand name (1 headline)

**Descriptions (up to 4, 90 chars each):**
- Expand on the headline promise
- Include primary keyword naturally
- One specific proof point per description
- End with implied CTA

**Display URL paths:**
- `/[keyword]/[action]` format — e.g., `/AI-marketing/tu-van-mien-phi`

### Vietnamese ad copy rules

**Language that converts in Vietnamese B2B:**
- "Trả một lần, dùng mãi mãi" — ownership framing
- "Bạn sở hữu toàn bộ" — Vietnamese buyers hate lock-in
- "Không retainer, không ràng buộc" — removes commitment fear
- Specific VND or USD amounts — vague pricing kills trust
- "Mình setup cho bạn" — personal, not corporate

**Language to avoid:**
- "Giải pháp toàn diện" — overused, meaningless
- "Đội ngũ chuyên nghiệp" — every competitor says this
- "Hỗ trợ 24/7" — unless actually true
- Overpromise: "Tăng doanh thu 300%" without proof

**Negative targeting copy:**
Include a qualifier that filters bad-fit clicks:
- "Dành cho doanh nghiệp đang trả >$300/tháng cho agency"
- "Phù hợp nếu bạn đã có sản phẩm/dịch vụ và muốn scale marketing"
This reduces CPC waste — wrong audience self-selects out.

### Copy testing framework

For each campaign, write 3 copy angles to test:

| Angle | Approach | Best for |
|---|---|---|
| Pain-led | Open with the problem they're living right now | Cold audience |
| Proof-led | Open with result/number, then explain | Warm audience |
| Contrarian | Challenge a common belief in the industry | Engaged/educated audience |

## Step 4 — Write output

Save to `outputs/assets/ads/ad-copy-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Ad Copy — [Campaign Name]
> Generated: [date] | Platform: [platform] | Goal: [goal] | Audience stage: [cold/warm/hot]

---

## Facebook/Instagram — Version A (Pain-led)

**Primary Text:**
[Full body copy]

**Headline:** [max 40 chars]
**Description:** [max 30 chars]
**CTA Button:** [button text]

---

## Facebook/Instagram — Version B (Proof-led)

**Primary Text:**
[Full body copy]

**Headline:** [max 40 chars]
**Description:** [max 30 chars]
**CTA Button:** [button text]

---

## Facebook/Instagram — Version C (Contrarian)

**Primary Text:**
[Full body copy]

**Headline:** [max 40 chars]
**Description:** [max 30 chars]
**CTA Button:** [button text]

---

## Google Search — Headlines (10 minimum)
1. [30 chars]
2. [30 chars]
[...]

## Google Search — Descriptions (4)
1. [90 chars]
2. [90 chars]
3. [90 chars]
4. [90 chars]

**Display URL:** [domain]/[path1]/[path2]

---

## TikTok Ad

**On-screen text hook:** "[max 8 words]"
**Caption:**
[Full caption with hashtags]

---

## Testing Notes
- Test A vs B first — [what you're isolating: hook angle]
- Winner condition: [metric] >[threshold] after [n] impressions
- Loser to pause at: CPC >[amount] or CTR <[%]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Ad copy cho '[Campaign]' đã hoàn chỉnh.**

**Versions written:** [n] — [angle names]
**Platforms:** [list]
**Recommended test order:** Version [X] first — [one-line reason]

📁 Đã lưu vào: `outputs/assets/ads/ad-copy-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/ad-campaign-structure` để build campaign architecture, hoặc `/ab-test-setup` để design test protocol cho các versions này."

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
