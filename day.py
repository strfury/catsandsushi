from ingredients import *
class Day():
    def __init__(self, day):
        self.day = day
        if(day < 3):
            self.customers = 5
        elif(day < 5):
            self.customers = 8
        else:
            self.customers = 10 
        self.goal = self.customers * 25 + self.day * 5
        self.time = 300
        self.orders = []
    def getCustomers(self):
        return self.customers
    def getGoal(self):
        return self.goal
    def makeOrders(self, player):
        result = []
        if self.day > 2:
            for i in range(self.day):
                result.append(makeDish(player))
        self.orders = result
        return self.orders
    def getOrders(self):
        return self.orders
    def orderString(self):
        result = ""
        for i in range(len(self.orders)):
            result += str(self.orders[i])
        return result

b = Player()
test = Day(1)
test.makeOrders(b)
#print(test.orders)
#print(test.goal)