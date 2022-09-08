import sqlite3

connection_obj = sqlite3.connect('stocks.db')
 
cursor_obj = connection_obj.cursor()
 
cursor_obj.execute("DROP TABLE IF EXISTS market")


table = """ CREATE TABLE market (
            stock_id INTEGER NOT NULL,
            ticker VARCHAR(255) NOT NULL,
            price REAL NOT NULL,
            shares INTEGER NOT NULL );
            """
cursor_obj.execute(table)

FILE = open('mystocks.txt','r')
for i in range(1,6):
    line=FILE.readline()
    line=line.split()
    

    insert = """
                INSERT INTO market(stock_id,ticker,price,shares)
                values(%s,"%s",%s,%s)
             """ % (i,line[0],line[1],100)
    print(insert)

    cursor_obj.execute(insert)

get = ''' SELECT * FROM market;'''

cursor_obj.execute(get)
print(cursor_obj.fetchall())

connection_obj.commit()

connection_obj.close()
