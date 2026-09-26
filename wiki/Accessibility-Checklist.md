# Accessibility Checklist — WCAG 2.2 AA Practical Audit

Target: **WCAG 2.2 Level AA** as floor, organized by POUR. Semantic HTML earns most of this — **use ARIA only to fill genuine gaps; wrong ARIA is worse than none** (first rule: don't use ARIA if native HTML can do it).

---

## 1. Perceivable

### Contrast (1.4.3 / 1.4.11)
- [ ] Text: 4.5:1
- [ ] Large text (≥ 24px, or ≥ 18.7px bold): 3:1
- [ ] UI component boundaries, states, graphical meaning-carriers: 3:1
- [ ] **Audit in both themes** — include placeholder, helper, error text, text over imagery (scrim it)

### Not Color Alone (1.4.1)
- [ ] Status, links in prose, chart series, validation → all carry second cue (icon, underline, label, pattern)

### Text Alternatives (1.1.1)
- [ ] Informative images → concrete `alt`
- [ ] Decorative images → `alt=""`
- [ ] Icon-only buttons → accessible name (`aria-label` or visually-hidden text)
- [ ] Complex charts → text/table equivalent

### Reflow & Resize (1.4.4 / 1.4.10)
- [ ] Page works at 200% text zoom AND 320px width without horizontal scroll or loss
- [ ] Use `rem`-based sizing, no fixed-height text containers, never disable pinch-zoom

### Text Spacing (1.4.12)
- [ ] Layout survives user overrides (line-height 1.5×, paragraph/letter/word spacing bumps)
- [ ] Avoid clipping containers around text

### Media
- [ ] Captions for video, transcripts for audio
- [ ] No audio autoplay > 3s without control

---

## 2. Operable

### Keyboard Complete (2.1.1 / 2.1.2)
- [ ] Every action reachable/operable by keyboard
- [ ] DOM order = visual order = tab order
- [ ] No traps — modals trap focus *by design* with Escape to close + focus returned to trigger
- [ ] Custom widgets implement expected keys (arrows in menus/tabs/radio groups, Enter/Space on buttons)

### Focus Visible & Not Obscured (2.4.7 / 2.4.11)
- [ ] Styled `:focus-visible` on everything interactive — ≥ 3:1 against adjacent, ≥ 2px, offset
- [ ] Sticky headers/footers must not cover focused element

### Target Size (2.5.8)
- [ ] ≥ 24×24 CSS px or equivalent spacing — **but design to 44px platform target** from playbook

### Dragging Alternative (2.5.7)
- [ ] Any drag interaction (sortable lists, sliders, kanban) → single-pointer non-drag path (buttons, menu actions, direct input)

### Skip & Structure (2.4.1)
- [ ] Skip-to-content link first in tab order
- [ ] Landmarks (`header/nav/main/footer`, one `main`)
- [ ] One `h1`; heading levels never skip
- [ ] Descriptive page `title` and link text (no bare "click here")

### Timing & Motion (2.2.x / 2.3.1)
- [ ] Adjustable/extendable timeouts
- [ ] Pause/stop for auto-moving content > 5s
- [ ] Nothing flashes > 3×/second
- [ ] Reduced-motion honored (see motion reference)

---

## 3. Understandable

### Language
- [ ] `lang` on `<html>` (and inline foreign phrases)

### Labels & Instructions (3.3.2)
- [ ] Every input programmatically labeled (`<label for>` or equivalent)
- [ ] Required/optional and format expectations stated up front, not revealed by failure

### Errors (3.3.1 / 3.3.3)
- [ ] Identified in text, specific, suggest fix
- [ ] Associated to field (`aria-describedby`)
- [ ] Announced (`role="alert"` or polite live region)
- [ ] Focus moves to first error on failed submit

### Redundant Entry (3.3.7)
- [ ] Never ask for same information twice in one flow — autofill or offer "same as"

### Accessible Authentication (3.3.8)
- [ ] No cognitive tests (transcription, puzzles) as only path — allow paste, password managers, alternatives

### Consistent Help & Navigation (3.2.3 / 3.2.6)
- [ ] Navigation and help mechanisms appear in same relative place across pages

### Predictability (3.2.1/3.2.2)
- [ ] Focus or input never triggers surprise context changes (no auto-submit on last field, no navigation on select change without button)

---

## 4. Robust

### Name, Role, Value (4.1.2)
- [ ] Custom components expose correct role, accessible name, current state (`aria-expanded`, `aria-selected`, `aria-checked`, `aria-current`)
- [ ] Prefer native elements so this is automatic

### Status Messages (4.1.3)
- [ ] Toasts, async results, cart counts, validation summaries → announce via live regions without stealing focus

### State Sync
- [ ] Forms/controls keep programmatic ↔ visual state in sync (visually disabled = programmatically disabled)

---

## Test Protocol (Evidence, Not Vibes)

| Pass | Method | Catches |
|------|--------|---------|
| **1. Automated** | axe / Lighthouse a11y | ~30-40%; clean score necessary, not sufficient |
| **2. Keyboard-only** | Unplug mouse; complete every primary flow | Invisible focus, traps, unreachable controls, illogical order |
| **3. Zoom** | 200% text zoom + 320px viewport | Reflow, clipping, horizontal scroll |
| **4. Contrast** | Measure failure-prone spots in both themes | Buttons, ghost buttons over imagery, placeholders, helper/error text |
| **5. Reduced-motion** | Emulate `prefers-reduced-motion: reduce` | All animations have path |
| **6. Screen-reader** | VoiceOver/NVDA spot-check | Page summary, landmarks, form completion, one async flow (errors/toasts announce?) |

**Log any unfixable finding in final report with reason — silence = failed audit.**

---

## Quick Reference: Common Failures

| Pattern | WCAG | Fix |
|---------|------|-----|
| `outline: none` without `:focus-visible` replacement | 2.4.7 | Add visible focus style |
| Placeholder as only label | 1.3.1, 3.3.2 | Add `<label>` above input |
| Ghost button over image (no scrim) | 1.4.3 | Add backdrop/scrim/stroke |
| `div` as button | 4.1.2 | Use `<button>` or add role+keyboard |
| Color-only status (red border only) | 1.4.1 | Add icon/text/pattern |
| Missing `alt` on informative image | 1.1.1 | Add descriptive `alt` |
| Fixed `h-screen` viewport | 1.4.10 | Use `min-h-[100dvh]` |
| `transition: all` | 2.3.3 (motion) | List properties explicitly |
| No reduced-motion path | 2.3.3 | Add `@media (prefers-reduced-motion)` block |
| Heading levels skip (h1 → h3) | 1.3.1 | Fix hierarchy |
| Missing skip link | 2.4.1 | Add skip-to-content link |
| Drag without alternative | 2.5.7 | Add button/menu alternative |

---

## Automated Test Commands

```bash
# axe-core CLI
npx @axe-core/cli https://your-url.com

# Lighthouse CI
npx lighthouse-ci autorun

# Pa11y
npx pa11y https://your-url.com --standard WCAG2AA
```