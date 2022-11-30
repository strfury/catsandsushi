#SOURCES:
#All images drawn by me using Procreate
from cmu_112_graphics import *
from button import *
from fish import *
from cooking import *
from mainscreen import *
from ingredients import *
from customer import *

def appStarted(app):
    app.mode = 'startMode'
    #object states
    app.time = 0
    app.bx = 0
    app.fx = app.width/2 #location of fish knife
    app.fy = app.height/2
    app.activeOrders = []
    app.currOrder = Dish()
    app.knifeHold = False
    app.fishCut = False
    #screen backgrounds
    app.fishScreen = ImageTk.PhotoImage(app.loadImage("screens/fish.png"))
    app.startScreen = ImageTk.PhotoImage(app.loadImage("screens/start.png"))
    app.cookScreen = ImageTk.PhotoImage(app.loadImage("screens/cook1.png"))
    app.bgColor = ImageTk.PhotoImage(app.loadImage("screens/cookbg.png"))
    app.hintScreen = ImageTk.PhotoImage(app.loadImage("screens/hint1.png"))
    #hints/tutorials
    app.fishHint = ImageTk.PhotoImage(app.loadImage("tutorials/fish.png"))
    #item assets
    app.knife = ImageTk.PhotoImage(app.loadImage("items/knife.png"))
    app.blank = ImageTk.PhotoImage(app.loadImage("blank.png"))
    #ingredients
    app.allFood = fish + toppings + sauces
    #customers
    app.rightCat = app.blank
    app.leftCat = app.blank
    app.blueH = ImageTk.PhotoImage(app.loadImage("cats/blue_happy.png"))
    app.blueN = ImageTk.PhotoImage(app.loadImage("cats/blue_neutral.png"))
    app.blueM = ImageTk.PhotoImage(app.loadImage("cats/blue_mad.png"))
    app.orangeH = ImageTk.PhotoImage(app.loadImage("cats/orange_happy.png"))
    app.orangeN = ImageTk.PhotoImage(app.loadImage("cats/orange_neutral.png"))
    app.orangeM = ImageTk.PhotoImage(app.loadImage("cats/orange_mad.png"))
    app.blueCat = Cat(app.blueH, app.blueN, app.blueM)
    app.orangeCat = Cat(app.orangeH, app.orangeN, app.orangeM)
    app.blueCat.addOrder(Dish(salmon))
    app.orangeCat.addOrder(Dish(tuna))
    app.currCats = [app.blueCat, app.orangeCat]
    app.allCats = [app.blueCat, app.orangeCat]
    #food on cooking screen
    app.rice = ImageTk.PhotoImage(app.loadImage("food/rice.png"))
    app.riceDisplay = app.blank
    app.salmon = ImageTk.PhotoImage(app.loadImage("fish/salmonb.png"))
    app.tuna = ImageTk.PhotoImage(app.loadImage("fish/tunab.png"))
    app.yellowtail = ImageTk.PhotoImage(app.loadImage("fish/yellowtailb.png"))
    app.shrimp = ImageTk.PhotoImage(app.loadImage("fish/shrimpb.png"))
    app.fishDisplay = app.blank
    app.toppingDisplay = app.blank
    app.sauceDisplay = app.blank
    #fish on the cutting screen
    app.salmonF = ImageTk.PhotoImage(app.loadImage("fish/salmon.png"))
    app.salmonFC = ImageTk.PhotoImage(app.loadImage("fish/salmonc.png"))
    app.tunaF = ImageTk.PhotoImage(app.loadImage("fish/tuna.png"))
    app.tunaFC = ImageTk.PhotoImage(app.loadImage("fish/tunac.png"))
    app.yellowtailF = ImageTk.PhotoImage(app.loadImage("fish/yellowtail.png"))
    app.yellowtailFC = ImageTk.PhotoImage(app.loadImage("fish/yellowtailc.png"))
    app.shrimpF = ImageTk.PhotoImage(app.loadImage("fish/shrimp.png"))
    app.shrimpFC = ImageTk.PhotoImage(app.loadImage("fish/shrimpc.png"))
    app.currFish = app.blank
    app.cutDict = {app.salmonF:app.salmonFC, app.tunaF:app.tunaFC, 
    app.yellowtailF:app.yellowtailFC, app.shrimpF:app.shrimpFC}
    #food in the order bubble
    app.salmonO = ImageTk.PhotoImage(app.loadImage("food/salmono.png"))
    app.tunaO = ImageTk.PhotoImage(app.loadImage("food/tunao.png"))
    app.yellowtailO = ImageTk.PhotoImage(app.loadImage("food/yellowtailo.png"))
    app.shrimpO = ImageTk.PhotoImage(app.loadImage("food/shrimpo.png"))
    app.riceO = ImageTk.PhotoImage(app.loadImage("food/riceo.png"))
    app.bubbleFood = {salmon:app.salmonO, tuna:app.tunaO, 
    yellowtail:app.yellowtailO, shrimp:app.shrimpO, rice:app.riceO}
    #GUI IMAGES
    app.hintButton = ImageTk.PhotoImage(app.loadImage("gui/hint.png"))
    app.fishArrow = ImageTk.PhotoImage(app.loadImage("gui/fish_arrow.png"))
    app.order = ImageTk.PhotoImage(app.loadImage("gui/order.png"))
    app.timeBar = ImageTk.PhotoImage(app.loadImage("gui/timebar.png"))
    app.timeArrow = ImageTk.PhotoImage(app.loadImage("gui/timearrow.png"))
    app.hintLine = ImageTk.PhotoImage(app.loadImage("gui/hintline.png"))
    app.hintBar = ImageTk.PhotoImage(app.loadImage("gui/slider.png"))

    #GUI OBJECTS
    app.fishHintButton = Buttons(10.5*app.width/13, 0.5*app.height/13, 
        12.5*app.width/13, 2.5*app.height/13)
    app.fishHintExit = Buttons(0.3*app.width/8, 0.3*app.height/8,
        1.2*app.width/8, 1.2*app.height/8)
    app.knifeButton = Buttons(app.width/14, 3*app.height/4,4*app.width/5,
        3.75*app.height/4)
    app.startButton = Buttons(2.5*app.width/8, 5*app.height/8, 
        5.5*app.width/8, 6*app.height/8)
    app.cutButton = Buttons(app.width/4-10, app.height/3-10, 2.6*app.width/4,
        1.7*app.height/3+20)
    app.fishArrowB = Buttons(5*app.width/6-30, 7*app.height/8-25, app.width-50,
        app.height-35)
    app.salmonB = Buttons(5*app.width/6, app.height/8-10, app.width-40,
        app.height/4-30)
    app.tunaB = Buttons(5*app.width/6, app.height/8+75, app.width-40,
        app.height/4+55)
    app.yellowB = Buttons(5*app.width/6, app.height/8+170, app.width-40,
        app.height/4+150)
    app.shrimpB = Buttons(5*app.width/6, app.height/8+255, app.width-40,
        app.height/4+235)
    app.riceB = Buttons(2*app.width/3+20, 5*app.height/6+10, app.width-40,
        app.height-40)
    app.bubbleRight = Buttons(app.width/2-35, 20, 3*app.width/4+25, 
        app.height/4+30)
    app.bubbleLeft = Buttons(75, 20, app.width/2-60, app.height/4+30)
runApp(width = 750, height = 750, title = "cats & sushi")
