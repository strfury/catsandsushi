from main import *
from cmu_112_graphics import *
#fixing formatting on rounding strings:
#https://stackoverflow.com/questions/56820/round-doesnt-seem-to-be-rounding-properly
def supplyMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.hintScreen)
    canvas.create_text(app.width/2, 50, text="Set the supply of items",
        font = ("Coolvetica Rg", 25))
    #print all text
    y = 0
    for i in range(4):
        canvas.create_text(app.width/5+120, app.height/8+45 + y,
            text=app.stock[app.allFood[i]], font = "Arial 35")
        canvas.create_text(app.width/5+120, app.height/8+75 + y,
            text= "%.2f" %app.supplyCurves[app.allFood[i]], font = "Arial 12")
        y += 80
    for i in range(3):
        canvas.create_text(app.width/5+120, app.height/8+45 + y,
            text=app.stock[app.allFood[i+4]], font = "Arial 35")
        canvas.create_text(app.width/5+120, app.height/8+75 + y,
            text= "%.2f" %app.supplyCurves[app.allFood[i+4]], font = "Arial 12")
        y += 92
    y = 0
    for i in range(3):
        canvas.create_text(app.width-173, app.height/3+45 + y,
            text=app.stock[app.allFood[i+7]], font = "Arial 35")
        canvas.create_text(app.width-173, app.height/3+75 + y,
            text="%.2f" %app.supplyCurves[app.allFood[i+7]], font = "Arial 12")
        y+=90
    canvas.create_text(app.width-180, 150, text = "Press any key\nto continue",
    font = ("Coolvetica Rg", 24))
    canvas.create_text(app.width-180, 600, text = f"Total cost: {app.supplyCost}",
    font = ("Coolvetica Rg", 24))
    canvas.create_text(app.width-180, 635, text = f"Your money: " + str("%.2f" % app.cash),
    font = ("Coolvetica Rg", 24))
    if app.poor:
        canvas.create_text(app.width-180, 670, text = "You don't have enough money!",
    font = ("Coolvetica Rg", 16))
#checking which button was clicked
def supplyMode_mousePressed(app, event):
    for i in range(len(app.hintDown)):
        if app.hintDown[i].isClicked(event.x, event.y):
            item = app.allFood[i]
            app.stock[item] -= 1
            itemcost = app.supplyCurves[item]
            if(app.supplyCost > itemcost) and app.amountBought[item] > 0:
                app.supplyCost = round((app.supplyCost -itemcost), 2)
    for j in range(len(app.hintUp)):
        if app.hintUp[j].isClicked(event.x, event.y):
            item = app.allFood[j]
            app.stock[item] += 1
            app.supplyCost = round((app.supplyCost +app.supplyCurves[item]), 2)
            app.amountBought[item] += 1

def supplyMode_keyPressed(app, event):
    if app.supplyCost > app.cash:
        app.poor = True
    else:
        app.cash -= app.supplyCost
        app.cash = round(app.cash, 2)
        app.supplyCost = 0
        app.poor = False
        app.mode = 'hintMode'
