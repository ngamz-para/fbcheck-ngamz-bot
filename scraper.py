from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_facebook_info(username):
    """
    Hàm giả lập để minh họa. Thu thập dữ liệu thực tế từ Facebook
    là việc phức tạp, dễ hỏng và có thể vi phạm điều khoản.
    """
    driver = webdriver.Chrome() # Cần cài đặt ChromeDriver phù hợp
    url = f"https://facebook.com/{username}"
    driver.get(url)
    time.sleep(5) # Chờ trang tải

    # CÁC THAO TÁC "SCRAPE" DỮ LIỆU GIẢ ĐỊNH
    # Ví dụ: tìm tên, thành phố... (Các bộ chọn CSS/HTML này sẽ THAY ĐỔI THƯỜNG XUYÊN)
    info = {
        "name": "Nguyễn Văn A (Ví dụ)",
        "uid": "Không xác định",
        "location": "Hà Nội",
        # ... các trường khác
    }
    driver.quit()
    return info