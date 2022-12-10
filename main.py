#SOURCES:
#All images drawn by me using Procreate
import random
from random import *
from cmu_112_graphics import *
from button import *
from fish import *
from cooking import *
from mainscreen import *
from ingredients import *
from customer import *
from day import *
from supply import *
from hint import *
import math

def appStarted(app):
    app.mode = 'startMode'
    #object states
    app.day = 1
    app.time = 0
    app.timeS = 0
    app.bx = 0
    app.timeG = 0
    app.w = app.width/2
    app.h = app.height/2
    app.fx = app.width/2 #location of fish knife
    app.fy = app.height/2
    app.drag = False
    app.gravity = False
    app.activeOrders = []
    app.currOrder = Dish()
    app.knifeHold = False
    app.fishCut = False
    app.draw = False
    app.showHint = False
    app.credits = 0
    #variables for cutting fish
    app.x = 0
    app.y = 0
    app.x1 = 0
    app.y1 = 0
    app.points = []
    app.lines = 0
    app.similarity = []
    app.fishPercent = 0
    #player information
    app.cash = 0
    app.goal = 100
    app.poor = False
    app.negCredits = False
    #ingredients
    app.rice = Ingredient('rice', 1)
    app.salmon = Fish('salmon', 5)
    app.tuna = Fish('tuna', 4)
    app.yellowtail = Fish('yellowtail', 6)
    app.shrimp = Fish('shrimp', 4)
    app.wasabi = Toppings('wasabi', 1)
    app.crunch = Toppings('crunch', 1)
    app.mayo = Sauce('mayo', 1)
    app.soy = Sauce('s_sauce', 1)
    app.eel = Sauce('eel_sauce', 1)
    app.allFish = [app.salmon, app.tuna, app.yellowtail, app.shrimp]
    app.allSauces = [app.soy, app.mayo, app.eel]
    app.allToppings = [app.crunch, app.wasabi]
    app.allFood = app.allFish + [app.rice] + app.allToppings + app.allSauces
    app.stock = dict()
    for item in app.allFood:
        app.stock[item] = 5
    #screen backgrounds
    app.fishScreen = ImageTk.PhotoImage(app.loadImage("screens/fish.png"))
    app.startScreen = ImageTk.PhotoImage(app.loadImage("screens/start.png"))
    app.cookScreen = ImageTk.PhotoImage(app.loadImage("screens/cook1.png"))
    app.bgColor = ImageTk.PhotoImage(app.loadImage("screens/cookbg.png"))
    app.hintScreen = ImageTk.PhotoImage(app.loadImage("screens/supply.png"))
    app.dayStart = ImageTk.PhotoImage(app.loadImage("screens/daystart.png"))
    app.dayEnd = ImageTk.PhotoImage(app.loadImage("screens/dayend.png"))
    app.priceHint = ImageTk.PhotoImage(app.loadImage("screens/price.png"))
    #hints/tutorials
    app.fishHint = ImageTk.PhotoImage(app.loadImage("tutorials/fish.png"))
    app.cookHint = ImageTk.PhotoImage(app.loadImage("screens/hintcook.png"))
    #item assets
    app.knife = ImageTk.PhotoImage(app.loadImage("items/knife.png"))
    app.blank = ImageTk.PhotoImage(app.loadImage("blank.png"))
    #customers
    app.rightCat = app.blank
    app.leftCat = app.blank
    app.blueH = ImageTk.PhotoImage(app.loadImage("cats/blue_happy.png"))
    app.blueN = ImageTk.PhotoImage(app.loadImage("cats/blue_neutral.png"))
    app.blueM = ImageTk.PhotoImage(app.loadImage("cats/blue_mad.png"))
    app.orangeH = ImageTk.PhotoImage(app.loadImage("cats/orange_happy.png"))
    app.orangeN = ImageTk.PhotoImage(app.loadImage("cats/orange_neutral.png"))
    app.orangeM = ImageTk.PhotoImage(app.loadImage("cats/orange_mad.png"))
    app.simH = ImageTk.PhotoImage(app.loadImage("cats/sim_happy.png"))
    app.simN = ImageTk.PhotoImage(app.loadImage("cats/sim_neutral.png"))
    app.simM = ImageTk.PhotoImage(app.loadImage("cats/sim_mad.png"))
    app.creamH = ImageTk.PhotoImage(app.loadImage("cats/cream_happy.png"))
    app.creamN = ImageTk.PhotoImage(app.loadImage("cats/cream_neutral.png"))
    app.creamM = ImageTk.PhotoImage(app.loadImage("cats/cream_mad.png"))
    app.spotsH = ImageTk.PhotoImage(app.loadImage("cats/spots_happy.png"))
    app.spotsN = ImageTk.PhotoImage(app.loadImage("cats/spots_neutral.png"))
    app.spotsM = ImageTk.PhotoImage(app.loadImage("cats/spots_mad.png"))
    app.purpleH = ImageTk.PhotoImage(app.loadImage("cats/purple_happy.png"))
    app.purpleN = ImageTk.PhotoImage(app.loadImage("cats/purple_neutral.png"))
    app.purpleM = ImageTk.PhotoImage(app.loadImage("cats/purple_mad.png"))
    app.greenH = ImageTk.PhotoImage(app.loadImage("cats/green_happy.png"))
    app.greenN = ImageTk.PhotoImage(app.loadImage("cats/green_neutral.png"))
    app.greenM = ImageTk.PhotoImage(app.loadImage("cats/green_mad.png"))
    app.blueCat = Cat(app.blueH, app.blueN, app.blueM)
    app.orangeCat = Cat(app.orangeH, app.orangeN, app.orangeM)
    app.creamCat = Cat(app.creamH, app.creamN, app.creamM)
    app.simCat = Cat(app.simH, app.simN, app.simM)
    app.spotsCat = Cat(app.spotsH, app.spotsN, app.spotsM)
    app.purpleCat = Cat(app.purpleH, app.purpleN, app.purpleM)
    app.greenCat = Cat(app.greenH, app.greenN, app.greenM)

    app.allCats = [app.blueCat, app.orangeCat, app.simCat, app.creamCat, 
        app.spotsCat, app.purpleCat, app.greenCat]
    app.currCats = []
    #food on cooking screen
    app.riceFood = ImageTk.PhotoImage(app.loadImage("food/rice.png"))
    app.salmonFish = ImageTk.PhotoImage(app.loadImage("fish/salmonb.png"))
    app.tunaFish = ImageTk.PhotoImage(app.loadImage("fish/tunab.png"))
    app.yellowtailFish = ImageTk.PhotoImage(app.loadImage("fish/yellowtailb.png"))
    app.shrimpFish = ImageTk.PhotoImage(app.loadImage("fish/shrimpb.png"))
    app.soyS = ImageTk.PhotoImage(app.loadImage("food/soysauce.png"))
    app.eelS = ImageTk.PhotoImage(app.loadImage("food/eel.png"))
    app.mayoS = ImageTk.PhotoImage(app.loadImage("food/mayo.png"))
    app.wasabiT = ImageTk.PhotoImage(app.loadImage("food/wasabi.png"))
    app.crunchT = ImageTk.PhotoImage(app.loadImage("food/crunch.png"))
    app.displayDict = {app.salmon:app.salmonFish, app.tuna:app.tunaFish, 
    app.yellowtail:app.yellowtailFish, app.shrimp:app.shrimpFish, 
    app.rice:app.riceFood, app.wasabi:app.wasabiT, app.crunch:app.crunchT,
    app.eel:app.eelS, app.mayo:app.mayoS, app.soy:app.soyS}
    app.riceDisplay = app.blank
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
    app.fishCutDict = {app.salmon:app.salmonF, app.tuna:app.tunaF, 
    app.yellowtail:app.yellowtailF, app.shrimp:app.shrimpF}
    app.cutDict = {app.salmonF:app.salmonFC, app.tunaF:app.tunaFC, 
    app.yellowtailF:app.yellowtailFC, app.shrimpF:app.shrimpFC}
    #food in the order bubble
    app.salmonO = ImageTk.PhotoImage(app.loadImage("food/salmono.png"))
    app.tunaO = ImageTk.PhotoImage(app.loadImage("food/tunao.png"))
    app.yellowtailO = ImageTk.PhotoImage(app.loadImage("food/yellowtailo.png"))
    app.shrimpO = ImageTk.PhotoImage(app.loadImage("food/shrimpo.png"))
    app.riceO = ImageTk.PhotoImage(app.loadImage("food/riceo.png"))
    app.crunchO = ImageTk.PhotoImage(app.loadImage("food/cruncho.png"))
    app.wasabiO = ImageTk.PhotoImage(app.loadImage("food/wasabio.png"))
    app.eelO = ImageTk.PhotoImage(app.loadImage("food/eelo.png"))
    app.mayoO = ImageTk.PhotoImage(app.loadImage("food/mayoO.png"))
    app.soyO = ImageTk.PhotoImage(app.loadImage("food/soysauceo.png"))
    app.bubbleFood = {app.salmon:app.salmonO, app.tuna:app.tunaO, 
    app.yellowtail:app.yellowtailO, app.shrimp:app.shrimpO, 
    app.rice:app.riceO, app.wasabi:app.wasabiO, app.crunch:app.crunchO,
    app.eel:app.eelO, app.mayo:app.mayoO, app.soy:app.soyO}
    #hints + supply/demand
    app.hints = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    app.demands = dict()
    app.hintDict = dict()
    app.supplyCurves = dict()
    app.amountBought = dict()
    app.supplyCost = 0
    for item in app.allFood:
        app.supplyCurves[item] = 1
        app.amountBought[item] = 0
    #starting the day
    app.currDay = Day(app.day)
    app.numCustomers = app.currDay.getCustomers()
    random.shuffle(app.allCats)
    app.currCats = app.allCats[0:app.numCustomers]
    for j in range(len(app.currCats)):
        app.currCats[j].addOrder(makeDish(app))

    #GUI IMAGES
    app.hintButton = ImageTk.PhotoImage(app.loadImage("gui/hint.png"))
    app.mainHint = ImageTk.PhotoImage(app.loadImage("gui/hint1.png"))
    app.fishArrow = ImageTk.PhotoImage(app.loadImage("gui/fish_arrow.png"))
    app.order = ImageTk.PhotoImage(app.loadImage("gui/order.png"))
    app.orderL = ImageTk.PhotoImage(app.loadImage("gui/order.png"))
    app.timeBar = ImageTk.PhotoImage(app.loadImage("gui/timebar.png"))
    app.timeArrow = ImageTk.PhotoImage(app.loadImage("gui/timearrow.png"))
    app.hintLine = ImageTk.PhotoImage(app.loadImage("gui/hintline.png"))
    app.hintBar = ImageTk.PhotoImage(app.loadImage("gui/slider.png"))
    app.guide = ImageTk.PhotoImage(app.loadImage("gui/guide.png"))
    app.guideLines = app.guide
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
    app.plateB = Buttons(app.width/3-125, 4*app.height/7+100, 2*app.width/3-25, 
        6*app.height/7 + 50)
    app.soyB = Buttons(15, 2*app.height/3, 80, 2*app.height/3+70)
    app.mayoB = Buttons(15, 2*app.height/3+75, 80, 2*app.height/3+145)
    app.eelB = Buttons(15, 2*app.height/3+150, 80, 2*app.height/3+220)
    app.wasabiB = Buttons(3*app.width/4-45, 3*app.height/4-70, app.width-130, 
        app.height-135)
    app.crunchB = Buttons(app.width-130, 3*app.height/4-70, 710, app.height-135)
    app.cookHintB = Buttons(app.width-120, 20, app.width-65, 65)
    app.showHintB = Buttons(3*app.width/4-90, 4*app.height/5-25, app.width-75,
    app.height-95)
    app.cookButtons = {app.salmon:app.salmonB, app.tuna:app.tunaB, 
    app.yellowtail:app.yellowB, app.shrimp:app.shrimpB,app.soy:app.soyB,
    app.mayo:app.mayoB, app.eel:app.eelB, app.wasabi:app.wasabiB, 
    app.crunch:app.crunchB, app.rice:app.riceB}
#hint buttons
    app.hint1 = Buttons(app.width/5+30, app.height/8+15, app.width/3-20,
        app.height/4-30)
    app.hint2 = Buttons(app.width/5+160, app.height/8+15, app.width/3+110,
        app.height/4-30)
    app.hint3 = Buttons(app.width/5+30, app.height/8+15+80, app.width/3-20,
        app.height/4+50)
    app.hint4 = Buttons(app.width/5+160, app.height/8+15+80, app.width/3+110,
        app.height/4+50)
    app.hint5 = Buttons(app.width/5+30, app.height/8+15+160, app.width/3-20,
        app.height/4+130)
    app.hint6 = Buttons(app.width/5+160, app.height/8+15+160, app.width/3+110,
        app.height/4+130)
    app.hint7 = Buttons(app.width/5+30, app.height/8+15+240, app.width/3-20,
        app.height/4+210)
    app.hint8 = Buttons(app.width/5+160, app.height/8+15+240, app.width/3+110,
        app.height/4+210)
    app.hint9 = Buttons(app.width/5+30, app.height/8+15+332, app.width/3-20,
        app.height/4+302)
    app.hint10 = Buttons(app.width/5+160, app.height/8+15+332, app.width/3+110,
        app.height/4+302)
    app.hint11 = Buttons(app.width/5+30, app.height/8+15+424, app.width/3-20,
        app.height/4+394)
    app.hint12 = Buttons(app.width/5+160, app.height/8+15+424, app.width/3+110,
        app.height/4+394)
    app.hint13 = Buttons(app.width/5+30, app.height/8+15+516, app.width/3-20,
        app.height/4+486)
    app.hint14 = Buttons(app.width/5+160, app.height/8+15+516, app.width/3+110,
        app.height/4+486)
    app.hint15 = Buttons(3*app.width/5+35, app.height/3+25, app.width-215,
    app.height/3+48.75+20)
    app.hint16 = Buttons(3*app.width/5+165, app.height/3+25, app.width-85,
    app.height/3+48.75+20)
    app.hint17 = Buttons(3*app.width/5+35, app.height/3+25+90, app.width-215,
    app.height/3+48.75+110)
    app.hint18 = Buttons(3*app.width/5+165, app.height/3+25+90, app.width-85,
    app.height/3+48.75+110)
    app.hint19 = Buttons(3*app.width/5+35, app.height/3+25+170, app.width-215,
    app.height/3+48.75+190)
    app.hint20 = Buttons(3*app.width/5+165, app.height/3+25+170, app.width-85,
    app.height/3+48.75+190)
    app.hintDown = [app.hint1, app.hint3, app.hint5, app.hint7, app.hint9, 
    app.hint11, app.hint13, app.hint15, app.hint17, app.hint19]
    app.hintUp = [app.hint2, app.hint4, app.hint6, app.hint8, app.hint10,
    app.hint12, app.hint14, app.hint16, app.hint18, app.hint20]
runApp(width = 750, height = 750, title = "cats & sushi")
