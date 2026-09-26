# Accessibility — WCAG 2.2 AA Practical Audit

Load at Phase 5 (and skim before Phase 3 on unfamiliar patterns). Target is
**WCAG 2.2 Level AA** as the floor, organized by POUR. Semantic HTML earns most
of this for free — **use ARIA only to fill genuine gaps; wrong ARIA is worse
than none** (first rule of ARIA: don't use ARIA if native HTML can do it).

---

## 1. Perceivable

- **Contrast (1.4.3 / 1.4.11):** text 4.5:1; large text 3:1; UI component
  boundaries, states, and graphical meaning-carriers 3:1. Audit in both themes;
  include placeholder, helper, error text, and text over imagery (scrim it).
- **Not color alone (1.4.1):** status, links in prose, chart series, and
  validation all carry a second cue (icon, underline, label, pattern).
- **Text alternatives (1.1.1):** informative images get concrete `alt`;
  decorative images get `alt=""`; icon-only buttons get an accessible name
  (`aria-label` or visually-hidden text); complex charts get a text/table
  equivalent.
- **Reflow & resize (1.4.4 / 1.4.10):** page works at 200% text zoom and at
  320px width without horizontal scroll or loss; use `rem`-based sizing, no
  fixed-height text containers, never disable pinch-zoom.
- **Text spacing (1.4.12):** layout survives user overrides (line-height 1.5×,
  paragraph/letter/word spacing bumps) — avoid clipping containers around text.
- Media: captions for video, transcripts for audio; no audio autoplay > 3s
  without control.

## 2. Operable

- **Keyboard complete (2.1.1 / 2.1.2):** every action reachable and operable by
  keyboard; DOM order = visual order = tab order; no traps — modals trap focus
  *by design* with Escape to close and focus returned to the trigger; custom
  widgets implement expected keys (arrows in menus/tabs/radio groups, Enter/
  Space on buttons).
- **Focus visible & not obscured (2.4.7 / 2.4.11):** styled `:focus-visible` on
  everything interactive — ≥ 3:1 against adjacent colors, ≥ 2px, offset from the
  element; sticky headers/footers must not cover the focused element.
- **Target size (2.5.8):** ≥ 24×24 CSS px or equivalent spacing — but design to
  the 44px platform target from the playbook.
- **Dragging alternative (2.5.7):** any drag interaction (sortable lists,
  sliders, kanban) offers a single-pointer, non-drag path (buttons, menu
  actions, direct input).
- **Skip & structure (2.4.1):** skip-to-content link first in tab order;
  landmarks (`header/nav/main/footer`, one `main`); one `h1`; heading levels
  never skip; descriptive page `title` and link text (no bare "click here").
- **Timing & motion (2.2.x / 2.3.1):** adjustable/extendable timeouts; pause/
  stop for auto-moving content > 5s; nothing flashes > 3×/second; reduced-motion
  honored (see motion reference).

## 3. Understandable

- **Language:** `lang` on `<html>` (and on inline foreign phrases).
- **Labels & instructions (3.3.2):** every input programmatically labeled
  (`<label for>` or equivalent); required/optional and format expectations
  stated up front, not revealed by failure.
- **Errors (3.3.1 / 3.3.3):** identified in text, specific, suggest the fix,
  associated to the field (`aria-describedby`), announced (`role="alert"` or
  polite live region); focus moves to the first error on failed submit.
- **Redundant entry (3.3.7):** never ask for the same information twice in one
  flow — autofill or offer "same as" options.
- **Accessible authentication (3.3.8):** no cognitive tests (transcription,
  puzzles) as the only path — allow paste, password managers, or alternatives.
- **Consistent help & navigation (3.2.3 / 3.2.6):** navigation and help
  mechanisms appear in the same relative place across pages.
- **Predictability (3.2.1/3.2.2):** focus or input never triggers surprise
  context changes (no auto-submit on last field, no navigation on select
  change without a button).

## 4. Robust

- **Name, role, value (4.1.2):** custom components expose correct role, an
  accessible name, and current state (`aria-expanded`, `aria-selected`,
  `aria-checked`, `aria-current`); prefer native elements so this is automatic.
- **Status messages (4.1.3):** toasts, async results, cart counts, validation
  summaries announce via live regions without stealing focus.
- Forms and controls keep programmatic ↔ visual state in sync (a visually
  disabled control is programmatically disabled).

---

## 5. Test protocol (evidence, not vibes)

1. **Automated sweep:** axe / Lighthouse a11y — catches ~30–40%; a clean score
   is necessary, not sufficient.
2. **Keyboard-only pass:** unplug the mouse; complete every primary flow; watch
   for invisible focus, traps, unreachable controls, illogical order.
3. **Zoom pass:** 200% text zoom and 320px-wide viewport.
4. **Contrast pass:** measure the failure-prone spots listed above in both
   themes.
5. **Reduced-motion pass:** emulate and confirm.
6. **Screen-reader spot-check** where available (VoiceOver/NVDA): page summary,
   landmark navigation, form completion, one async flow (do errors and toasts
   announce?).

Log any unfixable finding in the final report with a reason — silence is a
failed audit.