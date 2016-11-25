from cs1graphics import *
from time import sleep

scene = Canvas()
scene.setBackgroundColor('skyBlue')

def drawFractal(n, size, positionX, positionY):
    if n <= 1:
        lastLevelFractal = Square(size, Point(positionX, positionY))
        lastLevelFractal.setFillColor('red')
        lastLevelFractal.setDepth(n+10)
        scene.add(lastLevelFractal)
        print(n)
    else:
        nextLevelFractal = Square(size, Point(positionX, positionY))
        nextLevelFractal.setFillColor('black')
        nextLevelFractal.setDepth(n+10)
        scene.add(nextLevelFractal)
        drawFractal(n-1,size, positionX+10, positionY+10)
        drawFractal(n-1,size, positionX-10, positionY+10)
        print(n)
drawFractal(10, 10, 100, 30)
