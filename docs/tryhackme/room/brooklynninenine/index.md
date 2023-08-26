---
template: overrides/blog.html
icon: material/plus-circle
title: Brooklyn Nine Nine
description: > 
  
search:
  exclude: true
hide:
  - feedback


tags:
  - THM-Room
  - Privilege Escalation
---

# __Brooklyn Nine Nine__

Room: https://tryhackme.com/room/brooklynninenine

---

## __Task 1: Deploy and get hacking__

### __Answer the question bellow__

!!! question "User flag"
    ee11cbb19052e40b07aac0ca060c23ee

!!! question "Root flag" 
    63a9f0ea7bb98050796b649e85481845

### __Hướng tiếp cận__

Hướng tiếp cận thứ nhất là đi theo từ jake (hydra scan password - hint trong truy cập ẩn danh ftp)

Hướng tiếp cận thứ 2 là đi từ pasword của holt trong hình ảnh đã được ẩn tệp password trong đó (dùng stegseek), và đi theo đường leo thang đặc quyền nano.

![Alt text](image.png)
    