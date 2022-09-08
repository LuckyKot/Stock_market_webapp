class Position:
    def __init__(self,name='',shares=0):
        self.ticker=name
        self.shares=shares

    def createTicker(self,name,shares):
        self.ticker=name
        self.shares=shares
        
    def setTicker(self,name):
        self.ticker=name

    def setShares(self,shares):
        self.shares=shares

    def getTicker(self):
        return self.ticker
    
    def getShares(self):
        return self.shares
            


