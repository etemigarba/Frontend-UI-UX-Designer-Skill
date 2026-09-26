# Documentation

Welcome to the Frontend UI/UX Designer Skill documentation. This skill provides a complete, award-caliber design workflow for Claude Code and compatible agent harnesses.

## Quick Navigation

| Document | Description |
|---|---|
| [Getting Started](getting-started.md) | Installation, invocation, and first design |
| [Design Loop](design-loop.md) | Deep dive into the 5-phase loop |
| [Surface Modes](surface-modes.md) | Persuade, Operate, Read, Experience |
| [Design Tokens](design-tokens.md) | Semantic token system reference |
| [UX Playbook](ux-playbook.md) | Layout, components, forms, content |
| [Motion Guide](motion-guide.md) | Motion principles and implementation |
| [Accessibility](accessibility.md) | WCAG 2.2 AA practical audit |
| [Pre-Flight Checklist](preflight-checklist.md) | Termination gate checklist |
| [Companion Skills](companion-skills.md) | Integration and routing guide |
| [Examples](../examples/) | Working implementations for each surface mode |

## Skill Overview

The Frontend UI/UX Designer Skill transforms an AI agent into an award-caliber Design Director and Design Engineer. It enforces a **bounded, verifiable design loop** that produces distinctive, accessible, fast, and complete interfaces — the product of deliberate choices, never defaults.

### Core Philosophy

1. **The brief wins** — Honor pinned aesthetics, eras, fonts, and palettes
2. **Refinement preserves; redesign replaces** — Never polish a discarded look
3. **Verify in bounded passes** — Max 2 fix passes, then ship with honest report

### Design Loop

```text
Perceive → Direction → System → Build → Motion → Reflect
   ▲                                                │
   └──────── (bounded: max 2 fix passes) ───────────┘
```

| Phase | Focus | Reference |
|-------|-------|-----------|
| 0. Perceive | Context gate: subject, audience, mode, stack, dials | — |
| 1. Direction | Aesthetic family, palette, type, layout, signature | [design-direction.md](../references/design-direction.md) |
| 2. System | Semantic tokens (light + dark), spacing, type, radius, motion, z-index | [design-tokens-template.css](../assets/design-tokens-template.css) |
| 3. Build | Semantic HTML, layout, complete states, real content | [ux-playbook.md](../references/ux-playbook.md) |
| 4. Motion | Feedback, orientation, continuity, delight | [motion.md](../references/motion.md) |
| 5. Reflect | Accessibility, performance, checklist verification | [accessibility.md](../references/accessibility.md) + [preflight-checklist.md](../references/preflight-checklist.md) |

## Surface Modes

The mode re-weights every downstream decision:

| Mode | Visitor Goal | Density | Motion | Use Case |
|------|-------------|---------|--------|----------|
| **Persuade** | Decide and act | Low | Medium | Landing, marketing, pricing |
| **Operate** | Complete a task | High | Low | App UI, dashboards, editors |
| **Read** | Understand | Medium | Low | Docs, articles, changelogs |
| **Experience** | Be inside the work | Variable | High | Portfolios, galleries |

## Non-Negotiables

These are pre-flight failures when violated:

1. **Contrast** — WCAG AA everywhere (both themes)
2. **Focus** — `:focus-visible` styled, never removed
3. **States** — Complete state sets for all interactive elements
4. **Forms** — Label above input; no placeholder-as-label
5. **Touch** — Targets ≥ 44×44px with ≥ 8px spacing
6. **Motion** — `transform`/`opacity` only; reduced-motion path required
7. **Locks** — One theme, accent, radius, copy register per page
8. **Tokens** — No raw hex, magic numbers, ad-hoc z-index
9. **Performance** — LCP < 2.5s, INP < 200ms, CLS < 0.1
10. **Content Integrity** — No fabricated precision, no fake screenshots
11. **Honest Verification** — Evidence-based, never asserted

## Companion Skills

This skill orchestrates; companions add depth:

| Phase | Companion | Purpose |
|-------|-----------|---------|
| 0–1 | `brainstorming` | Diverge before committing |
| 1–2 | `ui-ux-pro-max` | Styles/palettes/font-pairing database |
| 1–5 | `design-taste-frontend`, `impeccable` | Anti-slop bias correction |
| 3 | `shadcn`, `21st-dev-builder-v2` | Source components (re-tokenized) |
| 3 | `react-best-practices`, `frontend-design` | Stack-correct architecture |
| 4 | `ui-animation`, `emilkowalski-motion` | Deep motion specs |
| 5 | `webapp-testing`, `agent-browser` | Live-render verification |
| Handoff | `production-ready-workflow`, `debug-and-fix-bugs` | Full-app production readiness |

## License

MIT License — Copyright (c) 2026 Prof. Etemi Joshua Garba

[Explicit permission](LICENSE#explicit-permission-statement) for adoption, editing, refactoring, and redistribution.