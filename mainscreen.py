from cmu_112_graphics import *
from button import *
from main import *

def startMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.startScreen)

def startMode_mousePressed(app, event):
    if app.startButton.isClicked(event.x, event.y):
        app.mode = 'cookMode'

def startMode_keyPressed(app, event):
    app.mode = 'fishMode'
