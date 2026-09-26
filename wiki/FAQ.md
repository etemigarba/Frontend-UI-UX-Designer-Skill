# FAQ

## General Questions

### What is this skill?

The Frontend UI/UX Designer Skill is a complete, award-caliber design workflow for AI coding agents (Claude Code, OpenCode, etc.). It enforces a bounded, verifiable design loop that produces distinctive, accessible, fast, and complete interfaces.

### How do I invoke it?

Use `/frontend-ui-ux-designer` or use triggering phrases like:
- "design a landing page for..."
- "make this look better / professional / modern"
- "improve the UX of..."
- "this looks generic or AI-generated"
- "pick a palette / font pairing"
- "add dark mode"
- "make it responsive"
- "add animations"

### What harnesses are supported?

- Claude Code (`.claude/skills/`)
- OpenCode (`.config/opencode/skills/`)
- Any harness that supports the ECC skill format

### Do I need to install companion skills?

No. The skill degrades gracefully to its bundled references when companions are not installed. Companions add depth but are optional.

---

## Design Loop Questions

### What is the Design Read?

A one-line summary output at Phase 0 that declares:
```
Read: <subject> for <audience> · mode=<mode> · stack=<stack> · <refine|redesign> · dials V<1-10>/M<1-10>/D<1-10>
```

It pins the subject, audience, surface mode, tech stack, refinement vs redesign decision, and three dials (Variance, Motion, Density).

### What are the three dials?

| Dial | Name | Range | Meaning |
|------|------|-------|---------|
| **V** | DESIGN_VARIANCE | 1-10 | Centered/safe → Asymmetric/bold |
| **M** | MOTION_INTENSITY | 1-10 | Static → Choreographed |
| **D** | VISUAL_DENSITY | 1-10 | Airy → Dense |

### How do I choose a surface mode?

Choose from the **requested surface**, not the product:
- Landing page for dev tool → **Persuade**
- Dashboard for same dev tool → **Operate**
- Docs for same dev tool → **Read**
- Portfolio of the dev tool creator → **Experience**

If genuinely ambiguous, ask **one** clarifying question — do not guess.

### What's the difference between refinement and redesign?

- **Refinement** — keeps incumbent identity, behavior, copy, and everything outside scope
- **Redesign** — keeps product truth, content, and function, but treats old look as evidence and anti-reference

**Never split the difference into polish on a discarded look.**

### How many fix passes are allowed?

**Maximum 2 fix passes for the entire cycle.** After Phase 5 verification, fix all findings in one batch, re-verify once, and stop. No open-ended self-QA.

---

## Token System Questions

### Why OKLCH for colors?

OKLCH is a perceptual color space where light/dark variants keep consistent perceived lightness and chroma. This ensures hierarchy parity between themes.

### Can I use Tailwind instead of CSS custom properties?

Yes. Mirror tokens in `tailwind.config.js` or `@theme` (v4). The skill outputs tokens in the stack's native format.

### What does "one accent, locked" mean?

Once chosen in Phase 1, the accent hue is used identically across every section — the CTA in section 7 does not switch hue, the footer badge does not go teal.

### What is "Theme Lock"?

One theme per page; no section inverts mid-scroll. The only exception is one deliberate full-theme color-block moment, brief-justified.

### What is "Radius Lock"?

One corner-radius system per page — all-sharp, all-soft (12–16px), or all-pill for interactive — or a documented mixed rule applied everywhere. Round buttons in a square layout is broken design.

---

## Accessibility Questions

### Is WCAG 2.2 AA mandatory?

Yes, it's the floor. The pre-flight checklist includes automated + manual accessibility verification.

### Do I need to test with screen readers?

The skill requires a screen-reader spot-check (VoiceOver/NVDA) where available. At minimum: page summary, landmark navigation, form completion, one async flow.

### What about reduced motion?

**Non-negotiable.** Every animation must have a reduced-motion path (instant state change or opacity-only fade). The token template includes the required `@media` block.

### What are the most common accessibility failures?

1. `outline: none` without `:focus-visible` replacement
2. Placeholder as only label
3. Ghost button over image (no scrim)
4. `div` as button
5. Color-only status
6. Missing `alt` on informative images
6. Fixed `h-screen` viewport
7. `transition: all`
8. No reduced-motion path
9. Heading levels skip (h1 → h3)
10. Missing skip link

---

## Companion Skills Questions

### Which companions should I install first?

For production use:
1. `impeccable` (anti-slop correction)
2. `shadcn` or `21st-dev-builder-v2` (components)
3. `webapp-testing` or `agent-browser` (verification)
4. `ui-animation` (motion depth)

### What if a companion skill conflicts with my tokens?

**Re-tokenize.** Replace all companion tokens with your Phase 2 tokens. Never ship a component in its default state.

### Can I use this skill without React?

Yes. The skill is stack-agnostic. It detects your stack (or defaults to HTML+Tailwind) and outputs accordingly. Examples exist for React, Vue, Svelte, and plain HTML.

---

## Verification Questions

### What counts as "evidence"?

- Screenshots (desktop-light, desktop-dark, mobile-light, mobile-dark)
- Contrast measurements (measured, not eyeballed)
- Lighthouse scores (actually run, not asserted)
- Axe violations (count + list)
- Keyboard test results (pass/fail + notes)
- Reduced-motion test results

### Can I skip the checklist if I'm in a hurry?

**No.** The checklist is the termination gate. If a single box cannot be honestly ticked, the work is not done. Brief-justified deviations are legitimate; silent ones are not.

### What if I can't fix something?

Document it in the final report with the specific box and reason. Silence = failed audit.

---

## Troubleshooting

### Skill not activating

1. Verify installation path matches your harness
2. Check skill name: `frontend-ui-ux-designer` (from SKILL.md frontmatter)
3. Restart the agent/harness

### Stack not detected

Ensure `package.json` or config files are in workspace root. Explicitly state stack in brief: "Stack: Next.js 14 + Tailwind"

### Design Read seems wrong

Provide more context in brief. Explicitly set mode: "Mode: Operate (it's a dashboard)". Pin aesthetic: "Use Neo-Brutalist direction."

### Output feels generic

Run the anti-default test. Install `impeccable` or `design-taste-frontend` for bias correction. Increase DESIGN_VARIANCE dial.

---

## Licensing

### Can I use this in commercial projects?

Yes. MIT License with explicit permission for adoption, editing, refactoring, and redistribution without explicit approval.

### Do I need to attribute?

Attribution is appreciated but not required.

### Can I fork and modify?

Yes. The license explicitly permits modification and redistribution.