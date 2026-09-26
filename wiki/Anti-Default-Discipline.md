# Anti-Default Discipline

The single biggest failure mode in AI-generated design is producing the design any model would produce for any similar brief. This skill enforces **anti-default discipline** at every phase.

---

## The Anti-Default Test

**Run before leaving Phase 1.** For each of {palette, display face, hero layout, section rhythm, signature element}:

1. **Simulate the generic answer:** "What would any model produce for a brief in this category?"
2. **If your plan matches it, that element is a default.** Replace it or justify it from the brief, in writing, in the direction plan.
3. **Confirm the plan's elements agree with each other** (temperature, radius system, copy register) — distinctiveness with internal consistency, not novelty scatter.

---

## Saturated Defaults (Fail on Sight)

These are the looks AI-generated design collapses into. Legitimate when the brief asks for them; failures when chosen by reflex.

### 1. Warm-Cream + Display-Serif + Terracotta/Clay Accent
- **The default "premium" reach**
- Backgrounds in `#f5f1ea`–`#efeae0` band
- Brass/clay/oxblood accents
- Espresso near-black text
- **Banned as default for premium-consumer briefs** — choose from rotation table instead
- **Note:** Terracotta band near `#D97757` is also Anthropic's own accent — on a user's brief it reads as a tell

### 2. Near-Black + Single Acid-Green or Vermilion Accent
- **The default "edgy dark" reach**

### 3. Broadsheet Layout
- Hairline rules, radius-0, dense columns
- **The default "editorial" reach**

### 4. AI-Purple/Violet Glow
- Purple→blue gradients, neon outer glows
- **Banned as defaults** — embrace only when brand explicitly owns purple, then execute with harmonized palette

### 5. Centered Hero + Three Equal Feature Cards + Gradient Blob
- **The default layout reach** — see layout rules in UX playbook

---

## Direction Families (Rotate — Never Reuse Consecutively)

Pick **one** family, name it in the direction plan, and justify it against the brief.

| Family | Feel | Palette Logic | Type Logic |
|--------|------|---------------|------------|
| **Bold Minimalism** | Confident restraint; precision is decoration | Off-white + off-black + one saturated accent | Grotesque display (tight tracking) + neutral body |
| **Editorial / Publication** | Magazine authority, typographic hierarchy | Paper neutrals, ink text, restrained accent | Display serif + text serif or sans (justified only when genuinely editorial) |
| **Neo-Brutalist** | Raw, structural, honest | High contrast, unmixed primaries, hard borders | Mono or condensed grotesque, visible grid |
| **Industrial / Utilitarian** | Tool-like, data-forward, console energy | Graphite scale + one signal color (amber/green) | Mono for data, compact sans for UI |
| **Soft Depth** | Tactile, layered, calm (glass/soft-shadow) | Low-chroma base, translucent surfaces, gentle elevation | Rounded or humanist sans |
| **Cold Luxury** | Silver, chrome, smoke; premium without warmth | Silver-grey + near-black + cool highlight | Extended/wide sans display, precise tracking |
| **Forest Heritage** | Outdoors premium, durable | Deep green + bone + amber accent | Sturdy slab or grotesque |
| **Black & Tan** | Sharp warm-contrast premium, no beige | True off-black + warm tan | High-contrast sans display |
| **Cobalt & Cream** | One saturated blue against single neutral | Cobalt + cream, no third color | Geometric sans |
| **Terracotta & Slate** | Warm rust against cool grey | Terracotta accent + slate neutrals | Humanist sans, generous leading |
| **Playful Geometric** | Energetic, shape-driven, consumer | 2–3 brights on neutral field, chunky radii (locked) | Rounded display + friendly body |
| **Retro-Futurist** | Period-specific optimism, executed precisely | Era-accurate palette (research it) | Era-accurate faces, modern spacing |
| **Data-Dense Console** | Operator-grade density (Operate mode) | Dark graphite, semantic status colors only | Mono numerals, compact sans labels |
| **Organic / Natural** | Textural, imperfect-on-purpose | Earth tones with one clarifying neutral | Humanist faces, looser rhythm |

**Rotation rule:** If the previous comparable project used a family, this one uses a different one unless the brief pins it.

---

## Typography Discipline

### Face Selection

- **Inter is discouraged as the default choice** — not because it's bad, but because it's the reflex
- Reach first for characterful workhorses: Geist, Outfit, Satoshi, Cabinet Grotesk, PP Neue Montreal, GT Walsheim, IBM Plex family, Söhne-class grotesques
- **Serif discipline:** Serif display is *not* the automatic answer to "creative/premium/editorial"
  - Use serif only when brief names one, or direction is genuinely editorial/luxury/heritage *and* you can articulate why this serif fits this brand
  - Rotate serifs across projects; do not reuse the same one twice in a row
  - Treat Fraunces and Instrument Serif as banned-as-default

### Pairing Logic

- **Two families maximum** (display + body), plus optional utility/mono
- Every additional family must earn its place
- Display face = personality (hero, section heads); use with restraint
- Body face = workhorse (excellent at 14–18px, tall x-height, full weight range)
- Emphasis inside headline uses italic/bold of *same* family — never inject serif into sans (or vice versa) for visual interest

---

## Color Discipline

- **60-30-10:** Dominant neutral field, secondary surface tone, one accent
- **One accent, locked** — same hue everywhere; CTA in section 7 ≠ teal
- **Neutrals have temperature** — warm OR cool greys, never mixed; tint toward accent by 2–5%
- **OKLCH preferred** — light/dark variants keep perceived lightness/chroma
- **Saturation < 80%** default; full saturation = stated choice
- **Status colors = semantic tokens only** — never decoration, never sole meaning carrier

---

## Layout Discipline

- **Hero:** Headline ≤ 2 lines, subtext ≤ 20 words, CTA above fold
- **Hero stack ≤ 4 text elements** — no trust-strips/taglines/pricing inside hero
- **Hero needs real visual** — text + gradient blob = placeholder, not hero
- **Layout-family variety:** 8 sections → ≥ 4 distinct families
- **Zigzag cap:** max 2 consecutive image/text-split
- **Eyebrow restraint:** ≤ 1 uppercase label per 3 sections
- **Split-header ban:** "big headline left, small paragraph right" banned as default
- **Bento:** cell count = content count; ≥ 2-3 cells visually varied

---

## Component Discipline

- **Complete state sets** — no interactive element ships with only resting state
- **Complete resource states** — no async view without loading/empty/error/ready
- **CTA integrity:** Button label fits one line at desktop; one label per intent page-wide
- **Forms:** Label above input; placeholder-as-label banned; errors specific, inline, below field
- **Touch targets ≥ 44×44px** with ≥ 8px gaps

---

## Motion Discipline

- **Delight scales inversely with frequency** — rare moments can carry personality; high-frequency = near invisible
- **Never animate keyboard-initiated actions**
- **No motion on mount without user trigger** (except 1 deliberate entrance)
- **One motion language per artifact** — consistent durations, easings, physics
- **`transform`/`opacity` only** — `transition: all` banned
- **Every animation has reduced-motion path**

---

## Content Discipline

- **No fabricated precision** — numbers from brief/real data or explicitly labeled sample data
- **No "Jane Doe / Acme / SmartFlow" filler** — locale-appropriate believable names
- **No div-built fake screenshots/dashboards/terminals**
- **No emoji as icons** — one SVG icon library consistently
- **No AI-tell filler copy** ("Elevate", "Seamless", "Unleash", "Next-Gen")
- **Copy self-audit before ship** — re-read every visible string

---

## Verification Discipline

- **Evidence-based, never asserted** — screenshots, measurements, tool output
- **Deviations documented with brief justification** — silent deviations = failed audit
- **Max 2 fix passes** — no open-ended self-QA
- **Honest report** — unticked boxes reported with reasons

---

## Summary: The Anti-Default Mindset

> "Not taking any risk is itself a risk — a competent-but-anonymous page fails a Persuade brief."

Every choice must be:
1. **Deliberate** — you can articulate why
2. **Justified** — from the brief or design reasoning
3. **Distinctive** — passes the anti-default test
4. **Consistent** — agrees with other choices (temperature, radius, copy register)