# Program: MovingBall.py
# Authors: Dr Denny
#
#
# Recursive and Non-Recursive (for loop) Version

from cs1graphics import *
from time import sleep

scene = Canvas()
scene.setBackgroundColor('skyBlue')

### Recursive Version
##
##def drawBallMoving(n, ball):
##    if n <= 1:
##        sleep(.15)
##        ball.move(5,1)
##         
##    else:
##        sleep(.35)
##        ball.scale(.95)
##        ball.move(20,1)
##        drawBallMoving(n-1, ball)
##         
##    
##N=10
##Size=20
##Position=Point(50,50)
##ball = Circle(Size, Position)
##ball.setFillColor('yellow')
##scene.add(ball)
##drawBallMoving(N, ball)


#Non-Recursive (for loop) Version


N=10
Size=20
Position=Point(23,23)
ball2 = Circle(Size, Position)
ball2.setFillColor('red')
scene.add(ball2)
for n in range(N,0,-1):
    sleep(.20)
    ball2.scale(.75)
    ball2.move(20,1)



