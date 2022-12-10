from main import *
from ingredients import *
from cooking import *
from hint import *
from cmu_112_graphics import *

class Day():
    def __init__(self, day):
        self.day = day
        if(day < 3):
            self.customers = 5
        else:
            self.customers = 7

        self.goal = self.customers * 4 
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

def dayMode_redrawAll(app, canvas):
    app.timeS = 0
    canvas.create_image(app.width/2, app.height/2, image=app.dayStart)
    canvas.create_text(app.width/2, app.height/2+150, text = f"Day: {app.day}",
    font = ("Coolvetica Rg", 35))
    canvas.create_text(app.width/2, app.height/2+200,
    text = f"Goal: {app.currDay.getGoal()}", font = ("Coolvetica Rg", 35))
    canvas.create_text(app.width/2, app.height/2+240,
    text = f"Press any key to start", font = ("Coolvetica Rg", 24))
def dayMode_timerFired(app):
    app.timeS +=1
    if app.timeS > 2 :
        app.mode = "cookMode"
def dayMode_keyPressed(app, event):
    app.mode = "cookMode"

def endMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.dayEnd)
    canvas.create_text(app.width/2, app.height/2+200, 
    text = f"Press any key to continue", font = ("Coolvetica Rg", 35))

def findPoint(line1, line2):
    result = 0
    x = line1[0] - line2[0]
    y = line2[1] - line1[1]
    if(x !=0):
        xval = y/x
    result = xval*line1[0] + line1[1]
    return result

def makeHints(app):
    for item in app.allFood:
        if item in app.demands:
            slope = (random.randint(-5, -1))
            intercept = (random.randint(5, 20))
            app.hintDict[item] = int(findPoint((slope, intercept), (app.supplyCurves[item], 0)))
        else: app.hintDict[item] = 0

def updateSupply(app):
    for item in app.allFood:
        app.supplyCurves[item] += round((0.1 * app.amountBought[item]), 1)

def endMode_keyPressed(app, event):
    #starting the next day, creating new customers and resetting images
    app.day += 1
    app.currDay = Day(app.day)
    app.numCustomers = app.currDay.getCustomers()
    random.shuffle(app.allCats)
    app.currCats = app.allCats[0:app.numCustomers]
    app.activeOrders = []
    for j in range(len(app.currCats)):
        app.currCats[j].addOrder(makeDish(app))
        app.currCats[j].setPatience()
        app.activeOrders.append(app.currCats[j].getOrder())
    getDemand(app.activeOrders, app.demands)
    updateSupply(app)
    makeHints(app)
    for item in app.amountBought:
        app.amountBought[item] = 0
    app.currOrder = Dish()
    app.orderL = app.order
    app.time = 0
    app.riceDisplay = app.blank
    app.fishDisplay = app.blank
    app.toppingDisplay = app.blank
    app.sauceDisplay = app.blank
    app.credits = getCredits(app)
    app.mode = 'supplyMode'