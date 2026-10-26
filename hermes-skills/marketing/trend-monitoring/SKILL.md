---
name: trend-monitoring
description: "Monitor market and content trends live."
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

# Trend Monitoring Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Monitors emerging trends in the Vietnamese market using Perplexity via OpenRouter. Use this skill when the user wants to stay ahead of industry shifts, spot what's gaining momentum, or find timely content angles. Trigger whenever the user mentions trend monitoring, what's trending, emerging topics, or staying current in their industry.

Slash command: load this skill and follow its Procedure. Short summary: Monitor market and content trends live.

## Procedure

Your job is to surface emerging signals in this industry — trends that are gaining momentum now, before they're obvious to everyone. Not 2023 trend reports. Live intelligence that this brand can act on this week.

## Step 1 — Read brand.md

Read `outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Target audience (Section 6)
- Location
- Content pillars (Section 12) — to align trend findings with existing strategy

If brand.md doesn't exist: ask the user for their industry before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a trend focus**
Use their focus. Go to Step 3.

**Path B — No focus provided**
Ask:
"Bạn muốn mình theo dõi xu hướng theo góc độ nào?
1. Xu hướng ngành và thị trường (industry trends)
2. Xu hướng hành vi người dùng và khách hàng (consumer behavior)
3. Xu hướng nội dung và marketing (content/marketing trends)
4. Tất cả (full trend scan)"

Wait for answer before continuing.

## Step 3 — Run trend research via OpenRouter

Use the `OPENROUTER_API_KEY` environment variable. Make POST requests to OpenRouter:

```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json
```

Run 3 separate queries:

### Query 1 — Industry trend scan
```json
{
  "model": "perplexity/sonar",
  "messages": [{
    "role": "user",
    "content": "What are the most significant emerging trends in the [INDUSTRY] industry in Vietnam in 2025? Focus on: new behaviors, shifts in how customers buy, new platforms or channels gaining traction, regulatory changes, and technology shifts that are just starting to impact this space. Include specific examples and data where available. Be specific to Vietnam — not global trends unless they're landing in Vietnam now."
  }]
}
```

### Query 2 — Consumer behavior shifts
```json
{
  "model": "perplexity/sonar",
  "messages": [{
    "role": "user",
    "content": "What's changing in how Vietnamese [TARGET_AUDIENCE] customers make decisions and consume content in 2025? Specifically: which platforms are growing, what content formats are winning, how has their trust and skepticism evolved, and what anxieties or aspirations are most prominent right now? Give me fresh insights — not evergreen advice."
  }]
}
```

### Query 3 — Content and marketing trend scan
```json
{
  "model": "perplexity/sonar",
  "messages": [{
    "role": "user",
    "content": "What content formats and marketing approaches are gaining momentum for [BUSINESS_TYPE] businesses in Vietnam in 2025? Which tactics are losing effectiveness? What's working on Facebook, TikTok, and Zalo right now? Give specific examples of brands or campaigns that are cutting through."
  }]
}
```

Replace `[INDUSTRY]`, `[TARGET_AUDIENCE]`, `[BUSINESS_TYPE]` with values from brand.md.

## Step 4 — Classify and prioritize trends

For each trend found, classify by:

**Urgency:**
- 🔴 **Act now** — trend is peaking, window closing fast
- 🟡 **Build toward** — trend is growing, 3–6 month runway
- 🟢 **Watch** — early signal, not yet actionable

**Relevance to this brand:**
- Direct: core to their business model or audience
- Adjacent: affects their customers but indirectly
- Background: macro shift to be aware of

**Content opportunity:**
- Is there a specific piece of content this trend enables?
- Can this brand be one of the first to comment on it?

## Step 5 — Generate content angle ideas

For each high-priority trend, suggest 1–2 specific content angles this brand can publish within the next 2 weeks:

Format: "[Trend] → [Content piece title] → [Platform] → [Why it will resonate]"

Example:
"AI tools adoption by SMBs → 'Bạn thực sự cần AI để làm marketing không?' → Facebook/Zalo → SMB owners are curious but skeptical — this question headline triggers clicks"

## Step 6 — Write output

Save to `outputs/research/trend-monitoring-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Trend Monitoring — [Brand Name]
> Generated: [date] | Industry: [industry] | Market: Vietnam

## High-Priority Trends (Act Now)
🔴 **[Trend name]**
- What's happening: [2–3 sentences]
- Why it matters for this brand: [1–2 sentences]
- Content angle: [specific piece to publish]
- Platform: [Facebook / TikTok / Zalo / Blog]

[Repeat for each 🔴 trend]

---

## Growing Trends (Build Toward)
🟡 **[Trend name]**
- What's happening:
- Runway: [timeframe]
- Strategic implication:

[Repeat for each 🟡 trend]

---

## Watch List
🟢 **[Trend name]** — [one-line summary]
[Repeat]

---

## 2-Week Content Calendar (Trend-Driven)
Content pieces to publish immediately based on these trends:
1. **[Piece title]** — Platform: [X] — Trend: [X] — Goal: [awareness / leads / trust]
2. ...
3. ...

---

## What's Losing Momentum
Tactics and topics to de-prioritize:
- [Tactic] — Why: [reason]
- [Topic] — Why: [reason]

---

## Sources
[Sources from Perplexity responses]
```

## Step 7 — Confirm

After writing, reply:

---
"✅ **Trend monitoring cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Xu hướng cần hành động ngay: [count] trends
- Góc nội dung hàng đầu: [top content angle]
- Xu hướng đang giảm: [what to stop doing]

📁 Đã lưu vào: `outputs/research/trend-monitoring-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/campaign-planning` để xây dựng chiến lược dựa trên research vừa hoàn thành."

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
