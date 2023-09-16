---
template: overrides/blog.html
icon: material/plus-circle
title: Cross Site Request Forgery
description: >
  
search:
  exclude: true
hide:
  - feedback

tags:
  - DVWA
  - CSRF
---

# __Cross Site Request Forgery__

_Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application._

---

## __Objective__

Your task is to make the current user change their own password, without them knowing about their actions, using a CSRF attack.

Tóm lại, mục đích của ta là tạo được link để người dùng click vào.

## __Security Level: Low__

Source code

```php title="vulnerabilities/csrf/source/low.php"
<?php

if( isset( $_GET[ 'Change' ] ) ) {
    // Get input
    $pass_new  = $_GET[ 'password_new' ];
    $pass_conf = $_GET[ 'password_conf' ];

    // Do the passwords match?
    if( $pass_new == $pass_conf ) {
        // They do!
        $pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
        $pass_new = md5( $pass_new );

        // Update the database
        $current_user = dvwaCurrentUser();
        $insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
        $result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

        // Feedback for the user
        echo "<pre>Password Changed.</pre>";
    }
    else {
        // Issue with passwords matching
        echo "<pre>Passwords did not match.</pre>";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?> 
```

### __Analysis and exploition__

![](image.png)

Challenge này họ không filter đầu vào. Quan trọng hơn việc đổi password không có 1 cơ chế xác thực nào cả. Xem hình trên ta có thể thấy ta đã nhập đại một password là `pass` và khi ta thử account admin với password mới. Ta login thành công (xem hình bên dưới)

![](image-1.png)

Hơn nữa, ta thấy trên url của phần thay đổi password chỉ là GET thuần và hoàn toàn không có cơ chế mã hóa nào cả.

> `http://localhost:4280/vulnerabilities/csrf/?password_new=pass&password_conf=pass&Change=Change#`

Do đó, thực tế là ta sẽ làm cho người dùng click vào link đó, làm cho họ đổi tài khoản của họ mà bản thân họ không biết.

---

## __Security Level: Medium__

Source code

```php title="vulnerabilities/csrf/source/medium.php"
<?php

if( isset( $_GET[ 'Change' ] ) ) {
    // Checks to see where the request came from
    if( stripos( $_SERVER[ 'HTTP_REFERER' ] ,$_SERVER[ 'SERVER_NAME' ]) !== false ) {
        // Get input
        $pass_new  = $_GET[ 'password_new' ];
        $pass_conf = $_GET[ 'password_conf' ];

        // Do the passwords match?
        if( $pass_new == $pass_conf ) {
            // They do!
            $pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
            $pass_new = md5( $pass_new );

            // Update the database
            $current_user = dvwaCurrentUser();
            $insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
            $result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

            // Feedback for the user
            echo "<pre>Password Changed.</pre>";
        }
        else {
            // Issue with passwords matching
            echo "<pre>Passwords did not match.</pre>";
        }
    }
    else {
        // Didn't come from a trusted source
        echo "<pre>That request didn't look correct.</pre>";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?> 
```

### __Analysis__

### __Exploition__

---

## __Security Level: High__

Source code

```php title=""
```

### __Analysis__

### __Exploition__

---

## __Security Level: Impossible__

Source code

```php title=""
```

### __Analysis__

### __Exploition__

---

### __What we learned__

## __More Information__


- https://owasp.org/www-community/attacks/csrf
- http://www.cgisecurity.com/csrf-faq.html
- https://en.wikipedia.org/wiki/Cross-site_request_forgery
