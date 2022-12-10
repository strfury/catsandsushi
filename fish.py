from cmu_112_graphics import *
from button import *
import math

# SOURCES: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
# distance formula: https://www.cuemath.com/distance-formula/
# IMAGE SOURCES: All images drawn by me
def fishMode_redrawAll(app, canvas):
    if not app.fishCut:
        app.guideLines = app.guide
    canvas.create_image(app.width/2, app.height/2, image=app.fishScreen)
    canvas.create_image(app.width/2, app.height/2, image=app.hintButton)
    canvas.create_image(app.width/2, app.height/2, image=app.fishArrow)
    canvas.create_image(app.width/2, app.height/2, image=app.currFish)
    canvas.create_image(app.fx, app.fy, image=app.knife)
    canvas.create_image(app.width/2, app.height/2, image = app.guideLines)
    canvas.create_text(40, 20, text = app.fishPercent, font = "Arial 25")

def fishMode_mousePressed(app, event):
    if app.fishHintButton.isClicked(event.x, event.y):
        app.mode = 'fishHint'
    elif app.fishArrowB.isClicked(event.x, event.y):
        app.similarity = []
        app.lines = 0
        app.mode = 'cookMode'
    elif app.knifeButton.isClicked(event.x, event.y):
        if not app.knifeHold: app.knifeHold = True
        else:
            app.knifeHold = False
            app.fx = app.width/2
            app.fy = app.height/2
    elif app.lines <2:
        if app.knifeHold:
            app.draw = True
            app.x = event.x
            app.y = event.y
def fishMode_mouseReleased(app, event):
    if app.draw:
        app.draw = False
        app.x1 = event.x
        app.y1 = event.y
        app.lines += 1
    if app.lines == 1:
        app.similarity.append(similarity(distance(app.x, app.y, 250, 220),
        distance(app.x1, app.y1, 290, 465), distance(app.x, app.y, app.x1,
        app.y1), 248.24))
    elif app.lines == 2 and len(app.similarity) < 2:
        app.similarity.append(similarity(distance(app.x, app.y, 370, 220),
        distance(app.x1, app.y1, 410, 465), distance(app.x, app.y, app.x1,
        app.y1), 248.24))
        app.fishCut = True
        app.currFish = app.cutDict[app.currFish]
        app.guideLines = app.blank
        app.fishPercent = (app.similarity[0] + app.similarity[1]) / 2
        app.fishPercent = round(app.fishPercent, 2)
    #if len(app.similarity)

def fishMode_mouseMoved(app, event):
    if app.knifeHold:
        app.fx = event.x + 150
        app.fy = event.y - 250
def fishMode_mouseDragged(app, event):
    if app.knifeHold:
        app.fx = event.x + 150
        app.fy = event.y -250
def distance(x, y, x1, y1):
    result = math.sqrt((x1-x)**2+(y1-y)**2)
    return result
def similarity(d1, d2, r1, r2):
    x = min(r1, r2)
    if x == 0: return 0.05
    result = 1-(max(d1, d2)/x)
    if result < 0:
        return 0.05
    return result

#FISH HINT SCREEN
def fishHint_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.fishHint)

def fishHint_mousePressed(app, event):
    if app.fishHintExit.isClicked(event.x, event.y):
        app.mode = 'fishMode'

