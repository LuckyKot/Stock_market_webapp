import sqlite3
import common
import market
import threading
from flask import Flask, request, json
import requests


api = Flask(__name__)

stocks=[]

def get_data():
    stocks=[]
    
    connection_obj = sqlite3.connect('C:/Users/...stock/server/stocks.db')
    
    cursor_obj = connection_obj.cursor()
    
    sqlID=cursor_obj.execute('''SELECT stock_id FROM market;''')
    sid=cursor_obj.fetchall()
    sqlTicker=cursor_obj.execute('''SELECT ticker FROM market;''')
    tic=cursor_obj.fetchall()
    sqlPrice=cursor_obj.execute('''SELECT price FROM market;''')
    pri=cursor_obj.fetchall()
    sqlShare=cursor_obj.execute('''SELECT shares FROM market;''')
    sha=cursor_obj.fetchall()

    connection_obj.close()

    for i in range(5):
        temp={"id":sid[i][0],"name":tic[i][0],"price":pri[i][0],"shares":sha[i][0]}
        stocks.append(temp)

    return stocks

background_thread = threading.Thread(target=market.liveUpdate)
background_thread.start()
    

@api.route('/stocks', methods=['GET'])
def get_stocks():
    stocks=get_data()
    return json.dumps(stocks)

@api.route('/stocks', methods=['POST'])
def transaction():
    try:
        req=request.get_data()
        req=req.decode("utf-8")
        req=req[2:]
        req=json.dumps(req)
        req=req.split()

        for i in range(len(req)):
            req[i]=req[i].strip('[]{}:"\\,')
        
        connection_obj = sqlite3.connect('C:/Users/.../stock/server/stocks.db')
        
        cursor_obj = connection_obj.cursor()

        if(req[1]=="buy"):

            query='''SELECT shares FROM market WHERE ticker="''' + req[5] + '''"'''
            sqlShare=cursor_obj.execute(query)
            sha=cursor_obj.fetchall()

            sha=int(sha[0][0])+int(req[9])

            upd="""
                       UPDATE market 
                       SET shares = %s
                       WHERE ticker= "%s";
                    """ % (sha,req[5])
            
            connection_obj.execute(upd)
            connection_obj.commit()
            connection_obj.close()
            
        elif(req[1]=="sell"):
            query='''SELECT shares FROM market WHERE ticker="''' + req[5] + '''"'''
            sqlShare=cursor_obj.execute(query)
            sha=cursor_obj.fetchall()

            sha=int(sha[0][0])+int(req[9])

            upd="""
                       UPDATE market 
                       SET shares = %s
                       WHERE ticker= "%s";
                    """ % (sha,req[5])
            
            connection_obj.execute(upd)
            connection_obj.commit()
            connection_obj.close()


        return json.dumps({'success':True}), 200
    except:
        return json.dumps({'success':False}), 500 

api.run(host='0.0.0.0',port=5000)


