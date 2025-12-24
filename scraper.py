from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time

def get_facebook_info(username):
    """
    Hàm demo thu thập thông tin từ Facebook.
    LƯU Ý: Thu thập dữ liệu thật từ Facebook có thể vi phạm Điều khoản dịch vụ.
    """
    options = Options()
    # CẤU HÌNH QUAN TRỌNG CHO SERVER (RENDER)
    options.add_argument("--headless=new")  # Chạy ẩn, không cần giao diện
    options.add_argument("--no-sandbox")  # Bắt buộc trên môi trường server
    options.add_argument("--disable-dev-shm-usage")  # Tránh lỗi bộ nhớ
    options.add_argument("--disable-gpu")  # Tắt GPU acceleration
    
    # Trên Render, Chromium thường nằm ở đường dẫn này
    options.binary_location = "/usr/bin/chromium-browser"
    
    driver = None
    try:
        # Thử khởi tạo trình duyệt
        driver = webdriver.Chrome(options=options)
        print(f"[DEBUG] Đã khởi tạo Chrome thành công cho: {username}")
        
        # ĐÂY LÀ PHẦN XỬ LÝ CHÍNH CỦA BẠN
        # Ví dụ: mở trang Facebook
        url = f"https://facebook.com/{username}"
        driver.get(url)
        time.sleep(3)  # Chờ trang tải
        
        # ... (code xử lý HTML, tìm kiếm thông tin của bạn ở đây)
        
        # DỮ LIỆU DEMO - HÃY THAY THẾ BẰNG CODE THẬT CỦA BẠN
        info = {
            'name': 'Nguyễn Văn Demo',
            'uid': '1000123456789',
            'username': username,
            'follower': '15.7K',
            'friends': '1.2K',
            'verified': 'Có ✓',
            'country': 'Việt Nam',
            'registration_date': '15/03/2015'
        }
        
        return info
        
    except WebDriverException as e:
        # Ghi lại lỗi Selenium
        print(f"[ERROR] Lỗi WebDriver: {e}")
        # Trả về dữ liệu mặc định nếu có lỗi
        return {
            'name': 'Lỗi khi thu thập',
            'uid': 'N/A',
            'username': username,
            'follower': 'N/A',
            'friends': 'N/A',
            'verified': 'N/A',
            'country': 'N/A',
            'registration_date': 'N/A',
            'error': str(e)
        }
    except Exception as e:
        # Ghi lại bất kỳ lỗi nào khác
        print(f"[ERROR] Lỗi không xác định: {e}")
        return {
            'name': 'Lỗi hệ thống',
            'uid': 'N/A',
            'username': username,
            'follower': 'N/A',
            'friends': 'N/A',
            'verified': 'N/A',
            'country': 'N/A',
            'registration_date': 'N/A',
            'error': str(e)
        }
    finally:
        # LUÔN đóng trình duyệt dù có lỗi hay không
        if driver:
            driver.quit()
            print(f"[DEBUG] Đã đóng trình duyệt cho: {username}")

