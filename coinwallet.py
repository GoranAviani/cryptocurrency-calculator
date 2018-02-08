import os
import json
import time
#version 1 , version 2 and vesion 3 bellow:
coin_wallet={'XLM':42,'MIOTA':30,'COSS':50,'APPC':12}


#version 1
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



#firsttask = CoinMarketCap()
#firsttask.get_price_lists()
#firsttask.read_all_prices()
#firsttask.read_prices_for_my_wallet(coin_wallet)

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

#while True:
#    read_prices_for_my_wallet(coin_wallet)

################
#version 3 - without txt file

class CryptoProtfolioValue():
    def __init__(self, prices_json,):
        self.prices_json=prices_json

    def read_prices(self,):
        prices = os.popen("curl -X GET https://api.coinmarketcap.com/v1/ticker/?limit=0").read()
        self.prices_json = json.loads(prices)
        time.sleep(5)
    def print_my_portfolio_value(self,):
        wallet_sum=0
        for x in coin_wallet:
            for valuta in self.prices_json:
                if valuta['symbol'] == x:
                    print("*Currency: "+valuta['symbol']+ " has current price of: " + valuta['price_usd'])
                    vrijednost = (float(valuta['price_usd']) * float(coin_wallet[x]))
                    wallet_sum += vrijednost
                    print("**Currency: "+valuta['symbol']+ " has a total value of: " + str(vrijednost))
        print("According to Coinmarketcap.com your cryptocurrency wallet is worth: "+ "%.2f" % round(wallet_sum,2) )


secondtask = CryptoProtfolioValue("")
while True:
    secondtask.read_prices()
    secondtask.print_my_portfolio_value()
