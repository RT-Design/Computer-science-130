from cs1graphics import *
from time import sleep
## 
##      Test 3                           NAME_____Ryan Tolentino__________________                
##      CSC 130 Fall 2016
##      
##Create Python 2.7 programs using the Python Module 2.7 window and save them in one py file 
##Upload your  py file to the Canvas before end of class.
##I will send you answers then. 
##
##             PART Ch2 Lists and Strings
##Complete the Python programs:
##
##1. Complete the program below to replace the lowest score from 
## the list scores with the value in
##improvedScore. Your program should work with any other list
## of an length!

scores=[90,99,19,77]
improvedScore=95
print "Problem 1 initial values:    ", "scores are ", scores
scores.pop()
scores.insert(len(scores), improvedScore)
print "Problem 1 results:           ",  "scores after update  ", scores
print('')



##2. Create an empty list numbers. Populate the list with 
##this specific sequence of numbers   
##8, 7, 6, 5, 4, 3, 2, 1 , 2, 3, 4, 5, 6, 7, 8,
##using the range function and the extend 
##method. Print the list.

numbers = []
sequenceGenerated = range (8, 0, -1)
sequenceGenerated2 = range (0, 9, 1)
numbers.extend(sequenceGenerated)
numbers.extend(sequenceGenerated2)
print "Problem 6 results:           ", "numbers are ", numbers
print('')


##3. Assign a full name e.g. “Denny Czejdo”
##fullName. Split the full name  into first, and last 
##name. Display them in three separate lines. 
##(your program should work with any other name)

fullName = "Denny Czejdo"
print "Problem initial values:    ", "full name is ", fullName
names = fullName.split()
print "Problem  results:                 "
print "                             ", names[0]
print "                             ", names[1]
##print "                             ", names[2]
print('')




##4. Complete the program below.
##Insert the middle initial into the full name e.g. 
##for “Denny Czejdo” display  “Denny D. Czejdo”. 

fullName = "Denny Czejdo"
middleInitial = "D"

print "Problem 1 initial values:    ", "firstName is ", fullName
userName = fullName[:5]+' ' + middleInitial [:1]+' ' + fullName[5:12]
print "Problem 1 results:           ", "userName is ", userName
print('')



##5. Assign a full name e.g. “Denny D. Czejdo” to the 
##variable fullName.  Make the all characters of the 
##last name lowercase i.e. “Denny D. CZEJDO”. Display 
##the resulting name.

fullName = "Denny D. Czejdo"
print "Problem initial values:   ", "full name is ", fullName
names = fullName.split()
newLastName = names[2].upper()
print "Problem results:           ", "name is", names[0]+" ", names[1]+" "+newLastName
print('')





##         PART Ch4 Tracing Programs      
##

##6.

##listA = [8,4,2,0]
##for item  in listA:
##      if item != 0:
##           newItem = 8/item
##           print (newItem)
##Complete the Trace table.
##                 newItem (insert below the values of newItem in each cycle)
##Before   loop : -
##After Cycle 0 : 0
##After Cycle 1 : 1
##After Cycle 2 : 2
##After Cycle 3 : 4
##
##

##7.

##listA = [8,4,2,0]
##sum=0
##for item  in listA:
##   if item != 0:
##       sum=sum + 8/item
## 	 print(sum)
##print(sum)
##
##Complete the Trace table.
##                 sum (insert below the appropriate values for each cycle)
##Before   loop : -
##After Cycle 0 : 1
##After Cycle 1 : 3
##After Cycle 2 : 7
##After Cycle 3 : 7
##

##8

##listA = [2,4,16,0]
##for index in range(len(listA)-1):
##		specialValue = max(listA[index], listA[index+1]
##   		print(specialValue)
##
##Complete the Trace table.
##                 specialValue (insert below the appropriate values for each cycle)
##Before   loop -
##After Cycle 0 2
##After Cycle 1 4
##After Cycle 2 16
##

##
##              PART Ch 5.1
##
##9. Write a non-recursive function getGrades1() to input 
##John’s scores (e.g. 90, 70, 110) using an explicit prompt 
##YES/NO to continue. Replace any score
## above 100 by 100. i.e. for our example display 
##[99, 77, 100]. Assume the following interactions with the user:
## 
##Input Initial Values
##Would you like to start entering scores? (Y/N)Y
##What is the next score? 90
##Would you like to enter more grades? (Y/N)y
##What is the next score? 70
##Would you like to enter more grades? (Y/N)y
##What is the next score? 10
##Would you like to enter more grades? (Y/N)n
##Result: ['99', '77', '11']

print "PROBLEM 9"
def getGrades1():
    grades = []
    yesOrNo = raw_input("Would you like to start entering scores? (Y/N) ")
    while yesOrNo == "Y" or yesOrNo == "y":
        newGrade = raw_input("What is the next score? ")
        processedGrade = int(newGrade)*1.1 
        grades.append(processedGrade)
        yesOrNo = raw_input("Would you like to enter more grades? (Y/N) ")
    return grades    
print("Input Initial Values:")
grades=getGrades1()





##10. Write a non-recursive function getGrades2() to input 
##John’s scores (e.g. 90, 70, 10) terminated by a blank 
##as the list of integers. Skip all negative numbers 
##(display the WRONG SCORE TRY AGAIN  message). Replace any score
## above 100 by 100.
##Provide function call and print the list of scores 
##after after the modifications i.e. for our example 
##display [99, 77, 11]. Assume the following interactions 
##with the user:
## 
##Input Initial Values
##What is the next score? 99
##What is the next score? 70
##What is the next score? -10
##WRONG NUMBER TRY AGAIN
##What is the next score? 110
##What is the next score? 
##Result: ['99', '70', '100']

print("Problem #10:")
def getGradesNoNegative():
    gradestart=input("Would you like to start entering scores? (Y/N)")
    grade=int(input('Input score.'))
    gradeList=[]
    while gradestart.lower()=="y":
        if grade<0 or  grade> 100:
            print("WRONG NUMBER TRY AGAIN")
            gradeList.append(grade)
            gradeList.pop(-1)
        if gradestart.lower()!="y":
            break
        grade=int(input("What is the next score?"))
        gradeList.append(grade)
        gradestart=input("Would you like to enter more scores? (Y/N)")
    return gradeList
print("Result:" + str(getGradesNoNegative()))



##11. Write a recursive function getGradesAdjust() 
##to input sequence of John’s scores (e.g. 90 and 10) 
##terminated by an empty string. Replace any score
## above 100 by 100. Provide 
##function call and print the list of all entered 
##scores with the adjustment after the 
##function call had returned the results.
##
##Input Initial Values
##What is the next score? 90
##What is the next score? 110
##What is the next score? 
##Result: ['90', '100']

def getGradesAdjust():
    newGrade = raw_input("What is the next score? ")
    if newGrade != '':
        newGrade2 = raw_input("What is the next score? ")
        processedGrade = int(newGrade)
        remaining= getGradeAdjust()
        if newGrade >= 100:
            return 
            
        else:
            print('greater than 100 not allowed')
            return remaining
    else:
        return []

print("Input Initial Values:")
grades=getGradesAdjust()
print("Result:  ", grades)
print("-------------------------------------------")
print(" ")




##12. Write a  non-recursive function (use the for loop) to 
##place a ball in the middle of the Canvas and keep increasing
## it until covers al the Canvas. 
##Provide the appropriate function call.

print("Problem #12:")
print("Initial Value:")
def squareleftlowrightUp():
    paper=Canvas(800,800,"white","SquareMovement1")
    ball=Circle(100,Point(400,400))
    ball.setFillColor("purple")
    start=Button("Click this to Start!",Point(500,500))
    start.setWidth(1000)
    start.setFillColor('grey')
    paper.add(start)
    start.wait()
    paper.remove(start)
    paper.add(ball)
    for x in range(0,10):
        ball.move(60,0)
        ball.move(0,-60)
        sleep(0.18)
print("Result:Click \"Start\" on Other Window.")
squareleftlowrightUp()



##13. Write a  recursive function (use the for loop) to 
##place a square in the middle of the Canvas and keep increasing
## it until covers al the Canvas. 
##Provide the appropriate function call.



print("Problem #13:")

print("Write a  recursive function (use the for loop) to describe the ball movement taking into consideration the gravity  with the ball size decreasing when it gets closer to the edge. Provide the appropriate function call.")
print("Initial Value")
def ballGravity():
    paper=Canvas(1000,1000,"white","BallMovement1")
    ball=Square(100,Point(0,0))
    ball.setFillColor("purple")
    start=Button("Click this to Start!",Point(500,500))
    start.setWidth(1000)
    start.setFillColor('grey')
    paper.add(start)
    start.wait()
    paper.remove(start)
    paper.add(ball)
    y,count=50,0
    for x in range(0,21):
        if count>=20:
            y=-x
        ball.move(50,y)
        sleep(0.18)
        ball.scale(0.82)
        count+=1
print("Result:Click \"Start\" on Other Window.")
ballGravity()



##
##                     PART Ch 6.1
##
##Extend and modify the Television program menu and the class definition 
##to include method jumpPrevValume to jump back to the previous volume:
##uncomment myTV.jumpPrevValume() in order to test it
##
class Television:
    def __init__(self):
        self._powerOn = False
        self._muted = False
        self._volume = 5
        self._channel = 2
        self._prevChan = 2
    def __str__(self):
        return 'Power is On: '+str(self._powerOn)+'  Volume is :   '+str(self._volume)
		
#Clicking flips if on then off and off then on
    def togglePower(self):
        self._powerOn = not self._powerOn

#Clicking flips between muted and unmuted.
    def toggleMute(self):
        if self._powerOn:
            self._muted = not self._muted
#volume can range from 1 upto including 10
    def volumeUp(self):
        if self._powerOn:
            if self._volume < 10:
                self._volume += 1
            self._muted = False
            return self._volume #volume is #displayed on tv when it is changed. 
#channel increases by one and wraps back to 2
    def channelUp(self):
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 99:
                self._channel = 2
            else:
                self._channel += 1
            return self._channel
#Channel is set to number.
    def setChannel(self, number):
        if self._powerOn:
            if 2 <= number <= 99: 
                self._prevChan = self._channel
                self._channel = number
            return self._channel
#Flip to previous channel.
    def jumpPrevChannel(self):
        if self._powerOn:
            incoming = self._channel
            self._channel = self._prevChan
            self._prevChan = incoming
            return self._channel
myTV=Television()
myTV.togglePower()
myTV.volumeUp()

#myTV.jumpPrevValume()

print myTV
