import random
from random import randrange
from main import *

class Cat():
    def __init__(self, happy, neutral, angry):
        self.happy = happy
        self.neutral = neutral
        self.angry = angry
        self.moods = [happy, neutral, angry]
        self.image = happy
        self.patience = 100
        #decrease at timer fired
        self.orderFulfilled = False
    def getOrder(self):
        return self.order
    def getPatience(self):
        return self.patience
    def addOrder(self, order):
        self.order = order
    def changeImage(self, image):
        self.image = image
    def getImage(self):
        return self.image
    def getMoods(self):
        return self.moods
    def changeMood(self):
        if self.patience < 25:
            self.changeImage(self.angry)
        elif(self.patience < 75):
            self.changeImage(self.neutral)
    def checkOrder(self, order):
        if order == self.order:
            #calcPrice 
            self.orderFulfilled = True
        else:
            #calcwrongorder
            self.orderFulfilled = True