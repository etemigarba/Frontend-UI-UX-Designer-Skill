# Frontend UI/UX Designer Skill Wiki

Welcome to the wiki for the **Frontend UI/UX Designer Skill** — an award-caliber design workflow for Claude Code and compatible agent harnesses.

## Quick Links

| Page | Description |
|------|-------------|
| [Design Loop Deep Dive](Design-Loop-Deep-Dive) | Complete phase-by-phase guide |
| [Anti-Default Discipline](Anti-Default-Discipline) | How to avoid generic AI designs |
| [Token System Guide](Token-System-Guide) | Semantic tokens, light/dark, OKLCH |
| [Motion Principles](Motion-Principles) | When, how, and why to animate |
| [Accessibility Checklist](Accessibility-Checklist) | WCAG 2.2 AA practical audit |
| [Companion Skill Integration](Companion-Skill-Integration) | Routing table and delegation |
| [FAQ](FAQ) | Common questions and answers |
| [Migration Guide](Migration-Guide) | Upgrading between versions |

## About This Skill

This skill transforms an AI agent into an award-caliber Design Director and Design Engineer. It enforces a **bounded, verifiable design loop** that produces distinctive, accessible, fast, and complete interfaces — the product of deliberate choices, never defaults.

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

## Surface Modes

| Mode | Purpose | Density | Motion |
|------|---------|---------|--------|
| **Persuade** | Visitor decides and acts | Low | Medium |
| **Operate** | Visitor completes a task | High | Low |
| **Read** | Visitor understands | Medium | Low |
| **Experience** | Visitor is inside the work | Variable | High |

## Non-Negotiables

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

## Getting Started

1. Install the skill in your harness (`~/.claude/skills/` or `~/.config/opencode/skills/`)
2. Invoke with `/frontend-ui-ux-designer` or use triggering phrases
3. Provide a brief — the skill outputs a Design Read, then runs the full loop

## Resources

- [GitHub Repository](https://github.com/etemigarba/frontend-ui-ux-designer-skill)
- [Issues](https://github.com/etemigarba/frontend-ui-ux-designer-skill/issues)
- [Discussions](https://github.com/etemigarba/frontend-ui-ux-designer-skill/discussions)
- [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills)

## License

MIT License — Copyright (c) 2026 Prof. Etemi Joshua Garba

[Explicit permission](../LICENSE#explicit-permission-statement) for adoption, editing, refactoring, and redistribution.