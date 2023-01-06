import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import sendBotMessage

url = 'http://www.sberbank.ru/ru/quotes/currenciesbeznal'
url2 = 'http://www.sberbank.ru/ru/quotes/currencies?tab=sbol'
path = '/Users/User/Downloads/chromedriver'

service = Service(path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)

def sendRequest():
    while True:
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url2)

        #WebDriverWait(driver, timeout=3).until(lambda d: d.find_element('xpath', '//*[@id="page-main"]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div[1]'))

        WebDriverWait(driver, timeout=3).until(lambda d: d.find_element('xpath', '//*[@id="page-main"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]'))

        #currencyValue = driver.find_element('xpath', '//*[@id="page-main"]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div[1]')

        currencyValue = driver.find_element('xpath', '//*[@id="page-main"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]')

        result = float(currencyValue.text.replace(',', '.'))

        if result > 50.0:
            sendBotMessage.sendCurrencyValue(currencyValue.text)
            driver.quit()
            time.sleep(10)

        driver.quit()
        time.sleep(10)
