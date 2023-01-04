import requests
import os

TOKEN = os.environ['TOKEN']
chat_id = os.environ['chat_id']

def sendCurrencyValue(value):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=Current price is {value}"
    requests.get(url).json()
