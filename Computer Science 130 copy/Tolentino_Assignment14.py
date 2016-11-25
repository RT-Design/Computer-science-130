#Assignment: Assignment 14
#Student: Ryan Tolentino
#Date: September 26, 2016
from cs1graphics import *
from time import sleep

scene=Canvas()
scene.setBackgroundColor('white')

def drawTriangle(n,triangle=Polygon(Point(50,100),Point(100,200),Point(150,100))):
    if n <=1:
        triangle=Polygon(Point(50,100),Point(100,200),Point(150,100))
        triangle.setDepth(1)
        scene.add(triangle)
    else:
        triangle1=triangle.clone()
        triangle2=triangle1.clone()
        triangle3=triangle1.clone()
        triangle1.adjustReference(50,0)
        triangle2.adjustReference(50,0)
        triangle3.adjustReference(50,0)
        triangle1.scale(0.5)
        triangle2.scale(0.5)
        triangle3.scale(0.5)
        square=((0.5**(n-1))*200)
        triangle1.move(0,-(square))
        triangle2.move(-(square),(square))
        triangle3.move((square),(square))
        triangle1.setDepth(10-n)
        triangle2.setDepth(10-n)
        triangle3.setDepth(10-n)
        scene.add(triangle1)
        scene.add(triangle2)
        scene.add(triangle3)
        drawTriangle(n-1,triangle1)

drawTriangle(3)
triangle=Polygon(Point(0,200),Point(100,0),Point(200,200))#Representation
scene.add(triangle)
