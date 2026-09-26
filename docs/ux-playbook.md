# UX Playbook — Reference

Load at Phase 3. Layout rules marked **[HARD]** are pre-flight failures when violated (absent explicit brief override).

---

## 1. UX Laws → Design Implications

| Law | Build Implication |
|-----|-------------------|
| **Fitts's Law** | Primary actions large & near interaction locus; destructive actions neither adjacent nor styled like them |
| **Hick's Law** | Fewer, clearer choices; progressive disclosure over walls of options |
| **Jakob's Law** | Users spend most time on *other* products — honor platform conventions (esp. Operate mode) |
| **Miller's Law** | Chunk info: groups of 5±2; group form fields; break long flows into steps |
| **Doherty Threshold** | Respond < 400ms or show progress; optimistic UI for likely-success mutations |
| **Peak–End Rule** | Invest in success/confirmation moment and exit — they define memory |
| **Aesthetic–Usability** | Polish buys forgiveness — never substitutes for working states |
| **Tesler's Law** | Complexity conserved; absorb in system, don't push to user |
| **Postel's Law** | Accept forgiving input (paste with spaces, either date format), emit strict output |
| **Von Restorff** | The one different thing gets attention — make only primary action different |
| **Zeigarnik** | Show progress/resume state for interrupted flows |

---

## 2. Layout Discipline

### Hero **[HARD]**

- Fits initial viewport: headline ≤ 2 lines desktop, subtext ≤ ~20 words/4 lines, primary CTA visible without scroll
- Font scale planned *with* hero asset: `text-4xl→6xl` for most; `7xl+` only for 3-5 word headlines
- Top padding capped (~6rem desktop); hero floating mid-viewport = bug, not air
- **Hero stack ≤ 4 text elements:** (eyebrow *or* brand strip *or* neither) + headline + subtext + CTAs (1 primary + ≤ 1 secondary)
- Hero is a thesis: open with most characteristic thing in subject's world (headline, image, live demo, interactive moment)
- Hero needs real visual — text + gradient blob = placeholder, not hero

### Sections & Rhythm **[HARD]**

- **Layout-family variety:** 8 sections → ≥ 4 distinct families; no consecutive repeats beyond caps
- **Zigzag cap:** max 2 consecutive image/text-split; break 3rd with full-width, vertical stack, bento, or marquee (≤ 1/page)
- **Eyebrow restraint:** ≤ 1 uppercase label per 3 sections (hero counts); count `uppercase tracking` labels
- **Split-header ban:** "big headline left, small paragraph right" banned as default; stack vertically unless right column has real visual/interactive
- **Bento:** cell count = content count (no blank tiles); rhythm via asymmetric sizes; ≥ 2-3 cells visually varied
- Structural devices (numbering, dividers, labels) must encode truth about content
- Whitespace is material: vary section padding deliberately (denser for related, more air at chapter breaks)

### Navigation **[HARD]**

- Single line desktop, height ≤ 80px (default 64-72px); condense/drop/collapse if overflow at 1024px
- Back always works; every meaningful state deep-linkable; current location visible (active state, breadcrumbs at depth ≥ 3)
- Mobile bottom nav ≤ 5 destinations; primary action thumb-reachable

### Responsive Mechanics

- Mobile-first; breakpoints where *content* breaks, not device folklore
- Declare < 768px collapse explicitly per multi-column section
- `min-h-[100dvh]`, never `h-screen`; respect safe-area insets; no horizontal scroll (except deliberate scroll-snap); no fixed-px containers; never disable zoom

---

## 3. Components & States

**Every interactive element ships complete cycle** — resting state alone = half component:

```
default → hover → focus-visible → active → disabled → loading
```

- Hover gated: `@media (hover: hover) and (pointer: fine)`
- Focus-visible: styled (3:1 contrast, ≥ 2px, offset), **never removed**
- Active: tactile (`scale-[0.98]` / 1px translate)
- Loading: disables + shows progress in place

**Every async view renders all four resource states:**

| State | Requirements |
|-------|--------------|
| **Loading** | Skeletons matching final layout shape (not generic spinners) |
| **Empty** | Composed, explains why empty, points to next action |
| **Error** | What happened + how to recover (inline for forms, toast for transient) |
| **Ready** | Actual content |

- Touch targets ≥ 44×44px with ≥ 8px gaps (WCAG floor 24px — design to 44px)
- **CTA integrity [HARD]:** button label fits one line desktop (≤ 3 words primary, ideally 1-2); one label per intent page-wide; button text passes contrast vs button bg
- Destructive actions: visually distinct, never default-focused, confirm or undo-able

---

## 4. Forms

- Label **above** input, always visible. **Placeholder-as-label banned** — placeholders show format only, must pass contrast
- Helper text in markup (even if subtle); error text below field, specific + actionable ("Card number must be 16 digits"), announced to AT
- **Validate on blur**, re-validate on change after first error; never every keystroke; never only top summary (may supplement for long forms, linking to fields)
- Single-column default; group related fields (`fieldset`/`legend`); mark **optional** not required when most required
- Right keyboard/autofill: correct `type`/`inputmode`, `autocomplete`, no paste-blocking, forgiving parsing
- Multi-step for > ~7 fields: progress shown, back never loses data, review step before irreversible submits
- Submit: disable + inline progress on button; on failure keep data + focus first error

---

## 5. Content, Assets & Copy

### Visual Assets — Priority Order **[HARD]**

1. **Image-generation tool** (section-specific, right aspect ratio)
2. **Real photography** (brief URLs, open-license, seeded `picsum.photos/seed/<desc>/<w>/<h>`)
3. **Explicit slots** (last resort): `<!-- TODO: hero product photo, 1600×1200 -->` + closing note

**Never:** div-fake screenshots/dashboards/terminals; hand-rolled decorative SVG as default; emoji as icons (one SVG library — Phosphor/Radix/Tabler/Heroicons — consistently, `currentColor`, one stroke weight). Minimalist pages need 2-3 real images; pure-text = incomplete, not minimalism. Logo walls **under** hero, real SVG marks (Simple Icons CDN or generated monograms), both themes, logos only — no captions.

### Data & Numbers

- No fake precision: from brief/real data or explicitly labeled sample data; realistic messy values (`47.2%` not `50%`)
- No "Jane Doe / Acme / SmartFlow" filler — locale-appropriate believable names/avatars
- Long lists (> 5 items) → different component (2-col split, card grid, tabs, scroll-snap pills, top-N + "view all"); 10-row hairline table = worst default
- Charts: legends, tooltips, axis labels, accessible palettes; never color as only encoding; data as text/table for AT

### UX Writing

- Name by what people control ("Notifications" not "Webhook config"); active voice; control says exactly what it does ("Save changes" not "Submit"); action keeps one name through flow (button "Publish" → toast "Published")
- Errors: what happened + how to fix (no apology, no vagueness); empty states invite action; sentence case; plain verbs; no filler ("Elevate", "Seamless", "Unleash", "Next-Gen")
- **Copy self-audit before ship:** re-read every visible string; flag grammatically broken, unclear referent, LLM-flavored (forced wordplay, mock-poetic micro-copy); boring-but-clear > cute-but-wrong
- Default marketing section: headline ≤ 8 words, sub ≤ 25 words, one visual or CTA
- One copy register per page (technical-mono vs editorial vs marketing) — mixing needs brand reason
- Quotes/testimonials: ≤ 3 lines body; attribution = name + role (+ company); real quote marks or none
- i18n-aware: strings externalizable, layouts tolerate ~1.3× expansion, logical properties (`margin-inline-start`) for RTL, locale-formatted dates/numbers