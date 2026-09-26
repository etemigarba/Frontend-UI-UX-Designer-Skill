# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

Only the latest major version receives security updates.

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

Instead, report vulnerabilities via:

1. **GitHub Security Advisories** (preferred): Use the "Report a vulnerability" button on the [Security tab](https://github.com/etemigarba/frontend-ui-ux-designer-skill/security)
2. **Email**: security@ethereal.ng (PGP key available on [ORCID profile](https://orcid.org/0000-0001-6707-0220))

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Response Timeline

| Severity | Acknowledgment | Fix Target |
| -------- | -------------- | ---------- |
| Critical | 24 hours       | 7 days     |
| High     | 48 hours       | 14 days    |
| Medium   | 72 hours       | 30 days    |
| Low      | 1 week         | Next release |

## Security Considerations for This Skill

### Design-Time Risks

- **Token exposure**: Design tokens may contain brand colors, spacing, typography — not secrets, but treat as proprietary IP
- **Companion skill supply chain**: Delegated skills execute in the same context — verify companion sources
- **Asset generation**: Image generation tools may produce content with licensing implications

### Runtime Risks (When Skill Output Is Deployed)

- **Content Security Policy**: Ensure generated HTML/CSS/JS complies with your CSP
- **Subresource Integrity**: Use SRI for external fonts, icons, images
- **CORS**: Verify font/icon CDN headers allow your origin
- **Reduced motion**: Always implement `prefers-reduced-motion` — missing path is an accessibility violation

### Safe Usage Practices

1. **Never commit generated secrets** — tokens are design values, not credentials
2. **Audit companion skills** — only delegate to trusted, reviewed skills
3. **Validate outputs** — run pre-flight checklist before deploying generated code
4. **Review generated HTML** — ensure no inline scripts, unsafe patterns
5. **Test accessibility** — run axe/Lighthouse on rendered output

## Dependency Security

This skill has **zero runtime dependencies**. Validation scripts use:
- Python 3.10+ standard library only
- No external packages required

Companion skills (optional) have their own supply chains — audit independently.

## Disclosure Policy

- Coordinated disclosure preferred
- Public disclosure after fix released + 30 days
- Credit given to reporters (unless anonymous requested)
- CVE requested for qualifying vulnerabilities

## Contact

**Security Team**: Prof. Etemi Joshua Garba  
**Email**: security@ethereal.ng  
**PGP**: Available on [ORCID](https://orcid.org/0000-0001-6707-0220)

---

*This policy follows [GitHub's security policy guidelines](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).*