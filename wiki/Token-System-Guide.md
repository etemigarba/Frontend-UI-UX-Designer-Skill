# Token System Guide

The token system is the single source of truth for all design decisions. Components consume **ONLY these tokens** — raw hex, magic spacing numbers, or ad-hoc z-index in a component is a pre-flight failure.

---

## Token Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      :root (light)                          │
├─────────────────────────────────────────────────────────────┤
│  Color Roles    │  Spacing    │  Type      │  Radius        │
│  ────────────   │  ────────   │  ──────    │  ──────        │
│  --color-*      │  --space-*  │  --text-*  │  --radius-*    │
│  --font-*       │             │  --leading-│                │
│                 │             │  --tracking-               │
│  Motion         │  Z-index    │  --measure │  Baseline      │
│  ────────       │  ───────    │            │  ────────      │
│  --duration-*   │  --z-*      │            │  :focus-visible│
│  --ease-*       │             │            │  [data-theme-  │
│                 │             │            │   switching]   │
│  Reduced Motion │             │            │  @media        │
│  ────────────── │             │            │  (prefers-     │
│  @media block   │             │            │   reduced-     │
│                 │             │            │   motion)      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              @media (prefers-color-scheme: dark)           │
├─────────────────────────────────────────────────────────────┤
│  :root:not([data-theme="light"]) { /* dark overrides */ }  │
│  [data-theme="dark"] { /* mirror for manual toggle */ }    │
└─────────────────────────────────────────────────────────────┘
```

---

## Color Roles (Required)

All colors in **OKLCH** for perceptual consistency across light/dark. Hex fallbacks acceptable.

| Token | Purpose | Light Example | Dark Example | Contrast Req |
|-------|---------|---------------|--------------|--------------|
| `--color-background` | Page field | `oklch(0.985 0.003 260)` | `oklch(0.17 0.008 260)` | — |
| `--color-surface` | Cards, wells | `oklch(0.965 0.004 260)` | `oklch(0.21 0.009 260)` | — |
| `--color-surface-elevated` | Raised layers, popovers | `oklch(1 0 0 / 0.72)` | `oklch(0.25 0.01 260)` | — |
| `--color-border` | Subtle borders | `oklch(0.90 0.006 260)` | `oklch(0.30 0.01 260)` | 3:1 vs bg |
| `--color-border-strong` | Emphasis borders | `oklch(0.80 0.008 260)` | `oklch(0.40 0.012 260)` | 3:1 vs bg |
| `--color-text-primary` | Body text, headings | `oklch(0.22 0.01 260)` | `oklch(0.93 0.005 260)` | 4.5:1 |
| `--color-text-secondary` | Metadata, captions | `oklch(0.42 0.012 260)` | `oklch(0.75 0.008 260)` | 4.5:1 |
| `--color-text-muted` | Placeholders, disabled | `oklch(0.55 0.01 260)` | `oklch(0.62 0.008 260)` | 4.5:1* |
| `--color-accent` | **One locked accent** | `oklch(0.55 0.18 260)` | `oklch(0.68 0.16 260)` | 4.5:1 on bg |
| `--color-accent-hover` | Accent hover state | `oklch(0.50 0.18 260)` | `oklch(0.73 0.16 260)` | 4.5:1 on bg |
| `--color-accent-contrast` | Text ON accent | `oklch(0.985 0.003 260)` | `oklch(0.17 0.008 260)` | 4.5:1 |
| `--color-destructive` | Errors, dangerous actions | `oklch(0.55 0.19 25)` | `oklch(0.55 0.19 25)` | 3:1 |
| `--color-success` | Success states | `oklch(0.55 0.15 150)` | `oklch(0.55 0.15 150)` | 3:1 |
| `--color-warning` | Warnings | `oklch(0.70 0.15 80)` | `oklch(0.70 0.15 80)` | 3:1 |
| `--color-focus-ring` | Focus indicator | `var(--color-accent)` | `var(--color-accent)` | 3:1 adj |

*\*Muted text exempt from AA but keep ≥ 3:1 where feasible*

### Color Rules

1. **60-30-10**: Dominant neutral (background), secondary (surface), one accent
2. **One accent, locked** — same hue everywhere; CTA in section 7 ≠ teal
3. **Neutrals have temperature** — warm OR cool greys, never mixed; tint toward accent by 2-5%
4. **OKLCH preferred** — light/dark variants keep perceived lightness/chroma
5. **Hover/active = lightness steps**, not opacity hacks
6. **Saturation < 80%** default; full saturation = stated choice
7. **Status colors = semantic tokens only** — never decoration, never sole meaning carrier

---

## Spacing Scale (Required)

4px or 8px base. Use `--space-*` tokens only.

```css
/* 4px base (default) */
--space-1: 0.25rem;  /* 4px  */
--space-2: 0.5rem;   /* 8px  */
--space-3: 0.75rem;  /* 12px */
--space-4: 1rem;     /* 16px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-12: 3rem;    /* 48px */
--space-16: 4rem;    /* 64px */
--space-24: 6rem;    /* 96px — hero padding cap */
```

| Token | Use Case |
|-------|----------|
| `--space-1` to `--space-3` | Inline gaps, icon spacing |
| `--space-4` | Base unit: component padding, grid gap |
| `--space-6` to `--space-8` | Section rhythm, card internal spacing |
| `--space-12` to `--space-16` | Major section breaks |
| `--space-24` | Hero top padding (capped) |

**No magic numbers** in components. `margin: 17px` → pre-flight failure.

---

## Type Scale (Required)

Fluid via `clamp(min, preferred, max)`. Ratio ≈ 1.2 (dense/Operate) to 1.333 (expressive/Persuade). Base = 16px.

```css
--font-display: "Display-Face", ui-sans-serif, system-ui, sans-serif;
--font-body:    "Body-Face", ui-sans-serif, system-ui, sans-serif;
--font-mono:    "Mono-Face", ui-monospace, "SFMono-Regular", monospace;

--text-xs:   0.75rem;     /* 12px — captions floor */
--text-sm:   0.875rem;    /* 14px — small UI */
--text-base: 1rem;        /* 16px — body floor */
--text-lg:   clamp(1.125rem, 1rem + 0.5vw, 1.25rem);
--text-xl:   clamp(1.25rem, 1.1rem + 0.9vw, 1.563rem);
--text-2xl:  clamp(1.563rem, 1.3rem + 1.4vw, 1.953rem);
--text-3xl:  clamp(1.953rem, 1.5rem + 2.2vw, 2.441rem);
--text-4xl:  clamp(2.441rem, 1.8rem + 3.2vw, 3.5rem);  /* hero band */

--leading-tight: 1.15;   /* headings; ≥1.1 if italic descenders */
--leading-body:  1.6;    /* body copy */

--tracking-display: -0.02em;  /* large display */
--tracking-label:    0.06em;  /* small caps / labels only */

--measure: 65ch;  /* max line width */
```

### Type Rules

- **Two families max** (display + body) + optional mono
- Display face = personality (hero, section heads); use with restraint
- Body face = workhorse (excellent at 14-18px, tall x-height, full weights)
- Variable fonts preferred; subset + preload display face
- `text-wrap: balance` on headings; `text-wrap: pretty` on body
- Real typographic quotes (“ ”) or none

---

## Radius System (Required)

**One system per page** — all-sharp, all-soft (12-16px), or all-pill. Or documented mixed rule applied everywhere.

```css
--radius-interactive: 0.75rem;  /* buttons, inputs — 12px */
--radius-container:   1rem;     /* cards, dialogs — 16px */
--radius-full:        9999px;   /* pills — ONLY if system is pill */
```

| System | Interactive | Container | Use Case |
|--------|-------------|-----------|----------|
| Sharp | 0 | 0 | Neo-Brutalist, Industrial |
| Soft | 0.75rem (12px) | 1rem (16px) | Most directions |
| Pill | 9999px | 9999px | Playful Geometric |

**Round buttons in square layout = broken design** (Shape Consistency Lock).

---

## Elevation (Required)

Shadows tinted toward background hue. Layered small shadows > one big black blur. Dark mode = lighter surface, not heavier shadow.

```css
/* Light */
--shadow-sm: 0 1px 2px oklch(0.25 0.02 260 / 0.06);
--shadow-md: 0 2px 6px oklch(0.25 0.02 260 / 0.07),
             0 8px 24px oklch(0.25 0.02 260 / 0.06);

/* Dark (in @media block) */
--shadow-sm: 0 1px 2px oklch(0 0 0 / 0.4);
--shadow-md: 0 2px 8px oklch(0 0 0 / 0.45);
```

**Cards only when elevation = real hierarchy**. Otherwise: borders (`border-t`, `divide-y`) or negative space.

---

## Motion Tokens (Required)

From `references/motion.md`. Register as CSS custom properties.

```css
--duration-fast:   150ms;  /* press, small popovers */
--duration-base:   200ms;  /* hover color, dropdowns */
--duration-slow:   300ms;  /* modals, drawers, slides */

--ease-enter:  cubic-bezier(0.22, 1, 0.36, 1);  /* entrances, transform hover */
--ease-move:   cubic-bezier(0.25, 1, 0.5, 1);   /* slides, panels, drawers */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);  /* iOS-feel drawer */
```

### Duration Guidelines

| Element | Duration | Easing |
|---------|----------|--------|
| Button press | 100-160ms | enter |
| Tooltips/popovers | 125-200ms | ease-out / enter |
| Dropdowns/selects | 150-250ms | enter |
| Hover color/opacity | ~200ms | ease |
| Hover transform/scale | 100-150ms | enter |
| Modals/drawers | 200-350ms | enter / drawer |
| Move/slide | 200-300ms | move |
| Page transitions | 250-400ms | enter / move |
| Expressive moments | up to ~1000ms | spring / custom |

**Routine UI < 300ms**. Avoid `ease-in` (lags). Springs: critically damped, subtle overshoot max.

---

## Z-Index Scale (Required)

Documented scale — **nothing outside it**.

```css
--z-sticky:  100;  /* sticky nav */
--z-overlay: 200;  /* scrims */
--z-modal:   300;  /* dialogs, drawers */
--z-toast:   400;  /* toasts */
--z-top:     500;  /* grain/pointer-events-none overlays */
```

**Ad-hoc `z-50`, `z-[9999]` = pre-flight failure**.

---

## Dark Mode Protocol

### Token Swap (Not Inversion)

```css
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* Hierarchy parity: what pops in light pops in dark */
    /* Brand fidelity: accent recognizable — desaturate slightly, raise lightness */
    --color-background:       oklch(0.17 0.008 260);  /* off-black */
    --color-surface:          oklch(0.21 0.009 260);
    --color-surface-elevated: oklch(0.25 0.01 260);   /* LIGHTER = elevated */
    --color-accent:           oklch(0.68 0.16 260);   /* lifted + desaturated */
    /* ... all other tokens swapped ... */
  }
}
[data-theme="dark"] { /* mirror for manual toggle */ }
```

### Rules

- No pure `#000000` or `#ffffff` — off-black/off-white keep depth
- Elevation in dark = **lighter surface**, not heavier shadow
- **Theme Lock**: one theme per page; no mid-scroll inversion (exception: one brief-justified color-block)
- Default to `prefers-color-scheme`; manual toggle when either mode loses brand expression
- **Test both modes before finishing** — never ship page seen in only one

---

## Reduced Motion Block (Required)

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

Every animation must have a reduced-motion path (instant state change or opacity-only fade).

---

## Baseline Behaviors (Included in Template)

```css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;   /* styled, never removed */
}

[data-theme-switching] * { transition: none !important; }
```

---

## Framework Integration

### Tailwind CSS

Mirror in `tailwind.config.js` or `@theme` (v4):

```js
// tailwind.config.js
theme: {
  extend: {
    colors: {
      background: 'var(--color-background)',
      surface: 'var(--color-surface)',
      accent: 'var(--color-accent)',
      // ... all color roles
    },
    spacing: {
      1: 'var(--space-1)',
      2: 'var(--space-2)',
      // ... map all space tokens
    },
    borderRadius: {
      interactive: 'var(--radius-interactive)',
      container: 'var(--radius-container)',
      full: 'var(--radius-full)',
    },
    // ... etc
  }
}
```

### shadcn/ui

CSS variables map directly to shadcn's `--background`, `--foreground`, `--primary`, etc.

### CSS-in-JS / Styled Components

```js
import { css } from 'styled-components';

export const tokens = css`
  :root {
    --color-accent: oklch(0.55 0.18 260);
    /* ... all tokens ... */
  }
`;
```

---

## Validation Checklist

- [ ] All tokens defined in one place
- [ ] Light + dark themes complete
- [ ] OKLCH used for color (or documented hex fallbacks)
- [ ] One accent, locked page-wide
- [ ] One radius system (or documented mixed rule)
- [ ] Z-index scale documented; no ad-hoc values
- [ ] Motion tokens match `references/motion.md` curves
- [ ] Reduced-motion block present
- [ ] Focus-visible styled (not removed)
- [ ] Theme-switching transition disable present
- [ ] Components consume tokens only (grep for raw hex/z-index/spacing)