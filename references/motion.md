# Motion

Load at Phase 4. Motion here is product motion: felt, not seen. It exists for
**feedback, orientation, continuity, or deliberate delight** — if the honest
justification is "it looks cool" and the user sees it often, don't animate it.

---

## 1. When (and when not) to animate

- **Delight scales inversely with frequency.** Rare moments (first-run, success,
  empty states) can carry personality; high-frequency interactions must be near
  invisible.
- **Never animate keyboard-initiated actions** (shortcuts, arrow navigation,
  focus movement) — they repeat constantly and animation makes them feel slow.
- No motion on mount without a user trigger, except one deliberate, orchestrated
  page-entrance moment (and even that collapses under reduced motion).
- No endless decorative loops unless they communicate live status/progress; no
  custom cursors; no scroll-hijacking; no motion that competes with reading.
- One motion language per artifact: a consistent set of durations, easings, and
  physics. Mixed unrelated easings are the most common "something feels off".

## 2. Duration & easing defaults

| Element | Duration | Easing |
|---|---|---|
| Button press feedback | 100–160ms | enter curve |
| Tooltips, small popovers | 125–200ms | ease-out / enter curve |
| Dropdowns, selects | 150–250ms | enter curve |
| Hover — color/opacity | ~200ms | ease |
| Hover — transform/scale | 100–150ms | enter curve |
| Modals, drawers | 200–350ms | enter / drawer curve |
| Move/slide on screen | 200–300ms | move curve |
| Page transitions | 250–400ms | enter or move curve |
| Expressive/marketing moments | up to ~1000ms | spring or custom |

**Named curves** (register these as motion tokens in Phase 2):

- **enter** `cubic-bezier(0.22, 1, 0.36, 1)` — entrances, transform hover
- **move** `cubic-bezier(0.25, 1, 0.5, 1)` — slides, panels, drawers
- **drawer (iOS-feel)** `cubic-bezier(0.32, 0.72, 0, 1)`

Rules of thumb: routine UI stays **under 300ms**; duration scales with distance
(full-screen slide may exceed 300ms; a 6px tooltip shift stays under 150ms).
Avoid `ease-in` for UI — it lags the user's action and reads sluggish; prefer
decisive custom curves over the soft built-ins. Springs (for playful/gestural
work): perceptually critically damped, no more than a subtle overshoot for UI.

**Asymmetric timing:** occasional surfaces enter slightly slower, exit fast.
High-frequency ephemeral UI (hover highlights, popovers, panel toggles) inverts
this — enter instantly (0ms), exit with a brief 100–150ms fade — so the action
feels immediate.

## 3. Choreography principles

- **Continuity over teleportation.** Elements present in both states transition
  in place; expand from where things sit; never hard-cut between views that
  share components, and never duplicate a persistent element.
- **Emerge from the trigger.** Overlays and panels animate outward from the
  element that opened them: popover `transform-origin` at the trigger (modals
  stay `center`); entrances from `scale(0.85–0.9)`, never `scale(0)`.
- **Direction matches spatial layout.** Tabs/carousels slide the way the content
  actually sits (forward = leftward travel, back = rightward).
- **Paired states animate together.** If open animates, close animates; if hover
  moves, focus and pressed get equivalent feedback.
- **Paired elements share timing.** Modal + overlay, tooltip + arrow, FAB +
  label use identical duration and easing.
- **Stagger sparingly:** 30–50ms steps, small groups only, total under 300ms,
  most important element leading. Never animate a container *and* stagger its
  children — one entrance per container.
- Subsequent tooltips in a group open instantly once one is open.
- A tiny `filter: blur(2px)` crossfade hides rough content swaps.

## 4. Implementation

Priority: **CSS transitions > WAAPI > CSS keyframes > rAF/JS.** Transitions
retarget mid-flight when interrupted (keyframes restart from zero) and stay
smooth under main-thread load. Use keyframes only for predetermined sequences.

- Animate **`transform` and `opacity` only** for movement; `color` /
  `background-color` / `opacity` for state feedback. Never layout properties
  (`width`, `height`, `top`, `left`) — the one exception is a deliberate
  container-resize tween done knowingly.
- **`transition: all` is banned** — list properties explicitly.
- `@starting-style` for DOM-entry transitions; fall back to a `data-mounted`
  attribute where unsupported.
- `transform: scale()` scales children too — a feature for press feedback;
  counter-scale inner elements that must stay fixed.
- SVG: put transforms on a `<g>` with
  `transform-box: fill-box; transform-origin: center` or they pivot around the
  canvas origin.
- Disable transitions during theme switches
  (`[data-theme-switching] * { transition: none !important }`) or every themed
  property animates at once.
- Framework motion (Motion/Framer, GSAP): isolate in leaf components, memoize,
  and clean up every observer/timeline/instance on unmount. Scroll-linked work
  uses `useScroll`/ScrollTrigger/IntersectionObserver or CSS scroll-driven
  animations — never a raw `window.addEventListener('scroll')` handler.
- During direct manipulation (drag), the element stays locked to the pointer
  with **no easing**; easing applies only after release, and boundaries get
  friction, not hard stops.

## 5. Performance

- `will-change` toggled on just before heavy motion and removed after; only for
  `transform`/`opacity`; permanent promotion across many elements is worse than
  none.
- Pause looping animations off-screen with `IntersectionObserver`.
- Avoid animating `filter` in core interactions; if unavoidable keep blur ≤ 20px.
- Don't drive drag via CSS variables on a container (recalculates styles for all
  children) — set `transform` directly on the moving element.
- Budget: motion must not push INP over 200ms or jank scrolling on mid-tier
  mobile.

## 6. Accessibility

Every animation ships with a reduced-motion path — transform/keyframe motion
disabled, replaced by instant state change or opacity-only fade:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

(Or the framework equivalent, e.g. `useReducedMotion()` degrading to static.)
Parallax, infinite loops, scroll-linked and "magnetic" effects collapse to
static under reduced motion — non-negotiable. Gate hover animation behind
`@media (hover: hover) and (pointer: fine)` or touch devices replay hover on
tap. Autoplaying moving content longer than 5s needs pause/stop controls; no
flashing > 3 times/second.

## 7. Validation (evidence, not "looks fine")

- Grep the diff for layout-property transitions and `transition: all`.
- Rapidly retoggle components: transitions must retarget, not restart.
- DevTools Animations panel at 10% speed: timing and `transform-origin` issues
  hide at full speed.
- Emulate `prefers-reduced-motion: reduce` and confirm every animation has a
  path.
- Confirm `will-change` is transient and loops pause off-screen.
- Test touch on a real device where possible — simulators under-report
  hover-on-tap and gesture issues.