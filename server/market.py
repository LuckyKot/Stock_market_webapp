import common
import sqlite3
import threading

def liveUpdate():
    connection_obj = sqlite3.connect('C:/Users/.../server/stocks.db')

    cursor_obj = connection_obj.cursor()

    while True:
        stocks=[]
        sqlID=cursor_obj.execute('''SELECT stock_id FROM market;''')
        sid=cursor_obj.fetchall()
        sqlTicker=cursor_obj.execute('''SELECT ticker FROM market;''')
        tic=cursor_obj.fetchall()
        sqlPrice=cursor_obj.execute('''SELECT price FROM market;''')
        pri=cursor_obj.fetchall()
        sqlShare=cursor_obj.execute('''SELECT shares FROM market;''')
        sha=cursor_obj.fetchall()
        
        for i in range(5):
            temp=common.Position(tic[i][0],pri[i][0],sha[i][0])
            stocks.append(temp)
        
        print("\nMarket updated")   
        for i in range(len(stocks)):
            stocks[i].updatePrice()

            upd="""
                   UPDATE market 
                   SET price = %s
                   WHERE ticker= "%s";
                """ % (stocks[i].price,stocks[i].ticker)
            
            cursor_obj.execute(upd)
            connection_obj.commit()
            
        common.time.sleep(10)
    
    connection_obj.close()


