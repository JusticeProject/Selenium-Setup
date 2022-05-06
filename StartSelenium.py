from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Change to True if you want to run Chrome in the background 
# (it won't be visible when navigating to websites)
USE_HEADLESS_MODE = False

###################################################################################################

def initialize():
    # This assumes the chromedriver has already been downloaded from here:
    # https://chromedriver.chromium.org/downloads

    serv=Service("./chromedriver.exe")

    if (USE_HEADLESS_MODE):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=serv, options=chrome_options)
    else:
        driver = webdriver.Chrome(service=serv)

    driver.delete_all_cookies()
    return driver

###################################################################################################

def save_website_title(driver):
    title = driver.title
    current_url = driver.current_url
    print("found title: " + driver.title + " at url: " + current_url)

    file = open("website_titles.txt", "a", encoding="utf-8")
    file.write(current_url + "\n" + title + "\n")
    file.close()

###################################################################################################

def do_automated_google_search(driver):
    url = "https://www.google.com/"
    driver.get(url)
    save_website_title(driver)

    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("n")
    time.sleep(1)
    elem.send_keys("e")
    time.sleep(1)
    elem.send_keys("w")
    time.sleep(1)
    elem.send_keys("s")
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    save_website_title(driver)

    elems = driver.find_elements(By.TAG_NAME, "a")
    print(f"found {len(elems)} links")

    for elem in elems:
        link = elem.get_attribute("href")
        if (link is not None):
            if ("cnn.com" in link) or ("nbcnews.com" in link) or ("cbsnews.com" in link) or ("cnbc.com" in link):
                elem.click()
                break

    save_website_title(driver)

###################################################################################################

driver = initialize()
do_automated_google_search(driver)
driver.close()
