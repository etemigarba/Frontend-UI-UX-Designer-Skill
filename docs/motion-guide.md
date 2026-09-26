# Motion Guide — Reference

Load at Phase 4. Motion is **product motion: felt, not seen**. Exists for feedback, orientation, continuity, or deliberate delight. If honest justification is "it looks cool" and user sees it often → don't animate.

---

## 1. When (and When Not) to Animate

| Animate | Don't Animate |
|---------|---------------|
| Feedback on important controls | Keyboard-initiated actions (shortcuts, arrows, focus) |
| State transitions | High-frequency interactions (must be near-invisible) |
| Entry reveal for primary content | Mount without user trigger (except 1 deliberate entrance) |
| Scroll reveal serving story | Endless decorative loops (unless live status/progress) |
| Continuity between shared states | Custom cursors, scroll-hijacking, motion competing with reading |

**Delight scales inversely with frequency.** Rare moments (first-run, success, empty) can carry personality; high-frequency = near invisible.

**One motion language per artifact:** consistent durations, easings, physics. Mixed easings = "something feels off."

---

## 2. Duration & Easing Defaults

| Element | Duration | Easing |
|---------|----------|--------|
| Button press feedback | 100–160ms | enter curve |
| Tooltips, small popovers | 125–200ms | ease-out / enter |
| Dropdowns, selects | 150–250ms | enter curve |
| Hover — color/opacity | ~200ms | ease |
| Hover — transform/scale | 100–150ms | enter curve |
| Modals, drawers | 200–350ms | enter / drawer curve |
| Move/slide on screen | 200–300ms | move curve |
| Page transitions | 250–400ms | enter or move curve |
| Expressive/marketing | up to ~1000ms | spring or custom |

**Named Curves (register as tokens):**

- **enter** `cubic-bezier(0.22, 1, 0.36, 1)` — entrances, transform hover
- **move** `cubic-bezier(0.25, 1, 0.5, 1)` — slides, panels, drawers
- **drawer (iOS-feel)** `cubic-bezier(0.32, 0.72, 0, 1)`

### Rules of Thumb

- Routine UI **under 300ms**
- Duration scales with distance (full-screen slide may exceed 300ms; 6px tooltip shift < 150ms)
- Avoid `ease-in` for UI — lags action, reads sluggish
- Prefer decisive custom curves over soft built-ins
- Springs: perceptually critically damped, subtle overshoot max for UI

### Asymmetric Timing

- Occasional surfaces: enter slightly slower, exit fast
- High-frequency ephemeral UI (hover highlights, popovers, toggles): **enter instantly (0ms), exit with 100-150ms fade** — action feels immediate

---

## 3. Choreography Principles

| Principle | Application |
|-----------|-------------|
| **Continuity over teleportation** | Elements in both states transition in place; expand from where things sit; never hard-cut between views sharing components |
| **Emerge from trigger** | Overlays/panels animate outward from trigger: popover `transform-origin` at trigger (modals stay `center`); entrances from `scale(0.85–0.9)`, never `scale(0)` |
| **Direction matches spatial layout** | Tabs/carousels slide way content actually sits (forward = leftward, back = rightward) |
| **Paired states animate together** | If open animates, close animates; if hover moves, focus/pressed get equivalent feedback |
| **Paired elements share timing** | Modal + overlay, tooltip + arrow, FAB + label = identical duration/easing |
| **Stagger sparingly** | 30-50ms steps, small groups only, total < 300ms, most important element leads; never animate container AND stagger children |
| **Subsequent tooltips** | Open instantly once one is open |
| **Content swap crossfade** | Tiny `filter: blur(2px)` hides rough swaps |

---

## 4. Implementation Priority

**CSS transitions > WAAPI > CSS keyframes > rAF/JS**

| Method | When to Use |
|--------|-------------|
| CSS transitions | Default — retarget mid-flight, smooth under load |
| WAAPI | Need JS control but want compositing |
| CSS keyframes | Predetermined sequences only (restart from zero on interrupt) |
| rAF/JS | Last resort — custom physics, complex orchestration |

### Hard Rules

- **`transform` and `opacity` only** for movement; `color`/`background-color`/`opacity` for state feedback
- **Never layout properties** (`width`, `height`, `top`, `left`) — exception: deliberate container-resize tween
- **`transition: all` banned** — list properties explicitly
- `@starting-style` for DOM-entry transitions; fallback: `data-mounted` attribute
- `transform: scale()` scales children — feature for press feedback; counter-scale inner elements that must stay fixed
- SVG: transforms on `<g>` with `transform-box: fill-box; transform-origin: center`
- Disable transitions during theme switches: `[data-theme-switching] * { transition: none !important }`
- Framework motion (Motion/Framer, GSAP): isolate in leaf components, memoize, cleanup every observer/timeline/instance on unmount
- Scroll-linked: `useScroll`/ScrollTrigger/IntersectionObserver or CSS scroll-driven — never raw `window.addEventListener('scroll')`
- Direct manipulation (drag): element locked to pointer with **no easing**; easing only after release; boundaries = friction, not hard stops

---

## 5. Performance

- `will-change` toggled on just before heavy motion, removed after; only for `transform`/`opacity`; permanent promotion across many elements = worse than none
- Pause looping animations off-screen with `IntersectionObserver`
- Avoid animating `filter` in core interactions; if unavoidable, blur ≤ 20px
- Don't drive drag via CSS variables on container (recalculates styles for all children) — set `transform` directly on moving element
- Budget: motion must not push INP > 200ms or jank scrolling on mid-tier mobile

---

## 6. Accessibility (Non-Negotiable)

**Every animation ships with reduced-motion path** — transform/keyframe motion disabled, replaced by instant state change or opacity-only fade:

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

(Or framework equivalent: `useReducedMotion()` degrading to static.)

**Collapse to static under reduced motion:**
- Parallax, infinite loops
- Scroll-linked effects
- "Magnetic" effects

**Gate hover animation:** `@media (hover: hover) and (pointer: fine)` or touch devices replay hover on tap.

**Autoplaying moving content > 5s:** needs pause/stop controls.

**No flashing > 3 times/second.**

---

## 7. Validation (Evidence, Not "Looks Fine")

- Grep diff for layout-property transitions and `transition: all`
- Rapidly retoggle components: transitions must retarget, not restart
- DevTools Animations panel at 10% speed: timing and `transform-origin` issues hide at full speed
- Emulate `prefers-reduced-motion: reduce` → confirm every animation has path
- Confirm `will-change` is transient and loops pause off-screen
- Test touch on real device where possible — simulators under-report hover-on-tap and gesture issues

---

## Motion Token Reference (Phase 2)

```css
--duration-fast:   150ms;
--duration-base:   200ms;
--duration-slow:   300ms;
--ease-enter:  cubic-bezier(0.22, 1, 0.36, 1);
--ease-move:   cubic-bezier(0.25, 1, 0.5, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

Components consume tokens only — no raw durations/easings in component code.