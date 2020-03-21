import os
import time
from selenium import webdriver

def log(string):
    t = time.asctime(time.localtime())
    print("[{}] {}".format(t, string))
    
def build_driver():
    GOOGLE_CHROME_PATH = os.environ["GOOGLE_CHROME_BIN"]
    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    WAIT = 10
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(WAIT)
    
    return driver
