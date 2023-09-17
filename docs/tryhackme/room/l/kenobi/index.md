# __Kenobi__

---

## __Task 1: Deploy the vulnerable machine__

![](image.png)

<div style="text-align: center"> This room will cover accessing a Samba share, manipulating a vulnerable version of proftpd to gain initial access and escalate your privileges to root via an SUID binary. </div>

??? question "Answer the questions bellow"

    Question: Make sure you're connected to our network and deploy the machine
    > Ans: No Answer Needed

    Question: Scan the machine with nmap, how many ports are open?
    > Ans: 7
    > ![](image-2.png)

## __Task 2: Enumerating Samba for shares__

![](image-1.png)

<div style="text-align: center"> Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system. </div>

<div style="text-align: center"> Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network. </div>

??? question "Answer the questions bellow"
    
    Using nmap we can enumerate a machine for SMB shares.

    Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!

    <div style="color: red">nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP</div>

    SMB has two ports, 445 and 139.

    ![](image-3.png)

    Question: Using the nmap command above, how many shares have been found?
    > Ans: 3
    > ![](image-5.png)

    On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.

    <div style="color: red">smbclient //MACHINE_IP/anonymous</div>

    Using your machine, connect to the machines network share.

    ![](image-4.png)

    Question: Once you're connected, list the files on the share. What is the file can you see?
    > Ans: log.txt
    > ![](image-6.png)

    You can recursively download the SMB share too. Submit the username and password as nothing.

    <div style="color: red">smbget -R smb://MACHINE_IP/anonymous</div>

    Open the file on the share. There is a few interesting things found.

    - Information generated for Kenobi when generating an SSH key for the user
    - Information about the ProFTPD server.

    What port is FTP running on?
    > Ans: 21
    > ![Download file log](image-7.png)
    > ![](image-8.png)

    Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. 

    In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

    <div style="color: red">nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP</div>

    What mount can we see?
    > Ans: /var
    > ![](image-9.png)

## __Task 3: Gain initial access with ProFtpd__

![](image-10.png)

<div style="text-align: center">ProFtpd is a free and open-source FTP server, compatible with Unix and Windows systems. Its also been vulnerable in the past software versions.</div>

??? question "Answer the questions bellow"

    Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port.

    Question: What is the version?
    > Ans: 1.3.5
    > ![](image-11.png)
    
    We can use searchsploit to find exploits for a particular software version.

    Searchsploit is basically just a command line search tool for exploit-db.com.

    Question: How many exploits are there for the ProFTPd running?
    > Ans: 4
    > ![](image-12.png)

    You should have found an exploit from ProFtpd's [mod_copy module](http://www.proftpd.org/docs/contrib/mod_copy.html). 

    The mod_copy module implements __SITE CPFR__ and __SITE CPTO__ commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.

    We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user. 
    > Ans: No answer needed

    We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.
    > Ans: No answer needed

    Lets mount the /var/tmp directory to our machine

    <div style="color: red">mkdir /mnt/kenobiNFS</div>
    <div style="color: red">mount MACHINE_IP:/var /mnt/kenobiNFS</div>
    <div style="color: red">ls -la /mnt/kenobiNFS</div>

    ![](image-13.png)

    We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.

    ![](image-14.png)

    Question: What is Kenobi's user flag (/home/kenobi/user.txt)?
    > Ans: d0b0f3f53b6caa532a83915e19224899

## __Task 4: Privilege Escalation with Path Variable Manipulation__

![](image-15.png)

<div style="text-align: center">Lets first understand what what SUID, SGID and Sticky Bits are.</div>

| __Permission__ |	__On Files__ | __On Directories__ |
| :---: | :---: |  :---: |
| SUID Bit	| User executes the file with permissions of the file owner	| - |
| SGID Bit	| User executes the file with the permission of the group owner. |  File created in directory gets the same group owner. |
| Sticky Bit | 	No meaning	 | Users are prevented from deleting files from other users. | 

??? question "Answer the questions bellow"
    
    SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.

    To search the a system for these type of files run the following: <div style="color: red">find / -perm -u=s -type f 2>/dev/null</div>

    Question: What file looks particularly out of the ordinary? 
    > Ans: /usr/bin/menu

    Question: Run the binary, how many options appear?
    > Ans: 3

    Strings is a command on Linux that looks for human readable strings on a binary.
    ![](image-16.png)

    This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname).

    As this file runs as the root users privileges, we can manipulate our path gain a root shell.

    ![](image-17.png)

    We copied the /bin/sh shell, called it curl, gave it the correct permissions and then put its location in our path. This meant that when the /usr/bin/menu binary was run, its using our path variable to find the "curl" binary.. Which is actually a version of /usr/sh, as well as this file being run as root it runs our shell as root!
    >Ans: No needed answer

    Question: What is the root flag (/root/root.txt)?
    > Ans: 177b3cd8562289f37382721c28381f02


