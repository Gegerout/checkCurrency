from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import sendBotMessage

url = 'http://www.sberbank.ru/ru/quotes/currenciesbeznal'
path = '/Users/User/Downloads/chromedriver'

service = Service(path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath','//*[@id="page-main"]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div[1]'))

currencyValue = driver.find_element('xpath', '//*[@id="page-main"]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div[1]')

sendBotMessage.sendCurrencyValue(currencyValue.text)

driver.quit()
