import position
import portfolio as p
import requests
import json


def get_market(api_url="http://127.0.0.1:5000/stocks",for_user=0):
    response = requests.get(api_url)
    x=json.loads(response.text)
    x = json.dumps(x)

    x=x.split()
    output = []
    
    for i in range(len(x)):
        x[i]=x[i].strip('[]{}:",')

    for i in range(0,len(x),8):
        output.append(x[i+1])
        output.append(x[i+3])
        output.append(x[i+5])
        output.append(x[i+7])
    if for_user==1:
        print("Current market:")
        for i in range(0,len(output),4):
           print(output[i],
                  "ticker: ", output[i+1],
                  "price: ", output[i+2],
                  "shares: ", output[i+3])
        print("\n")
    
    return output

def get_sum(market,ticker,shares):
    for i in range(len(market)):
        if market[i]==ticker:
            order_sum=float(market[i+1])*float(shares)
            return order_sum
    return 0

def get_shares(p,t,s):
    for i in range(len(p.positions)):
        if p.positions[i].ticker==t:
            return p.positions[i].shares
    return 0

def search_market(ticker,market,shares):
    for i in range(len(market)):
        if market[i]==ticker:
            available_shares=market[i+2]
            price=market[i+1]
            return available_shares,price,i-1

def updatePortfolio(p,t,s):
    for i in range(len(p.positions)):
        if p.positions[i].ticker==t:
            p.positions[i].shares+=s
            return 0
    temp=position.Position(t,s)
    p.positions.append(temp)
    return 0

def buy_on_market(portfolio,ticker,shares,api_url="http://127.0.0.1:5000/stocks"):
    
    current_market=get_market(api_url)
    
    order_sum=get_sum(current_market,ticker,shares)
    if order_sum<=0:
        print("\nstock unavailable\n")
        return 1
    elif shares<=0:
        print("\ncannot buy 0 or less shares\n")
        return 1
    elif order_sum>portfolio.balance:
        print("\nnot enough balance\n")
        return 1
    available_shares,price,sID=search_market(ticker,current_market,shares)
    if float(available_shares)<shares:
        print("\nnot enough shares on the market\n")
        return 1
    
    data = {
            "type":"buy",
            "stock_id":sID,
            "ticker":ticker,
            "price":price,
            "shares":-shares,
            }

    response=requests.post(api_url,data=json.dumps(data))

    
    if "success" not in response.text:
        print("transaction failed")
        return 2
    else:
        portfolio.balance-=order_sum
        updatePortfolio(portfolio,ticker,shares)
        
    return 0
    

def sell_on_market(portfolio,ticker,shares,api_url="http://127.0.0.1:5000/stocks"):
    
    current_market=get_market(api_url)
    order_sum=get_sum(current_market,ticker,shares)
    available_shares=get_shares(portfolio,ticker,shares)

    if shares<=0:
        print("\ncannot buy 0 or less shares\n")
        return 1
    elif available_shares<shares:
        print("\nNot enough shares\n")
        return 1

    market_shares,market_price,sID=search_market(ticker,current_market,shares)
    
    data = {
            "type":"sell",
            "stock_id":sID,
            "ticker":ticker,
            "price":market_price,
            "shares":shares,
            }
    
    response=requests.post(api_url,data=json.dumps(data))

    if "success" not in response.text:
        print("\ntransaction failed\n")
        return 2
    else:
        portfolio.balance+=order_sum
        updatePortfolio(portfolio,ticker,-shares)

    return 0
