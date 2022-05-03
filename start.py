
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time
import pyautogui
import requests
import shutil
import subprocess

COINBASE = 0
PAYPAL = 0
CASHAPP = 0
VENMO = 0
ZELLE = 0
AMAZON = 0
UBER_EATS = 0
UBER = 0

EMAIL = " EMAIL HERE FOR NOW"
EMAIL_CHAR_LIST = []

PASSWD = "PASSWD HERE FOR NOW"
PASSWD_CHAR_LIST = []

for LETTER in EMAIL:
        EMAIL_CHAR_LIST.append(LETTER)

for LETTER in PASSWD:
        PASSWD_CHAR_LIST.append(LETTER)

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def GMAIL():
        driver.get("http://m.gmail.com")
#pyautogui.prompt('This lets the user type in a string and press OK.')
#pyautogui.alert('This displays some text with an OK button.')
        fw = pyautogui.getInfo()
        print(fw)
        for LETTER in EMAIL_CHAR_LIST:
                pyautogui.press("{0}".format(LETTER))
        pyautogui.press("enter")
        time.sleep(5)
        if driver.find_element_by_id("captchaimg").get_attribute('src'):
                                print("found +++++++++++++++")
                                url = str(driver.find_element_by_("captchaimg").get_attribute('src'))
                                response = requests.get(url, stream=True)
                                with open('img.png', 'wb') as out_file:
                                        shutil.copyfileobj(response.raw, out_file)
                                        out_file.close()
                                subprocess.Popen(["display", "img.png"])
                                CAPTCHA = pyautogui.prompt('enter captcha you noob')
                                time.sleep(5)
                                for LETTER in CAPTCHA:
                                        pyautogui.press("{0}".format(LETTER))
                                pyautogui.press("enter")

                                time.sleep(120)          
        else:
                        for LETTER in PASSWD_CHAR_LIST:
                                pyautogui.press("{0}".format(LETTER))
                        pyautogui.press("enter")
                        time.sleep(5)

                        try:
                                if driver.find_element_by_xpath("//span[text()='Verify it’s you']"):
                                        print("needs verification")
                        except Exception:
                                pass
                        time.sleep(5)
                        try:
                                if driver.find_element_by_xpath("//a[@id='bnm']"):
                                        print("logged in")
                                        time.sleep(5)
                                        try:
                                        ### IF ELEMENT HAS ATTRIBUTE EMAIL PRINE EMAIL ##
                                                MAX = 19
                                                i = 0
                                                for x in range(MAX):
                                                        e = driver.find_element_by_id('subj{0}'.format(i)).click()
                                                        MAIL = driver.find_elements_by_class_name('email')
                                                        for M in MAIL:
                                                                print(M.text)
                                                        time.sleep(5)
                                                        driver.get("http://m.gmail.com")
                                                        i+=1
                                                        time.sleep(5)
                        
                                        except Exception as e:
                                                print(e)
                                                pass

                        except Exception:
                                pass
                        time.sleep(5)

def yahoo_mail():
        print("yahoomail")


               

## ENTERING PASSWORD##
