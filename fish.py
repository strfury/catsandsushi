from cmu_112_graphics import *
from button import *

# SOURCES: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
# IMAGE SOURCES: All images drawn by me
def fishMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.fishScreen)
    canvas.create_image(app.width/2, app.height/2, image=app.hintButton)
    canvas.create_image(app.width/2, app.height/2, image=app.fishArrow)
    canvas.create_image(app.width/2, app.height/2, image=app.currFish)
    canvas.create_image(app.fx, app.fy, image=app.knife)

def fishMode_mousePressed(app, event):
    if app.fishHintButton.isClicked(event.x, event.y):
        app.mode = 'fishHint'
    elif app.fishArrowB.isClicked(event.x, event.y):
        app.mode = 'cookMode'
    elif app.knifeButton.isClicked(event.x, event.y):
        app.knifeHold = True
    elif(app.cutButton.isClicked(event.x, event.y)):
        if app.knifeHold == True:
            app.currFish = app.cutDict[app.currFish]
            app.fishCut = True
    elif (0 <= event.x <= app.width) and (0 <= event.y <= app.height):
        app.knifeHold = False
        app.fx =  app.width/2
        app.fy = app.height/2

def fishMode_mouseMoved(app, event):
    if app.knifeHold == True:
        app.fx = event.x + 150
        app.fy = event.y - 250

#FISH HINT SCREEN
def fishHint_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.fishHint)
    canvas.create_rectangle(0.3*app.width/8, 0.3*app.height/8,
    1.2*app.width/8, 1.2*app.height/8)

def fishHint_mousePressed(app, event):
    if app.fishHintExit.isClicked(event.x, event.y):
        app.mode = 'fishMode'
