# Companion Skill Integration

This skill is the **orchestrator**. It owns the design loop and gates. Companion skills own depth inside a phase. Their output still must pass Phase 5's checklist.

---

## Routing Table

| Phase | Companion Skill | Purpose | When to Delegate |
|-------|-----------------|---------|------------------|
| 0–1 Direction | `brainstorming` (obra/superpowers) | Diverge on direction before committing | Brief is ambiguous; need multiple aesthetic directions to evaluate |
| 1–2 System | `ui-ux-pro-max` | Searchable styles/palettes/font-pairing/UX-rule database; `--design-system` output feeds Phase 2 | Need curated design system data, palette exploration, font pairing search |
| 1–5 Taste | `design-taste-frontend`, `impeccable` | Anti-slop bias correction; `impeccable` sub-commands (`critique`, `audit`, `polish`, `bolder`, `quieter`) map onto Phase 5 | Output feels generic; need taste correction; Phase 5 audit |
| 3 Components | `shadcn`, `21st-dev-builder-v2` | Sourcing/installing components — **always re-tokenized to Phase 2's system**, never shipped in default state | Need specific component primitives (dialog, select, toast, etc.) |
| 3 Implementation | `react-best-practices`, `react-expert`, `frontend-design` | Stack-correct component architecture | Building React/Vue/Svelte components; need framework-specific patterns |
| 4 Motion | `ui-animation`, `emilkowalski-motion`, `css-animations`, `animation-designer` | Deep motion specs, springs, gesture work, reverse-engineering recorded motion | Complex motion choreography; spring physics; gesture-driven animation |
| 5 Verification | `webapp-testing`, `agent-browser`, `verification-before-completion` | Live-render screenshots, interaction testing, done-means-done gate | Need browser automation for verification; Playwright screenshots; live a11y testing |
| Handoff | `/production-ready-workflow`, `/debug-and-fix-bugs` | When center of gravity shifts from design to full-app production readiness or correctness | Design complete; need zero-mock-data production hardening or bug hunting |

---

## Delegation Protocol

### 1. Check Availability
```bash
# In your agent harness, check installed skills
# Only delegate if companion is installed
```

### 2. Delegate with Context
Pass the relevant phase context:
- **Phase 1→2**: Direction plan + palette + type choices
- **Phase 2→3**: Complete token system (CSS custom properties or Tailwind config)
- **Phase 3→4**: Built components with all states
- **Phase 4→5**: Motion specifications + implementation

### 3. Integrate Result
- Companion output replaces the bundled reference for that phase
- Validate integration against Phase 5 checklist
- Document delegation in final report

### 4. Fallback = Bundled Reference
If companion not installed → use bundled reference file:
- `references/design-direction.md` (Phase 1)
- `assets/design-tokens-template.css` (Phase 2)
- `references/ux-playbook.md` (Phase 3)
- `references/motion.md` (Phase 4)
- `references/accessibility.md` + `preflight-checklist.md` (Phase 5)

**Never block on missing companion.**

---

## Companion Skill Details

### `brainstorming` (Phase 0–1)
- **Source:** obra/superpowers ecosystem
- **Use when:** Brief is open-ended; need 3-5 distinct direction concepts to evaluate
- **Input:** Brief + Design Read
- **Output:** Multiple direction plans with trade-offs
- **Integration:** Pick one, run anti-default test, proceed to Phase 2

### `ui-ux-pro-max` (Phase 1–2)
- **Source:** Agentic Engineering Skills
- **Use when:** Need searchable database of styles, palettes, font pairings, UX rules
- **Key feature:** `--design-system` flag outputs token-ready JSON
- **Integration:** Feed output directly into Phase 2 token creation

### `design-taste-frontend` + `impeccable` (Phase 1–5)
- **Source:** Anti-slop ecosystem
- **`impeccable` sub-commands map to phases:**
  - `critique` → Phase 5 audit
  - `audit` → Full pre-flight checklist
  - `polish` → Refinement pass
  - `bolder` → Increase DESIGN_VARIANCE dial
  - `quieter` → Decrease VISUAL_DENSITY dial
- **Integration:** Run at Phase 5 before final verification

### `shadcn` / `21st-dev-builder-v2` (Phase 3)
- **Source:** Component ecosystem
- **Critical rule:** Components **must be re-tokenized** to Phase 2 system
- **Never ship default state** — replace shadcn's default tokens with yours
- **Integration:** Install → extract primitives → apply your tokens → use

### `react-best-practices` / `react-expert` / `frontend-design` (Phase 3)
- **Source:** Framework-specific expertise
- **Use for:** Component architecture, state management, performance patterns
- **Integration:** Apply patterns to your tokenized components

### `ui-animation` / `emilkowalski-motion` / `css-animations` / `animation-designer` (Phase 4)
- **Source:** Motion expertise ecosystem
- **Use for:** Spring physics, gesture-driven animation, complex choreography, reverse-engineering recorded motion
- **Integration:** Motion specs → implement with your motion tokens

### `webapp-testing` / `agent-browser` / `verification-before-completion` (Phase 5)
- **Source:** Verification ecosystem
- **Use for:** Live-render screenshots (Playwright), interaction testing, done-means-done gate
- **Integration:** Run verification → feed screenshots/results into Phase 5 checklist

### `/production-ready-workflow` / `/debug-and-fix-bugs` (Handoff)
- **Source:** Loop Engineer companions
- **Use when:** Design complete → need full-app production hardening
- **`production-ready-workflow`:** 6-phase zero-mock-data production hardening
- **`debug-and-fix-bugs`:** Three-phase debugging with live verification
- **Integration:** Pass token system, component inventory, Design Read

---

## Installation

Companion skills are **optional but recommended**. Install via your harness:

```bash
# Example for Claude Code
# Place in ~/.claude/skills/ or use skill manager

# For OpenCode
# Place in ~/.config/opencode/skills/
```

### Recommended Minimum Set

For production use, install at least:
1. `impeccable` (anti-slop correction)
2. `shadcn` or `21st-dev-builder-v2` (components)
3. `webapp-testing` or `agent-browser` (verification)
4. `ui-animation` (motion depth)

---

## Version Compatibility

| This Skill | Compatible Companions |
|------------|----------------------|
| 1.0.x | Latest versions of all companions as of 2026-08-04 |

Check companion repos for breaking changes:
- [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills)

---

## Writing Custom Companions

To create a companion for a new phase:

1. **Define the phase contract** — what input it needs, what output it produces
2. **Follow the skill spec** — SKILL.md with frontmatter, phases, references
3. **Register in routing table** — add row to this document
4. **Test integration** — run full loop with companion installed
5. **Document fallback** — what bundled reference it replaces

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Companion output doesn't match tokens | Companion used its own defaults | Re-tokenize: replace all companion tokens with Phase 2 tokens |
| Phase 5 fails after companion | Companion skipped states | Run Phase 5 checklist on companion output before integrating |
| Multiple companions conflict | Overlapping responsibilities | Define clear phase boundaries; one companion per phase per category |
| Companion not found | Not installed | Use bundled reference fallback; document in report |