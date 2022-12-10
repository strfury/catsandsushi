from cmu_112_graphics import *
from main import *
from day import *

def startMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.startScreen)

def startMode_mousePressed(app, event):
    if app.startButton.isClicked(event.x, event.y):
        app.mode = 'dayMode'