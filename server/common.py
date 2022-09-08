import random

RAND_MAX=32767

class Position:
    def __init__(self,name='',price=0,shares=0):
        self.ticker=name
        self.price=price
        self.shares=shares

    def createTicker(self,name,price,shares):
        self.ticker=name
        self.price=price
        self.shares=shares
        
    def setTicker(self,name):
        self.ticker=name

    def setPrice(self,price):
        self.price=price

    def setShares(self,shares):
        self.shares=shares

    def getTicker(self):
        return self.ticker

    def getPrice(self):
        return self.price

    def getShares(self):
        return self.shares

    def updatePrice(self):
        perturbation = 2/self.price
        multiplier = (random.randrange(RAND_MAX)) / RAND_MAX * perturbation
        multiplier -= perturbation/2
        multiplier += 1
        self.price *= multiplier
        if self.price<=0:
            self.price=.00000001
            


