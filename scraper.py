from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_facebook_info(username):
    options = Options()
    options.add_argument("--headless")  # Chạy ẩn
    options.add_argument("--no-sandbox")  # Cần thiết cho môi trường server
    options.add_argument("--disable-dev-shm-usage")  # Cần thiết cho môi trường server
    
    driver = webdriver.Chrome(options=options)
    # ... phần code xử lý của bạn ...
    driver.quit()
    return info
