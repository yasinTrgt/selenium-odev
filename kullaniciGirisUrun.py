from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  # import time

class Test_SauceDemo:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        try:
         WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
         print("Kullanıcı /inventory.html sayfasına yönlendirildi.")
        except:
         print("Yönlendirme başarısız oldu.")
        product_items = driver.find_elements(By.XPATH, "//*[@id='inventory_container']/div/div/div/div/div/div[2]")  # Ürünlerin bulunduğu elementlerin listesi
        if len(product_items) == 6:
          print("Ürün sayısı doğru.(6 adet)")
        else:
         print(f"Ürün sayısı doğru değil, beklenen 6 adet, bulunan {len(product_items)} adet.")


testClass = Test_SauceDemo()
testClass.test_invalid_login()