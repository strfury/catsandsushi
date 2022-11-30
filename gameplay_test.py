from ingredients import Dish, Player, Ingredient, Fish, makeDish
from customer import Customer, getCat, makeCatList
from day import Day
from cmu_112_graphics import *

def makeCustomerList(day):
    result = dict()
    num = day.getCustomers()
    for i in range(num):
        result[i] = f"customer {i}"
    return result
#general gameplay loop
#lists of all images, indexes are parallel
icons = [1, 2, 3, 4, 5]
neutral = [1, 2, 3, 4, 5]
angry = [1, 2, 3, 4, 5]
# will be moved inside a loop later
daynum = 1
today = Day(1)
currCustomers = today.getCustomers()
currOrders = today.getOrders()
activeCustomers = 0
names = makeCustomerList(today)
for i in range(currCustomers):
    if(activeCustomers < 2):
        cat = makeCatList(icons, neutral, angry)
        Customer(cat[0], cat[1], cat[2], currOrders[i])
        #display 
    pass