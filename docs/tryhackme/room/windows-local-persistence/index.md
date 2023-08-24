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