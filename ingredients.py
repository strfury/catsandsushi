from main import *
import random
from random import randrange
def remove(list, val):
   return [value for value in list if value != val]
class Ingredient():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def incPrice(self):
        self.price +=1
    def decPrice(self):
        self.price -=1
    def __repr__(self):
        return self.name
class Fish(Ingredient):
    def __init__(self, name, price):
        super().__init__(name, price)
class Toppings(Ingredient):
    def __init__(self, name, price):
        super().__init__(name, price)
class Sauce(Ingredient):
    def __init__(self, name, price):
        super().__init__(name, price)
#list removal https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
class Dish():
    def __init__(self, *args):
        self.ingredients = []
        for item in args:
            self.ingredients.append(item)
    def addItem(self, item):
        self.ingredients.append(item)
    def getRecipe(self):
        return self.ingredients
    def setRecipe(self):
        return set(self.ingredients)
    def __eq__(self, other):
        if len(self.setRecipe()) != len(other.setRecipe()):
            return False
        for item in other.getRecipe():
            if item not in self.getRecipe():
                return False
        return True
    def __repr__(self):
        result = ""
        for item in self.ingredients:
            result += str(item) + " "
    def __str__(self):
        return str(self.ingredients)
# function to randomly generate dishes
# randrange from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
def makeDish(app):
    items = random.randint(0, 2)
    fishNum = random.randint(0, len(app.allFish) - 1)
    sauceNum = random.randint(0, len(app.allSauces) - 1)
    toppingNum = random.randint(0, len(app.allToppings) - 1)
    fish = app.allFish[fishNum]
    if items == 0:
        return Dish(app.rice, fish)
    elif(items == 1):
        temp = random.randint(0, 1)
        if temp == 1:
            return Dish(app.rice, fish, app.allToppings[toppingNum])
        else:
            return Dish(app.rice, fish, app.allSauces[sauceNum])
    else:
        return Dish(app.rice, fish, app.allSauces[sauceNum],
        app.allToppings[toppingNum])
#find price of the dish you just made compared with correct version, with fish cost lowered depending on accuracy
def calcPrice(dish1, dish2, fishAcc):
    result = 0
    for item in dish1.setRecipe():
        if item in dish2.setRecipe():
            if isinstance(item, Fish):
                result += item.getPrice() * fishAcc
            else: result += item.getPrice()
    return round(result, 2)
#returns dict of all ingredients that show up and their frequency
def getDemand(l, dict):
    for dish in l:
        for item in dish.getRecipe():
            dict[item] = dict.get(item, 0) + 1
    return dict
#check if you still have any of the item left
def checkSupply(item, supply):
    if item in supply:
        if supply[item] > 0:
            return True
    return False
def getCredits(app):
    result = 0
    for item in app.allFood:
        if app.hintDict[item] > item.getPrice():
            result += app.hintDict[item] - item.getPrice()
        else: result -= abs(app.hintDict[item] - item.getPrice())
    return result