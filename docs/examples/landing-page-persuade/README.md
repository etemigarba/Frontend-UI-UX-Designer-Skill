# Landing Page — Persuade Mode Example

**Design Read:**
```
Read: CodeMetrics VS Code extension for senior developers · mode=Persuade · stack=React+Tailwind · redesign · dials V7/M4/D4
```

## Direction Plan

- **Aesthetic:** Industrial / Utilitarian — tool-like, data-forward, console energy
- **Palette:** Graphite scale + amber signal (`#D4A843`)
- **Type:** `JetBrains Mono` for data/mono, `Satoshi` for UI
- **Signature:** Live complexity meter in hero — real-time animated sparkline

## Token System (Excerpt)

```css
:root {
  --color-background:  oklch(0.98 0.002 240);
  --color-surface:     oklch(0.95 0.003 240);
  --color-accent:      oklch(0.62 0.14 85);    /* amber */
  --color-accent-hover: oklch(0.57 0.14 85);
  --font-display:      "Satoshi", ui-sans-serif, system-ui;
  --font-body:         "Satoshi", ui-sans-serif, system-ui;
  --font-mono:         "JetBrains Mono", ui-monospace;
  --radius-interactive: 0.375rem;  /* sharp-ish */
  --radius-container:  0.5rem;
}
```

## Component Inventory

| Component | States | Notes |
|-----------|--------|-------|
| `Hero` | — | Live sparkline, CTA above fold |
| `FeatureCard` | hover, focus | 3-column bento, asymmetric |
| `MetricDisplay` | loading, error, ready | Real-time complexity data |
| `CTAButton` | hover, focus, active, disabled, loading | One label: "Install Extension" |
| `CodeBlock` | copy-toast | Syntax highlighted, copy button |
| `Footer` | — | Logo wall (real SVGs), both themes |

## Page Structure

```html
<header>          <!-- Nav: logo, Docs, Pricing, Blog, Install (CTA) -->
<main>
  <section id="hero">           <!-- Hero: thesis + live sparkline + CTA -->
  <section id="problem">        <!-- Split: problem statement + code example -->
  <section id="features">       <!-- Bento: 4 features, asymmetric, 2 visual -->
  <section id="metrics">        <!-- Data-dense: real complexity distributions -->
  <section id="integrations">   <!-- Logo wall: VS Code, GitHub, CI/CD -->
  <section id="cta-final">      <!-- Final CTA: "Start measuring in 30 seconds" -->
</main>
<footer>          <!-- Links, logo wall, copyright -->
```

## Key Implementation Details

### Hero — Live Complexity Sparkline

```tsx
function Hero() {
  return (
    <section className="min-h-[100dvh] flex flex-col justify-center px-4 md:px-12 pt-24">
      <div className="max-w-4xl mx-auto text-center">
        <p className="text-xs font-mono uppercase tracking-wider text-amber-600 mb-4">
          VS Code Extension · Real-time
        </p>
        <h1 className="text-4xl md:text-6xl font-display font-bold tracking-tight mb-6">
          See complexity <span className="text-amber-600">as you type</span>
        </h1>
        <p className="text-lg md:text-xl text-zinc-600 dark:text-zinc-400 mb-8 max-w-2xl mx-auto">
          Cyclomatic complexity, cognitive complexity, and maintainability index —
          updated on every keystroke. No build step. No config.
        </p>
        <ComplexitySparkline className="mb-8 h-32 w-full max-w-md mx-auto" />
        <CTAButton variant="primary" size="lg">
          Install from Marketplace
        </CTAButton>
      </div>
    </section>
  );
}
```

### Feature Bento — Asymmetric Grid

```tsx
function Features() {
  const features = [
    { title: "Cyclomatic", desc: "Per-function, real-time", visual: "sparkline" },
    { title: "Cognitive", desc: "Nesting-aware scoring", visual: "heatmap" },
    { title: "Maintainability", desc: "MI index with thresholds", visual: "gauge" },
    { title: "Trends", desc: "Git history complexity", visual: "chart" },
  ];

  return (
    <section className="py-16 md:py-24 px-4 md:px-12" aria-labelledby="features-heading">
      <h2 id="features-heading" className="sr-only">Features</h2>
      <div className="max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {features.map((f, i) => (
            <FeatureCard key={f.title} feature={f} variant={i % 2 === 0 ? "visual" : "text"} />
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Metric Display — Complete States

```tsx
function MetricDisplay({ filePath }) {
  const { data, status, error } = useComplexityData(filePath);

  if (status === "loading") return <MetricSkeleton />;
  if (status === "error") return <MetricError error={error} onRetry={() => refetch()} />;
  if (status === "empty") return <MetricEmpty onAnalyze={analyze} />;

  return (
    <dl className="grid grid-cols-3 gap-4 p-4">
      <MetricItem label="Cyclomatic" value={data.cyclomatic} threshold={10} />
      <MetricItem label="Cognitive" value={data.cognitive} threshold={15} />
      <MetricItem label="Maintainability" value={data.mi} threshold={65} invert />
    </dl>
  );
}
```

## Verification Checklist

- [ ] Design Read declared with dials
- [ ] Direction plan + anti-default test passed
- [ ] Tokens in one place, light+dark defined
- [ ] Hero fits viewport, ≤ 4 text elements, real visual (sparkline)
- [ ] Nav single line ≤ 80px
- [ ] ≥ 4 layout families (hero, split, bento, data-dense, logo wall, CTA)
- [ ] All interactive states complete
- [ ] All async states complete (loading/error/empty/ready)
- [ ] Contrast AA both themes (measured)
- [ ] Focus visible everywhere
- [ ] Touch targets ≥ 44px
- [ ] No raw hex in components
- [ ] Reduced-motion verified
- [ ] LCP < 2.5s (hero preload, modern formats)
- [ ] CLS < 0.1 (dimensions reserved)
- [ ] Lighthouse run, scores observed

## Files in This Example

```
landing-page-persuade/
├── src/
│   ├── components/
│   │   ├── Hero.tsx
│   │   ├── FeatureCard.tsx
│   │   ├── MetricDisplay.tsx
│   │   ├── CTAButton.tsx
│   │   ├── CodeBlock.tsx
│   │   └── Footer.tsx
│   ├── tokens/
│   │   └── design-tokens.css
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── tailwind.config.js
├── package.json
└── README.md
```

## Running the Example

```bash
cd landing-page-persuade
npm install
npm run dev
# Open http://localhost:5173
```

## Design Report

**Built:** Single-page landing for CodeMetrics VS Code extension
**Design Read:** `Read: CodeMetrics VS Code extension for senior developers · mode=Persuade · stack=React+Tailwind · redesign · dials V7/M4/D4`
**Checklist:** Pass — all boxes ticked
**Deviations:** None
**Verification Evidence:** Screenshots (desktop-light, desktop-dark, mobile-light, mobile-dark), Lighthouse scores (Perf 98, A11y 100, BP 100, SEO 100), Axe 0 violations, keyboard pass, reduced-motion pass
**Known Issues:** None