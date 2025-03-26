from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Inisialisasi WebDriver sebelum semua tes dijalankan."""
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_all(context):
    """Menutup browser setelah semua tes selesai."""
    context.driver.quit()
