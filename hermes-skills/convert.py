#!/usr/bin/env python3
"""Convert the Claude Code marketing system (.claude/agents + .claude/commands)
into Hermes Agent skills (marketing/<skill>/SKILL.md).

Hermes standard (v0.22.x, agentskills.io):
- SKILL.md frontmatter: name (<=64, lowercase-hyphens), description (<=60 chars),
  version, author, license, platforms, metadata.hermes.{tags,related_skills},
  required_environment_variables.
- Body sections: When to Use / Prerequisites / Procedure / Pitfalls / Verification.
- Long descriptions & agent routing context live in the body, not frontmatter.
"""
import re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_COMMANDS = ROOT / ".claude" / "commands"
SRC_AGENTS = ROOT / ".claude" / "agents"
OUT = Path(__file__).resolve().parent / "marketing"
SCHEMA_SRC = SRC_COMMANDS / "01-brand-foundation" / "references" / "brand-md-schema.md"

# category dir -> (hermes prefix, agent file, tags, short descriptions per skill)
CATEGORIES = {
    "01-brand-foundation": ("brand", "agent-01-brand-foundation.md", ["Marketing", "Brand"]),
    "02-research": ("research", "agent-02-research.md", ["Marketing", "Research"]),
    "03-strategy": ("strategy", "agent-03-strategy.md", ["Marketing", "Strategy"]),
    "04-cro": ("cro", "agent-04-cro.md", ["Marketing", "CRO"]),
    "05-content": ("content", "agent-05-content.md", ["Marketing", "Content"]),
    "06-seo": ("seo", "agent-06-seo.md", ["Marketing", "SEO"]),
    "07-email": ("email", "agent-07-email.md", ["Marketing", "Email"]),
    "08-social": ("social", "agent-08-social.md", ["Marketing", "Social"]),
    "09-ads": ("ads", "agent-09-ads.md", ["Marketing", "Ads"]),
    "10-video-creative": ("video", "agent-10-video-creative.md", ["Marketing", "Video"]),
    "11-cold-outreach": ("outreach", "agent-11-cold-outreach.md", ["Marketing", "Outreach"]),
    "12-sales": ("sales", "agent-12-sales.md", ["Marketing", "Sales"]),
    "13-distribution": ("distribution", "agent-13-distribution.md", ["Marketing", "Distribution"]),
    "14-performance": ("performance", "agent-14-performance.md", ["Marketing", "Performance"]),
    "15-feedback": ("feedback", "agent-15-feedback.md", ["Marketing", "Feedback"]),
}

SHORT = {  # <=60 chars, capability only, ends with period
    "brand-setup": "Build a complete 12-section brand.md profile.",
    "brand-voice": "Define brand voice, tone, and writing style.",
    "audience-profile": "Build target audience and ICP profiles.",
    "positioning": "Define market positioning and core offer.",
    "usp-definition": "Define USP, unique mechanism, key messages.",
    "market-research": "Run live market research via Perplexity.",
    "competitor-analysis": "Analyze competitor sites, offers, messaging.",
    "keyword-research": "Research keywords and SERP demand via SerpAPI.",
    "trend-monitoring": "Monitor market and content trends live.",
    "campaign-planning": "Plan a full marketing campaign end to end.",
    "content-calendar": "Build a scheduled multi-channel content calendar.",
    "lead-magnet": "Design lead magnets that capture contacts.",
    "campaign-brief": "Write a complete campaign brief document.",
    "offer-positioning": "Position an offer for maximum conversion.",
    "lp-builder": "Build high-converting landing page copy.",
    "cta-optimization": "Optimize calls to action for conversion.",
    "ab-test-setup": "Set up structured A/B tests for pages.",
    "page-audit": "Audit a page for conversion weaknesses.",
    "sales-page": "Write long-form sales page copy.",
    "content-brief": "Write briefs that guide content production.",
    "blog-writer": "Write publish-ready SEO blog posts.",
    "case-study-writer": "Write customer case studies with proof.",
    "website-copy": "Write website copy in brand voice.",
    "thought-leadership": "Write thought-leadership content pieces.",
    "on-page-seo": "Optimize a page for on-page SEO ranking.",
    "local-seo": "Optimize presence for local search results.",
    "schema-markup": "Generate schema.org structured data markup.",
    "technical-seo-audit": "Audit technical SEO issues on a site.",
    "link-building-strategy": "Plan a white-hat link building strategy.",
    "email-sequence": "Write multi-email nurture and sales sequences.",
    "newsletter": "Write newsletters subscribers actually open.",
    "subject-line-ab": "Generate and A/B test email subject lines.",
    "re-engagement": "Write re-engagement campaigns for cold lists.",
    "transactional-email": "Write clear transactional email copy.",
    "social-copy": "Write social media posts per platform.",
    "social-creative": "Brief social creative and visual concepts.",
    "hashtag-research": "Research hashtags for reach and relevance.",
    "social-calendar": "Build a social media posting calendar.",
    "community-management": "Plan community replies and engagement.",
    "video-script": "Write short and long-form video scripts.",
    "ad-creative": "Brief ad creative concepts and visuals.",
    "ad-copy": "Write paid ad copy for Meta and Google.",
    "audience-targeting": "Define paid ad audience targeting sets.",
    "ad-campaign-structure": "Structure ad campaigns and ad sets.",
    "google-pmax-brief": "Brief Google Performance Max campaigns.",
    "creative-brief": "Write creative briefs for designers.",
    "branded-deck": "Outline branded presentation decks.",
    "ugc-script": "Write UGC-style video ad scripts.",
    "cold-email": "Write cold outreach emails that reply.",
    "linkedin-dm": "Write LinkedIn DM outreach sequences.",
    "follow-up-sequence": "Write follow-up sequences for outreach.",
    "objection-handler": "Write replies that handle sales objections.",
    "personalization-framework": "Build outreach personalization frameworks.",
    "proposal-writer": "Write client proposals that win deals.",
    "testimonial-framework": "Collect and frame customer testimonials.",
    "case-study": "Write sales case studies with proof.",
    "content-atomizer": "Atomize one asset into many formats.",
    "platform-formatter": "Reformat content for each platform.",
    "press-release": "Write press releases for media pickup.",
    "podcast-pitch": "Write podcast guest pitch emails.",
    "partnership-brief": "Write partnership outreach briefs.",
    "campaign-report": "Build end-of-campaign performance reports.",
    "weekly-report": "Build weekly marketing performance reports.",
    "roi-calculator": "Calculate marketing ROI from campaign data.",
    "data-visualization": "Plan charts and dashboards for reports.",
    "monthly-strategy-review": "Run monthly strategy review from data.",
    "audience-update": "Update audience profile from real data.",
    "messaging-refinement": "Refine messaging from performance data.",
    "positioning-evolution": "Evolve positioning from market feedback.",
    "marketing-orchestrator": "Route marketing work across all skills.",
}
# disambiguate same base names across categories
PREFIX_FIX = {
    ("06-seo", "keyword-research"): "seo-keyword-research",
    ("08-social", "video-script"): "social-video-script",
    ("10-video-creative", "video-script"): "video-script",
    ("12-sales", "sales-page"): "sales-page-writer",
    ("04-cro", "sales-page"): "cro-sales-page",
    ("04-cro", "ab-test-setup"): "cro-ab-test-setup",
    ("09-ads", "ab-test-setup"): "ads-ab-test-setup",
    ("12-sales", "objection-handler"): "sales-objection-handler",
    ("11-cold-outreach", "objection-handler"): "outreach-objection-handler",
    ("12-sales", "case-study"): "sales-case-study",
    ("05-content", "case-study-writer"): "case-study-writer",
    ("14-performance", "monthly-strategy-review"): "performance-monthly-review",
    ("15-feedback", "monthly-strategy-review"): "feedback-monthly-review",
    ("10-video-creative", "creative-brief"): "video-creative-brief",
    ("05-content", "content-brief"): "content-brief",
}

ENV_RESEARCH = """required_environment_variables:
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
"""
ENV_BY_PREFIX = {"research": ENV_RESEARCH, "seo": ENV_RESEARCH}

PATH_FIXES = [
    (r"/outputs/profiles-output/brand\.md", "outputs/profiles-output/brand.md"),
    (r"/profiles-output/brand\.md", "outputs/profiles-output/brand.md"),
    (r"/profiles/brand\.md", "outputs/profiles-output/brand.md"),
    (r"profiles-output/brand\.md", "outputs/profiles-output/brand.md"),
    (r"\.claude/commands/[A-Za-z0-9_/-]*references/brand-md-schema\.md", "references/brand-md-schema.md"),
    (r"\.claude/commands/brand-foundation/references/brand-md-schema\.md", "references/brand-md-schema.md"),
    (r"(?<![\w/.])/outputs/", "outputs/"),
    (r"(?<![\w/.])/(research|strategy|assets|distribution|performance)/", r"outputs/\1/"),
    (r"outputs/+outputs/", "outputs/"),
    (r"outputsoutputs/", "outputs/"),
    (r"Claude Code", "Hermes Agent"),
    (r"the Agent tool", "the skill_view tool"),
    (r"Use the Agent tool to launch[^.]*\.", "Load the matching Hermes skill with skill_view."),
]

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return "", text.strip()
    return m.group(1), m.group(2).strip()

def fm_field(fm, field):
    m = re.search(rf'^{field}:\s*"?((?:[^"\\]|\\.)*)"?\s*$', fm, re.M)
    if not m:
        m2 = re.search(rf"^{field}:\s*'([^']*)'", fm, re.M)
        return m2.group(1).strip() if m2 else ""
    return m.group(1).replace('\\n', ' ').replace('\\"', '"').strip()

def clean_body(body):
    body = re.sub(r"<example>.*?</example>", "", body, flags=re.S)
    body = re.sub(r"<commentary>.*?</commentary>", "", body, flags=re.S)
    for pat, rep in PATH_FIXES:
        body = re.sub(pat, rep, body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()

def first_heading(body):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else ""

def strip_first_heading(body):
    return re.sub(r"^#\s+.+\n+", "", body, count=1).strip()

def agent_context(agent_file):
    if not agent_file or not agent_file.exists():
        return ""
    _, body = split_frontmatter(agent_file.read_text(encoding="utf-8"))
    body = clean_body(strip_first_heading(body))
    # keep agent context lean: cap at ~6000 chars, cut at a heading boundary
    if len(body) > 6000:
        cut = body.rfind("\n## ", 0, 6000)
        body = body[: cut if cut > 2000 else 6000].rstrip() + "\n\n*(Full agent spec: see the marketing-orchestrator skill and sibling skills in this category.)*"
    return body

def when_to_use(full_desc, short):
    d = (full_desc or short).strip()
    if len(d) > len(short) + 10 and d != short:
        return f"{d}\n\nSlash command: load this skill and follow its Procedure. Short summary: {short}"
    return short

def build_skill(name, short, full_desc, tags, related, env, body, agent_ctx, title):
    fm = [
        "---",
        f"name: {name}",
        f'description: "{short}"',
        "version: 1.0.0",
        "author: Henry Le, Hermes Agent",
        "license: MIT",
        "platforms: [linux, macos, windows]",
        "metadata:",
        "  hermes:",
        f"    tags: [{', '.join(tags)}]",
    ]
    if related:
        fm.append(f"    related_skills: [{', '.join(related)}]")
    if env:
        fm.append(env.rstrip())
    fm.append("---")
    parts = ["\n".join(fm), "", f"# {title}", ""]
    parts.append("Part of the AI Marketing Agent Team (Hermes edition) — a 15-category marketing "
                 "system for Vietnamese businesses. Every skill reads `outputs/profiles-output/brand.md` "
                 "first; if it is missing, load the `brand-setup` skill before doing anything else.")
    parts += ["", "## When to Use", "", when_to_use(full_desc, short), ""]
    parts += ["## Procedure", "", body, ""]
    if agent_ctx:
        parts += ["## Agent Context", "", agent_ctx, ""]
    parts += ["## Pitfalls", "",
              "- Never run an execution skill before `outputs/profiles-output/brand.md` exists — route to `brand-setup` first.",
              "- All outputs land under `outputs/` for human review. The system proposes; the human decides.",
              "- Speak Vietnamese to Vietnamese users, English to English users.", ""]
    parts += ["## Verification", "",
              "- Confirm the output file exists at its documented `outputs/...` path.",
              "- Confirm it follows the brand voice, audience, and key messages in `brand.md`.", ""]
    return "\n".join(parts).rstrip() + "\n"

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    created, related_map = [], {}

    # pass 1: collect names per category
    cat_skills = {}
    for cat, (prefix, agent_file, tags) in CATEGORIES.items():
        names = []
        for f in sorted((SRC_COMMANDS / cat).glob("*.md")):
            base = re.sub(r"^\d+-", "", f.stem)
            name = PREFIX_FIX.get((cat, base), base)
            name = re.sub(r"[^a-z0-9-]", "-", name.lower()).strip("-")[:64]
            names.append((name, f))
        cat_skills[cat] = names
        related_map[cat] = [n for n, _ in names]

    for cat, (prefix, agent_file, tags) in CATEGORIES.items():
        agent_ctx = agent_context(SRC_AGENTS / agent_file)
        related = related_map[cat] + (["marketing-orchestrator"] if cat != "01-brand-foundation" else [])
        for name, f in cat_skills[cat]:
            raw = f.read_text(encoding="utf-8")
            fm, body = split_frontmatter(raw)
            full_desc = fm_field(fm, "description") or SHORT.get(name, "")
            body = clean_body(body)
            title = first_heading(body) or name.replace("-", " ").title()
            body = strip_first_heading(body)
            short = SHORT.get(name) or SHORT.get(re.sub(r"^(seo|social|cro|ads|sales|outreach|video|performance|feedback)-", "", name), "Run this marketing skill.")
            assert len(short) <= 60, (name, len(short), short)
            env = ENV_BY_PREFIX.get(prefix, "")
            skill_dir = OUT / name
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                build_skill(name, short, full_desc, tags, related, env, body, agent_ctx, title),
                encoding="utf-8")
            created.append(name)

    # brand-md schema as reference of brand-setup (+ brand skills)
    if SCHEMA_SRC.exists():
        for s in ["brand-setup", "brand-voice", "audience-profile", "positioning", "usp-definition"]:
            ref = OUT / s / "references"
            ref.mkdir(exist_ok=True)
            shutil.copy(SCHEMA_SRC, ref / "brand-md-schema.md")

    # orchestrator skill
    raw = (SRC_AGENTS / "orchestrator.md").read_text(encoding="utf-8")
    fm, body = split_frontmatter(raw)
    body = clean_body(strip_first_heading(body))
    odir = OUT / "marketing-orchestrator"
    odir.mkdir(parents=True)
    (odir / "SKILL.md").write_text(
        build_skill("marketing-orchestrator", SHORT["marketing-orchestrator"],
                    fm_field(fm, "description"), ["Marketing", "Orchestrator"],
                    sorted(set(related_map["01-brand-foundation"] + related_map["03-strategy"])),
                    "", body, "", "Marketing Orchestrator"),
        encoding="utf-8")
    created.append("marketing-orchestrator")

    print(f"Created {len(created)} Hermes skills in {OUT}")
    for n in sorted(created):
        print(" -", n)

if __name__ == "__main__":
    main()
