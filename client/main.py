import operations

def load_portfolio():
    filename="myportfolio.txt"
    portfolio = operations.p.Portfolio()
    try:
        a = open(filename, 'r')
        line=a.readline()
        portfolio.balance=float(line)
        i=0
        while line!='':
            try:
                line=a.readline()
                line=line.split()
                tic=line[0]
                sha=int(line[1])
                temp=operations.c.Position()
                portfolio.positions.append(temp)
                portfolio.positions[i].ticker=tic
                portfolio.positions[i].shares=sha
                i+=1
            except:
                a.close()
                return portfolio
        a.close()
        return portfolio
    except:
        print("Portfolio file not found")
        print("Creating new portfolio...\n")
        return portfolio
    
def save_portfolio(portfolio):
    filename="myportfolio.txt"
    a = open(filename, 'w')
    a.write(str(portfolio.balance))
    a.write('\n')
    for i in range(len(portfolio.positions)):
        line=portfolio.positions[i].ticker+' '+str(portfolio.positions[i].shares)+'\n'
        a.write(line)

def print_portfolio(portfolio):
    if (len(portfolio.positions)<=0):
        print("\nYour portfolio is empty at the moment!\n")
    else:
        for i in range(len(portfolio.positions)):
            print(i+1, " ticker: ", portfolio.positions[i].ticker, " shares: ",portfolio.positions[i].shares)
        print("\n")  

def buy_request(portfolio):
    print("Choose a stock option")
    current_market=operations.get_market(for_user=1)
    try:
        option=input("Option:")
        option=(int(option)-1)*4+1
        ticker=current_market[option]
        shares=int(input("How many shares:"))
        operations.buy_on_market(portfolio,ticker,shares)
    except:
        print("\nwrong option selected\n")

def sell_request(portfolio):
    print("Choose a stock option")
    print_portfolio(portfolio)
    option=int(input("Option:"))
    try:
        ticker=portfolio.positions[option-1].ticker
        shares=int(input("How many shares:"))
        operations.sell_on_market(portfolio,ticker,shares)
    except:
        print("\nWrong option selected\n")

def UI(portfolio):
    print("Welcome to the stock market")
    while True:
        print("Choose an option")
        print("1. Check current stock prices")
        print("2. Buy stock")
        print("3. Sell stock")
        print("4. Check balance")
        print("5. Check portfolio")
        print("6. Save and exit\n")
        choice=input("Your choice: ")
        print('\n')
        match choice:
            case "1":
                operations.get_market(for_user=1)
            case "2":
                buy_request(portfolio)
            case "3":
                sell_request(portfolio)
            case "4":
                print("Your balance: ", portfolio.balance, "\n")
            case "5":
                print_portfolio(portfolio)
            case "6":
                break

def main():
    portfolio=load_portfolio()
    UI(portfolio)
    save_portfolio(portfolio)
    print("Saved\nHave a nice day")

main()
