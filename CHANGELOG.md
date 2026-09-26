# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-04

### Added
- Initial release of Frontend UI/UX Designer Skill
- 5-phase design loop (Perceive → Direction → System → Build → Motion → Reflect)
- 4 surface modes: Persuade, Operate, Read, Experience
- Semantic token system with OKLCH color, fluid type, 4px/8px spacing, radius, shadows, motion, z-index
- WCAG 2.2 AA accessibility reference (POUR organization)
- Pre-flight checklist termination gate (mechanical + full checklist)
- Anti-default discipline with 14 direction families and 12 saturated defaults banned
- Complete state coverage for interactive elements and async views
- Core Web Vitals budgets (LCP < 2.5s, INP < 200ms, CLS < 0.1)
- Companion skill routing table for 8 integration points
- Bundled references: design-direction, ux-playbook, motion, accessibility, preflight-checklist
- Design tokens template (CSS custom properties, light + dark themes)
- MIT License with explicit permission for adoption/editing/refactoring

### Design Decisions
- **Rotation rule**: Direction families never reused consecutively unless brief pins
- **Theme Lock**: One theme per page, no mid-scroll inversion
- **Accent Lock**: One accent locked page-wide
- **Radius Lock**: One corner-radius system per page
- **Copy Register**: One copy register per page (technical-mono vs editorial vs marketing)
- **Icon Library**: One SVG icon library, one stroke weight, `currentColor`
- **Verification**: Evidence-based (screenshots, measurements, tool output), never asserted
- **Fix Passes**: Maximum 2 fix passes for entire cycle

---

## [Unreleased]

### Planned
- Example implementations for all 4 surface modes
- MkDocs documentation site
- npm package publication
- GitHub Actions CI workflow
- Wiki content migration