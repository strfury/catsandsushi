from main import *
from cmu_112_graphics import *

def hintMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.hintScreen)
    canvas.create_rectangle(app.width/5+30, app.height/8+15, app.width/3-20,
    app.height/4-30)
    canvas.create_rectangle(app.width/5+160, app.height/8+15, app.width/3+110,
    app.height/4-30)
    canvas.create_rectangle(app.width/5+30, app.height/8+100, app.width/3-20,
    app.height/4+55)
    y = 0
    for i in range(4):
        canvas.create_rectangle(app.width/5+30, app.height/8+15 + y, 
        app.width/3-20, app.height/4-30 + y)
        canvas.create_rectangle(app.width/5+160, app.height/8+15 + y, 
        app.width/3+110, app.height/4-30 + y)
        y += 85
    for i in range(3):
        canvas.create_rectangle(app.width/5+30, app.height/8+15 + y, 
        app.width/3-20, app.height/4-30 + y)
        canvas.create_rectangle(app.width/5+160, app.height/8+15 + y, 
        app.width/3+110, app.height/4-30 + y)
        y += 100