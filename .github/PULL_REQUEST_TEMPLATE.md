# Pull Request Template

## Description

Brief description of changes.

## Type of Change

- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing behavior to change)
- [ ] Documentation update
- [ ] Example addition/update
- [ ] Refactoring (no functional changes)
- [ ] CI/CD improvement

## Phase Affected

- [ ] Phase 0 — Perceive
- [ ] Phase 1 — Direction
- [ ] Phase 2 — System (Tokens)
- [ ] Phase 3 — Build
- [ ] Phase 4 — Motion
- [ ] Phase 5 — Reflect & Verify
- [ ] Companion Skill Routing
- [ ] Documentation
- [ ] Examples
- [ ] Tooling/Scripts

## Checklist

- [ ] SKILL.md updated (if phases, references, or routing changed)
- [ ] Reference files updated (if phase content changed)
- [ ] Design tokens template updated (if token system changed)
- [ ] Documentation updated (docs/)
- [ ] Examples updated (docs/examples/)
- [ ] CHANGELOG.md updated with entry under [Unreleased]
- [ ] Validator passes: `python scripts/validate-skill.py`
- [ ] Markdown lint passes
- [ ] No broken links introduced

## Design Read (if applicable)

```
Read: <subject> for <audience> · mode=<mode> · stack=<stack> · <refine|redesign> · dials V<1-10>/M<1-10>/D<1-10>
```

## Verification

- [ ] Pre-flight checklist run on changes
- [ ] Automated a11y sweep clean
- [ ] Keyboard-only pass complete
- [ ] 200% zoom / 320px reflow verified
- [ ] Reduced-motion pass verified
- [ ] Contrast measured in both themes
- [ ] Lighthouse run, scores observed

## Screenshots (if visual changes)

| Before | After |
|--------|-------|
| ![before](url) | ![after](url) |

## Breaking Changes

If this is a breaking change, describe the migration path:

## Related Issues

Closes #<issue_number>

## Additional Notes

Any additional information for reviewers.