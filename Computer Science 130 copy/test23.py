from csgraphics import *
paper = Canvas(300,200, 'skyBlue', 'My World')

sun = Circle(30, Point(250,50))
sun.setFillColor('yellow')
paper.add(sun)

façade = Square(60, Point(140,130))
façade.setFillColor('white')
paper.add(façade)
