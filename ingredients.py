import math
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
    def __init__(self, fish = 0, sauce = 0, topping = 0):
        self.ingredients = remove([rice, fish, sauce, topping], 0)
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
            print(item)
            if item not in self.getRecipe():
                return False
        return True
    def __repr__(self):
        result = ""
        for item in self.ingredients:
            result += str(item) + " "
    def __str__(self):
        return str(self.ingredients)
    def getImages(self):
        result = []
        for item in self.getRecipe():
            result.append(item.getImage())
        return result
class Player():
    def __init__(self):
        #start with some basic ingredients
        self.fish = [salmon, tuna]
        self.toppings = [wasabi]
        self.sauces = [soySauce]
        self.money = 0
        # self.prices = {salmon:5, tuna:5, wasabi:1, soySauce:1}
    def getMoney(self):
        return self.money
    def addMoney(self, amount):
        self.money += amount
    def checkDish(self, dish):
        for item in dish.ingredients:
            if(isinstance(item, Fish)):
                if item not in self.fish:
                    return False
            elif(isinstance(item, Toppings)):
                if item not in self.toppings:
                    return False
            elif(isinstance(item, Sauce)):
                if item not in self.sauces:
                    return False
        return True
    def getFish(self):
        return self.fish
    def addFish(self, fish):
        self.fish.append(fish)
    def addToppings(self, topping):
        self.toppings.append(topping)
    def addSauce(self, sauce):
        self.sauces.append(sauce)
# function to randomly generate dishes
# randrange from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
def makeDish(player):
    items = random.randint(0, 2)
    fishNum = random.randint(0, len(player.fish) - 1)
    sauceNum = random.randint(0, len(player.sauces) - 1)
    toppingNum = random.randint(0, len(player.toppings) - 1)
    fish = player.fish[fishNum]
    if items == 0:
        return Dish(fish)
    elif(items == 1):
        temp = random.randint(0, 1)
        if temp == 1:
            return Dish(fish, player.toppings[toppingNum])
        else:
            return Dish(fish, player.sauces[sauceNum])
    else:
        return Dish(fish, player.toppings[toppingNum], player.sauces[sauceNum])
def calcPrice(dish1):
    result = 0
    for item in dish1.setRecipe():
        result += item.getPrice()
    return result
#dish2 is goal
def calcPriceW(dish1, dish2):
    result = 0
    correct = dish2.setRecipe()
    for item in dish1.setRecipe():
        if item in correct:
            result += item.getPrice()
    return result



# creating all ingredients
salmon = Fish('salmon', 5)
tuna = Fish('tuna', 4)
yellowtail = Fish('yellowtail', 6)
shrimp = Fish('shrimp', 4)
wasabi = Toppings('wasabi', 1)
crunch = Toppings('crunch', 1)
spicyMayo = Sauce('mayo', 1)
soySauce = Sauce('s_sauce', 1)
eelSauce = Sauce('eel_sauce', 1)
rice = Ingredient('rice', 1)
fish = [salmon, tuna, yellowtail, shrimp]
toppings = [wasabi, crunch]
sauces = [spicyMayo, soySauce, eelSauce ]
#creating recipes
s_nigiri = Dish(salmon)
t_nigiri = Dish(tuna)
s_nigiri_s = Dish(salmon, soySauce, wasabi)
t_nigiri_s = Dish(tuna, soySauce, wasabi)
test = Dish(tuna, soySauce, wasabi)
test1 = [s_nigiri, t_nigiri]
a = Player()
a.addFish(yellowtail)
print(s_nigiri)
print(calcPriceW(test, s_nigiri))