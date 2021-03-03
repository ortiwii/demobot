import requests
import json
import time

# Programa nagusia
if __name__ == '__main__':
    uri = "https://eth.2miners.com/api/accounts/0x3C99c18A9DB8063F2edB586AE24E9d05DD045b2e"
    metodoa = 'GET'
    goiburuak = {'Host': 'eth.2miners.com'}
    edukia = ''

    erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia)
    edukia = json.loads(erantzuna.content)
    money = float(edukia["stats"]["balance"]) * (10 ** (-9))

    uri = "https://api.gdax.com/products/eth-eur/ticker"
    metodoa = 'GET'
    goiburuak = {'Host': 'api.gdax.com'}
    edukia = ''
    erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia)
    edukia = json.loads(erantzuna.content)
    price = float(edukia["price"])
    act = money*price
    print("ETHEREUM PRICE (eur) = " +str(price))
    print("MONEY (eth) = "+str(money))
    print("\nMONEY (eur) = "+str(act)+" €")
    time.sleep(20)

