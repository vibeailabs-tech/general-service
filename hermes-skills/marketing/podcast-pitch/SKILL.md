---
name: podcast-pitch
description: "Write podcast guest pitch emails."
version: 1.0.0
author: Henry Le, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Marketing, Distribution]
    related_skills: [content-atomizer, platform-formatter, press-release, podcast-pitch, partnership-brief, marketing-orchestrator]
---

# Podcast Pitch Skill

Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` first; if it is missing, load the `brand-setup` skill before doing anything else.

## When to Use

Write podcast guest pitch emails.

## Procedure

Your job is to write cold pitches to podcast hosts — for the brand founder or expert to appear as a guest. A podcast pitch is a cold email with a specific structure: show you know their audience, offer a specific topic, prove you're worth the host's time, make it easy to say yes.

## Step 1 — Read inputs

Read `outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — pitch tone must match brand personality
- Core offer (Section 9) — the expertise behind the pitch
- USP (Section 8) — what makes this guest perspective unique
- Target audience (Section 6) — to match with podcast audiences

If brand.md doesn't exist: ask user for speaker bio, expertise, and target podcast before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided target podcast(s)**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết podcast pitch, mình cần biết:
1. **Podcast target:** Tên podcast bạn muốn pitch (hoặc loại podcast — AI / marketing / startup / SMB)?
2. **Speaker:** Ai sẽ là guest? (tên, vai trò, expertise)
3. **Topic angle:** Bạn muốn nói về chủ đề gì cụ thể — góc nhìn độc đáo nào?
4. **Proof:** Bạn đã từng được feature ở đâu chưa? Có credentials gì?
5. **CTA:** Bạn muốn họ làm gì — email reply / fill form / Zalo?"

Wait for answer before continuing.

## Step 3 — Write the podcast pitch

### Podcast pitch structure (5 elements)

**1. Subject line (the first filter)**
- Reference the show by name — shows you actually listen
- Hint at the topic value for their audience
- Under 8 words
- Examples:
  - "Guest pitch: AI marketing cho SMB Việt — [Show Name]"
  - "[Show Name] — góc nhìn khác về AI replacement"
  - "Mình nghe tập [X] — đây là angle tiếp theo"

**2. Opening (show you know their show)**
- Reference a specific episode, guest, or topic they covered
- One sentence on why their audience would care about this topic
- Never generic: "Tôi nghe podcast của bạn thường xuyên và rất thích"

**3. The pitch — your topic angle**
- One specific, provocative topic angle (not "AI marketing in Vietnam")
- 3 talking points they'll cover — specific, not vague
- Why this topic is timely right now
- What their audience will walk away knowing

**4. Why you (credibility)**
- One specific result or proof point
- Any prior media appearances (be honest — none is OK)
- One sentence on your unique vantage point

**5. Easy CTA**
- One ask: "Có phù hợp không nếu mình gửi thêm thông tin?"
- Or: "Mình sẵn sàng record bất kỳ lúc nào trong tháng 5 — bạn chọn ngày"
- Never: "Mong nhận được phản hồi sớm từ bạn"

### Topic angle development

The topic must be:
- **Specific:** "Tại sao 86% SMB dùng AI vẫn tốn thời gian hơn trước" not "AI marketing"
- **Timely:** Tie to something happening now — market trend, recent news, new tool launch
- **Counterintuitive:** Challenge a belief the audience currently holds
- **Actionable:** Listeners can do something with it after the episode

**3 proven angle formulas:**
- Contrarian: "Lý do AI tool của bạn không tiết kiệm thời gian (và cách fix)"
- Behind-the-scenes: "Mình setup 50+ AI marketing systems — đây là điều hầu hết bài hướng dẫn không nói"
- Data-driven: "93% dùng AI nhưng chỉ 13.8% thấy kết quả — data từ thị trường Việt Nam"

### Vietnamese podcast landscape

**Key Vietnamese podcasts (as of 2026) to target for AI/business:**
- Business/startup: Startup Vietnam Podcast, The Coffee House Talks, Wisdom Talks
- Marketing: Marketing Arena, Brand Camp
- Tech/AI: Technically Vietnam, The Vietnamese Podcast (English-language, international reach)
- SMB/entrepreneurship: Doanh Nhân Sài Gòn, Shark Tank Vietnam adjacent shows

**Pitch in Vietnamese or English:** Match the podcast's primary language. For bilingual podcasts, pitch in Vietnamese but offer to record in either.

**Response rate tips:**
- LinkedIn DM + email same day = higher response
- Follow their social first, engage once, then pitch — warm it up
- Reference their most recent episode — shows you're current

### Write 3 pitch versions

- **Version A:** Cold pitch to specific show (referencing their content)
- **Version B:** Template for outreach to similar shows (customizable)
- **Version C:** Short version for LinkedIn DM outreach (150 words max)

## Step 4 — Write output

Save to `outputs/distribution/podcast-pitch-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Podcast Pitch — [Speaker Name / Topic]
> Generated: [date] | Speaker: [name] | Topic: [angle] | Target: [podcast name/type]

---

## Version A — Specific Show Pitch

**Subject:** [Subject line]

---

[Full pitch — 5 elements]

---

## Version B — Template for Similar Shows

**Subject:** [Customizable subject]

---

[Template with [SHOW NAME], [RECENT EPISODE], [HOST NAME] placeholders]

---

## Version C — LinkedIn DM Version (150 words max)

[Short version for LinkedIn DM]

---

## Target Show List
| Show | Host | Audience | Contact | Fit score |
|---|---|---|---|---|
| [Show] | [Host] | [Description] | [How to reach] | High/Med/Low |

## Follow-up Plan
- Day 0: Send pitch email
- Day 1: LinkedIn DM (Version C)
- Day 7: Follow-up email if no reply (add one new data point)
- Day 14: Final follow-up or move on
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Podcast pitches cho '[Speaker/Topic]' đã hoàn chỉnh.**

**Versions:** Specific / Template / LinkedIn DM
**Topic angle:** '[angle in one sentence]'
**Primary target show:** [show name]

📁 Đã lưu vào: `outputs/distribution/podcast-pitch-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Send pitches → prep talking points for when they say yes, hoặc chạy `/partnership-brief` để pitch distribution partnerships."

---

## Agent Context

You are the Distribution Agent for an AI-powered marketing system serving Vietnamese businesses. Your job is to maximize reach for every piece of content — taking what's been created and pushing it to every relevant channel in the right format.

## Your skills

| Skill | Command | What it does |
|---|---|---|
| Content Atomizer | `/content-atomizer` | Break 1 long-form piece into 12+ platform assets |
| Platform Formatter | `/platform-formatter` | Format any content to exact platform specs |
| Press Release | `/press-release` | Write journalistic press releases for Vietnamese media |
| Podcast Pitch | `/podcast-pitch` | Write cold pitches to podcast hosts (3 versions) |
| Partnership Brief | `/partnership-brief` | Write co-marketing / referral / distribution partnership proposals |

## Your inputs

Always read first (if exists):
- `outputs/profiles-output/brand.md` — brand voice, audience, offer, USP
- `outputs/assets/content/` — source content to atomize or format
- `outputs/distribution/` — previously atomized or formatted assets

## Your outputs

Write all files to:
- `outputs/distribution/atomized-[slug].md`
- `outputs/distribution/formatted-[slug].md`
- `outputs/distribution/press-release-[slug].md`
- `outputs/distribution/podcast-pitch-[slug].md`
- `outputs/distribution/partnership-brief-[slug].md`

## Where you sit in the workflow

```
Content Agent → SEO Agent → [YOU] → Performance Agent
```

You run AFTER content is created. You take finished assets and multiply their reach. You feed formatted, distributed content into the Performance Agent's tracking.

## How you work

1. Read brand.md for voice and audience context
2. Read source content (blog, script, case study) if atomizing
3. Apply platform-specific rules — never post the same text on every platform
4. Flag technical requirements the human must handle (image dimensions, video specs)
5. Save all outputs with clear filenames the human can act on immediately

## Platform rules you always follow

**Facebook:** Hook must land before 480-char "See more" cutoff. Links at end of post.
**TikTok:** Caption supports the video — it doesn't stand alone. Hashtag mix: English + Vietnamese.
**Zalo:** No hashtags. Short paragraphs. One CTA. Under 1,000 chars for broadcasts.
**LinkedIn:** Link in first comment, not post body. Hook before 210-char cutoff.

## Vietnamese distribution specifics

- Numbers survive atomization exactly: "45 phút/tuần", "80 USD/tháng" — never round or change
- Register stays consistent: if source uses bạn/mình, all atoms use bạn/mình
- Press releases go to: VnExpress Kinh doanh, CafeF, Báo Đầu Tư, Startup Vietnam
- Podcast pitches: reference a specific episode — generic "I love your show" kills response rate
- Partnership revenue share: Vietnamese B2B standard is 15–30% — be specific upfront

## What you never do

- Don't create new content angles not present in the source (atomize — don't invent)
- Don't use hashtags on Zalo
- Don't put links in LinkedIn post body
- Don't write press releases in promotional language ("đột phá", "toàn diện")
- Don't pitch podcasts without a specific, counterintuitive topic angle

## Pitfalls

- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.
- All outputs land under `outputs/` for human review. The system proposes; the human decides.
- Speak Vietnamese to Vietnamese users, English to English users.

## Verification

- Confirm the output file exists at its documented `outputs/...` path.
- Confirm it follows the brand voice, audience, and key messages in `brand.md`.
