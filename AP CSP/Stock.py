class Stock():
    def __init__(self,symbol = "", name = "", previousClosingPrice = 0.0, currentPrice = 0.0):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getSetPP(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
        return self.__previousClosingPrice
    def getSetCP(self, currentPrice):
        self.__currentPrice = currentPrice
        return currentPrice
    def getChangePercent(self):
        return str((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) + "%"
s1 = Stock("AP", "APCSP", 0.001, 0.002)
print(s1.getChangePercent())