import webbrowser,requests,bs4,time,pprint
import pandas as pd
from collections import defaultdict

url = f"https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
stock_dictionary=defaultdict(list)

def get_stock_prize_nifty50():

    headers={
              "User-Agent" : "Mozilla/5.0",
              "Cache-Control": "no-cache",
              "Pragma":"no-cache",
              }
   
    session=requests.session()
    webaddress=session.get(url,headers=headers)
    moneycontroldata=bs4.BeautifulSoup(webaddress.text,"html.parser")
    receiveddata=moneycontroldata.find_all("td",class_="ReuseTable_PR__i6dgj")
    print("No of stocks:-",len(receiveddata))
  
    for eachtag in receiveddata:
        stockname=eachtag.find("a").text
        print(f"NAME:{stockname}")
        nameprize=eachtag.find_next_siblings("td",limit=4)   
        headings={1:"INDUSTRY",2:"LTP",3:"CHG PRICE",4:"CHG %"}
        iterno=1
        for eachtag1 in nameprize:
             print(f"{headings.get(iterno,"nothing")} : {eachtag1.text}")
             stock_dictionary[stockname].append(f"{headings.get(iterno,"nothing")} : {eachtag1.text}")
             iterno+=1
        print("----------------------------------") 

def save_stockdata_To_file():

    df=pd.DataFrame(stock_dictionary)
    df.to_csv("nifty50.csv",index=False)
    print("save data sucessfully")
       
get_stock_prize_nifty50()
save_stockdata_To_file()