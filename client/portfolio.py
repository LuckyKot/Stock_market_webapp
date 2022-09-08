import copy

class Portfolio:
    def __init__(self,positions=[],balance=20000):
        self.positions=[]
        self.positions=copy.deepcopy(positions)
        self.balance=balance

    def setBalance(self,bal):
        self.balance=bal

    def getBalance(self):
        return self.balance
