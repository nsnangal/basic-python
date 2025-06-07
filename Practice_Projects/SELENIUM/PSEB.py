import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time,random
from fake_useragent import UserAgent



def setup_connection():
    url="https://registration2024.pseb.ac.in/Login"
    
    ua=UserAgent()
    random_user_agent=ua.random
     
    chrome_options=uc.ChromeOptions()
    chrome_options.page_load_strategy='normal'
    
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    #chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--force-device-scale-factor=1.5")  # Zoom here
    chrome_options.add_argument("--high-dpi-support=2")
   
    driver=uc.Chrome(options=chrome_options)
    driver.get(url)
    driver.maximize_window()
    
    
    wait=WebDriverWait(driver,random.randint(60,70))
    return wait,driver

def exit(driver):
    
    driver.quit()

def pseb_Login_website():
     wait,driver=setup_connection()
    
     username=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='username']")))
     username.click()
     
     username.send_keys("0055234",Keys.TAB,"school0049",Keys.TAB*3,Keys.ENTER)
     time.sleep(random.randint(1,3))
     print("Login Successfully")
     time.sleep(random.randint(1,3))
     
     Navigation_to_Registeration_Page(wait,driver)
     #next function name which will be called to reach upto registration page.
def Navigation_to_Registeration_Page(wait,driver):
    
    time.sleep(random.randint(1,3))
    registration_click=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='HPL']/div[2]/div/div/div[2]/ul[1]/li[4]/a")))
    driver.execute_script("arguments[0].click();",registration_click)
     
    time.sleep(random.randint(1,2))
    registration_portal_click=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='HPL']/div[2]/div/div/div[2]/ul[1]/li[4]/ul/li[1]/a")))
    driver.execute_script("arguments[0].click();",registration_portal_click) 

    time.sleep(random.randint(1,3))
    pop_up=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='popup1']/center/table/tbody/tr[2]/td/a")))
    driver.execute_script("arguments[0].click();",pop_up)
    time.sleep(random.randint(1,3))
    N2_form_selection(wait,driver)
def N2_form_selection(wait,driver):

    N2_form_select=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='collapse5']/div/ul/li[1]/a")))
    driver.execute_script("arguments[0].click();",N2_form_select)
    time.sleep(random.randint(1,3))
    terms_agree=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='Submit']")))
    driver.execute_script("arguments[0].click();",terms_agree)
    time.sleep(2)
    Fill_N2_Form(wait,driver)
def Fill_N2_Form(wait,driver):
  
    
    def previous_class_detail():
        check_flag="notok"
        all_tag_ids=["//*[@id='ddlcategory']","//*[@id='ddlboard']","//*[@id='OtherBoard']",
                 "//*[@id='txtboardroll']","//*[@id='ddlmonthses']","//*[@id='ddlyear']",
                 "//*[@id='prevschoolname']","//*[@id='IsPrevSchoolSelf']",
                 "//*[@id='IsPSEBRegNum']","//*[@id='IsNRICandidate']"]
        count=0
        for tag_id in all_tag_ids:
            time.sleep(2)
            count +=1
            N2_form_fill=wait.until(EC.presence_of_element_located((By.XPATH,tag_id)))
            
          
            if N2_form_fill.get_attribute("id")=="ddlcategory" or N2_form_fill.get_attribute("id")=="ddlboard" or N2_form_fill.get_attribute("id")=="ddlmonthses" or N2_form_fill.get_attribute("id")=="ddlyear":
               insert_value=Select(N2_form_fill)
              
               if N2_form_fill.get_attribute("id")=="ddlboard":
                     N2_form_fill.click()
                     board="P.S.E.B BOARD"
                     N2_form_fill.click()
                     time.sleep(1)
                     
                     N2_form_fill.send_keys(board)
                     print(f"'{insert_value.first_selected_option.text}' after send keys")
                     
                     if board =="OTHER BOARD":
                         check_flag="ok"
                    
                     while insert_value.first_selected_option.text=="---SELECT BOARD--":
                         driver.execute_script("alert('please select the board')")
                         time.sleep(10)
                                        
                     
               elif N2_form_fill.get_attribute("id")=="ddlmonthses":
                    N2_form_fill.click()
                    time.sleep(2)
                    insert_value.select_by_visible_text("April")
                    N2_form_fill.click()
               elif N2_form_fill.get_attribute("id")=="ddlyear" :
                    
                    N2_form_fill.click()
                    time.sleep(2)
                    N2_form_fill.send_keys("2020")
               elif N2_form_fill.get_attribute("id")=="ddlcategory":
                    time.sleep(1)
                    N2_form_fill.click()
                    time.sleep(1)
                    N2_form_fill.send_keys("8TH PASSED") 

            if N2_form_fill.get_attribute("id")=="OtherBoard" and check_flag=="ok":
                 time.sleep(2)
                 N2_form_fill.click()
                 time.sleep(1)
                 N2_form_fill.send_keys("type other board here")
                 check_flag="notok"
        
            elif  N2_form_fill.get_attribute("id")=="txtboardroll":    
            
              N2_form_fill.click()
              time.sleep(1)
              N2_form_fill.send_keys("112222")
        
            elif N2_form_fill.get_attribute("id")=="prevschoolname":
              
              N2_form_fill.click()
              time.sleep(1)
              N2_form_fill.send_keys("gsss nangal lubana")
            elif N2_form_fill.get_attribute("id")=="IsPrevSchoolSelf":
                N2_form_fill.click()
            elif N2_form_fill.get_attribute("id")=="IsPSEBRegNum":
                N2_form_fill.click()
            elif N2_form_fill.get_attribute("id")=="IsNRICandidate":
                N2_form_fill.click()

    previous_class_detail()
    time.sleep(60)
    exit(driver)
    print("done")
    time.sleep(60)
 
if __name__== "__main__":
 pseb_Login_website()

