# Pre-Flight Checklist — Termination Gate

Load at Phase 5. This is the loop's exit condition. Run mechanical checks first (cheap, objective), then full checklist. **If a single box cannot be honestly ticked, the work is not done** — fix it, or report the specific box and reason. Brief-justified deviations are legitimate; silent ones are not. Maximum two fix passes, then ship with honest report.

---

## 1. Mechanical Checks (grep/measure — no judgment required)

Run against diff/output; each hit = finding:

```bash
# Banned patterns
grep -r "transition: all"                                    # → list properties explicitly
grep -rE "transition.*(width|height|top|left)"              # → layout-prop animation (exception: deliberate resize tween)
grep -rE "outline:\s*none|outline-none"                     # → allowed only with replacement :focus-visible style
grep -rE "#[0-9a-fA-F]{3,8}" --include="*.tsx" --include="*.vue" --include="*.svelte" --include="*.jsx"  # → raw hex outside token file
grep -r "h-screen"                                           # → replace with min-h-[100dvh]
grep -r "addEventListener.*scroll"                           # → use IntersectionObserver / scroll-driven APIs
grep -rE "z-(40|50|\[.*\])"                                 # → outside documented z-index scale
grep -r "uppercase.*tracking"                                # → count ≤ ceil(sectionCount / 3)
grep -r '<img' --include="*.html" --include="*.tsx" --include="*.vue" --include="*.svelte" | grep -vE "width|height|aspect"  # → CLS risk; reserve space
grep -r 'placeholder=' --include="*.tsx" --include="*.vue" --include="*.svelte" | grep -v 'placeholder.*label'  # → placeholder-as-label banned
```

**Then measure:**
- Contrast at failure-prone spots (buttons, ghost buttons over imagery, placeholders, helper/error text) in **both** themes
- Tab through every primary flow
- Emulate `prefers-reduced-motion`
- Screenshot desktop + mobile × light + dark (if browser tooling exists)

---

## 2. Full Checklist

### Identity & Consistency
- [ ] Design Read (Phase 0) declared; dials explicit and reasoned, not defaulted
- [ ] Direction plan exists; anti-default test passed or brief-overridden
- [ ] **Theme Lock:** one theme for whole page; no section inverts mid-scroll
- [ ] **Accent Lock:** one accent used identically across every section
- [ ] **Radius Lock:** one corner-radius system (or documented mixed rule) everywhere
- [ ] One copy register; one icon library, one stroke weight
- [ ] Signature element present; boldness spent once; one decoration removed on review

### Layout & Hero
- [ ] Hero fits viewport: headline ≤ 2 lines, subtext ≤ 20 words, CTA above fold
- [ ] Hero stack ≤ 4 text elements; no trust-strips/taglines/pricing inside hero
- [ ] Hero has real visual (not text + gradient blob)
- [ ] Nav on one line at desktop, ≤ 80px tall
- [ ] ≥ 4 layout families across page; zigzag ≤ 2 consecutive; marquee ≤ 1
- [ ] Eyebrow count within cap; no split-header pattern as default
- [ ] Bento: cell count = content count; 2–3 cells visually varied
- [ ] Mobile collapse explicit per section; no horizontal scroll; safe areas respected

### Type & Color
- [ ] ≤ 2 families (+ optional utility); pairing justified; not reflex default
- [ ] Body ≥ 16px, measure ≤ 75ch, leading in range; italic descenders clear
- [ ] Contrast AA at every audited spot, both themes; no pure #000/#fff
- [ ] Dark mode: tokens defined, hierarchy parity, tested in both modes

### Components, States & Forms
- [ ] Every interactive element: default/hover/focus-visible/active/disabled/loading
- [ ] Every async view: loading (layout-matched skeleton)/empty/error/ready
- [ ] Focus visible everywhere; keyboard completes every primary flow; modals trap + return focus
- [ ] Touch targets ≥ 44px with spacing; hover-only paths eliminated
- [ ] CTAs: one line at desktop; one label per intent page-wide; contrast passes
- [ ] Forms: label above; no placeholder-as-label; errors specific, below field, announced; validate on blur

### Content & Copy
- [ ] Real/generated/slotted images per priority order; zero div-fake screenshots; zero emoji-as-icons
- [ ] Logo wall (if any) under hero, real SVG marks, logos only, both themes
- [ ] No fabricated precision; sample data labeled; no Jane Doe / Acme filler
- [ ] Copy self-audit done: every visible string re-read; no broken or LLM-flavored phrases; no filler verbs
- [ ] Long lists use appropriate component (not 10-row hairline table)
- [ ] Quotes ≤ 3 lines; attribution complete

### Motion
- [ ] Every animation justified in one sentence (feedback/orientation/continuity/delight)
- [ ] transform/opacity only; no `transition: all`; durations/easings from token set
- [ ] Paired states and paired elements share timing; entrances from scale ≥ 0.85, origin at trigger
- [ ] Reduced-motion path verified for everything; hover gated behind `(hover: hover)`
- [ ] No mount animation without trigger (beyond one deliberate entrance); no scroll-hijack; loops pause off-screen; `will-change` transient
- [ ] Interruption tested: rapid retoggles retarget smoothly

### Accessibility (full pass = accessibility.md §5)
- [ ] Automated sweep clean (axe/Lighthouse) — and the four manual passes done
- [ ] Landmarks + one h1 + ordered headings; skip link; `lang` set
- [ ] Alt text policy applied; status messages announced; drag has non-drag path
- [ ] 200% zoom and 320px reflow hold

### Performance
- [ ] LCP < 2.5s plausible: hero media prioritized/preloaded, modern formats, sized
- [ ] CLS < 0.1: dimensions reserved for images/fonts/embeds; `font-display: swap` + subset + preload
- [ ] INP < 200ms: heavy work off main thread; below-fold lazy-loaded; heavy libs code-split
- [ ] Lighthouse (or equivalent) actually run when tooling exists — score observed, not asserted

### Process Honesty
- [ ] Verification evidence is real (screenshots/measurements/tool output), never asserted
- [ ] Deviations from this skill listed with their brief justification
- [ ] Fix passes ≤ 2; remaining known issues reported, not hidden

---

## Fix Pass Protocol

| Pass | Action | Trigger |
|------|--------|---------|
| **1** | Fix ALL mechanical + checklist findings in one batch | After first full verification |
| **2** | Fix remaining issues from pass 1 | After re-verification of pass 1 fixes |
| **STOP** | Ship with honest report of any unticked boxes | After pass 2 (ceiling for entire cycle) |

**No open-ended self-QA.** Two passes max for the whole cycle.

---

## Deviation Reporting

For any checklist item that cannot be ticked:

```markdown
## Deviation Report

| Checklist Item | Reason | Brief Justification |
|----------------|--------|---------------------|
| Hero has real visual | Client has no product photography yet; brief explicitly states "use placeholder" | Brief: "No assets available — use branded placeholder pattern" |
| Motion intensity M8 | Brief requests "highly animated, playful feel" for Experience mode portfolio | Brief: "Experience mode with high motion — choreographed scroll narrative" |
```

**Silent deviations = failed audit.** Every deviation must be documented with the brief instruction that justified it.

---

## Final Report Template

```markdown
# Design Report

## Built
[Description of deliverable: pages, components, states, motions]

## Design Read
[Exact Design Read from Phase 0]

## Checklist Result
- [ ] Pass — all boxes ticked
- [ ] Pass with deviations — see Deviation Report
- [ ] Fail — specific boxes unticked with reasons

## Deviation Report
[Table as above, or "None"]

## Verification Evidence
- Screenshots: [desktop-light, desktop-dark, mobile-light, mobile-dark]
- Contrast measurements: [link to spreadsheet or inline table]
- Lighthouse scores: [Performance, Accessibility, Best Practices, SEO]
- Axe violations: [count + list if any]
- Keyboard test: [pass/fail + notes]
- Reduced-motion test: [pass/fail + notes]

## Known Issues
[Any unticked checklist boxes with reasons, or "None"]

## Handoff Notes
[For production-ready-workflow or debug-and-fix-bugs: token file location, component inventory, API contracts, etc.]
```