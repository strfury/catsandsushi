from cmu_112_graphics import *
import random

#create text for the hint based on if the users price is too high, too low, or correct
def hintMode_redrawAll(app, canvas):
    for i in range(len(app.allFood)):
        if app.allFood[i].getPrice() < app.hintDict[app.allFood[i]]:
            app.hints[i] = "+"
        elif app.allFood[i].getPrice() > app.hintDict[app.allFood[i]]:
            app.hints[i] = "-"
        elif app.allFood[i].getPrice() == app.hintDict[app.allFood[i]]:
            app.hints[i] = "="
    canvas.create_image(app.width/2, app.height/2, image=app.priceHint)
    canvas.create_text(app.width/2, 50, text="Set the price of items",
        font = ("Coolvetica Rg", 25))
    canvas.create_text(app.width-180, 550, text = f"Credits left: {app.credits}",
    font = ("Coolvetica Rg", 24))
    if app.negCredits:
        canvas.create_text(app.width-180, 700, text = "You can't have \n negative credits!",
    font = ("Coolvetica Rg", 18))
    y = 0
    for i in range(4):
        canvas.create_text(app.width/5+120, app.height/8+45 + y,
            text=app.allFood[i].getPrice(), font = "Arial 35")

        if app.showHint:
            canvas.create_text(app.width/5+145, app.height/8+45 + y,
            text=app.hints[i], font = "Arial 25")    
        y += 80
    for i in range(3):
        canvas.create_text(app.width/5+120, app.height/8+45 + y,
            text=app.allFood[i+4].getPrice(), font = "Arial 35")
        if app.showHint:
            canvas.create_text(app.width/5+145, app.height/8+45 + y,
            text=app.hints[i+4], font = "Arial 25")    
        y += 92
    y = 0
    for i in range(3):
        canvas.create_text(app.width-173, app.height/3+45 + y,
            text=app.allFood[i+7].getPrice(), font = "Arial 35")
        if app.showHint:
            canvas.create_text(598, app.height/3+45 + y,
            text=app.hints[i+7], font = "Arial 25")    
        y+=90
    canvas.create_text(app.width-180, 150, text = "Press any key\nto continue",
    font = ("Coolvetica Rg", 24))
#to adjust the price of each item
def hintMode_mousePressed(app, event):
    for i in range(len(app.hintDown)):
        if app.hintDown[i].isClicked(event.x, event.y):
            app.allFood[i].decPrice()
            app.credits += 1
    for j in range(len(app.hintUp)):
        if app.hintUp[j].isClicked(event.x, event.y):
            app.allFood[j].incPrice()
            app.credits -= 1
    if app.showHintB.isClicked(event.x, event.y):
        app.showHint = True
#hint button is not a toggle, you must hold it to show hints
def hintMode_mouseReleased(app, event):
    app.showHint = False
#to start the next day
def hintMode_keyPressed(app, event):
    if app.credits < 0:
        app.negCredits = True
    else:
        app.negCredits = False
        app.mode = 'dayMode'

