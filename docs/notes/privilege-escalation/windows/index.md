---
template: overrides/blog.html
icon: material/plus-circle
title: Windows Privilege Escalation
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - Privilege Escalation 
  - Windows
---

# __Windows Privilege Escalation__

---

## __Privilege Escalation Methods__

- Basic System Enumeration
- Finding clear text credentials
- GPP (Group Policy Preference)
- Secrets dump via SAM (VHD Mounted Share)
- Kernel Expliots
- AlwaysInstallElevated
- DNSAdmin DLL Injection
- RunAs with Saved Credentials
- BinPATH Service Re-Direct - Weak Permissions
- USP (Unquoted Service Path)
- SeImpersonate / SeAssignPrimaryToken - Service Accounts
- MSSQL via UDF User Defined Function