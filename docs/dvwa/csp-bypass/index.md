---
template: overrides/blog.html
icon: material/plus-circle
title: CSP Bypass
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - DVWA
  - CSP
---

# __CSP Bypass__



---

## __About__

Content Security Policy (CSP) is used to define where scripts and other resources can be loaded or executed from. This module will walk you through ways to bypass the policy based on common mistakes made by developers.

None of the vulnerabilities are actual vulnerabilities in CSP, they are vulnerabilities in the way it has been implemented.

## __Objective__

Bypass Content Security Policy (CSP) and execute JavaScript in the page.

## __Security Level: Low__

Source code

```python title="vulnerabilities/csp/source/low.php"
--8<-- "dvwa/csp-bypass/sources/low.php"
```

### __Analysis__

### __Exploition__

---

## __Security Level: Medium__

Source code

```python title="vulnerabilities/csp/source/medium.php"
--8<-- "dvwa/csp-bypass/sources/medium.php"
```

### __Analysis__


### __Exploition__


---

## __Security Level: High__

Source code

```python title="vulnerabilities/csp/source/high.php"
--8<-- "dvwa/csp-bypass/sources/high.php"
```

### __Analysis__


### __Exploition__

---

## __Security Level: Impossible__

Source code

```python title="vulnerabilities/csp/source/impossible.php"
--8<-- "dvwa/csp-bypass/sources/impossible.php"
```

### __Analysis__

---

## __What we learned__

## __More Information__

- [Content Security Policy Reference](https://content-security-policy.com/)
- [Mozilla Developer Network - CSP: script-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [Mozilla Security Blog - CSP for the web we have](https://blog.mozilla.org/security/2014/10/04/csp-for-the-web-we-have/)
