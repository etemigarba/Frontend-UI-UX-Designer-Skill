#!/usr/bin/env python3
"""
Frontend UI/UX Designer Skill Validator

Validates the skill structure, references, and cross-references.
Run from the repository root: python scripts/validate-skill.py
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).parent.parent

# Expected structure
REQUIRED_FILES = [
    "SKILL.md",
    "LICENSE",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "assets/design-tokens-template.css",
    "references/design-direction.md",
    "references/ux-playbook.md",
    "references/motion.md",
    "references/accessibility.md",
    "references/preflight-checklist.md",
]

REQUIRED_DIRS = [
    "docs",
    "docs/examples",
    "assets",
    "references",
    "scripts",
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
    "wiki",
]

PHASE_REFERENCES = {
    "Phase 0": [],  # No reference
    "Phase 1": ["references/design-direction.md"],
    "Phase 2": ["assets/design-tokens-template.css"],
    "Phase 3": ["references/ux-playbook.md"],
    "Phase 4": ["references/motion.md"],
    "Phase 5": ["references/accessibility.md", "references/preflight-checklist.md"],
}

COMPANION_SKILLS = [
    "brainstorming",
    "ui-ux-pro-max",
    "design-taste-frontend",
    "impeccable",
    "shadcn",
    "21st-dev-builder-v2",
    "react-best-practices",
    "react-expert",
    "frontend-design",
    "ui-animation",
    "emilkowalski-motion",
    "css-animations",
    "animation-designer",
    "webapp-testing",
    "agent-browser",
    "verification-before-completion",
    "production-ready-workflow",
    "debug-and-fix-bugs",
]

GITHUB_REPOS = [
    "Loop-Engineer-Skill",
    "Agentic-Engineering-Skills",
    "Systematic-Implementation-Skill",
    "Production-Ready-Workflow-Skill",
    "Debug-and-Fix-Bugs-Skill",
    "Etemi-Prompt-Enhancer-Skill",
    "Practical-React",
    "Practical-Next.js",
]

def check_file_exists(path: Path) -> bool:
    return path.exists() and path.is_file()

def check_dir_exists(path: Path) -> bool:
    return path.exists() and path.is_dir()

def validate_frontmatter(skill_md: Path) -> List[str]:
    """Validate SKILL.md frontmatter."""
    errors = []
    content = skill_md.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        errors.append("SKILL.md: Missing frontmatter delimiter (---)")
        return errors
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append("SKILL.md: Malformed frontmatter")
        return errors
    
    frontmatter = parts[1]
    
    required_fields = ['name', 'description']
    for field in required_fields:
        if f'{field}:' not in frontmatter:
            errors.append(f"SKILL.md: Missing required frontmatter field: {field}")
    
    # Check name matches directory
    if 'name: frontend-ui-ux-designer' not in frontmatter:
        errors.append("SKILL.md: name field should be 'frontend-ui-ux-designer'")
    
    return errors

def validate_phase_references(skill_md: Path) -> List[str]:
    """Validate that phase references match expected files."""
    errors = []
    content = skill_md.read_text(encoding='utf-8')
    
    for phase, refs in PHASE_REFERENCES.items():
        for ref in refs:
            # Check reference format in skill
            ref_pattern = rf'\[.*?\]\({re.escape(ref)}\)'
            if not re.search(ref_pattern, content):
                errors.append(f"SKILL.md: Missing reference to {ref} in {phase}")
            
            # Check file exists
            if not (REPO_ROOT / ref).exists():
                errors.append(f"Missing reference file: {ref}")
    
    return errors

def validate_companion_skills(skill_md: Path) -> List[str]:
    """Validate companion skill routing table."""
    errors = []
    content = skill_md.read_text(encoding='utf-8')
    
    # Check routing table exists
    if 'Companion Skill Routing' not in content:
        errors.append("SKILL.md: Missing 'Companion Skill Routing' section")
        return errors
    
    # Check each companion mentioned exists in our list (or is a known external)
    for companion in COMPANION_SKILLS:
        if companion not in content:
            errors.append(f"SKILL.md: Companion skill '{companion}' not referenced in routing table")
    
    return errors

def validate_cross_references(readme: Path) -> List[str]:
    """Validate GitHub cross-references in README."""
    errors = []
    content = readme.read_text(encoding='utf-8')
    
    # Check for broken etemigarba links - capture only repo name (first path segment)
    etemigarba_links = re.findall(r'https://github\.com/etemigarba/([^/\s)]+)', content)
    for repo in etemigarba_links:
        # Allow self-referential links (this repo)
        if repo == "frontend-ui-ux-designer-skill":
            continue
        # These are the known valid repos
        if repo not in GITHUB_REPOS and not repo.endswith('.git'):
            errors.append(f"README.md: Potentially broken link to etemigarba/{repo}")
    
    return errors

def validate_design_tokens(css_file: Path) -> List[str]:
    """Validate design tokens template."""
    errors = []
    content = css_file.read_text(encoding='utf-8')
    
    required_tokens = [
        '--color-background',
        '--color-surface',
        '--color-accent',
        '--color-text-primary',
        '--space-4',
        '--font-display',
        '--font-body',
        '--radius-interactive',
        '--duration-base',
        '--ease-enter',
        '--z-modal',
        '@media (prefers-color-scheme: dark)',
        '@media (prefers-reduced-motion: reduce)',
        ':focus-visible',
    ]
    
    for token in required_tokens:
        if token not in content:
            errors.append(f"design-tokens-template.css: Missing required token/block: {token}")
    
    # Check for REPLACE placeholders
    if 'REPLACE-Display' not in content or 'REPLACE-Body' not in content:
        errors.append("design-tokens-template.css: Missing REPLACE placeholders for fonts")
    
    return errors

def validate_example_readmes() -> List[str]:
    """Validate example README files exist."""
    errors = []
    examples = [
        "landing-page-persuade",
        "dashboard-operate",
        "docs-read",
        "portfolio-experience",
    ]
    
    for example in examples:
        readme = REPO_ROOT / "docs" / "examples" / example / "README.md"
        if not readme.exists():
            errors.append(f"Missing example README: docs/examples/{example}/README.md")
        else:
            content = readme.read_text(encoding='utf-8')
            if 'Design Read' not in content:
                errors.append(f"Example {example}: Missing Design Read in README")
            if 'Verification Checklist' not in content:
                errors.append(f"Example {example}: Missing Verification Checklist in README")
    
    return errors

def validate_license(license_file: Path) -> List[str]:
    """Validate LICENSE file."""
    errors = []
    content = license_file.read_text(encoding='utf-8')
    
    required = [
        'MIT License',
        'Copyright (c) 2026 Prof. Etemi Joshua Garba',
        'Explicit Permission Statement',
    ]
    
    for req in required:
        if req not in content:
            errors.append(f"LICENSE: Missing required text: {req}")
    
    return errors

def main():
    print("[VALIDATE] Validating Frontend UI/UX Designer Skill...")
    print(f"Repository root: {REPO_ROOT}")
    print()
    
    all_errors = []
    
    # Check required files
    print("Checking required files...")
    for f in REQUIRED_FILES:
        path = REPO_ROOT / f
        if not check_file_exists(path):
            all_errors.append(f"Missing required file: {f}")
        else:
            print(f"  [OK] {f}")
    
    # Check required directories
    print("\nChecking required directories...")
    for d in REQUIRED_DIRS:
        path = REPO_ROOT / d
        if not check_dir_exists(path):
            all_errors.append(f"Missing required directory: {d}")
        else:
            print(f"  [OK] {d}/")
    
    # Validate SKILL.md
    print("\nValidating SKILL.md...")
    skill_md = REPO_ROOT / "SKILL.md"
    all_errors.extend(validate_frontmatter(skill_md))
    all_errors.extend(validate_phase_references(skill_md))
    all_errors.extend(validate_companion_skills(skill_md))
    print("  [OK] Frontmatter")
    print("  [OK] Phase references")
    print("  [OK] Companion skills")
    
    # Validate README.md
    print("\nValidating README.md...")
    readme = REPO_ROOT / "README.md"
    all_errors.extend(validate_cross_references(readme))
    print("  [OK] Cross-references")
    
    # Validate design tokens
    print("\nValidating design tokens...")
    tokens = REPO_ROOT / "assets" / "design-tokens-template.css"
    all_errors.extend(validate_design_tokens(tokens))
    print("  [OK] Required tokens present")
    
    # Validate examples
    print("\nValidating examples...")
    all_errors.extend(validate_example_readmes())
    print("  [OK] Example READMEs")
    
    # Validate LICENSE
    print("\nValidating LICENSE...")
    license_file = REPO_ROOT / "LICENSE"
    all_errors.extend(validate_license(license_file))
    print("  [OK] MIT License with explicit permission")
    
    # Summary
    print("\n" + "="*50)
    if all_errors:
        print(f"[FAIL] Validation FAILED with {len(all_errors)} error(s):")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("[PASS] All validations PASSED!")
        sys.exit(0)

if __name__ == "__main__":
    main()