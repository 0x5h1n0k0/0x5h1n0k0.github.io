---
template: overrides/blog.html
icon: material/plus-circle
title: TryHackMe - Hacking with Powershell - Walkthrough
description: >
  
search:
  exclude: true
hide:
  - feedback
tags:
  - THM-Room
---

# __TryHackMe - Hacking with Powershell - Walkthrough__

---

## __Task 1:  Objectives__

<span> 
    <span class="twemoji mdx-heart content-heart">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu"> Content </span>
</span>

Before completing this room, you should be aware of some fundamentals. For example, the differences between CMD, PS and some syntax. This room will cover the following:

- What is Powershell
- Basic Powershell commands
- Windows enumeration skills
- Powershell scripting

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__Read the above and deploy the machine!__"
    No answer needed

## __Task 2: What is Powershell?__

<span> 
    <span class="twemoji mdx-heart content-heart">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu"> Content </span>
</span>

Powershell is the Windows Scripting Language and shell environment built using the .NET framework.

This also allows Powershell to execute .NET functions directly from its shell. Most Powershell commands, called cmdlets, are written in .NET. Unlike other scripting languages and shell environments, the output of these cmdlets are objects - making Powershell somewhat object-oriented.

This also means that running cmdlets allows you to perform actions on the output object (which makes it convenient to pass output from one cmdlet to another). The normal format of a cmdlet is represented using **Verb-Noun**; for example, the cmdlet to list commands is called `Get-Command`

Common verbs to use include:

- Get
- Start
- Stop 
- Read
- Write
- New
- Out

To get the complete list of approved verbs, visit [this](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7) link.

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__What is the command to get a new object?__"
    Get-New

To see the usage of a cmdlet we use the syntax `Get-Help + <name of cmdlet> -Examples`. For example, we want to see the usage of the Get-Command[^2] command, we use the `Get-Help Get-Command -Examples` syntax. See picture bellow.

<figure markdown>
  ![Image title](/blog/offensive-security/init-access/red-team-weaponization/images/powershell-getcommand.png#zoom)
  <figcaption>This pic describes how to use the Get-Command command syntax</figcaption>
</figure>

## __Task 3: Basic Powershell Commands__

<span> 
    <span class="twemoji mdx-heart content-heart">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu"> Content </span>
</span>

Now that we've understood how cmdlets work - let's explore how to use them! The main thing to remember here is that `Get-Command` and `Get-Help` are your best friends! 

### __Using Get-Help__

`Get-Help` displays information about a cmdlet. To get help with a particular command, run the following:

`Get-Help Command-Name`

You can also understand how exactly to use the command by passing in the `-examples` flag. This would return output like the following: 

<div class="result" markdown>

``` powershell title="Running the Get-Help cmdlet to explain a command"
PS C:\Users\Administrator> Get-Help Get-Command -Examples

NAME
    Get-Command

SYNOPSIS
Gets all commands.

Example 1: Get cmdlets, functions, and aliases

PS C:\>Get-Command
```

</div>

### __Using Get-Command__

`Get-Command` gets all the cmdlets installed on the current Computer. The great thing about this cmdlet is that it allows for pattern matching like the following `Get-Command Verb-*` or `Get-Command *-Noun`

Running `Get-Command New-*` to view all the cmdlets for the verb new displays the following: 

<div class="result" markdown>

``` powershell title="Using the Get-Command to list all cmdlets installed"
PS C:\Users\Administrator> Get-Command New-*

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           New-AWSCredentials                                 3.3.563.1  AWSPowerShell
Alias           New-EC2FlowLogs                                    3.3.563.1  AWSPowerShell
Alias           New-EC2Hosts                                       3.3.563.1  AWSPowerShell
Alias           New-RSTags                                         3.3.563.1  AWSPowerShell
Alias           New-SGTapes                                        3.3.563.1  AWSPowerShell
Function        New-AutologgerConfig                               1.0.0.0    EventTracingManagement
Function        New-DAEntryPointTableItem                          1.0.0.0    DirectAccessClientComponents
Function        New-DscChecksum                                    1.1        PSDesiredStateConfiguration
Function        New-EapConfiguration                               2.0.0.0    VpnClient
Function        New-EtwTraceSession                                1.0.0.0    EventTracingManagement
Function        New-FileShare                                      2.0.0.0    Storage
Function        New-Fixture                                        3.4.0      Pester
Function        New-Guid                                           3.1.0.0    Microsoft.PowerShell.Utility
--cropped for brevity--
```

</div>

### __Object Manipulation__

In the previous task, we saw how the output of every cmdlet is an object. If we want to manipulate the output, we need to figure out a few things:

- passing the output to other cmdlets
- using specific object cmdlets to extract information

The Pipeline(`|`) is used to pass output from one cmdlet to another. A major difference compared to other shells is that Powershell passes an object to the next cmdlet instead of passing text or string to the command after the pipe. Like every object in object-oriented frameworks, an object will contain methods and properties.

You can think of methods as functions that can be applied to output from the cmdlet, and you can think of properties as variables in the output from a cmdlet. To view these details, pass the output of a cmdlet to the `Get-Member` cmdlet:

`Verb-Noun | Get-Member` 

An example of running this to view the members for `Get-Command` is:

`Get-Command | Get-Member -MemberType Method`

<div class="result" markdown>

``` powershell title="Using pipe (|) to pass output from one cmdlet to another"
PS C:\Users\Administrator> Get-Command | Get-Member -MemberType Method


   TypeName: System.Management.Automation.AliasInfo

Name             MemberType Definition
----             ---------- ----------
Equals           Method     bool Equals(System.Object obj)
GetHashCode      Method     int GetHashCode()
GetType          Method     type GetType()
ResolveParameter Method     System.Management.Automation.ParameterMetadata ResolveParameter(string name)
ToString         Method     string ToString()


   TypeName: System.Management.Automation.FunctionInfo

Name             MemberType Definition
----             ---------- ----------
Equals           Method     bool Equals(System.Object obj)
GetHashCode      Method     int GetHashCode()
GetType          Method     type GetType()
ResolveParameter Method     System.Management.Automation.ParameterMetadata ResolveParameter(string name)
ToString         Method     string ToString()


   TypeName: System.Management.Automation.CmdletInfo

Name             MemberType Definition
----             ---------- ----------
Equals           Method     bool Equals(System.Object obj)
GetHashCode      Method     int GetHashCode()
GetType          Method     type GetType()
ResolveParameter Method     System.Management.Automation.ParameterMetadata ResolveParameter(string name)
ToString         Method     string ToString()


PS C:\Users\Administrator>
```

!!! note "From the above flag in the command, you can see that you can also select between methods and properties."

</div>

### __Creating Objects From Previous _cmdlets___

One way of manipulating objects is pulling out the properties from the output of a cmdlet and creating a new object. This is done using the `Select-Object` cmdlet. 

Here's an example of listing the directories and just selecting the mode and the name:

<div class="result" markdown>

``` powershell title="Listing the directories and filtering via mode and name"
PS C:\Users\Administrator> Get-ChildItem | Select-Object -Property Mode, Name
Mode   Name
----   ----
d-r--- Contacts
d-r--- Desktop
d-r--- Documents
d-r--- Downloads
d-r--- Favorites
d-r--- Links
d-r--- Music
d-r--- Pictures
d-r--- Saved Games
d-r--- Searches
d-r--- Videos

PS C:\Users\Administrator>
```

</div>  

You can also use the following flags to select particular information:

- first - gets the first x object
- last - gets the last x object
- unique - shows the unique objects
- skip - skips x objects

### __Filtering Objects__

When retrieving output objects, you may want to select objects that match a very specific value. You can do this using the `Where-Object` to filter based on the value of properties. 

The general format for using this _cmdlet_ is 

`Verb-Noun | Where-Object -Property PropertyName -operator Value`

`Verb-Noun | Where-Object {$_.PropertyName -operator Value}`

The second version uses the `$_` operator to iterate through every object passed to the `Where-Object` _cmdlet_.

__Powershell is quite sensitive, so don't put quotes around the command!__

Where `-operator` is a list of the following operators:

- `-Contains`: if any item in the property value is an exact match for the specified value
- `-EQ`: if the property value is the same as the specified value
- `-GT`: if the property value is greater than the specified value

For a full list of operators, use [this](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-6) link.

Here's an example of checking the stopped processes:

<div class="result" markdown>

``` powershell title="Demonstrating the use of operators only to show stopped services"
PS C:\Users\Administrator> Get-Service | Where-Object -Property Status -eq Stopped

Status   Name               DisplayName
------   ----               -----------
Stopped  AJRouter           AllJoyn Router Service
Stopped  ALG                Application Layer Gateway Service
Stopped  AppIDSvc           Application Identity
Stopped  AppMgmt            Application Management
Stopped  AppReadiness       App Readiness
Stopped  AppVClient         Microsoft App-V Client
Stopped  AppXSvc            AppX Deployment Service (AppXSVC)
Stopped  AudioEndpointBu... Windows Audio Endpoint Builder
Stopped  Audiosrv           Windows Audio
Stopped  AxInstSV           ActiveX Installer (AxInstSV)
Stopped  BITS               Background Intelligent Transfer Ser...
Stopped  Browser            Computer Browser
Stopped  bthserv            Bluetooth Support Service
-- cropped for brevity--
```

</div> 

### __Sort-Object__

When a _cmdlet_ outputs a lot of information, you may need to sort it to extract the information more efficiently. You do this by pipe-lining the output of a _cmdlet_ to the `Sort-Object` _cmdlet_.

The format of the command would be:

`Verb-Noun | Sort-Object`

Here's an example of sorting the list of directories:

<div class="result" markdown>

``` powershell title="Using the Sort-Object cmdlet to sort piped information"
PS C:\Users\Administrator> Get-ChildItem | Sort-Object
    Directory: C:\Users\Administrator
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        10/3/2019   5:11 PM                Contacts
d-r---        10/5/2019   2:38 PM                Desktop
d-r---        10/3/2019  10:55 PM                Documents
d-r---        10/3/2019  11:51 PM                Downloads
d-r---        10/3/2019   5:11 PM                Favorites
d-r---        10/3/2019   5:11 PM                Links
d-r---        10/3/2019   5:11 PM                Music
d-r---        10/3/2019   5:11 PM                Pictures
d-r---        10/3/2019   5:11 PM                Saved Games
d-r---        10/3/2019   5:11 PM                Searches
d-r---        10/3/2019   5:11 PM                Videos
PS C:\Users\Administrator>
```

</div> 

!!! note "Now that you've understood how Powershell works let's try some commands to apply this knowledge!"
---
<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__What is the location of the file "interesting-file.txt"__"

    === "Answer"
        ``` powershell
        C:\Program Files
        ```
    === "Explain"

        To find the file interesting-file.txt we will scan the directory with the following command:
        ``` powershell
        Get-ChildItem -Path D:\ -Include *interesting-file*.txt -File -Recurse -ErrorAction SilentlyContinue
        ```
        I will explain the flags:

        1. Flag -Path: Specify the path to scan
        2. Flag -Include: Specify the file to scan (You can use the `*` operator to specify to find files whose filename includes the string between the two `*` operators we have set.)
        3. Flag -File: Specify only file
        4. Flag -Recurse: Recursive search
        5. Flag -ErrorAction SilentlyContinue: Ignore error

!!! question "__Specify the contents of this file__"

    === "Answer"
        ``` powershell
        notsointerestingcontent
        ```
    === "Explain"

        To view content of file, you can use:
        ``` powershell
        1. Get-Content -Path + path_of_file
        2. More + path_of_file
        ```

!!! question "__How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?__"

    === "Answer"
        ``` powershell
        6638
        ```
    === "Explain"

        First of all, you must know all functions and cmdlets on the system by listing them. Use `Get-Commnad`. You see that the output consists of 4 columns in order: CommandType, Name, Version, Source. Focus at CommandType to filter.
        Second, filter the results to find the number of cmdlets by: `Where-Object -Property CommandType -like Cmdlet`. Ye, you have filtered out all cmdlets on the system.
        Last, let's count them by `Measure command`

        <figure markdown>
        ![Image title](/blog/room/hacking-with-powershell/images/t3q3.png#zoom)
        <figcaption>The image describes the result</figcaption>
        </figure>

!!! question "__Get the MD5 hash of interesting-file.txt__"

    === "Answer"
        ``` powershell
        49A586A2A9456226F8A1B4CEC6FAB329
        ```
    === "Explain"
        To get hash of file, you can use Get-FileHash + <file/path_of_file> -Algorithm -MD5. 
        The full syntax to solve this question is:
        ``` powershell
        Get-FileHash C:\'Program Files'\interesting-file.txt.txt -Algorithm -MD5
        ```

!!! question "__What is the command to get the current working directory?__"

    === "Answer"
        ``` powershell
        Get-Location
        ```
    === "Explain"

        To get the current working directory, you will use Get-Location command. Furthermore, you can use Get-LocalUser command to computer show up `all user` in computer.

!!! question "__Does the path "C:\Users\Administrator\Documents\Passwords" Exist (Y/N)?__"

    === "Answer"
        ``` powershell
        N
        ```
    === "Explain"

        Like the previous scenario, we will use `Get-Location + path` to check if the working directory exists or not. 
        
        Full syntax:
        ```powershell
        Get-Location C:\Users\Administrator\Documents\Passwords
        ```

        <figure markdown>
        ![Image title](/blog/room/hacking-with-powershell/images/t3q4.png#zoom)
        <figcaption>The image describes the result</figcaption>
        </figure>

!!! question "__What command would you use to make a request to a web server?__"

    === "Answer"
        ``` powershell
        Invoke-WebRequest
        ```
    === "Explain"
        [Search](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.1&viewFallbackFrom=powershell-6) google or find in all cmdlets on the system by filtering as follows:

        1. Find all cmdlets and funtions by `Get-Command command`
        2. Filter to get cmdlets which itself has one and keywords like call, request,... in the name by `Where-Object -Property Name -like *request*`. You will see Invoke-WebRequest command in results.

!!! question "__Base64 decode the file b64.txt on Windows.__"

    === "Answer"
        ``` powershell
        ihopeyoudidthisonwindows
        ```
    === "Explain"
        To showup this question, use `Certutil command` with flag decode.
        Besides, Certutil command also has some useful flags:
        
        - encode: encode according to base64
        - decodehex: decode according to hexadecimal

        View more at https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil

        Full step: 
        
        1. Certutil -decode b64.txt output.txt
        2. Get-Content output.txt

        ``` powershell hl_lines="6"
        PS C:\Users\Administrator\Desktop> certutil -decode .\b64.txt a.txt        
        Input Length = 432                                                         
        Output Length = 323                                                        
        CertUtil: -decode command completed successfully.                          
        PS C:\Users\Administrator\Desktop> Get-Content a.txt                              
        this is the flag - ihopeyoudidthisonwindows                                
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                        
        the rest is garbage                                                                                                                                    
        ```

## __Task 4:  Enumeration__

<span> 
    <span class="twemoji mdx-heart content-heart">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu"> Content </span>
</span>

The first step when you have gained initial access to any machine would be to enumerate. We'll be enumerating the following:

- users
- basic networking information
- file permissions
- registry permissions
- scheduled and running tasks
- insecure files

Your task will be to answer the following questions to enumerate the machine using Powershell commands! 

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__How many users are there on the machine?__"

    === "Answer"
        ``` powershell
        5
        ```
    === "Explain"
        
        Use Get-LocalUser command which I explained at __What is the command to get the current working directory?__ question 

!!! question "__Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?__"

    === "Answer"
        ``` powershell
        Guest
        ```
    === "Explain"
        
        Use `Get-LocalUser | Select *` command to showup full property. Then, filter output and get results.

        ```powershell hl_lines="13"
        PS C:\Users\Administrator\Desktop> get-localuser | select * | where-object sid -like *501*
        AccountExpires         :                                                                         
        Description            : Built-in account for guest access to the computer/domain                
        Enabled                : False                                                                   
        FullName               :                                                                         
        PasswordChangeableDate :                                                                         
        PasswordExpires        :                                                                         
        UserMayChangePassword  : False                                                                   
        PasswordRequired       : False                                                                   
        PasswordLastSet        :                                                                         
        LastLogon              :                                                                        
        Name                   : Guest                                                                   
        SID                    : S-1-5-21-1394777289-3961777894-1791813945-501                          
        PrincipalSource        : Local                                                                   
        ObjectClass            : User                                                                    
        ```

!!! question "__How many users have their password required values set to False?__"

    === "Answer"
        ``` powershell
        4
        ```
    === "Explain"
        
        Filter, filter, filter,...

        ```powershell
        PS C:\Users\Administrator\Desktop> get-localuser | select * | where-object passwordrequired -match false | measure        
                                                                                                                                                                                                                        
        Count    : 4                                                                                                    
        Average  :                                                                                                      
        Sum      :                                                                                                      
        Maximum  :                                                                                                      
        Minimum  :                                                                                                      
        Property :
        ```
            
    
!!! question "__How many local groups exist?__"

    === "Answer"
        ``` powershell
        24
        ```
    === "Explain"
        
        Use `get-command | where name -like *group* | where name -like *local*` to file cmdlet, and filter then.

        ```powershell hl_lines="58" 
        PS C:\Users\Administrator\Desktop> get-command | where-object name -like *group* | where-object name -like *local*                                          
                                                                                            
        CommandType     Name                                               Version    Source                                    
        -----------     ----                                               -------    ------                                    
        Cmdlet          Add-LocalGroupMember                               1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Get-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Get-LocalGroupMember                               1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          New-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Remove-LocalGroup                                  1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Remove-LocalGroupMember                            1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Rename-LocalGroup                                  1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Set-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts 
                                                                                                                                                                                                                                 
        PS C:\Users\Administrator\Desktop> get-command | where name -like *group* | where name -like *local*        

        CommandType     Name                                               Version    Source                                    
        -----------     ----                                               -------    ------                                    
        Cmdlet          Add-LocalGroupMember                               1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Get-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Get-LocalGroupMember                               1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          New-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Remove-LocalGroup                                  1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Remove-LocalGroupMember                            1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Rename-LocalGroup                                  1.0.0.0    Microsoft.PowerShell.LocalAccounts        
        Cmdlet          Set-LocalGroup                                     1.0.0.0    Microsoft.PowerShell.LocalAccounts  

                                                                                                                                                                                                                                                            
        PS C:\Users\Administrator\Desktop> get-localgroup                      
                                                                                                                                                                                
        Name                                Description                                                                         
        ----                                -----------                                                                         
        Access Control Assistance Operators Members of this group can remotely query authorization attributes and permission... 
        Administrators                      Administrators have complete and unrestricted access to the computer/domain         
        Backup Operators                    Backup Operators can override security restrictions for the sole purpose of back... 
        Certificate Service DCOM Access     Members of this group are allowed to connect to Certification Authorities in the... 
        Cryptographic Operators             Members are authorized to perform cryptographic operations.                         
        Distributed COM Users               Members are allowed to launch, activate and use Distributed COM objects on this ... 
        Event Log Readers                   Members of this group can read event logs from local machine                        
        Guests                              Guests have the same access as members of the Users group by default, except for... 
        Hyper-V Administrators              Members of this group have complete and unrestricted access to all features of H... 
        IIS_IUSRS                           Built-in group used by Internet Information Services.                               
        Network Configuration Operators     Members in this group can have some administrative privileges to manage configur... 
        Performance Log Users               Members of this group may schedule logging of performance counters, enable trace... 
        Performance Monitor Users           Members of this group can access performance counter data locally and remotely      
        Power Users                         Power Users are included for backwards compatibility and possess limited adminis... 
        Print Operators                     Members can administer printers installed on domain controllers                     
        RDS Endpoint Servers                Servers in this group run virtual machines and host sessions where users RemoteA... 
        RDS Management Servers              Servers in this group can perform routine administrative actions on servers runn... 
        RDS Remote Access Servers           Servers in this group enable users of RemoteApp programs and personal virtual de... 
        Remote Desktop Users                Members in this group are granted the right to logon remotely                       
        Remote Management Users             Members of this group can access WMI resources over management protocols (such a... 
        Replicator                          Supports file replication in a domain                                               
        Storage Replica Administrators      Members of this group have complete and unrestricted access to all features of S... 
        System Managed Accounts Group       Members of this group are managed by the system.                                    
        Users                               Users are prevented from making accidental or intentional system-wide changes an...      

        PS C:\Users\Administrator\Desktop> get-localgroup | measure
        Count    : 24                                                                                                           
        Average  :                                                                                                              
        Sum      :                                                                                                              
        Maximum  :                                                                                                              
        Minimum  :                                                                                                              
        Property :         
        ```             
            

!!! question "__What command did you use to get the IP address info?__"

    === "Answer"
        ``` powershell
        Get-NetIPAddress
        ```
    === "Explain"
        
        Use `Get-Command | Where-Object -property name -like "*ip*" | where-object -property Name -like "*address*"` to find cmdlets.

!!! question "__How many ports are listed as listening?__"

    === "Answer"
        ``` powershell
        20
        ```
    === "Explain"
        
        Use this command: `get-nettcpconnection | where state -match listen | measure ` 

!!! question "__What is the remote address of the local port listening on port 445?__"

    === "Answer"
        ``` powershell
        ::
        ```
    === "Explain"
        
        Use this command: `get-nettcpconnection | where localport -match 445`

!!! question "__How many patches have been applied?__"

    === "Answer"
        ``` powershell
        20
        ```
    === "Explain"
        
        Use this command: `get-hostfix` 

!!! question "__When was the patch with ID KB4023834 installed?__"

    === "Answer"
        ``` powershell
        6/15/2017 12:00:00 AM
        ```
    === "Explain"
        
        Use this command: `get-hostfix | where hostfixID -match KB4023834`  

!!! question "__Find the contents of a backup file.__"

    === "Answer"
        ``` powershell
        backpassflag
        ```
    === "Explain"
        
        First, you must find backup (in window, it has the extension __.bak__). Find it by 
        ```pơershell
        get-childitem -path C:\ -include *.bak* -file  -recurse -erroraction silentlycontinue
        ```

        Second, read it
        ```powershell
        PS C:\Users\Administrator> more 'C:\Program Files (x86)\Internet Explorer\passwords.bak.txt' 
        backpassflag                                                                                                                                                                            
        ```

!!! question "__Search for all files containing API_KEY__"

    === "Answer"
        ``` powershell
        fakekey123
        ```
    === "Explain"
        
        Use this command to solve:
        ```powershell
        get-childitem -path c:\* -recurse -erroraction silentlycontinue | select-string -pattern API_KEY
        ``` 

!!! question "__What command do you do to list all the running processes?__"

    === "Answer"
        ``` powershell
        Get-Process
        ```
    === "Explain"
        Find cmdlet by using get-command command and filter
         

!!! question "__What is the path of the scheduled task called new-sched-task?__"

    === "Answer"
        ``` powershell
        /
        ```
    === "Explain"
        
        Find command that it provides schedule task: `get-command | where name -like *schedule*`. You will see `get-scheduledtask`, this is the command to look for.
        Then, filter output and get result.
        ```powershell
        PS C:\Users\Administrator> get-scheduledtask | where taskname -like *new*                                                                                                                   
        TaskPath                                       TaskName                          State        
        --------                                       --------                          -----        
        \                                              new-sched-task                    Ready        
        ```
!!! question "__Who is the owner of the C:\?__"

    === "Answer"
        ``` powershell
        NT SERVICE\TrustedInstaller
        ```
    === "Explain"
        
        To get owner of X (path_of_folder/path_of_file), use `Get-Acl command`.

        Full syntax to solve:

        ```powershell
        PS C:\Users\Administrator\Desktop> get-acl C:\          
                                                                                                                                                             
                Directory:                                                                                                                                                                                           
        Path        Owner                               Access        
                            
        ----        -----                               ------                           
        C:\         NT SERVICE\TrustedInstaller         CREATOR OWNER Allow  268435456... 
        ```

## __Task 5: Basic Scripting Challenge__

Now that we have run Powershell commands, let's try to write and run a script to do more complex and powerful actions. 

For this ask, we'll use Powershell ISE (the Powershell Text Editor). Let's use a particular scenario to show an example of this script. Given a list of port numbers, we want to use this list to see if the local port is listening. Open the listening-ports.ps1 script on the Desktop using Powershell ISE. Powershell scripts usually have the ***.ps1*** file extension. 

```ps1
$system_ports = Get-NetTCPConnection -State Listen

$text_port = Get-Content -Path C:\Users\Administrator\Desktop\ports.txt

foreach($port in $text_port){

    if($port -in $system_ports.LocalPort){
        echo $port
     }

}
```

On the first line, we want to get a list of all the ports on the system that are listening. We do this using the `Get-NetTCPConnection` cmdlet. We are then saving the output of this cmdlet into a variable. The convention to create variables is used as:

```ps1
$variable_name = value
```

In the following line, we want to read a list of ports from the file. We do this using the `Get-Content` cmdlet. Again, we store this output in the variables. The simplest next step is to iterate through all the ports in the file to see if the ports are listening. To iterate through the ports in the file, we use the following:

```ps1
foreach($new_var in $existing_var){}
```

This particular code block is used to loop through a set of objects. Once we have each individual port, we want to check if this port occurs in the listening local ports. Instead of doing another for loop, we just use an if statement with the `-in` operator to check if the port exists in the `LocalPort` property of any object. A full list of if statement comparison operators can be found here. To run the script, call the script path using Powershell or click the green button on Powershell ISE:

<figure markdown>
![Image title](https://tryhackme-images.s3.amazonaws.com/user-uploads/5c549500924ec576f953d9fc/room-content/e72e79a91264766cbefdbf33e9763202.png#zoom)
<figcaption></figcaption>
</figure>

Now that we've seen what a basic script looks like - it's time to write one of your own. The emails folder on the Desktop contains copies of the emails John, Martha, and Mary have been sending to each other(and themselves). Answer the following questions with regard to these emails (try not to open the files and use a script to answer the questions). 

Scripting may be a bit difficult, but [here](https://learnxinyminutes.com/docs/powershell/) is a good resource to use: 

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__What file contains the password__"

    === "Answer"
        ``` powershell
        Doc3M
        ```
    === "Explain"
        We use `select-string -pattern password` command to solve this chall. Let's try it with each file.

        Full command
        ```powershell
         get-childitem -path .\emails\ -file -recurse | select-string -pattern password
         ```
!!! question "__What is the password?__"

    === "Answer"
        ``` powershell
        johnisalegend99
        ```
    === "Explain"

!!! question "__What files contains an HTTPS link?__"

    === "Answer"
        ``` powershell
        Doc2Mary
        ```
    === "Explain"

## __Task 6: Intermediate Scripting__

<span> 
    <span class="twemoji mdx-heart content-heart">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu"> Content </span>
</span>

Now that you've learnt a little bit about how scripting works - let's try something a bit more interesting. Sometimes we may not have utilities like Nmap and Python available, and we are forced to write scripts to do very rudimentary tasks.

Why don't you try writing a simple port scanner using Powershell? Here's the general approach to use: 

- Determine IP ranges to scan(in this case it will be localhost) and you can provide the input in any way you want
- Determine the port ranges to scan
- Determine the type of scan to run(in this case it will be a simple TCP Connect Scan)

<span> 
    <span class="twemoji mdx-heart ans-wu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 20.408c-.492.308-.903.546-1.192.709-.153.086-.308.17-.463.252h-.002a.75.75 0 0 1-.686 0 16.709 16.709 0 0 1-.465-.252 31.147 31.147 0 0 1-4.803-3.34C3.8 15.572 1 12.331 1 8.513 1 5.052 3.829 2.5 6.736 2.5 9.03 2.5 10.881 3.726 12 5.605 13.12 3.726 14.97 2.5 17.264 2.5 20.17 2.5 23 5.052 23 8.514c0 3.818-2.801 7.06-5.389 9.262A31.146 31.146 0 0 1 14 20.408z"></path></svg>
    </span>
        <span class="content-wu ans-wu"> Answer the questions below </span>
</span>

!!! question "__How many open ports did you find between 130 and 140(inclusive of those two)?__"

    === "Answer"
        ``` powershell
        11
        ```
    === "Explain"
        Use `Test-Netconnection` command to test connection. 

        Script
        ```powershell title="script.ps1"
        for ($i=130;i -le 140; $i ++){
            test-connection localhost -port $i
        }
        ```

## More

Operator in powershell: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comparison_operators?view=powershell-7.3&viewFallbackFrom=powershell-6

Script file: https://learnxinyminutes.com/docs/powershell/

Full command: https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.3&viewFallbackFrom=powershell-7 
