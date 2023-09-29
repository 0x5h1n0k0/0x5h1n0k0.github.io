import requests
import re

# URL của trang web bạn muốn truy cập
url = 'http://localhost:4280/vulnerabilities/brute/'

# Tạo yêu cầu GET để tải trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Sử dụng biểu thức chính quy để tìm giá trị của thẻ có name="user_token"
    pattern = r'<input.*?type=["\']hidden["\'].*?name=["\']user_token["\'].*?value=["\'](.*?)["\'].*?>'
    match = re.search(pattern, response.text)
    
    # Kiểm tra xem có tìm thấy giá trị hay không
    if match:
        user_token_value = match.group(1)
        print(f'Giá trị của thẻ có name="user_token_value" là: {user_token_value}')
    else:
        print('Không tìm thấy thẻ có name="user_token_value" trên trang web.')
else:
    print('Không thể truy cập trang web.')
