---
name: market-research
description: "Run live market research via Perplexity."
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

# Market Research Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Conducts live market research for a Vietnamese business using Perplexity via OpenRouter. Use this skill when the user wants to understand their market size, industry trends, customer behavior, or competitive landscape in Vietnam. Trigger whenever the user mentions market research, industry analysis, market size, or wants to understand their market.

Slash command: load this skill and follow its Procedure. Short summary: Run live market research via Perplexity.

## Procedure

Your job is to pull live, specific market intelligence for this business — not generic industry overviews, but data that directly informs their marketing and positioning decisions.

## Step 1 — Read brand.md

Read `outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Location (city/region)
- Target audience
- Competitors already identified

If brand.md doesn't exist: ask the user for their industry and location before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a research focus**
Use their focus. Go to Step 3.

**Path B — No focus provided**
Ask:
"Bạn muốn mình tập trung vào khía cạnh nào của thị trường?
1. Quy mô và tăng trưởng thị trường (market size + growth)
2. Hành vi khách hàng (customer behavior + trends)
3. Cơ hội thị trường (gaps + opportunities)
4. Tất cả (full market overview)"

Wait for answer before continuing.

## Step 3 — Run market research via OpenRouter

Make a POST request to OpenRouter using the Perplexity Sonar model:

```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json

{
  "model": "perplexity/sonar",
  "messages": [
    {
      "role": "user",
      "content": "Research the [INDUSTRY] market in Vietnam in 2024-2025. Provide: 1) Market size and growth rate with specific numbers, 2) Key customer segments and their behaviors, 3) Major trends shaping the industry, 4) Market gaps and opportunities for [BUSINESS TYPE] targeting [TARGET AUDIENCE]. Focus on Vietnam specifically — Ho Chi Minh City and Hanoi if relevant. Include specific statistics, growth rates, and actionable insights."
    }
  ]
}
```

Replace `[INDUSTRY]`, `[BUSINESS TYPE]`, `[TARGET AUDIENCE]` with values from brand.md.

Run 2 separate queries:
1. **Market size + trends query** — broad industry overview
2. **Customer behavior query** — specific to their target audience in Vietnam

## Step 4 — Synthesize and structure findings

From the API responses, extract and organize:

**Market Overview:**
- Market size (USD or VND)
- Growth rate (CAGR or YoY)
- Key market drivers
- Vietnam-specific dynamics

**Customer Insights:**
- How Vietnamese customers in this segment make buying decisions
- Online vs. offline behavior
- Platform preferences (Facebook, TikTok, Zalo, etc.)
- Price sensitivity and spending patterns

**Market Opportunities:**
- Gaps no one is filling well
- Underserved segments
- Emerging trends to ride early
- Geographic opportunities (HCMC vs Hanoi vs other cities)

**Threats & Risks:**
- Market saturation risks
- Regulatory or economic risks
- Competitor momentum

## Step 5 — Write output

Save findings to `outputs/research/market-research-[Mon-DD-YYYY].md` using this structure:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Market Research — [Brand Name]
> Generated: [date] | Industry: [industry] | Market: Vietnam

## Market Overview
[size, growth, drivers]

## Customer Behavior
[how they buy, where they are, what they care about]

## Opportunities
[specific gaps and trends]

## Threats
[risks to watch]

## Key Data Points
[bullet list of most important stats to reference in content/strategy]

## Sources
[list sources from Perplexity response]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Market research cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Quy mô thị trường: [market size]
- Tăng trưởng: [growth rate]
- Cơ hội lớn nhất: [top opportunity]
- Rủi ro cần chú ý: [top risk]

📁 Đã lưu vào: `outputs/research/market-research-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/competitor-analysis` để phân tích đối thủ cụ thể."

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
