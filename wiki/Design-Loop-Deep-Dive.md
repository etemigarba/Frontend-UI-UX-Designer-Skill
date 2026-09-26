# Design Loop Deep Dive

The design loop is the heart of this skill. Every engagement runs through all six phases with explicit entry actions, exit criteria, and a hard cap of **two fix passes** for the entire cycle.

```text
Perceive → Direction → System → Build → Motion → Reflect
   ▲                                                │
   └──────── (bounded: max 2 fix passes) ───────────┘
```

---

## Phase 0 — Perceive (Context Gate)

**Do not choose colors, fonts, or layouts until this gate passes.**

### Entry Actions

1. **Pin the subject** — Name product, audience, surface's single job
2. **Choose surface mode** — Based on requested surface, not product
3. **Detect stack** — Check `package.json`, `tailwind.config`, etc.
4. **Inventory incumbent visual truth** — Declare refinement or redesign
5. **Output Design Read** — One-line summary with dials

### Design Read Format

```
Read: <subject> for <audience> · mode=<mode> · stack=<stack> · <refine|redesign> · dials V<1-10>/M<1-10>/D<1-10>
```

### Dials

| Dial | Name | Range | Meaning |
|------|------|-------|---------|
| **V** | DESIGN_VARIANCE | 1-10 | Centered/safe → Asymmetric/bold |
| **M** | MOTION_INTENSITY | 1-10 | Static → Choreographed |
| **D** | VISUAL_DENSITY | 1-10 | Airy → Dense |

### Exit Criterion

All of: subject, mode, stack, refine-vs-redesign, and dials explicit in Design Read.

---

## Phase 1 — Direction

**Load:** `references/design-direction.md`

### Deliverable: Direction Plan

1. **Aesthetic direction** — One named family from rotation table + justification
2. **Palette** — 4-6 named hex values, one accent locked page-wide
3. **Type** — Display face (restrained), body face (workhorse), optional utility face
4. **Layout concept** — One sentence + ASCII wireframe of key screen
5. **Signature element** — The one thing this interface will be remembered by

### Anti-Default Test

For each: palette, display face, hero layout, section rhythm, signature element:

1. Simulate: "What would any model produce for this brief category?"
2. If plan matches → it's a default. Replace or justify from brief in writing.
3. Confirm internal consistency: temperature, radius system, copy register

### Saturated Defaults (Banned as Reflex)

- Warm-cream + display-serif + terracotta/clay accent
- Near-black + acid-green/vermilion accent
- Broadsheet: hairline rules, radius-0, dense columns
- AI-purple/violet glow, purple→blue gradients, neon glows
- Centered hero + three equal cards + gradient blob

Override only with explicit brief instruction, stated in plan.

### Exit Criterion

Direction plan written; anti-default test passed or brief-overridden.

---

## Phase 2 — System (Tokens)

**Load:** `assets/design-tokens-template.css`

### Deliverable: Complete Token System

All tokens in **one place** (CSS custom properties, Tailwind theme, or platform native).

#### Required Token Categories

| Category | Requirements |
|----------|-------------|
| **Color roles** | background, surface, surface-elevated, border, border-strong, text-primary, text-secondary, text-muted, accent, accent-hover, accent-contrast, destructive, success, warning, focus-ring |
| **Spacing** | 4px or 8px base scale (--space-1 through --space-24) |
| **Type** | Fluid scale via `clamp()`, ratio ≈ 1.2–1.333, display + body + mono families |
| **Radius** | **One system**: interactive, container, full (pill) — or documented mixed rule |
| **Elevation** | Shadows tinted to background hue; layered small shadows; dark mode = lighter surface |
| **Motion** | Durations (fast/base/slow) + named easings (enter/move/drawer) |
| **Z-index** | Documented scale (sticky/overlay/modal/toast/top) — nothing outside |

### Light + Dark from Start

- Dark mode = token swap with **hierarchy parity** + **brand fidelity**
- No pure `#000000` or `#ffffff`
- Respect `prefers-color-scheme`; manual toggle when brand needs it
- Test both modes before finishing

### Exit Criterion

Tokens exist in one place, both themes defined, every subsequent component consumes them.

---

## Phase 3 — Build

**Load:** `references/ux-playbook.md`

### Build Order (Hard Rules Apply)

1. **Semantic HTML first, ARIA last** — Landmarks, one `h1`, ordered headings
2. **Structure & layout** — Mobile-first, explicit collapse, `min-h-[100dvh]`
3. **Complete interactive states** — default → hover → focus-visible → active → disabled → loading
4. **Complete resource states** — loading (skeletons), empty (composed), error (specific), ready
5. **Real content strategy** — Image-gen tool → real photography → explicit slots

### Layout Hard Rules (Pre-Flight Failures)

- Hero fits viewport: headline ≤ 2 lines, subtext ≤ 20 words, CTA above fold
- Hero stack ≤ 4 text elements; real visual (not text + gradient blob)
- Nav: single line desktop, ≤ 80px
- ≥ 4 layout families per page; zigzag ≤ 2 consecutive; marquee ≤ 1
- Eyebrow count ≤ ceil(sections/3)
- No split-header pattern as default
- Bento: cell count = content count; 2-3 cells visually varied
- Mobile collapse explicit per section

### Exit Criterion

All states implemented, layout hard rules pass, content real or explicitly slotted.

---

## Phase 4 — Motion

**Load:** `references/motion.md`

### When to Animate

| Do Animate | Don't Animate |
|------------|---------------|
| Feedback on important controls | Keyboard-initiated actions |
| State transitions | High-frequency interactions |
| Entry reveal for primary content | Mount without user trigger |
| Scroll reveal serving story | Endless decorative loops |

**One motion language per artifact:** consistent durations, easings, physics.

### Choreography Principles

- Continuity over teleportation
- Emerge from trigger (transform-origin at trigger)
- Direction matches spatial layout
- Paired states/elements share timing
- Stagger sparingly (30-50ms, total < 300ms)

### Hard Rules

- `transform` and `opacity` only for movement
- `transition: all` **banned**
- `@starting-style` for DOM entry
- Disable transitions during theme switches
- Framework motion: isolate, memoize, cleanup on unmount

### Exit Criterion

Every animation justifiable in one sentence; reduced-motion verified; no layout-property animation.

---

## Phase 5 — Reflect & Verify (Termination Gate)

**Load:** `references/accessibility.md` + `references/preflight-checklist.md`

### Verification Steps

1. **Browser tooling available** → Screenshot desktop+mobile × light+dark; run Lighthouse/axe
2. **Mechanical checks** (grep/measure) → then full checklist
3. **Fix all findings in one batch** → re-verify once → stop (max 2 passes total)
4. **Report**: what built, Design Read satisfied, checklist result, deviations with brief justification

### Mechanical Checks (Auto-Detectable)

```bash
grep -r "transition: all"
grep -r "transition.*width\|height\|top\|left"
grep -r "outline: none\|outline-none"
grep -r "#[0-9a-fA-F]\{3,8\}" --include="*.tsx" --include="*.vue" --include="*.svelte"
grep -r "h-screen"
grep -r "addEventListener.*scroll"
grep -r "z-\[40\|50\|.*\]"
```

### Full Checklist Categories

- Identity & Consistency (7 items)
- Layout & Hero (8 items)
- Type & Color (4 items)
- Components, States & Forms (6 items)
- Content & Copy (6 items)
- Motion (6 items)
- Accessibility (4 items)
- Performance (4 items)
- Process Honesty (3 items)

### Termination Condition

**Every checklist box honestly ticked** OR specific unticked boxes reported with reason. Never declare done otherwise.

---

## Fix Pass Budget

| Pass | Scope | When |
|------|-------|------|
| 1 | All mechanical + checklist findings | After first verification |
| 2 | Remaining issues from pass 1 | After re-verification |
| **Stop** | Ship with honest report | After pass 2 |

---

## Reporting Template

```markdown
## Design Report

**Built:** [description of deliverable]
**Design Read:** [exact Design Read from Phase 0]
**Checklist:** [Pass / Pass with deviations / Fail — specific boxes]
**Deviations:**
- [Item] — [Brief instruction that justified it]
**Verification Evidence:** [Screenshots, measurements, tool output]
**Known Issues:** [Any unticked boxes with reasons]
```