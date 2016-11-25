print('assignment: Assignment 5')
print('programmer: Ryan Tolentino ')
print('')

from math import*
##Initial Class Definition
class Rectangle:
    def __init__(self):
        self.x = 0 
        self.y = 0

    def getX(self):
        return self._x
    def setX(self, val):
        self._x = val
    def getY(self):
        return self._y
    def setY(self, val):
        self._y = val
##creating an object of the class and operating on it
corner = Rectangle()
print "Initial: coordinates for the corner set to <2,2>"
corner.setX(2) #2 is value of _x in object corner
corner.setY(2) #2 is value of _y in object corner 
c1=corner.getX() 
c2=corner.getY()  
print "Result: print corner coordinates: <", c1,',',c2, '>'

#Part 2

from math import*
##Initial Class Definition
class Point:
    def __init__(self, initX = 0, initY = 0):
        self.x = initX
        self.y = initY
    def __str__(self):
        return '<'+str(self._x)+', '+str(self._y)+ '>'    
    def getX(self):
        return self._x
    def setX(self, val):
        self._x = val
    def getY(self):
        return self._y
    def setY(self, val):
        self._y = val
    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx*dx + dy*dy)

    def scale(self, factor):
        self._x *= factor
        self._y *= factor

    def normalize(self):
        mag=self.distance(Point())

        if mag>0:
            self.scale(1/mag)    
##creating an object of the class and operating on it
#using new initialization  
point1 = Point(2,2)
print("Result1 print point1: ", point1)
#using the distance method
point1 = Point(2,2)
point2 = Point(0,0) 
#3
from math import*
##Initial Class Definition
class Point:
    def __init__(self, initX = 0, initY = 0):
        self._x = initX
        self._y = initY
    def __str__(self):
        return '<'+str(self._x)+', '+str(self._y)+ '>'
    def getX(self):
        return self._x
    def setX(self, val):
        self._x = val
    def getY(self):
        return self._y
    def setY(self, val):
        self._y = val
    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx*dx + dy*dy)

    def scale(self, factor):
        self._x *= factor
        self._y *= factor


    def normalize(self):
        mag = self.distance(Point()) 
#Point() creates new point at origin
        if mag > 0: #don't scale if point is at origin
            self.scale(1/mag)
##creating an object of the class and operating on it
#using new initialization
point1 = Point(1,1)
print "Result1 print point1: ", point1
#using the distance method
point1 = Point(1,1)
point2 = Point(3,2) 
apartAmt = point1.distance(point2)
print "Result2 print distance: ", apartAmt
#applying normalization
point1 = Point(1,1)
point1.normalize()
print "Result3 print point1 after normalization: ", point1
apartAmt = point1.distance(Point(0,0))
print "Result4 print distance to origin for point 1 after normalization: ", apartAmt


print "Initial: coordinates for the corner set to <1,1>,<3,2>"
corner.setX(1) #1 is value of _x in object corner
corner.setY(1) #1 is value of _y in object corner
corner.setX(3) #3 is value of _x in object corner
corner.setY(2) #2 is value of _y in object corner 
c1=corner.getX() 
c2=corner.getY()  
print "Result: print corner coordinates: <", c1,',',c2, '>'
