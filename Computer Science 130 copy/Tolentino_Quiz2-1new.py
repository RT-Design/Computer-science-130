print("Assignment: Quiz 2")
print("Programmer: Ryan Tolentino")

print("Problem #1")
def getGradesNoNegatives():
    grades=[]
    more=input("Would you like to start entering scores? (Y/N) ")
    while more.upper()=="Y" or (more.upper()=="YES"):
        score=int(input("What is the next score?"))
        if score<0:
            print("Error")
            more=input("Would you like to start entering scores? (Y/N) ")
        else:
            grades.append(score)
            more=input("Would you like to start entering scores? (Y/N) ")
    return grades
print("Input Initial Values")
results=getGradesNoNegatives()
print("Results:", results)

print("Problem #2")
def getGrades():
    grades=[]
    more=input("What is the next score?")
    while more!="":
        score1=int(more)*1.1
        grades.append(score1)
        more=input("What is the next score? ")
    return grades
print("Input Initial Values")
results=getGrades()
print("Results:",results)

print("Problem #3")
print('Input Initial Values')
print('Enter the sequence of names one in each line terminated by an empty string.')
def getNames():
    lst=[]
    names=input('Enter the name to add to the list(terminate by return key): ')
    lst.append(names)
    while names !="":

       names=input('Enter the name to add to the list(terminate by return key): ')
       lst.append(names)
       if names=='':
            return lst[0:-1]
    return lst[0:-1]
     

def shortestName(lst):
    shortestname=lst[-1]
    for name in lst:
        if len(shortestname)>len(name):
            shortestname=name
    return shortestname 

List = getNames()
print('Result: ')
print('The shortest name in', List,'is',shortestName(List))

print("Problem #4")
from cs1graphics import *
from time import sleep
scene = Canvas()
scene.setBackgroundColor('skyBlue')
N=10
Size=20
Position=Point(23,23)
ball2=Square(30,
Point(0,200))
ball2.setFillColor('red')
scene.add(ball2)
for n in range(N,0,-1):
    sleep(.15)
    ball2.move(20,-20)

print('Problem #5')
from cs1graphics import *
from time import sleep
scene = Canvas()
scene.setBackgroundColor('skyBlue')

N=10
Size=20
Position=Point(23,23)
ball2 = Circle(Size, Position)
ball2.setFillColor('red')
scene.add(ball2)
for n in range(N,0,-1):
    sleep(.20)
    ball2.move(35,35)

print('Problem #6')
from cs1graphics import *
from time import sleep
scene = Canvas()
scene.setBackgroundColor('skyBlue')

N=10
Size=20
Position=Point(23,23)
ball2 = Circle(Size, Position)
ball2.setFillColor('red')
scene.add(ball2)
for n in range(N,0,-1):
    sleep(.20)
    ball2.move(40,65)
