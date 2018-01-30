import os
import json
import time

class CoinMarketCap():
    def __init__(self,):
        print("")
    def get_price_lists(self):
        os.system("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0 > prices.txt")

    def read_price(self,first_currency,second_currency):
        currency = first_currency + second_currency
        with open('prices.txt', 'r') as content_file:
            content = content_file.read()
            sve = json.loads(content)
            for valuta in sve:
            	if valuta['symbol']==currency: #currency variable
                    print(currency + ": " + valuta['price'])


    def read_all_prices(self,):
        with open('prices.txt', 'r') as content_file:
            content = content_file.read()
            sve = json.loads(content)
            for valuta in sve:
                if valuta['price_usd'] is not None:
                    print("Currency: "+valuta['symbol']+ " has current price of: " + valuta['price_usd'])


    def read_prices_for_my_wallet(self, coin_wallet):
        wallet_sum=0
        with open('prices.txt', 'r') as content_file:
            content = content_file.read()
            sve = json.loads(content)
            print(coin_wallet)
            for x in coin_wallet:
                for valuta in sve:
                    if valuta['symbol'] == x:
                        print("Currency: "+valuta['symbol']+ " has current price of: " + valuta['price_usd'])
                        vrijednost = (float(valuta['price_usd']) * float(coin_wallet[x]))
                        wallet_sum += vrijednost
                        print(vrijednost)
            print("According to Coinmarketcap.com your cryptocurrency wallet is worth: "+ "%.2f" % round(wallet_sum,2) )


coin_wallet={'XLM':42,'MIOTA':30,'COSS':50,'APPC':12}
firsttask = CoinMarketCap()
firsttask.get_price_lists()
#firsttask.read_all_prices()
firsttask.read_prices_for_my_wallet(coin_wallet)

#####################################
#2nd version- refresh every 60 seconds.

def read_prices_for_my_wallet(coin_wallet):
    os.system("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0 > prices.txt")
    wallet_sum=0
    with open('prices.txt', 'r') as content_file:
        content = content_file.read()
        sve = json.loads(content)
        print(coin_wallet)
        for x in coin_wallet:
            for valuta in sve:
                if valuta['symbol'] == x:
                    print("*Currency: "+valuta['symbol']+ " has current price of: " + valuta['price_usd'])
                    vrijednost = (float(valuta['price_usd']) * float(coin_wallet[x]))
                    wallet_sum += vrijednost
                    print("**Currency: "+valuta['symbol']+ " has a total value of: " + str(vrijednost))
        print("According to Coinmarketcap.com your cryptocurrency wallet is worth: "+ "%.2f" % round(wallet_sum,2) )

    time.sleep(5)

while True:
    read_prices_for_my_wallet(coin_wallet)
