---
template: overrides/blog.html
icon: material/plus-circle
title: tomghost
description: >
  
search:
  exclude: true
hide:
  - feedback
tags:
  - THM-Room
  - Privilege Escalation
---

# __tomghost__

Link room: https://tryhackme.com/room/tomghost

---

## __Task 1: Flags__

![Alt text](image.png)

Are you able to complete the challenge?
The machine may take up to 5 minutes to boot and configure.



Admins Note: This room contains inappropriate content in the form of a username that contains a swear word and should be noted for an educational setting. - Dark

### __Answer the question bellow__

!!! question "Compromise this machine and obtain user.txt"
    THM{GhostCat_1s_so_cr4sy}
    
    ??? info "Hint"
        Web này bị lỗ hỏng CVE nào đó trên apache tomcat version 9.0.30 (48xxx)

!!! question "Escalate privileges and obtain root.txt" 
    THM{Z1P_1S_FAKE}
    
    ??? info "Hint"
        gpg2john, john, gpg --import, gpg --decrypt

        https://gtfobins.github.io/gtfobins/zip/#shell