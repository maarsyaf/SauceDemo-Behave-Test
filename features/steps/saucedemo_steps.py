from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given("Pengguna membuka halaman login")
def open_login_page(context):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get("https://www.saucedemo.com")
    assert 'Swag Labs' in context.driver.title

@when("Pengguna memasukkan username dan password")
def enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")

@when("Pengguna menekan tombol login")
def click_login(context):
    context.driver.find_element(By.ID, 'login-button').click()
    context.driver.implicitly_wait(5)

@then("Pengguna berhasil login")
def verify_login(context):
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert context.driver.current_url == expected_url, f"URL tidak sesuai: {context.driver.current_url}"

@when("Pengguna memilih produk dan menambahkannya ke keranjang")
def add_product_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.implicitly_wait(2)

@then("Produk berhasil ditambahkan ke keranjang")
def verify_cart(context):
    cart_badge = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

@when("Pengguna menuju halaman checkout")
def go_to_checkout(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.ID, "checkout").click()

@when("Pengguna mengisi informasi checkout")
def fill_checkout_info(context):
    context.driver.find_element(By.ID, "first-name").send_keys("Abdillah")
    context.driver.find_element(By.ID, "last-name").send_keys("Arsyaf")
    context.driver.find_element(By.ID, "postal-code").send_keys("42116")

@when("Pengguna menekan tombol continue dan menyelesaikan checkout")
def complete_checkout(context):
    context.driver.find_element(By.ID, "continue").click()
    context.driver.implicitly_wait(3)
    context.driver.find_element(By.ID, "finish").click()

@then("Checkout berhasil")
def verify_checkout(context):
    thank_you_message = context.driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]')
    assert thank_you_message.text == "Thank you for your order!"

@then("Tutup browser")
def close_browser(context):
    context.driver.quit()
