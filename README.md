# Frontend UI/UX Designer Skill

> **Award-caliber frontend UI/UX design workflow for Claude Code** — A 5-phase design loop with semantic tokens, WCAG 2.2 AA accessibility, Core Web Vitals budgets, anti-default discipline, and four surface modes (Persuade, Operate, Read, Experience).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Year: 2026](https://img.shields.io/badge/Year-2026-blue.svg)]
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-purple.svg)](https://claude.ai/code)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-green.svg)](https://opencode.ai)
[![Agentic Engineering](https://img.shields.io/badge/Agentic%20Engineering-Skill-orange.svg)](https://github.com/etemigarba/Agentic-Engineering-Skills)
[![Build Status](https://img.shields.io/github/actions/workflow/status/etemigarba/Frontend-UI-UX-Designer-Skill/validate.yml?branch=main&label=CI)](https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/actions)
[![Issues](https://img.shields.io/github/issues/etemigarba/Frontend-UI-UX-Designer-Skill)](https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/issues)
[![Stars](https://img.shields.io/github/stars/etemigarba/Frontend-UI-UX-Designer-Skill?style=social)](https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/stargazers)

## Overview

This skill transforms an AI coding agent into an **award-caliber Design Director and Design Engineer**. It enforces a **bounded, verifiable design loop** that produces distinctive, accessible, fast, and complete interfaces — the product of deliberate choices, never defaults.

### Core Philosophy

1. **The brief wins** — Honor pinned aesthetics, eras, fonts, and palettes even when they collide with anti-default rules
2. **Refinement preserves; redesign replaces** — Never polish a discarded look
3. **Verify in bounded passes** — Max 2 fix passes, then ship with honest report

## Key Features

| Feature | Description |
|---------|-------------|
| **5-Phase Design Loop** | Perceive → Direction → System → Build → Motion → Reflect (max 2 fix passes) |
| **4 Surface Modes** | Persuade, Operate, Read, Experience — each re-weights every downstream decision |
| **Semantic Token System** | OKLCH color, fluid type scale, 4px/8px spacing, one radius system, motion tokens, documented z-index |
| **WCAG 2.2 AA Compliance** | Contrast, focus, keyboard, motion, reflow — verified, not asserted |
| **Core Web Vitals Budgets** | LCP < 2.5s, INP < 200ms, CLS < 0.1 |
| **Anti-Default Discipline** | 12 saturated default patterns banned; rotation across 14 direction families |
| **Complete State Coverage** | Every interactive element (default/hover/focus/active/disabled/loading), every async view (loading/empty/error/ready) |
| **Companion Skill Routing** | Delegates to `ui-ux-pro-max`, `impeccable`, `design-taste-frontend`, `ui-animation`, `shadcn`, `21st-dev-builder-v2`, `webapp-testing`, `agent-browser` when installed |

## The Design Loop

```text
Perceive → Direction → System → Build → Motion → Reflect
   ▲                                                │
   └──────── (bounded: max 2 fix passes) ───────────┘
```

| Phase | Focus | Reference | Exit Criterion |
|-------|-------|-----------|----------------|
| **0. Perceive** | Context gate: subject, audience, surface mode, stack, refine vs redesign, dials | — | All explicit in Design Read |
| **1. Direction** | Aesthetic family, palette (4-6 hex), type pairing, layout concept, signature element | `references/design-direction.md` | Anti-default test passed |
| **2. System** | Semantic tokens (light + dark), spacing, type scale, radius, shadows, motion, z-index | `assets/design-tokens-template.css` | Tokens in one place, both themes defined |
| **3. Build** | Semantic HTML, layout, complete state sets, real content strategy | `references/ux-playbook.md` | All states implemented, hard rules pass |
| **4. Motion** | Feedback, orientation, continuity, delight — transform/opacity only | `references/motion.md` | Every animation justifiable, reduced-motion verified |
| **5. Reflect** | Automated + manual accessibility, performance, checklist | `references/accessibility.md` + `preflight-checklist.md` | Every box honestly ticked or reported |

## Surface Modes

The mode names what the visitor's success looks like on this surface, and re-weights every downstream decision:

| Mode | Visitor Goal | Density | Motion | Example Use Cases |
|------|--------------|---------|--------|-------------------|
| **Persuade** | Decide and act | Low | Medium | Landing pages, marketing, pricing |
| **Operate** | Complete a task | High | Low | App UI, dashboards, editors, settings |
| **Read** | Understand | Medium | Low | Docs, articles, changelogs |
| **Experience** | Be inside the work | Variable | High | Portfolios, galleries, immersive stories |

## Quick Start

### Installation

```bash
# For Claude Code
# Place the skill folder in your .claude/skills/ directory
cp -r frontend-ui-ux-designer-skill ~/.claude/skills/

# For OpenCode
# Place in .config/opencode/skills/
cp -r frontend-ui-ux-designer-skill ~/.config/opencode/skills/

# Or use the skill archive
# frontend-ui-ux-designer.skill
```

### Invocation

```markdown
/frontend-ui-ux-designer
```

Or invoke implicitly with phrases like:
- "design a landing page for..."
- "make this look better / professional / modern"
- "improve the UX of..."
- "this looks generic or AI-generated"
- "pick a palette / font pairing"
- "add dark mode"
- "make it responsive"
- "add animations"

### Design Read Output

Before any design work, the skill outputs a **Design Read**:

```
Read: <subject> for <audience> · mode=<Persuade|Operate|Read|Experience> · stack=<React+Tailwind|Vue+CSS|HTML+CSS|...> · <refine|redesign> · dials V<1-10>/M<1-10>/D<1-10>
```

- **V** = DESIGN_VARIANCE (centered/safe → asymmetric/bold)
- **M** = MOTION_INTENSITY (static → choreographed)
- **D** = VISUAL_DENSITY (airy → dense)

## Non-Negotiables (Pre-Flight Failures)

These are **hard requirements** — violating any is shipping broken work:

1. **Contrast** — WCAG AA everywhere (4.5:1 body, 3:1 large/UI) — both themes
2. **Focus** — `:focus-visible` styled on every interactive element; never removed
3. **States** — No interactive element ships with only resting state
4. **Forms** — Label above input; placeholder-as-label banned; errors specific, inline, below field
5. **Touch** — Targets ≥ 44×44px with ≥ 8px spacing
6. **Motion** — `transform`/`opacity` only; `transition: all` banned; reduced-motion path required
7. **Locks** — One theme, one accent, one radius system, one copy register per page
8. **Tokens** — No raw hex, magic spacing, or ad-hoc z-index in components
9. **Performance** — LCP < 2.5s, INP < 200ms, CLS < 0.1
10. **Content Integrity** — No fabricated precision, no div-fake screenshots, no AI-tell filler copy
11. **Honest Verification** — Never claim render, contrast, or Lighthouse score not observed

## Companion Skills (Delegation)

This skill is the **orchestrator**. Companions own depth inside a phase; their output still passes Phase 5's checklist.

| Phase | Companion Skill | Purpose |
|-------|-----------------|---------|
| 0–1 Direction | `brainstorming` (obra/superpowers) | Diverge before committing |
| 1–2 System | `ui-ux-pro-max` | Styles/palettes/font-pairing/UX-rules database; `--design-system` output feeds Phase 2 |
| 1–5 Taste | `design-taste-frontend`, `impeccable` | Anti-slop bias correction; `impeccable` sub-commands (`critique`, `audit`, `polish`, `bolder`, `quieter`) |
| 3 Components | `shadcn`, `21st-dev-builder-v2` | Source/install components — **always re-tokenized** to Phase 2's system |
| 3 Implementation | `react-best-practices`, `react-expert`, `frontend-design` | Stack-correct component architecture |
| 4 Motion | `ui-animation`, `emilkowalski-motion`, `css-animations`, `animation-designer` | Deep motion specs, springs, gesture work, reverse-engineering recorded motion |
| 5 Verification | `webapp-testing`, `agent-browser`, `verification-before-completion` | Live-render screenshots, interaction testing, done-means-done gate |
| Handoff | `production-ready-workflow`, `debug-and-fix-bugs` | Full-app production readiness / bug hunting |

## Bundled References

| File | Phase | Contents |
|------|-------|----------|
| `references/design-direction.md` | 1 | Direction families, typography & color systems, anti-default discipline |
| `references/ux-playbook.md` | 3 | UX laws, layout hard rules, navigation, forms, states, content & copy |
| `references/motion.md` | 4 | Duration/easing tables, motion principles, performance, reduced motion |
| `references/accessibility.md` | 5 | WCAG 2.2 AA practical audit (POUR) |
| `references/preflight-checklist.md` | 5 | Termination gate: mechanical checks + full ship checklist |
| `assets/design-tokens-template.css` | 2 | Semantic token skeleton: light+dark, motion, z-index, reduced-motion |

## Documentation

| Guide | Description |
|-------|-------------|
| [Getting Started](docs/getting-started.md) | Installation, invocation, first design |
| [Design Loop Deep Dive](docs/design-loop.md) | Phase-by-phase guide with entry/exit criteria |
| [Surface Modes](docs/surface-modes.md) | Persuade, Operate, Read, Experience in detail |
| [Design Tokens](docs/design-tokens.md) | Semantic token system reference |
| [UX Playbook](docs/ux-playbook.md) | Layout, components, forms, content strategy |
| [Motion Guide](docs/motion-guide.md) | Motion principles and implementation |
| [Accessibility](docs/accessibility.md) | WCAG 2.2 AA practical audit |
| [Pre-Flight Checklist](docs/preflight-checklist.md) | Termination gate checklist |
| [Companion Skills](docs/companion-skills.md) | Integration and routing guide |
| [Examples](docs/examples/) | Working implementations for each surface mode |

## Examples

| Example | Mode | Stack | Description |
|---------|------|-------|-------------|
| [Landing Page](docs/examples/landing-page-persuade/) | Persuade | React + Tailwind | Developer tool landing with hero, features, pricing |
| [Dashboard](docs/examples/dashboard-operate/) | Operate | Vue + CSS | Analytics dashboard with data density |
| [Documentation](docs/examples/docs-read/) | Read | HTML + CSS | Technical docs with comprehension focus |
| [Portfolio](docs/examples/portfolio-experience/) | Experience | Svelte + CSS | Creative portfolio with immersive moments |

## Repository Structure

```
frontend-ui-ux-designer-skill/
├── SKILL.md                          # Skill manifest (entry point)
├── LICENSE                           # MIT License with explicit permission
├── README.md                         # This file
├── CHANGELOG.md                      # Version history
├── CONTRIBUTING.md                   # Contribution guidelines
├── SECURITY.md                       # Security policy
├── package.json                      # npm metadata
├── .markdownlint.json                # Markdown lint config
├── assets/
│   └── design-tokens-template.css    # Semantic token skeleton
├── references/                       # Phase-loaded reference files
│   ├── design-direction.md
│   ├── ux-playbook.md
│   ├── motion.md
│   ├── accessibility.md
│   └── preflight-checklist.md
├── docs/                             # Documentation guides
│   ├── index.md
│   ├── getting-started.md
│   ├── design-loop.md
│   ├── surface-modes.md
│   ├── design-tokens.md
│   ├── ux-playbook.md
│   ├── motion-guide.md
│   ├── accessibility.md
│   ├── preflight-checklist.md
│   ├── companion-skills.md
│   └── examples/                     # Surface-mode examples
├── scripts/
│   └── validate-skill.py             # Skill structure validator
├── .github/
│   ├── workflows/                    # CI/CD workflows
│   │   ├── validate.yml
│   │   └── release.yml
│   ├── ISSUE_TEMPLATE/               # Issue templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── design_review.md
│   └── PULL_REQUEST_TEMPLATE.md
├── wiki/                             # GitHub Wiki content (9 pages)
└── frontend-ui-ux-designer.skill     # Skill archive
└── frontend-ui-ux-designer.zip       # Skill archive (alt)
```

## Installation for Development

```bash
# Clone the repo
git clone https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill.git
cd Frontend-UI-UX-Designer-Skill

# Validate skill structure
python scripts/validate-skill.py
```

## Validation

Run the skill validator to ensure structural integrity:

```bash
python scripts/validate-skill.py
```

This validates:
- SKILL.md frontmatter completeness
- Reference file existence and phase alignment
- Asset template validity
- Cross-reference link integrity
- Version consistency
- Example README completeness

## Related Repositories

| Repository | Description |
|------------|-------------|
| [Loop-Engineer-Skill](https://github.com/etemigarba/Loop-Engineer-Skill) | Bounded, self-correcting agent loops (Act→Observe→Verify→Retry→Stop) |
| [Agentic-Engineering-Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) | 33 technology-agnostic skills across 6 SDLC categories |
| [Systematic-Implementation-Skill](https://github.com/etemigarba/Systematic-Implementation-Skill) | Gate-controlled SDLC meta-skill with 13 phases |
| [Production-Ready-Workflow-Skill](https://github.com/etemigarba/Production-Ready-Workflow-Skill) | 6-phase zero-mock-data production hardening |
| [Debug-and-Fix-Bugs-Skill](https://github.com/etemigarba/Debug-and-Fix-Bugs-Skill) | Three-phase debugging with live verification |
| [Etemi-Prompt-Enhancer-Skill](https://github.com/etemigarba/Etemi-Prompt-Enhancer-Skill) | Transform rough prompts into production-ready instructions |
| [Practical-React](https://github.com/etemigarba/Practical-React) | Code-first React course (26 lessons, 3 projects) |
| [Practical-Next.js](https://github.com/etemigarba/Practical-Next.js) | Next.js 16 App Router companion codebase |

All cross-references verified as of 2026-09-26 — no broken links.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Follow the existing code style and conventions
- All changes must pass the pre-flight checklist
- Update documentation for any new features
- Add tests for new functionality

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

## License

MIT License — Copyright (c) 2026 Prof. Etemi Joshua Garba

[Explicit permission granted](LICENSE#explicit-permission-statement) for adoption, editing, refactoring, and redistribution without explicit approval.

## Author

**Prof. Etemi Joshua Garba**  
Ethereal Multimedia Technology Ltd.  
[GitHub](https://github.com/etemigarba) · [Website](https://ethereal.ng/) · [ORCID](https://orcid.org/0000-0001-6707-0220) · [LinkedIn](https://www.linkedin.com/in/ejgarba/)

---

**Repository**: https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill  
**Issues**: https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/issues  
**Discussions**: https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/discussions  
**Wiki**: https://github.com/etemigarba/Frontend-UI-UX-Designer-Skill/wiki