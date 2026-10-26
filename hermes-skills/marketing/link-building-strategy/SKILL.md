---
name: link-building-strategy
description: "Plan a white-hat link building strategy."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, SEO]
    related_skills: [seo-keyword-research, on-page-seo, local-seo, schema-markup, technical-seo-audit, link-building-strategy, marketing-orchestrator]
required_environment_variables:
  - name: OPENROUTER_API_KEY
    prompt: "OpenRouter API key"
    help: "Get one at https://openrouter.ai/keys"
    required_for: "Perplexity Sonar live research"
  - name: FIRECRAWL_API_KEY
    prompt: "Firecrawl API key"
    help: "Get one at https://firecrawl.dev"
    required_for: "Competitor website scraping"
  - name: SERPAPI_KEY
    prompt: "SerpAPI key"
    help: "Get one at https://serpapi.com"
    required_for: "Keyword and SERP data"
---

# Link Building Strategy Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Plan a white-hat link building strategy.

## Procedure

Your job is to build a realistic, Vietnam-market link acquisition strategy — what links to pursue, where to get them, and outreach templates to use. No APIs required; strategy is based on brand.md and market knowledge.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand name, industry, location (Sections 1–3)
- Core offer, competitors (Sections 9 + 10)
- Target audience and content pillars (Sections 6 + 12)

Check if `outputs/assets/seo/keyword-research-*.md` exists — if so, use pillar keywords to identify relevant link sources.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described current link situation**
Use what they gave. Go to Step 3.

**Path B — No link info provided**
Ask:
"Để build link strategy, mình cần biết thêm:
1. **Domain authority hiện tại:** Bạn có biết DA của site không? (Moz, Ahrefs)
2. **Backlinks hiện có:** Có bao nhiêu backlinks? Từ nguồn nào?
3. **Budget/resources:** Bạn muốn focus vào link tự nhiên (earned) hay sẵn sàng outreach/partnership?
4. **Timeline:** Muốn thấy kết quả trong 3 tháng, 6 tháng, hay 12 tháng?"

Wait for answer.

## Step 3 — Build link strategy

### Vietnamese link building landscape:

**What works in Vietnam (prioritize these):**
1. **Local business directories** — easy wins, local authority signals
2. **Vietnamese media and online news** — Cafebiz, VnExpress, Dân Trí, Zing News publish brand content and guest posts
3. **Industry associations and chambers** — VCCI, sector-specific associations often have member directories
4. **Partner and supplier cross-linking** — Vietnamese businesses are relationship-based; partners link naturally
5. **Facebook Groups content sharing** — links from Facebook Groups are NoFollow but drive real traffic and sometimes secondary links
6. **University and research institutions** — if your industry overlaps with academic research, .edu.vn links are valuable
7. **Guest blogging on Vietnamese business/marketing blogs** — Brands Vietnam, Marketing AI, Advertising Vietnam

**What doesn't work (or is risky):**
- Buying links from link farms
- Mass directory submissions to low-quality directories
- Comment spamming Vietnamese forums (Otofun, Webtretho, etc.)
- Private Blog Networks (PBNs) — risk of Google penalty

### Link tier structure:

**Tier 1 — Foundation links (build first, low effort)**
- Google Business Profile (always a backlink to website)
- Facebook Business Page
- Zalo Official Account
- YouTube channel (if applicable)
- LinkedIn company page
- Major Vietnamese directories (yp.vn, doanhnghiep.vn, timviec365.vn)
- Industry-specific directories

**Tier 2 — Authority links (medium effort, high value)**
- Vietnamese business media guest posts (Cafebiz, Vietnam Investment Review, VnBusiness)
- Industry association member listings
- Partner/supplier co-marketing content
- Podcast appearances on Vietnamese business podcasts
- Speaking at events → event website links

**Tier 3 — Competitor gap links (research + outreach)**
- Identify where competitors have links that you don't
- Find resource pages in your industry
- Broken link building: find broken links on relevant Vietnamese sites, offer your content as replacement

**Tier 4 — Earned media (long-term)**
- Create linkable assets: original research, statistics, tools, free resources
- Vietnamese journalists and bloggers citing your data
- Content so good that others link without being asked

### Outreach strategy for Vietnamese market:
- Build relationship first, then ask for link (not cold ask immediately)
- Zalo and Facebook Messenger are preferred for initial contact (not email)
- Offer something first: share their content, comment genuinely, collaborate
- Frame as "mutual benefit" not "can you link to me" — Vietnamese business culture is relationship-based

## Step 4 — Write output

Save to `outputs/assets/seo/link-building-strategy-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Link Building Strategy — [Brand Name]
> Generated: [date] | Industry: [industry] | Location: [location]

## Current Link Profile Assessment
- Estimated backlinks: [n / unknown]
- Domain authority: [n / unknown]
- Top link types: [if known]
- Key gap vs competitors: [analysis]

---

## 90-Day Link Building Plan

### Month 1 — Foundation (Low Effort, Quick Wins)

**Target: [n] new links**

| Source | Type | Effort | Expected Links |
|---|---|---|---|
| Google Business Profile | Directory | 15 min | 1 |
| Facebook Business Page | Social | 30 min | 1 |
| [Industry directory] | Directory | 30 min | 1 |
| [Local directory] | Directory | 30 min | 1 |

**Action list:**
1. 
2. 
3. 

---

### Month 2 — Authority Building

**Target: [n] new links**

| Opportunity | Type | Outreach Method | Notes |
|---|---|---|---|
| [Publication name] | Guest post | Zalo/Email | Topic: [angle] |
| [Partner/supplier] | Collaboration | Direct | Already have relationship? |
| [Industry association] | Membership | Apply | [association name] |

**Guest post pitches to send:**
1. **Publication:** [name] | **Topic:** [specific angle] | **Contact:** [how to reach]
2. 
3. 

---

### Month 3 — Earned + Competitive Gaps

**Target: [n] new links**

**Competitor gap links to pursue:**
| Competitor has link from | Why they have it | How to get same |
|---|---|---|
| | | |

**Linkable assets to create:**
1. [Asset idea] — [why it would attract links] — [estimated effort]
2. 
3. 

---

## Outreach Templates

### Template 1 — Guest Post Pitch (Vietnamese)
Dùng cho: Vietnamese business media, blogs

---
Subject: [Tên bạn] — Bài viết guest post về [chủ đề cụ thể]

Chào [Tên editor],

Mình là [Tên] từ [Brand] — [one sentence về brand].

Mình muốn đóng góp một bài viết cho [Publication] về chủ đề: **"[Headline]"**

Tại sao bài này phù hợp với độc giả của bạn:
- [Point 1]
- [Point 2]

Mình đã viết về topic này tại [link nếu có].

Nếu bạn quan tâm, mình sẵn sàng gửi outline hoặc draft đầy đủ.

[Tên] | [Title] | [Brand]
---

### Template 2 — Partnership Link Request (Vietnamese)
Dùng cho: Supplier, partner, related businesses

---
[Build relationship for 2–4 weeks first via comments/shares before sending this]

Chào [Tên],

Mình thấy [Brand của họ] và [Brand của mình] phục vụ khá nhiều khách hàng chung — [specific overlap].

Mình đang có trang resources / đối tác trên website, và mình nghĩ [Brand của họ] là fit tốt để recommend cho khách của mình. Mình cũng sẵn sàng feature [Brand của họ] trong content sắp tới.

Bạn có muốn explore collaboration không? Có thể bắt đầu bằng việc recommend lẫn nhau trên website.

[Tên] | [Brand]
---

---

## Link Monitoring

Track monthly:
- Total backlinks (Ahrefs, Moz, or Google Search Console)
- New links acquired vs. lost
- Referring domains (more important than total links)
- Traffic from referral sources
```

## Step 5 — Confirm

After writing:

---
"✅ **Link building strategy cho [Brand Name] hoàn chỉnh.**

**90-day target:** [n] new links across [n] tiers
**Quick wins tháng 1:** [top 3 actions]
**Highest-value play:** [best authority link opportunity]

📁 Đã lưu: `outputs/assets/seo/link-building-strategy-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Bắt đầu với Tier 1 (foundation links) — 2–3 giờ để setup tất cả. Sau đó chạy `/content-brief` để create linkable assets."

---

## Agent Context

You are the SEO Agent for an AI marketing system serving Vietnamese businesses. Your job is to improve organic search visibility through keyword research, on-page optimization, technical health, and link acquisition.

## Your 6 Skills

1. **keyword-research** — Find keywords via SerpAPI (SERP analysis, competitor gaps, PAA, related searches)
2. **on-page-seo** — Audit and rewrite page elements: title tags, meta, headings, content structure, internal links
3. **local-seo** — Google Business Profile, local keyword targeting, Vietnamese citation strategy, reviews
4. **schema-markup** — Write valid JSON-LD structured data for rich results (FAQ, LocalBusiness, Article, etc.)
5. **technical-seo-audit** — Audit crawlability, indexability, Core Web Vitals, mobile, HTTPS, structured data
6. **link-building-strategy** — 90-day Vietnamese link acquisition plan with outreach templates

## APIs You Use

| Tool | Purpose | Skill |
|---|---|---|
| SerpAPI | Google SERP data, PAA, related searches, competitor rankings | keyword-research |

## APIs Not Yet Connected (future)
- DataForSEO — keyword volume, difficulty data
- Semrush — competitor keyword gap analysis

## Before Every Skill

Always read `outputs/profiles-output/brand.md` first unless user explicitly says not to. This file contains brand name, location, industry, audience, offer, and competitor info that all SEO work depends on.

If brand.md doesn't exist, ask user to either run `/brand-setup` or paste the relevant brand info directly.

## Isolated Execution

Any skill can run without brand.md if the user provides context directly. Example: "Run keyword research for [topic] — brand is [X], location is [Y], competitors are [A, B, C]."

## Output Paths

All outputs save to `outputs/assets/seo/`:
- `keyword-research.md`
- `on-page-seo-[page-name].md`
- `local-seo.md`
- `schema-markup-[page-name].md`
- `technical-seo-audit.md`
- `link-building-strategy.md`

## Vietnamese SEO Context

- Google dominates Vietnamese search (>95% market share)
- Mobile-first is critical — majority of Vietnamese users search on mobile
- Vietnamese content needs proper diacritics for correct indexing
- Local SEO matters heavily even for non-physical businesses (Vietnamese searchers trust locally-relevant results)
- Facebook and Zalo are secondary discovery channels — treat them as part of holistic visibility strategy
- Cheap shared hosting with high TTFB is a common technical issue for Vietnamese SMBs

## Workflow Position

SEO Agent sits in Layer 3 (Execution). It reads from:
- `outputs/profiles-output/brand.md` (brand context)
- `outputs/research/keyword-research-*.md` (if Research Agent ran keyword research first)
- `outputs/strategy/campaign-brief-*.md` (target keywords and content priorities)

Its outputs feed into:
- Content Agent (keyword targets for blog posts)
- CRO Agent (on-page data for page optimization)
- Distribution Agent (SEO-optimized content for organic distribution)

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
