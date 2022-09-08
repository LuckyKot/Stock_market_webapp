# Stock_market_webapp
A simple stock market simulation web application.
Uses REST API.

Server folder has stocks.txt, a basic pool of 5 stocks to initialize the server assortment.
Create_sql.py creates a db out of stocks.txt for the server to use.
market.py and common.py contain simple OOP structures for the webapp.
main.py boots up the server, the server has a background thread of constantly fluctuating stock prices and main thread that processes requests.

Client folder contains portfolio.py and position.py similar to market.py and position.py. (simple OOPs structures)
operations.py contains primary functionality while main.py utilizes it and is also responsible for simple command line UI and saving/loading file between sessions.
