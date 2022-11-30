from cmu_112_graphics import *
from button import *
from main import *
from ingredients import *
from hint import *

def cookMode_redrawAll(app, canvas):
    for cat in app.currCats:
        app.activeOrders.append(cat.getOrder())
    canvas.create_image(app.width/2, app.height/2, image=app.bgColor)
    canvas.create_image(app.width/2, app.height/2, image=app.timeBar)
    canvas.create_image(app.width/2, app.height/2 + app.time, 
        image=app.timeArrow)
    canvas.create_image(app.width/2, app.height/2, image=app.rightCat)
    canvas.create_image(app.width/7, app.height/2, image=app.leftCat)
    canvas.create_image(app.width/2, app.height/2, image=app.order)
    canvas.create_image(app.width/7, app.height/2, image=app.order)
    canvas.create_image(app.width/2, app.height/2, image=app.cookScreen)
    canvas.create_image(app.width/2, app.height/2, image=app.riceDisplay)
    for i in range(len(app.currCats)):
        if i == 0:
            for item in app.activeOrders[0].getRecipe():
                canvas.create_image(app.width/2, app.height/2,
                image=app.bubbleFood[item])
        else:
            for item in app.activeOrders[1].getRecipe():
                canvas.create_image(app.width/7, app.height/2,
                image=app.bubbleFood[item])

    if app.fishCut == True:
        canvas.create_image(app.width/2, app.height/2, image=app.fishDisplay)

    for i in range(len(app.currCats)):
        if i == 0:
            app.rightCat = app.currCats[i].getImage()
        if i == 1:
            app.leftCat = app.currCats[i].getImage()

def cookMode_mousePressed(app, event):
    if app.salmonB.isClicked(event.x, event.y):
        app.currOrder.addItem(salmon)
        app.currFish = app.salmonF
        app.fishDisplay = app.salmon
        app.mode = 'fishMode'
    elif app.tunaB.isClicked(event.x, event.y):
        app.currOrder.addItem(tuna)
        app.currFish = app.tunaF
        app.fishDisplay = app.tuna
        app.mode = 'fishMode'
    elif app.yellowB.isClicked(event.x, event.y):
        app.currFish = app.yellowtailF
        app.currOrder.addItem(yellowtail)
        app.fishDisplay = app.yellowtail
        app.mode = 'fishMode'
    elif app.shrimpB.isClicked(event.x, event.y):
        app.currFish = app.shrimpF
        app.currOrder.addItem(shrimp)
        app.fishDisplay = app.shrimp
        app.mode = 'fishMode'
    elif app.riceB.isClicked(event.x, event.y):
        app.riceDisplay = app.rice
    elif app.bubbleRight.isClicked(event.x, event.y):
        if(len(app.currCats) > 0):
            app.riceDisplay = app.blank
            app.fishDisplay = app.blank
            app.toppingDisplay = app.blank
            app.sauceDisplay = app.blank
            if(app.currOrder == app.currCats[0].getOrder()):
                print(calcPrice(app.currOrder))
            else:
                print(calcPriceW(app.currOrder, app.currCats[0].getOrder()))
            app.currOrder = Dish()
            app.currCats.pop(0)
            app.activeOrders.pop(0)
    elif app.bubbleLeft.isClicked(event.x, event.y):
        if(len(app.currCats) > 1):
            app.riceDisplay = app.blank
            app.fishDisplay = app.blank
            app.toppingDisplay = app.blank
            app.sauceDisplay = app.blank
            if(app.currOrder == app.currCats[0].getOrder()):
                print(calcPrice(app.currOrder))
            else:
                print(calcPriceW(app.currOrder, app.currCats[0].getOrder()))
            app.currOrder = Dish()
            app.currCats.pop(1)
            app.activeOrders.pop(1)
    else:
        print(app.activeOrders)
        print(app.currCats)
        # print(app.currOrder) #debugging

def cookMode_timerFired(app):
    app.time = app.time + 0.5%250

def cookMode_keyPressed(app, event):
    app.mode = 'hintMode'