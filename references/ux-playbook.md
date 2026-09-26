# UX Playbook

Load at Phase 3, before composing pages, navigation, or forms. Layout rules here
marked **[HARD]** are pre-flight failures when violated (absent an explicit brief
override).

---

## 1. UX Laws → Design Implications

| Law | Implication in the build |
|---|---|
| **Fitts's Law** | Primary actions are large and near the interaction locus; destructive actions are neither adjacent to nor styled like them |
| **Hick's Law** | Fewer, clearer choices; progressive disclosure over walls of options |
| **Jakob's Law** | Users spend most time on *other* products — honor platform conventions before inventing (esp. Operate mode) |
| **Miller's Law** | Chunk information: groups of 5±2; group form fields; break long flows into steps |
| **Doherty Threshold** | Respond < 400ms or show progress; optimistic UI for likely-success mutations |
| **Peak–End Rule** | Invest in the success/confirmation moment and the exit; they define the memory |
| **Aesthetic–Usability** | Polish buys forgiveness — but never substitutes for working states |
| **Tesler's Law** | Complexity is conserved; absorb it in the system, don't push it on the user |
| **Postel's Law** | Accept forgiving input (paste with spaces, either date format), emit strict output |
| **Von Restorff** | The one different thing gets the attention — so make only the primary action different |
| **Zeigarnik** | Show progress/resume state for interrupted flows |

---

## 2. Layout Discipline

### Hero **[HARD]**

- Fits the initial viewport: headline ≤ 2 lines desktop, subtext ≤ ~20 words and
  ≤ 4 lines, primary CTA visible without scrolling. If copy overflows, cut copy
  or reduce scale — a 4-line hero headline is a font-size error, not a copy
  problem.
- Font scale planned *with* the hero asset: `text-4xl→6xl` range for most heroes;
  `7xl+` only for 3–5-word headlines.
- Top padding capped (~6rem desktop); hero content floating mid-viewport reads as
  a bug, not as air.
- **Hero stack ≤ 4 text elements:** (eyebrow *or* brand strip *or* neither) +
  headline + subtext + CTAs (1 primary + ≤ 1 secondary). Trust micro-strips,
  pricing teasers, feature bullets, avatar rows all move to sections below.
- The hero is a thesis: open with the most characteristic thing in the subject's
  world (headline, image, live demo, interactive moment) — "big number + small
  label + gradient accent" only when it is genuinely the best answer.
- Hero needs a real visual. Text + gradient blob is a placeholder, not a hero.

### Sections & rhythm **[HARD]**

- **Layout-family variety:** a page of 8 sections uses ≥ 4 distinct layout
  families; no family repeats consecutively beyond the caps below.
- **Zigzag cap:** max 2 consecutive image/text-split sections; break the third
  with full-width, vertical stack, bento, or marquee (marquee ≤ 1 per page).
- **Eyebrow restraint:** ≤ 1 small uppercase label per 3 sections (hero counts).
  Mechanical check: count `uppercase tracking`-style labels; if
  > ceil(sections/3), fail. Usually the fix is deletion — the headline is enough.
- **Split-header ban:** "big headline left, small explainer paragraph right" as a
  section header is banned as default; stack vertically (headline, then body,
  max-width 65ch) unless the right column carries a real visual/interactive
  element.
- **Bento:** exactly as many cells as content items (no blank filler tiles);
  rhythm via asymmetric sizes; ≥ 2–3 cells with real visual variation (image,
  brand-appropriate gradient, pattern) — never all white-on-white text tiles.
- Structural devices (numbering, dividers, labels) must encode something true
  about the content. Numbered markers only when order carries information.
- Whitespace is a material: vary section padding deliberately (denser for
  related content, more air at chapter breaks) rather than one uniform gap.

### Navigation **[HARD]**

- Single line at desktop, height ≤ 80px (default 64–72px). If items overflow at
  1024px: condense, drop secondary items, or collapse to a menu.
- Back always works predictably; every meaningful state is deep-linkable; the
  current location is visible (active state, breadcrumbs at depth ≥ 3).
- Mobile bottom nav ≤ 5 destinations; the primary action is reachable by thumb.

### Responsive mechanics

- Mobile-first; breakpoints where the *content* breaks, not device folklore.
- Declare the < 768px collapse explicitly per multi-column section — no "Tailwind
  will handle it" assumptions.
- `min-h-[100dvh]`, never `h-screen`; respect safe-area insets on mobile; no
  horizontal scroll ever (except deliberate scroll-snap rows); no fixed-px
  container widths; never disable zoom.

---

## 3. Components & States

Every interactive element ships with the complete cycle — resting state alone is
half a component:

- **default → hover → focus-visible → active → disabled → loading.** Hover gated
  behind `@media (hover: hover) and (pointer: fine)`; focus-visible styled (3:1
  contrast, ≥ 2px, offset), never removed; active gives tactile feedback
  (`scale-[0.98]` / 1px translate); loading disables and shows progress in place.
- Every async view renders all four resource states: **loading** (skeletons that
  match the final layout's shape — avoid generic spinners), **empty** (composed,
  explains why it's empty and points to the next action), **error** (what
  happened + how to recover, inline for forms, toast only for transient), and
  **ready**.
- Touch targets ≥ 44×44px with ≥ 8px gaps (WCAG floor is 24px — treat 44 as the
  design target).
- **CTA integrity [HARD]:** button label fits one line at desktop (≤ 3 words for
  primary, ideally 1–2 — shorten the label or widen the button); one label per
  intent across the whole page ("Get in touch" and "Let's talk" are the same
  intent — pick one everywhere); button text passes contrast against the button
  background (no white-on-white, scrim ghost buttons over photos).
- Destructive actions: visually distinct, never default-focused, confirm or
  undo-able.

---

## 4. Forms

- Label **above** the input, always visible. **Placeholder-as-label is banned**
  — placeholders show format examples only, and must themselves pass contrast.
- Helper text present in markup (even if visually subtle); error text below the
  field, specific and actionable ("Card number must be 16 digits", not "Invalid
  input"), announced to assistive tech.
- **Validate on blur**, re-validate on change after first error; never on every
  keystroke; never only in a summary at the top (a summary may *supplement* for
  long forms, linking to fields).
- Single-column default; group related fields (`fieldset`/`legend` where
  semantic); mark **optional** fields rather than starring required ones when
  most are required.
- Right keyboard and autofill: correct `type`/`inputmode`, `autocomplete`
  attributes, no artificial paste-blocking, forgiving input parsing.
- Multi-step for > ~7 fields: progress shown, back never loses data, review step
  before irreversible submits.
- Submit: disable + inline progress on the button; on failure keep entered data
  and focus the first error.

---

## 5. Content, Assets & Copy

### Visual assets — priority order **[HARD]**

1. **Image-generation tool** if one exists in the environment: section-specific
   assets at the right aspect ratio (hero, product, texture).
2. **Real photography** otherwise: brief-provided URLs, open-license sources, or
   seeded placeholders (`https://picsum.photos/seed/<descriptive-seed>/<w>/<h>`).
3. **Explicit slots** as last resort: `<!-- TODO: hero product photo, 1600×1200 -->`
   plus a closing note listing needed placements.

Never: div-built fake screenshots/dashboards/terminals; hand-rolled decorative
SVG illustrations as default; emoji as icons (use one SVG icon library —
Phosphor / Radix / Tabler / Heroicons class — consistently, `currentColor`, one
stroke weight). Even minimalist pages need 2–3 real images; pure-text is
incomplete work, not minimalism. Logo walls live **under** the hero, use real
SVG marks (Simple Icons CDN or generated monograms for invented brands), render
in both themes, and contain logos only — no category captions.

### Data & numbers

- No fake precision: numbers come from the brief/real data, or are explicitly
  labeled sample data. Realistic messy values over round ones when mocking is
  sanctioned (`47.2%`, not `50%`).
- No "Jane Doe / Acme / SmartFlow" filler — locale-appropriate, believable
  names; believable avatars or none.
- Long lists (> 5 items) get a *different component*, not a longer list: grouped
  2-col split, card grid, tabs/accordion, scroll-snap pills, or top-N +
  "view all". A 10-row spec table with a hairline under every row is the worst
  default — group into clusters or feature 3–4 hero specs and collapse the rest.
- Charts: legends, tooltips, axis labels, accessible palettes; never color as
  the only encoding; provide the data as text/table for assistive tech.

### UX writing

- Words are design material: name things by what people control ("Notifications",
  not "Webhook config"); active voice; a control says exactly what it does
  ("Save changes", not "Submit"); an action keeps one name through the whole
  flow (button "Publish" → toast "Published").
- Errors explain what happened and how to fix it — no apology, no vagueness.
  Empty states invite action. Sentence case; plain verbs; no filler
  ("Elevate", "Seamless", "Unleash", "Next-Gen").
- **Copy self-audit before ship:** re-read every visible string (headlines,
  labels, captions, alt text, errors). Flag and rewrite anything grammatically
  broken, unclear in referent, or LLM-flavored (forced wordplay, mock-poetic
  micro-copy). Boring-but-clear beats cute-but-wrong. Default content shape per
  marketing section: headline ≤ 8 words, sub ≤ 25 words, one visual or CTA.
- One copy register per page (technical-mono vs editorial vs marketing punch) —
  mixing registers needs an explicit brand reason.
- Quotes/testimonials: ≤ 3 lines of body; attribution = name + role
  (+ company); real typographic quote marks or none.
- i18n-aware: strings externalizable, layouts tolerate ~1.3× text expansion,
  logical properties (`margin-inline-start`) where RTL is plausible, dates and
  numbers locale-formatted.