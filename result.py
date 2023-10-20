from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

symbol_no = "23403271";
date_of_birth = "2062/03/14";

try:
    # NTC Website
    print("NTC Website")
    ntc_website = webdriver.Chrome()
    ntc_website.get("https://neb.ntc.net.np/")
    ntc_website.maximize_window()

    time.sleep(1)

    ntc_symbol = ntc_website.find_element("xpath", '//*[@id="symbol"]')
    ntc_symbol.send_keys(symbol_no)

    ntc_dob = ntc_website.find_element("xpath", '//*[@id="dob"]')
    ntc_dob.send_keys(date_of_birth)

    ntc_button = ntc_website.find_element("xpath", '//*[@id="innerpan"]/form/fieldset/table/tbody/tr[3]/td[2]/input')
    ntc_button.click()
    
    time.sleep(60)
    
except Exception as e:
    print(e)
    print("Error Occured")
    print("Please Check Your Internet Connection")
