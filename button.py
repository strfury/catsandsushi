#SOURCES: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#exampleGrids

class Buttons():
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
    #doesn't have to be a click, just checks if position is in the button
    def isClicked(self, x, y):
        if(self.x <= x <= self.x1) and (self.y <= y <= self.y1):
            return True
        return False