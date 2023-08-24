---
template: overrides/blog.html
icon: material/plus-circle
title: Root Me
description: >
  
search:
  exclude: true
hide:
  - feedback


tags:
  - THM-Room
  - Linux Privilege Escalation
---

# __Root Me__

---

## __Task 1: Deploy the machine__

Connect to TryHackMe network and deploy the machine. If you don't know how to do this, complete the OpenVPN room first.

### __Answer the questions bellow__

!!! question "Deploy the machine"
    No answer needed

## __Task 2: Reconnaissance__

First, let's get information about the target.

### __Answer the questions bellow__

!!! question "Scan the machine, how many ports are open?"
    Ans: 2
    ??? tip
        Dùng nmap để scan port, ta tìm được 2 port mở là 22 với dịch vụ ssh và 80 với dịch vụ http
        ```ps1
        nmap -sN -A VICTIM_IP
        ```

!!! question "What version of Apache is running?"
    Ans: 2.4.29

!!! question "What service is running on port 22?"
    Ans: ssh

!!! question "Find directories on the web server using the GoBuster tool."
    No answer needed

!!! question "What is the hidden directory?"
    /panel/

## __Task 3: Getting a shell__

Find a form to upload and get a reverse shell, and find the flag.

### __Answer the questions bellow__

!!! question "user.txt"
    THM{y0u_g0t_a_sh3ll}

    ??? tip
        find . -type f -iname user.txt

## __Task 4: Privilege escalation__

Now that we have a shell, let's escalate our privileges to root.

### __Answer the questions bellow__

!!! question "Search for files with SUID permission, which file is weird?"
    /usr/bin/python

    ??? tip 
        find / -user root -perm /4000 -type f 2>/dev/null 


!!! question "Find a form to escalate your privileges."
    no answer needed

!!! question "root.txt"
    Ans: THM{pr1v1l3g3_3sc4l4t10n}

Xem video hướng dẫn tại

<iframe width="560" height="315" src="https://www.youtube.com/embed/grbHmqWiDR8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


