from ingredients import *
from customer import *
from day import *
from cmu_112_graphics import *
def appStarted(app):
    """app.table = app.loadImage('tablecloth.png')
    app.plate = app.loadImage('plate.png')
    app.cat1 = Customer("tan", Dish(salmon))
    app.catDict = dict()
    app.catDict[app.cat1.getColor()] = app.cat1.getImage()
    app.cat1pic = app.loadImage(app.cat1.getImage())
    app.player = Player()"""
def redrawAll(app, canvas):
    """w = app.width
    h = app.height
    #canvas.create_oval(w/5, 5*h/8, 4*w/5, 7*h/8, fill = 'blue')
    #canvas.create_image(500, 500, image=ImageTk.PhotoImage(app.table))
    canvas.create_image(w/2, h/2, image=ImageTk.PhotoImage(app.cat1pic))
    canvas.create_image(w/2 + 300, h/2+ 20, 
    image=ImageTk.PhotoImage(app.cat1pic))
    canvas.create_image(w/2, h/2, image=ImageTk.PhotoImage(app.table))
    canvas.create_image(w/2 + 20, h/2, image=ImageTk.PhotoImage(app.plate))
    drawFish(app, canvas, 'sienna1', w-75, h/5)
    drawFish(app, canvas, 'firebrick2', w-75, h/5+75)
    drawFish(app, canvas, 'rosybrown1', w-75, h/5 + 150)"""
    #drawCat(app, canvas, app.cat1)
def addPic(app, canvas, customer):
    pass
def drawAllFish(app, canvas, player):
    for i in range(len(player.getFish())):
        color = player.getFish()[i].getColor()
        drawFish(app, canvas, color, app.width + i*75, app.height + i*75)
def drawFish(app, canvas, color, x, y):
    canvas.create_oval(x, y, x+50, y+50, fill = color, outline = 'black',
    width = 2)

def drawCat(app, canvas, customer):
    canvas.create_image(app.width/2, app.height/2, 
    image=ImageTk.PhotoImage(app.catDict[customer.getColor()]))

runApp(width = 750, height = 750, title = 'cats & sushi')
