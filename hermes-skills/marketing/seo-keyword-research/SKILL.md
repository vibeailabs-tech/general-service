---
name: seo-keyword-research
description: "Research keywords and SERP demand via SerpAPI."
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

# Keyword Research Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Research keywords and SERP demand via SerpAPI.

## Procedure

Your job is to find keywords the brand should rank for — including gaps competitors own that this brand doesn't. Uses SerpAPI to pull real SERP data.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Industry, location, language (Sections 1–3)
- Core offer and target audience (Sections 6 + 9)
- Competitors (Section 10)

If brand.md doesn't exist: ask user to provide brand name, industry, location, and 3 competitor URLs manually.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided seed keywords or a topic**
Use those as starting seeds. Go to Step 3.

**Path B — No seeds provided**
Ask:
"Để research keyword, mình cần biết:
1. **Chủ đề chính:** Bạn muốn rank cho chủ đề gì? (VD: 'AI marketing', 'phần mềm kế toán', 'spa tại TPHCM')
2. **Mục tiêu:** Bạn muốn keyword cho trang nào? (homepage / blog / landing page cụ thể)
3. **Ưu tiên:** Volume cao, competition thấp, hay intent mua hàng?"

Wait for answer.

## Step 3 — Run keyword research

### SerpAPI calls to make (3 rounds):

**Round 1 — Seed keyword SERPs**
For each seed keyword, call SerpAPI Google Search:
- `q`: seed keyword (+ "Vietnam" or location if local)
- `gl`: vn, `hl`: vi (or en depending on brand language)
- `num`: 10

Extract from each SERP:
- Top 10 organic results (title, URL, snippet)
- People Also Ask questions
- Related searches at bottom of SERP

**Round 2 — Competitor keyword gaps**
For each competitor domain from brand.md, call SerpAPI:
- Search `site:[competitor-domain] [seed topic]` to see what they rank for
- Note recurring themes and angles they cover

**Round 3 — Long-tail variations**
Based on PAA and related searches from Round 1, pick the 5 most promising long-tail terms and run SerpAPI searches on those too.

### Analyze results:

**Keyword scoring criteria:**
1. **Search intent alignment** — does searcher intent match the brand's offer?
   - Informational: research phase (blog content)
   - Commercial: comparing options (comparison pages, case studies)
   - Transactional: ready to buy (landing pages, service pages)
2. **Competitor difficulty** — how strong are current top 10 results?
   - Check: are top results big brand domains (hard) or thin content (opportunity)?
3. **Topic cluster fit** — does this keyword belong in a logical cluster around a pillar topic?
4. **Vietnamese market specificity** — is there a Vietnamese-specific angle that global content misses?

**Classify each keyword:**
- Quick win: lower competition, clear intent, brand can rank in 60–90 days
- Strategic: higher volume, worth pursuing with strong content over 6+ months
- Skip: dominated by huge brands or irrelevant intent

## Step 4 — Build keyword map

Organize into 3 tiers:

**Tier 1 — Pillar keywords (1–3 keywords)**
High-volume, defines the brand's main topic. Hard to rank immediately but anchor the whole strategy.

**Tier 2 — Cluster keywords (5–10 keywords)**
Medium difficulty, support the pillar. Each one becomes a piece of content.

**Tier 3 — Quick wins (10–20 keywords)**
Low competition, clear intent. Start ranking here to build authority for Tier 1.

## Step 5 — Write output

Save to `outputs/assets/seo/keyword-research-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Keyword Research — [Brand Name]
> Generated: [date] | Tools: SerpAPI | Location: [location]

## Executive Summary
- Pillar keyword: [main keyword]
- Total keywords mapped: [n]
- Quick wins identified: [n]
- Biggest competitor gap: [what they rank for that you don't]

---

## Tier 1 — Pillar Keywords

| Keyword | Est. Monthly Searches | Intent | Difficulty | Notes |
|---|---|---|---|---|
| | | | | |

---

## Tier 2 — Cluster Keywords

| Keyword | Intent | Content Type | Priority |
|---|---|---|---|
| | | | |

---

## Tier 3 — Quick Wins

| Keyword | Why It's a Quick Win | Recommended Page |
|---|---|---|
| | | |

---

## People Also Ask (High Value)
Questions from SERPs that represent content opportunities:
1. 
2. 
3. 

---

## Competitor Keyword Gaps
Keywords competitors rank for that [Brand] currently doesn't:

| Keyword | Competitor That Ranks | Opportunity |
|---|---|---|
| | | |

---

## Content Recommendations
Based on keyword clusters, these are the next 5 content pieces to create:
1. [Title] — targets [keyword] — [intent] — [page type]
2. 
3. 
4. 
5. 
```

## Step 6 — Confirm

After writing:

---
"✅ **Keyword research cho [Brand Name] hoàn chỉnh.**

**Highlights:**
- [n] pillar keywords, [n] cluster keywords, [n] quick wins
- Top quick win: '[keyword]' — [why]
- Biggest gap vs competitors: '[keyword]'

📁 Đã lưu: `outputs/assets/seo/keyword-research-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/on-page-seo` để tối ưu trang hiện có cho các keywords này, hoặc `/content-brief` để brief bài viết nhắm vào quick wins."

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
