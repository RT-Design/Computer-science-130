print('Programmer: Ryan Tolentino')
print('Class Work Chapter 3 and Recursive 3')
print('9/17/16')

print('\n Reversed list\n')
#Reversed List
def reverseList(OurList):
    if len(OurList)==0:
        return []
    else:
        head = OurList[0:1]
        rest = OurList[1:]
        print('This is head: ',head, '  and this is rest: ',rest, 'for this call of reverseList')
        return reverseList(rest)+ head
print(reverseList(['H','E','R','E']))
print('\n Factorial\n')
#Factorial
def factorial(n):
    if n <= 1: return 1
    else:
        return n * factorial(n - 1)
        print(n)
print('Factorial of 8 = ',factorial(8))

#A3 program 1
print('\n getgrades\n')
def getGrades():
    grade = raw_input('What is the next score: ')
    if grade == '':
        return []
    else:
        head = list()
        head.append(int(grade))
        rest = getGrades()
        return head + rest
print('Input John"s scores')
print('Result: the list of all Johns scores is ', getGrades())


#Pacer String
print('\n ParseString \n')
def parseString(ourString):
    positionPlus = ourString.find('+')
    if positionPlus == -1:
        return int(ourString)
    else:
        head = ourString[0:positionPlus]
        rest = ourString[positionPlus+1:]
        print head, '  ', rest
        return int(head) + parseString(rest)
print('\nParsestring')
print(parseString('1+2+3'))

#Graphics

print('\n Graphics \n')

from cs1graphics import *
from time import sleep

def Main():
    scene = Canvas()
    scene.setBackgroundColor('skyBlue')
    grass = Rectangle(200, 80, Point(100,160))
    grass.setFillColor('green')
    grass.setBorderColor('green')
    grass.setDepth(100)
    scene.add(grass)
    sun = Circle(20, Point(50,30))
    sun.setFillColor('yellow')
    scene.add(sun)

    target = Layer()
    outside = Rectangle(60,30)
    outside.setFillColor('white')
    outside.setDepth(49)
    target.add(outside)
    middle = Rectangle(40,20)
    middle.setFillColor('blue')
    middle.setDepth(48)
    target.add(middle)
    inside = Rectangle(20,10)
    inside.setFillColor('red')
    inside.setDepth(47)
    target.add(inside)
    legs = Path(Point(-25,45), Point(0,0), Point(25,45))
    legs.setBorderWidth(2)
    target.add(legs)
    target.move(160,110)
    target.setDepth(75)           
    scene.add(target)

    
    arrow1 = Layer()
    tip = Circle(5,Point(0,0))
    tip.setFillColor('black')
    arrow1.add(tip)
    
    arrow1.move(15,120)           
    arrow2 = arrow1.clone()
    arrow3 = arrow1.clone()

    dialogue = Text('Click target to fire an arrow')
    dialogue.move(100,170)
    scene.add(dialogue)

    target.wait()               
    scene.add(arrow1)
    arrow1.rotate(-20)
    sleep(0.15)
    arrow1.move(41,-15)
    arrow1.scale(.85)
    arrow1.rotate(7)
    sleep(0.15)
    arrow1.move(41,-5)
    arrow1.scale(.85)
    arrow1.rotate(7)
    sleep(0.15)
    arrow1.move(41,5)
    arrow1.scale(.85)
    arrow1.rotate(7)
    sleep(0.15)
    arrow1.move(41,17)
    arrow1.rotate(7)
    square1 = Layer()
    shape1 = Square(15, Point(180,75))
    shape1.setDepth(1)
    shape1.setFillColor('green')
    square1.add(shape1)
    scene.add(square1)
    square3 = Layer()
    shape3 = Square(15, Point(160,75))
    shape3.setDepth(1)
    shape3.setFillColor('red')
    square3.add(shape3)
    scene.add(square3)
    sleep(0.50)
    square2 = Layer()
    shape2 = Square(15, Point(180,75))
    shape2.setDepth(1)
    shape2.setFillColor('red')
    square2.add(shape2)
    scene.add(square2)
    square4 = Layer()
    shape4 = Square(15, Point(160,75))
    shape4.setDepth(1)
    shape4.setFillColor('green')
    square4.add(shape4)
    scene.add(square4)

    target.wait()               
    scene.add(arrow2)
    arrow2.rotate(-40)
    sleep(0.15)
    arrow2.move(39,-22)
    arrow2.scale(.85)
    arrow2.rotate(17)
    sleep(0.15)
    arrow2.move(39,-12)
    arrow2.scale(.85)
    arrow2.rotate(17)
    sleep(0.15)
    arrow2.move(39,3)
    arrow2.scale(.85)
    arrow2.rotate(17)
    sleep(0.15)
    arrow2.move(39,13)
    arrow2.rotate(17)
    square5 = Layer()
    shape5 = Square(15, Point(180,75))
    shape5.setDepth(1)
    shape5.setFillColor('green')
    square5.add(shape5)
    scene.add(square5)
    square7 = Layer()
    shape7 = Square(15, Point(160,75))
    shape7.setDepth(1)
    shape7.setFillColor('red')
    square7.add(shape7)
    scene.add(square7)
    sleep(0.50)
    square6 = Layer()
    shape6 = Square(15, Point(180,75))
    shape6.setDepth(1)
    shape6.setFillColor('red')
    square6.add(shape6)
    scene.add(square6)
    square8 = Layer()
    shape8 = Square(15, Point(160,75))
    shape8.setDepth(1)
    shape8.setFillColor('green')
    square8.add(shape8)
    scene.add(square8)

    target.wait()                 
    scene.add(arrow3)
    arrow3.rotate(-30)
    sleep(0.15)
    arrow3.move(37,-26)
    arrow3.scale(.85)
    arrow3.rotate(10)
    sleep(0.15)
    arrow3.move(37,-11)
    arrow3.scale(.85)
    arrow3.rotate(10)
    sleep(0.15)
    arrow3.move(37,6)
    arrow3.scale(.85)
    arrow3.rotate(10)
    sleep(0.15)
    arrow3.move(37,21)
    arrow3.rotate(10)
    square9 = Layer()
    shape9 = Square(15, Point(180,75))
    shape9.setDepth(1)
    shape9.setFillColor('green')
    square9.add(shape9)
    scene.add(square9)
    square11 = Layer()
    shape11 = Square(15, Point(160,75))
    shape11.setDepth(1)
    shape11.setFillColor('red')
    square11.add(shape11)
    scene.add(square11)
    sleep(0.50)
    square10 = Layer()
    shape10 = Square(15, Point(180,75))
    shape10.setDepth(1)
    shape10.setFillColor('red')
    square10.add(shape10)
    scene.add(square10)
    square12 = Layer()
    shape12 = Square(15, Point(160,75))
    shape12.setDepth(1)
    shape12.setFillColor('green')
    square12.add(shape12)
    scene.add(square12)
    dialogue.setMessage('Good shooting!')

    scene.wait()                
    scene.close()
x = ''

while True:
        x = input("Play Y/N:")
        if x == 'y' or 'Y':
                Main()
                
        elif x != 'y' or 'Y':
                exit()






