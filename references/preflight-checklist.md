# Pre-Flight Checklist — The Termination Gate

Load at Phase 5. This is the loop's exit condition. Run the mechanical checks
first (cheap, objective), then the full checklist. **If a single box cannot be
honestly ticked, the work is not done** — fix it, or report the specific box and
the reason to the user. Brief-justified deviations are legitimate; silent ones
are not. Maximum two fix passes, then ship with an honest report.

---

## 1. Mechanical checks (grep/measure — no judgment required)

Run these against the diff/output; each hit is a finding:

```
transition: all                     → banned; list properties explicitly
transition/animate on width|height|top|left  → layout-prop animation (exception: deliberate resize tween)
outline: none | outline-none        → allowed only with a replacement :focus-visible style present
#[0-9a-fA-F]{3,8} in components     → raw hex outside the token file
h-screen                            → replace with min-h-[100dvh]
addEventListener('scroll'           → use IntersectionObserver / scroll-driven APIs
z-(40|50|\[.*\]) ad hoc             → outside the documented z-index scale
uppercase tracking labels           → count ≤ ceil(sectionCount / 3)
<img without width/height|aspect    → CLS risk; reserve space
placeholder= used as the only label → banned
```

Then measure: contrast at the failure-prone spots (buttons, ghost buttons over
imagery, placeholders, helper/error text) in **both** themes; tab through every
primary flow; emulate `prefers-reduced-motion`; screenshot desktop + mobile ×
light + dark if browser tooling exists.

---

## 2. Full checklist

### Identity & consistency
- [ ] Design Read (Phase 0) declared; dials explicit and reasoned, not defaulted
- [ ] Direction plan exists; anti-default test passed or brief-overridden
- [ ] **Theme Lock:** one theme for the whole page; no section inverts mid-scroll
- [ ] **Accent Lock:** one accent used identically across every section
- [ ] **Radius Lock:** one corner-radius system (or documented mixed rule) everywhere
- [ ] One copy register; one icon library, one stroke weight
- [ ] Signature element present; boldness spent once; one decoration removed on review

### Layout & hero
- [ ] Hero fits the viewport: headline ≤ 2 lines, subtext ≤ 20 words, CTA above the fold
- [ ] Hero stack ≤ 4 text elements; no trust-strips/taglines/pricing inside the hero
- [ ] Hero has a real visual (not text + gradient blob)
- [ ] Nav on one line at desktop, ≤ 80px tall
- [ ] ≥ 4 layout families across the page; zigzag ≤ 2 consecutive; marquee ≤ 1
- [ ] Eyebrow count within cap; no split-header pattern as default
- [ ] Bento: cell count = content count; 2–3 cells visually varied
- [ ] Mobile collapse explicit per section; no horizontal scroll; safe areas respected

### Type & color
- [ ] ≤ 2 families (+ optional utility); pairing justified; not the reflex default
- [ ] Body ≥ 16px, measure ≤ 75ch, leading in range; italic descenders clear
- [ ] Contrast AA at every audited spot, both themes; no pure #000/#fff
- [ ] Dark mode: tokens defined, hierarchy parity, tested in both modes

### Components, states & forms
- [ ] Every interactive element: default/hover/focus-visible/active/disabled/loading
- [ ] Every async view: loading (layout-matched skeleton)/empty/error/ready
- [ ] Focus visible everywhere; keyboard completes every primary flow; modals trap + return focus
- [ ] Touch targets ≥ 44px with spacing; hover-only paths eliminated
- [ ] CTAs: one line at desktop; one label per intent page-wide; contrast passes
- [ ] Forms: label above; no placeholder-as-label; errors specific, below field, announced; validate on blur

### Content & copy
- [ ] Real/generated/slotted images per priority order; zero div-fake screenshots; zero emoji-as-icons
- [ ] Logo wall (if any) under hero, real SVG marks, logos only, both themes
- [ ] No fabricated precision; sample data labeled; no Jane Doe / Acme filler
- [ ] Copy self-audit done: every visible string re-read; no broken or LLM-flavored phrases; no filler verbs
- [ ] Long lists use an appropriate component (not a 10-row hairline table)
- [ ] Quotes ≤ 3 lines; attribution complete

### Motion
- [ ] Every animation justified in one sentence (feedback/orientation/continuity/delight)
- [ ] transform/opacity only; no `transition: all`; durations/easings from the token set
- [ ] Paired states and paired elements share timing; entrances from scale ≥ 0.85, origin at trigger
- [ ] Reduced-motion path verified for everything; hover gated behind `(hover: hover)`
- [ ] No mount animation without trigger (beyond one deliberate entrance); no scroll-hijack; loops pause off-screen; `will-change` transient
- [ ] Interruption tested: rapid retoggles retarget smoothly

### Accessibility (full pass = accessibility.md §5)
- [ ] Automated sweep clean (axe/Lighthouse) — and the four manual passes done
- [ ] Landmarks + one h1 + ordered headings; skip link; `lang` set
- [ ] Alt text policy applied; status messages announced; drag has a non-drag path
- [ ] 200% zoom and 320px reflow hold

### Performance
- [ ] LCP < 2.5s plausible: hero media prioritized/preloaded, modern formats, sized
- [ ] CLS < 0.1: dimensions reserved for images/fonts/embeds; `font-display: swap` + subset + preload
- [ ] INP < 200ms: heavy work off the main thread; below-fold lazy-loaded; heavy libs code-split
- [ ] Lighthouse (or equivalent) actually run when tooling exists — score observed, not asserted

### Process honesty
- [ ] Verification evidence is real (screenshots/measurements/tool output), never asserted
- [ ] Deviations from this skill listed with their brief justification
- [ ] Fix passes ≤ 2; remaining known issues reported, not hidden