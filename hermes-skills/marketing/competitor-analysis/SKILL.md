---
name: competitor-analysis
description: "Analyze competitor sites, offers, messaging."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Research]
    related_skills: [market-research, competitor-analysis, keyword-research, trend-monitoring, marketing-orchestrator]
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

# Competitor Analysis Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Scrapes and analyzes competitor websites using Firecrawl MCP and Playwright MCP. Use this skill when the user wants to understand what competitors are doing, their messaging, content strategy, offers, and weaknesses. Trigger whenever the user mentions competitor analysis, what competitors are doing, or wants to find gaps in the market.

Slash command: load this skill and follow its Procedure. Short summary: Analyze competitor sites, offers, messaging.

## Procedure

Your job is to scrape real competitor data — not guesses — and turn it into actionable intelligence about their messaging, offers, content strategy, and weaknesses.

## Step 1 — Read brand.md

Read `outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Competitors listed in Section 10
- Positioning and USP

If no competitors are listed in brand.md: ask the user to provide 2–3 competitor URLs or names before continuing.

## Step 2 — Collect competitor URLs

**Path A — Competitors with URLs already in brand.md**
Use those URLs. Go to Step 3.

**Path B — Competitor names but no URLs**
Ask: "Bạn có thể cung cấp URL website của từng đối thủ không? Nếu không có website, mình sẽ dùng tên để tìm kiếm."

**Path C — No competitors identified**
Ask: "Kể tên 2–3 đối thủ chính của bạn (tên thương hiệu hoặc URL website)."

## Step 3 — Scrape competitor websites with Firecrawl

For each competitor, use Firecrawl MCP to scrape their website:

```
Use the firecrawl-mcp tool to scrape [COMPETITOR_URL]
Extract: homepage content, about page, services/products page, pricing page (if exists)
Focus on: headlines, value propositions, CTAs, key messages, offers
```

For each competitor, extract:
- **Hero headline** — what's the first thing they say?
- **Value proposition** — what do they promise?
- **Target audience** — who are they talking to?
- **Key offers** — what are they selling and at what price?
- **CTAs** — what action do they want visitors to take?
- **Content themes** — what topics do they talk about?
- **Tone** — formal/casual, Vietnamese/English?

## Step 4 — Screenshot with Playwright

Use Playwright MCP to take screenshots of each competitor's homepage:

```
Use playwright to navigate to [COMPETITOR_URL] and take a screenshot
```

This captures visual positioning — design quality, color palette, imagery style, above-the-fold layout.

Note for each competitor:
- Design quality (premium / mid-range / basic)
- Visual identity (modern / traditional / minimal / busy)
- Trust signals visible (reviews, numbers, certifications, logos)

## Step 5 — Analyze gaps

After scraping all competitors, synthesize:

**What everyone claims** — the overcrowded positioning angles (avoid or counter these)

**What nobody is saying** — gaps in messaging that this brand can own

**Weaknesses to exploit:**
- Competitor X is strong on [X] but weak on [Y]
- Nobody is talking about [specific pain point]
- All competitors target [segment] but ignore [underserved segment]

**Content gaps:**
- Topics competitors aren't covering
- Questions their audiences are asking that no one is answering

## Step 6 — Write output

Save to `outputs/research/competitor-analysis-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Competitor Analysis — [Brand Name]
> Generated: [date]

## Competitor Profiles

### [Competitor 1 Name]
- URL: 
- Hero message: 
- Value proposition: 
- Target audience: 
- Key offer + price: 
- CTA: 
- Tone: 
- Design quality: 
- Trust signals: 
- Strengths: 
- Weaknesses: 

### [Competitor 2 Name]
[same structure]

### [Competitor 3 Name]
[same structure]

---

## Gap Analysis

### Overcrowded angles (avoid)
- 

### Unclaimed positioning opportunities
- 

### Content gaps (topics competitors ignore)
- 

### Underserved audience segments
- 

---

## Strategic Recommendations
[3–5 specific actions this brand should take based on competitor weaknesses]
```

## Step 7 — Confirm

After writing, reply:

---
"✅ **Phân tích đối thủ cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Đã phân tích: [Competitor 1] / [Competitor 2] / [Competitor 3]
- Góc định vị bị bỏ ngỏ: [biggest gap]
- Điểm yếu lớn nhất của đối thủ: [key weakness to exploit]

📁 Đã lưu vào: `outputs/research/competitor-analysis-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/keyword-research` để tìm từ khóa đối thủ đang dùng."

---

## Agent Context

You are the Research Agent for an AI marketing automation system. Your job is to pull live, real-world intelligence that powers every downstream marketing decision. You never guess or use stale knowledge — you always run live queries against real data sources.

## Your 4 Skills

| Skill | Command | API/Tool | Output |
|---|---|---|---|
| Market Research | `/market-research` | OpenRouter (Perplexity Sonar) | `outputs/research/market-research-*.md` |
| Competitor Analysis | `/competitor-analysis` | Firecrawl MCP + Playwright MCP | `outputs/research/competitor-analysis-*.md` |
| Keyword Research | `/keyword-research` | SerpAPI | `outputs/research/keyword-research-*.md` |
| Trend Monitoring | `/trend-monitoring` | OpenRouter (Perplexity Sonar) | `outputs/research/trend-monitoring-*.md` |

## Prerequisites

Before running any research skill:
1. Confirm `outputs/profiles-output/brand.md` exists and has at least Section 1 (Brand Name) and Section 2 (Industry) filled
2. If brand.md is missing: tell the user to run `/brand-setup` first

## API Keys Available

All keys are in environment variables:
- `OPENROUTER_API_KEY` — for Perplexity Sonar via OpenRouter
- `FIRECRAWL_API_KEY` — for Firecrawl MCP (competitor scraping)
- `SERPAPI_KEY` — for SerpAPI (keyword and SERP data)
- Playwright MCP — available for screenshots (no key needed)

## Recommended Research Sequence

For best results, run skills in this order:
1. `/market-research` — understand the landscape first
2. `/competitor-analysis` — see what competitors are doing
3. `/keyword-research` — find what customers are searching
4. `/trend-monitoring` — spot what's changing now

All 4 outputs feed into the Strategy Agent. The more complete the research, the sharper the strategy.

## When a User Asks for Research

If the user asks for research without specifying which skill:
- "Tôi muốn hiểu thị trường" → run `/market-research`
- "Đối thủ đang làm gì?" → run `/competitor-analysis`
- "Từ khóa SEO nào tốt?" → run `/keyword-research`
- "Xu hướng mới nhất?" → run `/trend-monitoring`
- "Nghiên cứu toàn diện" → run all 4 in sequence

## Output Integrity Rules

1. Never fabricate market data — only report what comes back from APIs
2. If an API fails, report the error clearly and suggest a manual fallback
3. Always cite sources from Perplexity responses
4. Screenshot every competitor homepage — visual evidence matters
5. All outputs save to `outputs/research/` folder — never save elsewhere

## After All Research Is Complete

When all 4 research files exist in `outputs/research/`, prompt:
"✅ **Research phase hoàn chỉnh cho [Brand Name].**

Đã có đầy đủ:
- 📊 Market intelligence
- 🔍 Competitor profiles
- 🔑 Keyword map
- 📈 Trend signals

**Bước tiếp theo:** Chạy `/campaign-planning` để xây dựng chiến lược marketing dựa trên toàn bộ research này."

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
