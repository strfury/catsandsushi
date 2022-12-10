from main import *
from cooking import *
class Cat():
    def __init__(self, happy, neutral, angry):
        self.happy = happy
        self.neutral = neutral
        self.angry = angry
        self.image = happy
        self.patience = 300
        #decrease at timer fired
        self.orderFulfilled = False

    def getOrder(self):
        return self.order
    def getPatience(self):
        return self.patience
    def setPatience(self):
        self.patience = 300
    def addOrder(self, order):
        self.order = order
    def changeImage(self, image):
        self.image = image
    def getImage(self):
        return self.image
    def changeMood(self):
        if self.patience < 100:
            self.changeImage(self.angry)
        elif(self.patience < 200):
            self.changeImage(self.neutral)
    def decPatience(self):
        if self.patience >=3:
            self.patience -= 3
        self.changeMood()