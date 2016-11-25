## 
##      Test 3                           NAME______Justin Crumpler python 2.7_________________                
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
print('Problem 1')
scores=[90,99,19,77]
improvedScore=95
print('Old:',scores)
x = 0
y = 'go'
for i in scores:
    if i == min(scores) and y == 'go':
        scores[x] = improvedScore
        y = 'stop'
    x = x+1
print('New:',scores)
print('Complete\n')


##2. Create an empty list numbers. Populate the list with 
##this specific sequence of numbers   
##8, 7, 6, 5, 4, 3, 2, 1 , 2, 3, 4, 5, 6, 7, 8,
##using the range function and the extend 
##method. Print the list.
print('Problem 2')
numbers = []
sequenceDecreasing = range (8, 0, -1)
sequenceIncreasing = range (2, 9)
numbers.extend(sequenceDecreasing)
numbers.extend(sequenceIncreasing)
print(numbers)
print('Complete\n')



##3. Assign a full name e.g. “Denny Czejdo”
##fullName. Split the full name  into first, and last 
##name. Display them in three separate lines. 
##(your program should work with any other name)
print('Problem 3')
fullName = "Denny D. Czejdo"
print ("Problem 3 initial values:    "), "full name is ", fullName
names = fullName.split()
print( "Problem 3 results:                 ")
print( "                             "), names[0]
print ("                             "), names[1][0]
print( "                             "), names[2]
print('')

print('Complete\n')




##4. Complete the program below.
##Insert the middle initial into the full name e.g. 
##for “Denny Czejdo” display  “Denny D. Czejdo”. 
print('Problem 4')
fullName = "Denny Czejdo"
middleInit = 'D.'
print fullName
names = fullName.split()
newName = []
newName.insert(0,names[0])
newName.insert(1,middleInit)
newName.insert(2,names[1])
newName
print newName

print('Complete\n')





##5. Assign a full name e.g. “Denny D. Czejdo” to the 
##variable fullName.  Make the all characters of the 
##last name lowercase i.e. “Denny D. CZEJDO”. Display 
##the resulting name.
print('Problem 5')
print('Result:')
firstName='Denny'
lastName='Czejdo'
print ('Initial Value: ' , firstName) 
print ('Initial Value: ' , lastName)

lastName= lastName.lower()
name=(firstName[0])+'. '+(lastName)
print ('Result: ' , name) 

print('Complete\n')





##         PART Ch4 Tracing Programs      
##

##1.

##listA = [8,4,2,0]
##for item  in listA:
##      if item != 0:
##           newItem = 8/item
##           print (newItem)
##Complete the Trace table.
##                 newItem (insert below the values of newItem in each cycle)
##Before   loop
##After Cycle 0       1
##After Cycle 1       1
##After Cycle 2       4
##After Cycle 3       4
##
##

##2.

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
##Before   loop       -
##After Cycle 0       1
##After Cycle 1       3
##After Cycle 2       7
##After Cycle 3       7
##

##3

##listA = [2,4,16,0]
##for index in range(len(listA)-1):
##		specialValue = max(listA[index], listA[index+1]
##   		print(specialValue)
##
##Complete the Trace table.
##                 specialValue (insert below the appropriate values for each cycle)
##Before   loop       
##After Cycle 0       4
##After Cycle 1       16
##After Cycle 2       16
##

##
##              PART Ch 5.1
##
##1. Write a non-recursive function getGrades1() to input 
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
def getGrades1():
    grades = []
    yesOrNo = raw_input("Would you like to start entering scores? (Y/N) ")
    while yesOrNo == "Y" or yesOrNo == "y":
        newGrade = raw_input("What is the next score? ")
        if int(newGrade) > 100:
            processedGrade = 100
        else:
            processedGrade = int(newGrade)*1.1
        grades.append(int(processedGrade))
        yesOrNo = raw_input("Would you like to enter more grades? (Y/N) ")
    return grades    
print("Input Initial Values:")
grades=getGrades1()

print("Processing by adding 10% and max 100")
print("Result:  ", grades)
print('Complete')




##2. Write a non-recursive function getGrades2() to input 
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
def getGrades1():
    grades = []
    newGrade = raw_input("What is the next score? ")
    while newGrade != "":
        if int(newGrade) > 100:
            newGrade = 100
        if int(newGrade) < 0:
            print('Worng number, Retry')
        else:
            processedGrade = newGrade
            grades.append(processedGrade)
        newGrade = raw_input("What is the next score? ")
    return grades    
print("Input Initial Values:")
grades=getGrades1()

print("Processing by adding 10%")
print("Result:  ", grades)

print('Complete')




##3. Write a recursive function getGradesAdjust() 
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
    newScore = raw_input("What is the next score? ")
    if newScore != "":
        if int(newScore) > 100:
            newScore = 100
        processedScore = int(newScore)       
        remaining = getGradesAdjust()
        return [processedScore] + remaining
    else:
        return []   

print("Input Initial Values:")
grades=getGradesAdjust()
print("Processing grades, replacing grades > 100 with 100")
print("Result:  ", grades)

print('Complete')
 


##4. Write a  non-recursive function (use the for loop) to 
##place a ball in the middle of the Canvas and keep increasing
## it until covers al the Canvas. 
##Provide the appropriate function call.
scene = Canvas()
scene.setBackgroundColor('skyBlue')

N=10
Size=20
Position=Point(23,23)
ball2 = Circle(Size, Position)
ball2.setFillColor('red')
scene.add(ball2)
for n in range(N,0,1):
    sleep(.20)
    ball2.scale(.75)
    ball2.move(20,1)

print('Complete')




##5. Write a  recursive function (use the for loop) to 
##place a square in the middle of the Canvas and keep increasing
## it until covers al the Canvas. 
##Provide the appropriate function call.
scene = Canvas()
scene.setBackgroundColor('skyBlue')

N=10
Size=20
square2 = Circle(Size, Position)
square2.setFillColor('green')
scene.add(ball2)
for n in range(N,0,1):
    sleep(.20)
    square2.scale(.75)
    square2.move(20,1)

print('Complete')




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
        self._prevVol = 5
    def __str__(self):
        return 'Power is On: '+str(self._powerOn)+'  Volume is :   '+str(self._volume)+'  Previous Volume is :   '+str(self._prevVol)
		
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
                self._prevVol = self._volume
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

#Previous volume.
    def jumpPrevVolume(self):
       if self._powerOn:
           tempVol = self._volume
           self._volume = self._prevVol
           self._prevVol = tempVol
           return self._volume
        
myTV=Television()
myTV.togglePower()
myTV.volumeUp()
print myTV
myTV.jumpPrevVolume()
print myTV
