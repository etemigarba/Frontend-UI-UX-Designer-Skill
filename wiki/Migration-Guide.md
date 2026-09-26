# Migration Guide

This guide covers upgrading between versions of the Frontend UI/UX Designer Skill.

---

## Version 1.0.x (Current)

Initial release. No migration needed.

---

## Future Versions

When new versions are released, this section will be updated with:

### Breaking Changes

- What changed
- Why it changed
- Migration steps
- Code examples

### New Features

- What was added
- How to use it
- Configuration options

### Deprecations

- What's deprecated
- Recommended alternatives
- Removal timeline

---

## General Migration Principles

### 1. Backup Your Customizations

Before upgrading, backup any:
- Custom token modifications
- Extended reference files
- Modified examples
- Companion skill configurations

### 2. Run the Validator

```bash
python scripts/validate-skill.py
```

Fix any validation errors before proceeding.

### 3. Review the Changelog

Check `CHANGELOG.md` for:
- Breaking changes (MAJOR version)
- New features (MINOR version)
- Fixes (PATCH version)

### 4. Test Your Design Loop

Run a test design through the full loop:
1. Phase 0: Design Read output
2. Phase 1: Direction plan + anti-default test
3. Phase 2: Token system generation
4. Phase 3: Component build with states
5. Phase 4: Motion implementation
6. Phase 5: Pre-flight checklist verification

### 5. Update Companion Skills

If you use companion skills, check their compatibility:
- [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) for latest versions
- Update companions to versions compatible with this skill version

---

## Common Migration Scenarios

### Upgrading Token System

If token structure changes:

1. Compare old vs new `assets/design-tokens-template.css`
2. Update your project's token file
3. Run grep for old token names in components
4. Replace with new token names
5. Verify both themes render correctly

### Upgrading Reference Files

If reference content changes:

1. Diff old vs new reference files in `references/`
2. Update any custom reference extensions
3. Re-run Phase 5 checklist on existing designs

### Adding New Companion Skills

When new companions are added to routing table:

1. Install the companion skill
2. Test delegation at the relevant phase
3. Verify output passes Phase 5 checklist
4. Document integration in your project

### Changing Surface Modes

If mode definitions or defaults change:

1. Review your Design Reads for correct mode assignment
2. Update dial defaults in your briefs if needed
3. Re-verify density/motion/variance for each mode

---

## Version Compatibility Matrix

| Skill Version | Companion Min Version | Notes |
|---------------|----------------------|-------|
| 1.0.x | 2026-08-04 | Initial release |

---

## Getting Help

- Check [FAQ](FAQ) for common issues
- Search [Issues](https://github.com/etemigarba/frontend-ui-ux-designer-skill/issues) for similar problems
- Open a [new issue](https://github.com/etemigarba/frontend-ui-ux-designer-skill/issues/new/choose) with the `bug` or `question` template
- Ask in [Discussions](https://github.com/etemigarba/frontend-ui-ux-designer-skill/discussions)

---

## Reporting Migration Issues

If you encounter issues during migration:

1. Run validator: `python scripts/validate-skill.py`
2. Note the exact error messages
3. Include your Design Read and phase outputs
4. File an issue with the `bug` template