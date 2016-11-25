from cs1graphics import *
from time import sleep
print('Programmer: Ryan Tolentino')
print('Date: 9/20/16')
print('Assignemnt: Quiz 2 preperation')
print('Problem 1')
print('Write a non-recursive function getGrades() to input John’s scores (e.g. 90, 70, 10) as the list of integers [99, 77, 19]. Provide function call and print the list of all entered scores increased by 10')
      
def getGrades():
    grades = [ ]
    more = input('Would you like to start entering scores? (Y/N)')
    while (more.upper() == 'Y') or (more.upper() == 'YES'):
        score = input('What is the next score? ')
        grades.append(int(score)*1.1)
        more = input('Would you like to enter more grades? (Y/N)')
    return grades
print('Input Initial Values')
results = getGrades()
print('Results:',results)

print('Complete')

print('Problem 2')
def getGrades():
    grade=input("Input Initial Values: ")
    if grade=="":
        
        return []
    else:
        head=list()
        print(head)
        head.append(int(grade))
        rest=getGrades()
        return head + rest
print("Result: the list of all John's scores is", getGrades())
print('End')


print('Problem 3')
print('Input Initial Values')
score=[]
again=input('Would you like to start entering scores? (Y/N)')
def getGradesNoNegatives():
    again= 'y'
    score=[]
    while again == 'y' or again =='Y':
        grade=int(input('What is the next score? '))
        
        if grade < 1:
            print('WRONG NUMBER TRY AGAIN')
            
        else:
            
            score.append(grade+(grade*.1))
        again=input('Would you like to enter more grades? (Y/N)')
    return score
             
 
print("Result: ", getGradesNoNegatives())
print("Problem #4")
def getGradesNoNegatives():
    grades=[]
    more=input("Would you like to start entering scores? (Y/N) ")
    while more=="":
        score=int(input("What is the next score?"))
        if score<0:
            print("Error")
        else:
            score1=(score*.01)
            grades.append(score1)
            more=input("Would you like to start entering scores? (Y/N) ")
    return grades
print("Input Initial Values")
results=getGradesNoNegatives()
print("Results:", results)
          

print('Problem Number 5')

print('Input Initial Values')
print('Enter the sequence of names one in each line terminated by an empty string.')
def getNames():
    lst=[]
    names= input('Enter the name to add to the list(terminate by return key): ')
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
        if len(shortestname)> len(name):
            shortestname=name
    return shortestname 

List = getNames()
print('Result: ')
print('The shortest name in', List,'is',shortestName(List))





#6
print('Problem 6')
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
    ball2.scale(.75)
    ball2.move(20,1)

#7
print('Problem 7')
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
    ball2.scale(.75)
    ball2.move(20,1)

#Problem *
print('Problem 8')
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
    ball2.scale(.75)
    ball2.move(10,12)
    



