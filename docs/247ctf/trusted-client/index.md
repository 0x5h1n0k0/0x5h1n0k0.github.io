---
template: overrides/blog.html
icon: material/plus-circle
title: Trusted Client
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - 247CTF
---

# __Trusted Client__

---

![Challenge](image-1.png)

## __WriteUp__

Challenge này cung cấp cho ta một form login gồm có username/password

![form login](image.png)

F12 lên thì thấy đoạn code javescript mang mục đích xử lí logic login

![Đoạn code javascript](image-2.png)

Đây là [JSFuck](https://en.wikipedia.org/wiki/JSFuck) và có nhiều tool để decode nó và tôi dùng https://www.dcode.fr/jsfuck-language

![Flag](image-3.png)

!!! success "Flag: 247CTF{6c91b7f7f12c852f892293d16dba0148}"

## __What we learned__

1. Shouldn't leave information (Eg: username/password,...) on the client side