from cmu_112_graphics import *
from button import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.image = ImageTk.PhotoImage(app.loadImage("items/knife.png"))
    app.knifeButton = Buttons(app.width/14, 3*app.height/4,4*app.width/5,
    3.75*app.height/4)
    app.knifeHold = False

def redrawAll(app, canvas):
    canvas.create_image(app.cx, app.cy, image=app.image)
    canvas.create_rectangle(app.width/14, 3*app.height/4,4*app.width/5,
    3.75*app.height/4)

def mousePressed(app, event):
    if app.knifeButton.isClicked(event.x, event.y):
        app.knifeHold = not app.knifeHold
    if(app.knifeHold == False):
        app.cx = app.width/2
        app.cy = app.height/2
def mouseMoved(app, event):
    if app.knifeHold == True:
        app.cx = event.x + 150
        app.cy = event.y -250


runApp(width = 750, height = 750, title = "cats & sushi")