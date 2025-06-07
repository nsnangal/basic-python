import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time,keyring,hashlib

def auto_login_incometax():
    driver=uc.Chrome()
    driver.get("https://eportal.incometax.gov.in/iec/foservices/#/login")
    
    time.sleep(2)
    userid=driver.find_element(By.XPATH,"//*[@id='panAdhaarUserId']")
    userid.click()
    userid.send_keys("EBFPS7499K")
       
    SUBMIT=driver.find_element(By.XPATH,"//*[@id='maincontentid']"
    "/app-login/div/app-login-page/div/div[2]/div[1]/div[2]/button")
    SUBMIT.click()
    
    time.sleep(1)

    PASSWORD=driver.find_element(By.XPATH,"//*[@id='loginPasswordField']")
    PASSWORD.click()
    
    PASSWORD.send_keys("innocent12@")
    
    time.sleep(5)

    login=driver.find_element(By.XPATH,"//*[@id='maincontentid']/app-login/div/app-password-page/div[1]/div[2]/div[1]/div[5]/button")
    login.click()
    print("clicked successfully")
    time.sleep(100)
    driver.quit()

auto_login_incometax()