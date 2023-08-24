---
template: overrides/blog.html
icon: material/plus-circle
title: TryHackMe - Metasploit
description: Learn the essentials of Command and Control to help you become a better Red Teamer and simplify your next Red Team assessment!
  
search:
  exclude: true
hide:
  - feedback

links:
  - setup/setting-up-site-search.md#built-in-search-plugin
  - insiders/index.md#how-to-become-a-sponsor
tags:
  - THM-Room
---

# __TryHackMe - Metasploit__

---

Metasploit is the most widely used exploitation framework. Learn how to use it and unlock its full potential.

The Metasploit framework is a set of open-source tools used for network enumeration, identifying vulnerabilities, developing payloads and executing exploit code against remote target machines. Get hands-on with the various tool and features Metasploit provides, from exploit development to post-exploitation techniques, this module covers it all.

## __Task 1: Introduction to Metasploit__

Metasploit is the most widely used exploitation framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation.



Metasploit has two main versions:

- __Metasploit Pro__: The commercial version that facilitates the automation and management of tasks. This version has a graphical user interface (GUI).
- __Metasploit Framework__: The open-source version that works from the command line. This room will focus on this version, installed on the AttackBox and most commonly used penetration testing Linux distributions.

The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.



The main components of the Metasploit Framework can be summarized as follows;

- __msfconsole__: The main command-line interface.
- __Modules__: supporting modules such as exploits, scanners, payloads, etc.
- __Tools__: Stand-alone tools that will help vulnerability research, vulnerability assessment, or penetration testing. Some of these tools are msfvenom, pattern_create and pattern_offset. We will cover msfvenom within this module, but pattern_create and pattern_offset are tools useful in exploit development which is beyond the scope of this module.


This room will cover the main components of Metasploit while providing you with a solid foundation on how to find relevant exploits, set parameters, and exploit vulnerable services on the target system. Once you have completed this room, you will be able to navigate and use the Metasploit command line comfortably.



You can deploy and use the AttackBox to complete tasks and answer the questions.

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__No answer needed__"

    === "Answer"
        ``` powershell
        No answer needed
        ```
    === "Explain"
        ``` powershell
        No answer needed
        ```

## __Task 2: Main Components of Metasploit__

While using the Metasploit Framework, you will primarily interact with the Metasploit console. You can launch it from the AttackBox terminal using the `msfconsole` command. The console will be your main interface to interact with the different modules of the Metasploit Framework. Modules are small components within the Metasploit framework that are built to perform a specific task, such as exploiting a vulnerability, scanning a target, or performing a brute-force attack.

Before diving into modules, it would be helpful to clarify a few recurring concepts: vulnerability, exploit, and payload.

- __Exploit__: A piece of code that uses a vulnerability present on the target system.
- __Vulnerability__: A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.
- __Payload__: An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.
Modules and categories under each one are listed below. These are given for reference purposes, but you will interact with them through the Metasploit console (msfconsole).

### __Auxiliary__

Any supporting module, such as scanners, crawlers and fuzzers, can be found here.

```powershell title="Terminal"
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 auxiliary/
auxiliary/
├── admin
├── analyze
├── bnat
├── client
├── cloud
├── crawler
├── docx
├── dos
├── example.py
├── example.rb
├── fileformat
├── fuzzers
├── gather
├── parser
├── pdf
├── scanner
├── server
├── sniffer
├── spoof
├── sqli
├── voip
└── vsploit

20 directories, 2 files
```

### __Encoders__

Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.

Signature-based antivirus and security solutions have a database of known threats. They detect threats by comparing suspicious files to this database and raise an alert if there is a match. Thus encoders can have a limited success rate as antivirus solutions can perform additional checks.

```ps1 title="Terminal"
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 encoders/
encoders/
├── cmd
├── generic
├── mipsbe
├── mipsle
├── php
├── ppc
├── ruby
├── sparc
├── x64
└── x86

10 directories, 0 files
```
### __Evasion__

While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software. On the other hand, “evasion” modules will try that, with more or less success.

```ps1 title="Terminal"
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 2 evasion/
evasion/
└── windows
    ├── applocker_evasion_install_util.rb
    ├── applocker_evasion_msbuild.rb
    ├── applocker_evasion_presentationhost.rb
    ├── applocker_evasion_regasm_regsvcs.rb
    ├── applocker_evasion_workflow_compiler.rb
    ├── process_herpaderping.rb
    ├── syscall_inject.rb
    ├── windows_defender_exe.rb
    └── windows_defender_js_hta.rb

1 directory, 9 files
```