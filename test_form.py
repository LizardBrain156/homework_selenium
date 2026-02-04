import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    submit_button.click()
    success = driver.find_element(By.CLASS_NAME, "success")
    assert success

def test_login_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    submit_button.click()
    failure = driver.find_element(By.CLASS_NAME, "error")
    assert failure