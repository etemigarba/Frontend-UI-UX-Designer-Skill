# Surface Modes

The surface mode names **what the visitor's success looks like** on this surface. It re-weights every downstream decision — from density to motion to copy register.

---

## The Four Modes

| Mode | Visitor Goal | Design Priority | Density | Motion | Copy Register |
|------|-------------|-----------------|---------|--------|---------------|
| **Persuade** | Decide and act | Earn attention; hero is a thesis | Low | Medium | Marketing punch |
| **Operate** | Complete a task | Scanability, consistency, native expectations | High | Low | Technical-mono |
| **Read** | Understand | Comprehension (45-75ch, generous leading) | Medium | Low | Editorial |
| **Experience** | Be inside the work | Artifact leads; interface recedes | Variable | High | Brand-expressive |

---

## Persuade Mode

**Use for:** Landing pages, marketing sites, pricing pages, launch pages, waitlist pages

### Characteristics

- **Hero is a thesis** — not a template. Opens with the most characteristic thing in the subject's world.
- **Earn attention** — every element fights for the visitor's decision.
- **Signature element critical** — spend boldness budget here; keep surroundings quiet.
- **Density low** — generous whitespace, focused CTAs.
- **Motion medium** — entrance reveal, feedback on key controls, deliberate delight moments.
- **Copy register: marketing punch** — headline ≤ 8 words, sub ≤ 25 words, active verbs.

### Layout Patterns

- Hero: headline ≤ 2 lines, subtext ≤ 20 words, primary CTA above fold
- Sections: ≥ 4 distinct layout families; zigzag ≤ 2 consecutive
- Trust indicators (logos, stats) **under** hero, not in it
- Bento grids for feature clusters (asymmetric, 2-3 visually varied cells)

### Example Brief

> "Design a landing page for 'CodeMetrics' — a VS Code extension showing real-time complexity metrics. Audience: senior developers. Goal: install extension."

### Design Read

```
Read: CodeMetrics VS Code extension for senior developers · mode=Persuade · stack=React+Tailwind · redesign · dials V7/M4/D4
```

---

## Operate Mode

**Use for:** App UI, dashboards, editors, settings, admin panels, data tools, IDEs

### Characteristics

- **Task completion > expression** — native expectations outrank brand expression.
- **Scanability paramount** — dense but organized; Miller's Law (5±2 chunks).
- **Consistency > novelty** — platform conventions (Jakob's Law).
- **Brand lives in precise details** — radius, focus rings, transition timing.
- **Density high** — compact spacing, small type, efficient layouts.
- **Motion low** — near-invisible feedback; no mount animations.
- **Copy register: technical-mono** — precise, terse, consistent terminology.

### Layout Patterns

- Single-line nav ≤ 80px; back always works; deep-linkable states
- Data tables: grouped clusters, not 10-row hairline tables
- Forms: single-column default; validate on blur; optional marked not required
- Panels/drawers for secondary workflows; modals for destructive confirmations
- Keyboard shortcuts for power users; no hover-only paths

### Example Brief

> "Design a dashboard for 'CodeMetrics' showing file complexity, function metrics, and trend charts. Audience: senior developers using it daily. Stack: React + Tailwind."

### Design Read

```
Read: CodeMetrics dashboard for senior developers · mode=Operate · stack=React+Tailwind · refinement · dials V3/M2/D8
```

---

## Read Mode

**Use for:** Documentation, articles, changelogs, blog posts, specifications, help centers

### Characteristics

- **Comprehension first** — measure 45-75ch, generous leading (1.6+), readable type.
- **Structure for scanning** — clear hierarchy, skip links, anchored headings.
- **Then make staying pleasant** — subtle motion, comfortable dark mode, good contrast.
- **Density medium** — not sparse, not dense; rhythm serves reading flow.
- **Motion low** — only scroll-reveal for chapter transitions, TOC highlight.
- **Copy register: editorial** — literary quality, varied sentence structure, proper quotes.

### Layout Patterns

- Single-column primary content (max-width 65ch)
- Sticky TOC/sidebar on desktop; collapsible on mobile
- Code blocks with copy buttons, line numbers, language labels
- Version switcher, edit-on-GitHub link, last-updated timestamp
- Search integration (Algolia, Pagefind, or native)
- Print stylesheet for offline reading

### Example Brief

> "Design documentation for 'CodeMetrics' API reference, getting started guide, and configuration docs. Audience: developers integrating the tool."

### Design Read

```
Read: CodeMetrics documentation for developers · mode=Read · stack=Next.js+MDX · redesign · dials V4/M2/D5
```

---

## Experience Mode

**Use for:** Portfolios, galleries, creative showcases, immersive stories, brand experiences

### Characteristics

- **Artifact leads from first viewport** — interface recedes, content commands.
- **No generic templates** — every page is bespoke to the work shown.
- **Motion high** — choreographed entrances, scroll-driven narratives, gestures.
- **Density variable** — breathing room for hero work; density for case study detail.
- **Copy register: brand-expressive** — voice matches the creator's personality.
- **Dark mode often default** — but must work in light too.

### Layout Patterns

- Full-bleed hero with work front-and-center
- Scroll-driven chapter transitions (IntersectionObserver / CSS scroll-driven)
- Case studies: problem → process → outcome → reflection
- Image sequences with captions, not grids
- Minimal chrome; navigation hidden until needed
- WebGL/Canvas for 3D/interactive work (with static fallback)

### Example Brief

> "Design a portfolio for a creative technologist showing 6 projects: 3 interactive installations, 2 generative art pieces, 1 data visualization. Audience: potential clients/collaborators."

### Design Read

```
Read: Creative technologist portfolio for clients · mode=Experience · stack=Svelte+Canvas · redesign · dials V9/M8/D4
```

---

## Choosing the Mode

**Choose from the requested surface, not the product:**

| Requested Surface | Mode |
|-------------------|------|
| Landing page for dev tool | Persuade |
| Dashboard for same dev tool | Operate |
| Docs for same dev tool | Read |
| Portfolio of the dev tool creator | Experience |

### Decision Checklist

- [ ] What does the visitor **need to do** on this surface?
- [ ] Is the primary goal **persuasion**, **operation**, **comprehension**, or **immersion**?
- [ ] Does the brief **explicitly name** a mode? (Honor it)
- [ ] If ambiguous, **ask one question** — do not guess.

---

## Mode-Specific Dial Defaults

| Dial | Persuade | Operate | Read | Experience |
|------|----------|---------|------|------------|
| **V** (Variance) | 6-8 | 2-4 | 3-5 | 7-10 |
| **M** (Motion) | 4-6 | 1-3 | 1-3 | 6-9 |
| **D** (Density) | 3-5 | 7-9 | 4-6 | 3-7 |

*Explicit brief instructions always override these defaults.*

---

## Cross-Mode Consistency (Same Product)

When designing multiple surfaces for one product:

| Element | Consistent Across Modes | Mode-Specific |
|---------|------------------------|---------------|
| Brand color (accent) | ✅ Yes | — |
| Typography (body face) | ✅ Yes | Display face may vary |
| Radius system | ✅ Yes | — |
| Icon library | ✅ Yes | — |
| Copy register | — | ✅ Per mode |
| Density | — | ✅ Per mode |
| Motion intensity | — | ✅ Per mode |
| Layout families | — | ✅ Per mode |

**Rule:** Product truth, content, and function stay consistent. Look and feel adapt to mode.