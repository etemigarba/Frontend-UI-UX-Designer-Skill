# Getting Started

## Installation

### For Claude Code

Place the skill folder in your Claude Code skills directory:

```bash
# macOS / Linux
cp -r frontend-ui-ux-designer-skill ~/.claude/skills/

# Windows PowerShell
Copy-Item -Recurse frontend-ui-ux-designer-skill $env:USERPROFILE\.claude\skills\
```

### For OpenCode

```bash
# macOS / Linux
cp -r frontend-ui-ux-designer-skill ~/.config/opencode/skills/

# Windows PowerShell
Copy-Item -Recurse frontend-ui-ux-designer-skill $env:APPDATA\opencode\skills\
```

### Using the Skill Archive

If you have the `.skill` archive file:

```bash
# The skill archive contains SKILL.md + assets + references
# Install via your harness's skill manager
```

## Invocation

### Explicit Invocation

```markdown
/frontend-ui-ux-designer
```

### Implicit Invocation

The skill activates automatically when you use phrases like:

- "design a landing page for..."
- "make this look better / professional / modern"
- "improve the UX of..."
- "this looks generic or AI-generated"
- "pick a palette / font pairing"
- "add dark mode"
- "make it responsive"
- "add animations"

## First Design: Quick Example

### 1. Provide a Brief

> "Design a landing page for a developer tool called 'CodeMetrics' — it's a VS Code extension that shows code complexity metrics in real-time. Audience: senior developers. Stack: React + Tailwind CSS."

### 2. Receive the Design Read

The skill outputs a **Design Read** before any design work:

```
Read: CodeMetrics VS Code extension for senior developers · mode=Persuade · stack=React+Tailwind · redesign · dials V7/M4/D5
```

- **V7** = DESIGN_VARIANCE: moderately bold/asymmetric
- **M4** = MOTION_INTENSITY: subtle motion
- **D5** = VISUAL_DENSITY: balanced

### 3. Review the Direction Plan

The skill produces a direction plan with:

- **Aesthetic family** (e.g., "Industrial / Utilitarian" — tool-like, data-forward)
- **Palette** (4-6 hex values, one locked accent)
- **Typography** (display + body + optional mono)
- **Layout concept** + ASCII wireframe
- **Signature element** (the one memorable thing)

### 4. Get the Token System

Tokens delivered as CSS custom properties (or Tailwind config):

```css
:root {
  --color-accent: oklch(0.55 0.18 260);
  --font-display: "Satoshi", ui-sans-serif, system-ui;
  --font-body: "Geist", ui-sans-serif, system-ui;
  --space-4: 1rem;
  --radius-interactive: 0.5rem;
  /* ... light + dark themes ... */
}
```

### 5. Receive Complete Implementation

The skill builds:
- Semantic HTML with landmarks
- Complete state sets (hover, focus, active, disabled, loading)
- All async view states (loading, empty, error, ready)
- Real content strategy (no fake data)
- Motion with reduced-motion paths
- Accessibility audit passed

## Configuration

### Stack Detection

The skill auto-detects from:
- `package.json` dependencies
- `tailwind.config.js` / `tailwind.config.ts`
- `pubspec.yaml` (Flutter)
- `*.xcodeproj` (iOS/macOS)
- Existing component library (shadcn, Radix, etc.)

If undetectable, it asks or defaults to **HTML + Tailwind**.

### Refinement vs Redesign

The skill inventories incumbent visual truth:
- Existing tokens / theme files
- Global CSS
- One representative component

Then declares: **refinement** (keep identity) or **redesign** (replace look, keep function).

### Dial Calibration

Three dials inferred from brief (1-10 scale):

| Dial | Low (1-3) | Mid (4-6) | High (7-10) |
|------|-----------|-----------|-------------|
| **V** DESIGN_VARIANCE | Centered, safe | Balanced | Asymmetric, bold |
| **M** MOTION_INTENSITY | Static | Subtle feedback | Choreographed |
| **D** VISUAL_DENSITY | Airy | Balanced | Dense |

Explicit brief instructions override inference.

## Output Formats

The skill can produce:

| Format | Use Case |
|--------|----------|
| **HTML + CSS** | Standalone pages, prototypes |
| **React + Tailwind** | Component libraries, apps |
| **Vue + CSS** | Vue applications |
| **Svelte + CSS** | Svelte applications |
| **Tailwind Config** | Design system integration |
| **CSS Custom Properties** | Framework-agnostic tokens |

Specify in brief: "Output as React components with Tailwind" or similar.

## Troubleshooting

### Skill Not Activating

1. Verify installation path matches your harness
2. Check skill name: `frontend-ui-ux-designer` (from SKILL.md frontmatter)
3. Restart the agent/harness

### Stack Not Detected

- Ensure `package.json` or config files are in workspace root
- Explicitly state stack in brief: "Stack: Next.js 14 + Tailwind"

### Design Read Seems Wrong

- Provide more context in brief
- Explicitly set mode: "Mode: Operate (it's a dashboard)"
- Pin aesthetic: "Use Neo-Brutalist direction"

### Companion Skills Not Found

- Skill degrades gracefully to bundled references
- Install companions for deeper integration:
  - `ui-ux-pro-max` for design system database
  - `impeccable` for anti-slop correction
  - `webapp-testing` for live verification

## Next Steps

- Read the [Design Loop](design-loop.md) for phase details
- Explore [Surface Modes](surface-modes.md) for mode-specific guidance
- Review [Examples](../examples/) for working implementations
- Check [Companion Skills](companion-skills.md) for ecosystem integration