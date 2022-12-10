from cmu_112_graphics import *
from main import *
from button import *
from ingredients import *
from hint import *
import random
import decimal

def cookMode_redrawAll(app, canvas):
    #preparing the orders for the current day
    for cat in app.currCats:
        app.activeOrders.append(cat.getOrder())
    #if you served all cats
    if len(app.currCats) == 0:
        app.mode = 'endMode'
    #if theres only one cat left, clear out other customer GUI
    if len(app.currCats) == 1:
        app.leftCat = app.blank
        app.orderL = app.blank
    #creating all images
    canvas.create_image(app.width/2, app.height/2, image=app.bgColor)
    canvas.create_image(app.width/2, app.height/2, image=app.timeBar)
    canvas.create_image(app.width/2, app.height/2 + app.time, 
        image=app.timeArrow)
    canvas.create_image(app.width/2, app.height/2, image=app.rightCat)
    canvas.create_image(app.width/7, app.height/2, image=app.leftCat)
    canvas.create_image(app.width/2, app.height/2, image=app.order)
    canvas.create_image(app.width/7, app.height/2, image=app.orderL)
    canvas.create_image(app.width/2, app.height/2, image=app.cookScreen)
    canvas.create_image(app.width/2, app.height/2, image=app.mainHint)
    canvas.create_text(60,30, text = str("%.2f" % app.cash) + f"/{app.currDay.getGoal()}", 
        font = ("Coolvetica Rg", 16))
    #creating the images in the orders
    for i in range(len(app.currCats)):
        if i == 0:
            for item in app.activeOrders[0].getRecipe():
                canvas.create_image(app.width/2, app.height/2,
                image=app.bubbleFood[item])
        else:
            for item in app.activeOrders[1].getRecipe():
                canvas.create_image(app.width/7, app.height/2,
                image=app.bubbleFood[item])
    #creating the cats
    for i in range(len(app.currCats)):
        if i == 0:
            app.rightCat = app.currCats[i].getImage()
        if i == 1:
            app.leftCat = app.currCats[i].getImage()
    #creating the food on the plate
    canvas.create_image(app.w, app.h, image=app.riceDisplay)
    #fish only shows if you cut it properly
    if app.fishCut == True:
        canvas.create_image(app.w, app.h, image=app.fishDisplay)
    canvas.create_image(app.w, app.h, image = app.sauceDisplay)
    canvas.create_image(app.w, app.h, image = app.toppingDisplay)
def cookMode_mousePressed(app, event):
    #checking which button you clicked
    for food in app.cookButtons:
        if app.cookButtons[food].isClicked(event.x, event.y):
            #check if you have at least one of the item
            if checkSupply(food, app.stock):
                app.stock[food] -= 1
                app.currOrder.addItem(food)
                if(isinstance(food, Fish)):
                    app.currFish = app.fishCutDict[food]
                    app.fishDisplay = app.displayDict[food]
                    app.fishCut = False
                    app.mode = 'fishMode'
                elif(isinstance(food, Toppings)):
                    app.toppingDisplay = app.displayDict[food]
                elif(isinstance(food, Sauce)):
                    app.sauceDisplay = app.displayDict[food]
                else:
                    app.riceDisplay = app.displayDict[food]
                    app.drag = True
                    app.w = event.x + 150
                    app.h = event.y - 200
        elif app.cookHintB.isClicked(event.x, event.y):
            app.mode = 'cookHint'
#drag and drop function
def cookMode_mouseDragged(app, event):
    if app.plateB.isClicked(event.x, event.y):
        app.drag = True
    if app.drag:
        app.gravity = False
        app.timeG = 0
        app.w = event.x + 150
        app.h = event.y - 200
#delivering orders
def cookMode_mouseReleased(app, event):
    if app.bubbleRight.isClicked(event.x, event.y) and app.drag:
        app.gravity = False
        app.drag = False
        app.w = app.width/2
        app.h = app.height/2
        if(len(app.currCats) > 0):
            app.riceDisplay = app.blank
            app.fishDisplay = app.blank
            app.toppingDisplay = app.blank
            app.sauceDisplay = app.blank
            app.cash += round(calcPrice(app.currOrder, 
app.activeOrders[0],app.fishPercent),2)
            app.currOrder = Dish()
            app.currCats.pop(0)
            app.activeOrders.pop(0)
    elif app.bubbleLeft.isClicked(event.x, event.y) and app.drag:
        app.gravity = False
        app.drag = False
        app.w = app.width/2
        app.h = app.height/2
        if(len(app.currCats) > 1):
            app.riceDisplay = app.blank
            app.fishDisplay = app.blank
            app.toppingDisplay = app.blank
            app.sauceDisplay = app.blank
            app.cash += round(calcPrice(app.currOrder, app.activeOrders[1], app.fishPercent), 2)
            app.currOrder = Dish()
            app.currCats.pop(1)
            app.activeOrders.pop(1)
    elif app.plateB.isClicked(event.x, event.y) and app.drag:
        app.drag = False
        app.gravity = False
        app.w = app.width/2
        app.h = app.height/2
        if app.riceFood not in app.currOrder.setRecipe():
            app.currOrder.addItem(app.riceFood)
    elif app.drag:
        app.gravity = True
#changes time and patience
def cookMode_timerFired(app):
    app.time = app.time + 0.5
    if app.time >= 275:
        app.mode = 'endMode'
    if app.h >=750:
        app.currOrder = Dish()
        app.riceDisplay = app.blank
        app.fishDisplay = app.blank
        app.toppingDisplay = app.blank
        app.sauceDisplay = app.blank
    if app.gravity:
        app.timeG +=1
        app.h += 4*app.timeG**2
    for i in range(len(app.currCats)):
        if i == 0 or i == 1:
            app.currCats[i].decPatience()

#if food is being dragged, make it follow the mouse
def dragCheck(app, x, y):
    if app.drag:
        app.gravity = False
        app.timeG = 0
        app.w = x + 150
        app.h = y - 200

def cookMode_keyPressed(app, event):
    if(event.key == 'c'):
        app.cash += 20
    else: app.mode = 'endMode'

def cookHint_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image = app.cookHint)
def cookHint_mousePressed(app, event):
    if app.fishHintExit.isClicked(event.x, event.y):
        app.mode = 'cookMode'