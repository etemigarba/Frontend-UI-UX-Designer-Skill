# Design Direction

Load at Phase 1. This file covers choosing an aesthetic direction, typography,
color, and the anti-default discipline that keeps output from converging on the
generic AI look. The brief always outranks anything here.

---

## 1. Direction Families (rotate — never reuse consecutively)

Pick **one** family, name it in the direction plan, and justify it against the
brief. Each entry: feel / typical palette logic / typical type logic.

| Family | Feel | Palette logic | Type logic |
|---|---|---|---|
| **Bold Minimalism** | Confident restraint; precision is the decoration | Off-white + off-black + one saturated accent | Grotesque display (tight tracking) + neutral body |
| **Editorial / Publication** | Magazine authority, typographic hierarchy | Paper neutrals, ink text, restrained accent | Justified only when genuinely editorial: display serif + text serif or sans |
| **Neo-Brutalist** | Raw, structural, honest | High contrast, unmixed primaries, hard borders | Mono or condensed grotesque, visible grid |
| **Industrial / Utilitarian** | Tool-like, data-forward, console energy | Graphite scale + one signal color (amber/green) | Mono for data, compact sans for UI |
| **Soft Depth** | Tactile, layered, calm (glass/soft-shadow, used sparingly) | Low-chroma base, translucent surfaces, gentle elevation | Rounded or humanist sans |
| **Cold Luxury** | Silver, chrome, smoke; premium without warmth | Silver-grey + near-black + cool highlight | Extended/wide sans display, precise tracking |
| **Forest Heritage** | Outdoors premium, durable | Deep green + bone + amber accent | Sturdy slab or grotesque |
| **Black & Tan** | Sharp warm-contrast premium, no beige | True off-black + warm tan | High-contrast sans display |
| **Cobalt & Cream** | One saturated blue against a single neutral | Cobalt + cream, no third color | Geometric sans |
| **Terracotta & Slate** | Warm rust against cool grey | Terracotta accent + slate neutrals | Humanist sans, generous leading |
| **Playful Geometric** | Energetic, shape-driven, consumer | 2–3 brights on neutral field, chunky radii (locked) | Rounded display + friendly body |
| **Retro-Futurist** | Period-specific optimism, executed precisely | Era-accurate palette (research it) | Era-accurate faces, modern spacing |
| **Data-Dense Console** | Operator-grade density (Operate mode) | Dark graphite, semantic status colors only | Mono numerals, compact sans labels |
| **Organic / Natural** | Textural, imperfect-on-purpose | Earth tones with one clarifying neutral | Humanist faces, looser rhythm |

Rotation rule: if the previous comparable project used a family, this one uses a
different one unless the brief pins it.

---

## 2. Saturated Defaults (fail the anti-default test on sight)

These are the looks AI-generated design collapses into. Legitimate when the brief
asks for them; failures when chosen by reflex.

- **Warm-cream + display-serif + terracotta/clay accent** — the default "premium"
  reach (backgrounds in the `#f5f1ea`–`#efeae0` band, brass/clay/oxblood accents,
  espresso near-black text). Banned as a default for premium-consumer briefs;
  choose from the rotation table instead. Note the terracotta band near `#D97757`
  is also Anthropic's own accent — on a user's brief it reads as a tell.
- **Near-black + single acid-green or vermilion accent** — the default "edgy dark"
  reach.
- **Broadsheet layout: hairline rules, radius-0, dense columns** — the default
  "editorial" reach.
- **AI-purple/violet glow, purple→blue gradients, neon outer glows** — banned as
  defaults; embrace only when the brand explicitly owns purple, and then execute
  with a harmonized palette, not gradient slop.
- **Centered hero + three equal feature cards + gradient blob** — the default
  layout reach; see the layout rules in the UX playbook.

Override path for all of the above: an explicit brief instruction, stated in the
direction plan.

---

## 3. Typography

### Pairing logic

- **Two families maximum** (display + body), plus an optional utility/mono for
  data and captions. Every additional family must earn its place.
- The display face carries the personality; use it with restraint (hero, section
  heads). The body face is a workhorse: excellent at 14–18px, tall x-height,
  full weight range.
- **Emphasis inside a headline** uses italic or bold of the *same* family. Never
  inject a serif word into a sans headline (or vice versa) for visual interest.

### Face selection discipline

- **Inter is discouraged as the default choice** — not because it is bad, but
  because it is the reflex. Reach first for characterful workhorses (e.g. Geist,
  Outfit, Satoshi, Cabinet Grotesk, PP Neue Montreal, GT Walsheim, IBM Plex
  family, Söhne-class grotesques). Inter is the right answer when the brief asks
  for neutral/systematic (Linear-style) or accessibility-first public-sector work.
- **Serif discipline:** serif display is *not* the automatic answer to "creative /
  premium / editorial." Use serif only when the brief names one, or the direction
  is genuinely editorial/luxury/heritage *and* you can articulate why this serif
  fits this brand. Rotate serifs across projects; do not reuse the same one twice
  in a row, and treat the two current LLM-favorite display serifs (Fraunces,
  Instrument Serif) as banned-as-default.
- Variable fonts preferred; subset and preload the display face.

### Setting type

- **Scale:** modular ratio 1.2 (dense/Operate) to 1.333 (expressive/Persuade),
  base 16px. Fluid display sizes via
  `clamp(min, preferred-vw-based, max)`.
- **Leading:** body 1.5–1.7; headings 1.1–1.2; display can hit 1.0 *unless* an
  italic word contains a descender (`g j p q y`) — then minimum 1.1 plus a small
  bottom reserve, or descenders clip.
- **Tracking:** slightly negative on large display (−0.01 to −0.03em); slightly
  positive on small caps/labels (+0.05 to +0.1em); never letterspace lowercase
  body.
- **Measure:** 45–75 characters (`max-width: 65ch` is the workhorse). Body text
  never below 16px; captions never below 12px.
- Real typographic quotes (“ ”) or none. Use `text-wrap: balance` on headings and
  `text-wrap: pretty` on body where supported.

---

## 4. Color

### System

- **60-30-10:** dominant neutral field, secondary surface tone, one accent.
- **One accent, locked.** Once chosen, it is the accent for every section — the
  CTA in section 7 does not switch hue, the footer badge does not go teal.
- **Neutrals have a temperature.** Choose warm or cool greys once per project and
  never mix scales. Pure `#808080`-family greys read dead; tint toward the accent
  hue by 2–5%.
- Build in a perceptual space (**OKLCH**) so light/dark variants keep consistent
  perceived lightness and chroma; derive hover/active as lightness steps, not
  opacity hacks.
- Saturation < 80% by default; a fully saturated accent must be a stated choice.
- **Status colors are semantic tokens** (success/warning/destructive/info), used
  only for status — never as decoration, and never the only carrier of meaning.

### Contrast (measured, not eyeballed)

- Body text 4.5:1; large text (≥ 24px, or ≥ 18.7px bold) 3:1; UI component
  boundaries and focus indicators 3:1 — in **both** themes.
- Audit the classic failure points: text on accent buttons, ghost buttons over
  imagery (add scrim/backdrop/stroke), placeholder text, helper/error text,
  disabled states (exempt from AA but keep ≥ 3:1 where feasible).

### Dark mode protocol

- Designed at Phase 2, not bolted on. It is a token swap with **hierarchy
  parity** (what pops in light pops in dark) and **brand fidelity** (the accent
  stays recognizable — usually desaturate slightly and raise lightness rather
  than reuse the light-mode value).
- No pure `#000000` or `#ffffff` — off-black (zinc-950-class) and off-white keep
  depth. Elevation in dark mode = *lighter* surface, not heavier shadow.
- One theme per page (Theme Lock): sections never invert mid-scroll. The only
  exception is one deliberate full-theme color-block moment, brief-justified.
- Default to `prefers-color-scheme`; add a manual toggle when either mode loses
  brand expression. Test both modes before finishing — never ship a page seen in
  only one.

---

## 5. Materiality, Shadows, Depth

- Cards only when elevation communicates real hierarchy; otherwise group with
  borders (`border-t`, `divide-y`) or negative space. Dense data breathes better
  in plain layout than in card chrome.
- Shadows tinted toward the background hue; layered small shadows over one big
  black blur. On dark themes, prefer surface-lightening to shadows.
- **Shape Consistency Lock:** one radius system per page — all-sharp, all-soft
  (12–16px), or all-pill for interactive — or a documented mixed rule applied
  everywhere. Round buttons in a square layout is broken design.
- Decorative texture (grain/noise) only on a fixed, `pointer-events-none`
  overlay, never on scrolling containers (continuous repaints kill mobile FPS).

---

## 6. The Signature Element

Every memorable interface has one thing it is remembered by: a type treatment, an
interaction, a layout device, a data visualization, an illustration system.
Choose it deliberately in the direction plan, spend the boldness budget on it,
and keep everything around it quiet. Before shipping, apply the reverse test:
look at the page and remove one decoration (Chanel's rule). Not taking any risk
is itself a risk — a competent-but-anonymous page fails a Persuade brief.

---

## 7. Anti-Default Test (run before leaving Phase 1)

For each of {palette, display face, hero layout, section rhythm, signature}:

1. Simulate the generic answer: "what would any model produce for a brief in this
   category?"
2. If your plan matches it, that element is a default. Replace it or justify it
   from the brief, in writing, in the direction plan.
3. Confirm the plan's elements agree with each other (temperature, radius
   system, copy register) — distinctiveness with internal consistency, not
   novelty scatter.