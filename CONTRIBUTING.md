# Contributing Guidelines

Thank you for contributing to the Frontend UI/UX Designer Skill! This skill is part of the [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) ecosystem.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold this code.

## How to Contribute

### Reporting Issues

- Use the [issue templates](.github/ISSUE_TEMPLATE/) for bug reports, feature requests, or design reviews
- Provide a clear title and description
- Include steps to reproduce for bugs
- Reference the specific phase/section if applicable

### Submitting Changes

1. **Fork** the repository
2. **Create a branch** from `main`: `git checkout -b feature/your-feature-name`
3. **Make your changes** following the conventions below
4. **Validate** your changes: `python scripts/validate-skill.py`
5. **Run the pre-flight checklist** mentally or with tooling
6. **Submit a PR** using the [PR template](.github/PULL_REQUEST_TEMPLATE.md)

### Conventions

#### Skill Structure

- Keep `SKILL.md` as the single source of truth for the skill definition
- Reference files in `references/` are loaded at specific phases — do not reorder
- Assets in `assets/` are templates — components consume tokens only
- Documentation in `docs/` mirrors references with additional guides

#### Writing Style

- Follow the [Agentic Engineering](https://github.com/etemigarba/Agentic-Engineering-Skills) house style
- Technology-agnostic: no framework-specific assumptions unless in examples
- Evidence-based: claims must be verifiable (measurements, tool output, screenshots)
- Strict house style: numbered equations, applied standards, no fluff

#### Design Principles

- **Anti-default**: Every choice must pass the anti-default test (Phase 1)
- **Locks respected**: Theme, Accent, Radius, Copy Register — one per page
- **States complete**: No partial state implementations
- **Tokens only**: No raw hex, magic numbers, or ad-hoc z-index in components
- **Accessibility first**: WCAG 2.2 AA is the floor, not the ceiling
- **Performance budgets**: LCP < 2.5s, INP < 200ms, CLS < 0.1

#### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

Example:
```
feat(tokens): add OKLCH color space conversion utility

- Add oklch() to hex conversion for Tailwind compatibility
- Update design-tokens-template.css with fallback values

Closes #42
```

### Pull Request Process

1. PR must pass CI validation (skill structure, markdown lint, link check)
2. At least one maintainer review required
3. All checklist items in PR template must be addressed
4. No merge if pre-flight checklist has unticked boxes without justification
5. Squash and merge to `main`

### Skill Validation

Run the validator before submitting:

```bash
python scripts/validate-skill.py
```

This checks:
- SKILL.md frontmatter completeness
- Reference file existence and phase alignment
- Asset template validity
- Cross-reference link integrity
- Version consistency

### Adding Companion Skills

To add a companion skill to the routing table:

1. Verify the skill exists in [Agentic-Engineering-Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) or is installable
2. Add entry to `SKILL.md` companion routing table with phase, skill name, and purpose
3. Document integration in `docs/companion-skills.md`
4. Add example if non-trivial

### Updating References

When updating a reference file:

1. Update the source file in `references/`
2. Sync corresponding documentation in `docs/`
3. Update `CHANGELOG.md` with the change
4. Run validator to ensure phase alignment

### Versioning

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes to the design loop, phases, or non-negotiables
- **MINOR**: New direction families, reference additions, companion integrations
- **PATCH**: Fixes, clarifications, typo corrections, example updates

## Getting Help

- Check existing [issues](https://github.com/etemigarba/frontend-ui-ux-designer-skill/issues)
- Review [documentation](docs/)
- Ask in [discussions](https://github.com/etemigarba/frontend-ui-ux-designer-skill/discussions)
- Reference [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) for ecosystem context

## Recognition

Contributors are recognized in:
- Release notes
- Contributors list (auto-generated)
- Skill lineage section (for significant architectural contributions)

---

**Remember**: This skill is the orchestrator. Companions own depth; this skill owns the loop and gates. Every change must preserve that architecture.