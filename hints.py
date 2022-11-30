from ingredients import *
def createHint():
    pass
def findBestHint(player, fishAccuracy, total):
    pass
def hint(player, fishAccuracy, total):
    result = dict()
    pass
def calcPrice(order, dish, player, fishAccuracy):
    prices = player.getPrices()
    if(order == dish) and fishAccuracy > 0.9:
        return perfectOrderPrice(order, player)
def calcDayPrice(orders, player, fishAccuracy):
    pass
def perfectOrderPrice(order, player):
    total = 0
    prices = player.getPrices()
    for item in order:
        total += prices[item]
    return total
def getPrice(order, player, fishAccuracy):
    total = 0
    prices = player.getPrices()
    for item in order:
        if not isinstance(item, Fish):
            total += prices[item]
        else:
            fish = prices[item] * fishAccuracy
            total += fish
    return total