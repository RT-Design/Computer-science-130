##      Test 3   Practice                        NAME_______________________                
##      CSC 130 Fall 2016
##
##Create Python 2.7 programs using the Python Module 2.7 window and save them in one py file 
##Upload your  py file to the Canvas before Monday noon for any credit.
##I will send you answers then. 
##
##             PART Ch2 Lists and Strings
##Complete the Python programs. DO NOT USE SPECIFIC EXAMPLE VALUES. 
##ASSUME ANY CONTENT OF THE VARIABLES :
##
##1. Complete the program below to create and print the username 
##constructed from first three letters of the assigned first name 
##e.g.  ‘Denny’ and two letters from the assigned last name e.g. 
##‘Czejdo’ as ‘DenCz’
 
firstName='Denny'
lastName='Czejdo'



##2. Complete the program below to compute and display the previous  
##uppercase character in the alphabet for the assigned character to 
##the variable ch  (assume that ‘A’ is not assigned to ch)

ch='D'



##3. Complete the program below to replace the last score with 
##improvedScore  using the pop and insert method, and print the 
##new list.

##scores=[90,99,77,19]
##improvedScore=95



##4. Complete the program below to replace the oldScore with 
##improvedScore  using the remove and insert method, and 
##print the new list.

scores=[90,99,77,19]
oldScore=19
improvedScore=95



##5. Complete the program below to remove the largest and 
##the smallest  elements from the list, and 
##print the new list.

numbers = [-1, 9, 5, -10, 9]




##6. Create an empty list numbers. Populate the list with 
##the sequence of numbers  12, 16, 20, 24, 28 using the 
##range function. Print the list.




##7. Create an empty list numbers. Populate the list with 
##the sequence of numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 
##6, 5, 4, 3, 2, 1 using the range function and the extend 
##method. Print the list.




##8. Assign a full name e.g. “Denny D. Czejdo” to the variable 
##fullName. Split the full name  into first, middle and last 
##name. Display them in three separate lines. 




##9. Assign a full name e.g. “Denny D. Czejdo” to the variable 
##fullName.  Remove the middle initial from the full name e.g. 
##for “Denny D. Czejdo” display  “Denny Czejdo”. 




##10. Create a list of John’s scores in the variable scores 
##(e.g. 0, 99, 77, 19, and 100). Display the resulting list. 
##Count number of grades in the list and display the count.




##11. Create a list of John’s scores in the variable scores  
##(e.g. 0, 99, 77, 19, and 100). Display the resulting list. 
##Check if the last score for John is the same as his first 
##score. Display YES or NO.




##12. Create a list of John’s scores in the variable scores 
##(e.g. 0, 99, 77, 19, and 100). Display the resulting list. 
##Compute and display the average of the grades.




##13. Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 
##7, 6, 5, 4, 3, 2, 1 using range function. Find the index 
##of the second occurrence of the number 1 in any example 
##of such list. 




##14. Assign a full name e.g. “Denny D. Czejdo” to the 
##variable fullName. Check if the length of the first 
##name is the same as the length of the 
##last name. Display YES or NO.




##15. Assign a full name e.g. “Denny D. Czejdo” to the 
##variable fullName.  Check if either of the names contains 
##letter “o”. Display YES or NO.




##16. Assign a full name e.g. “Denny D. Czejdo” to the 
##variable fullName.  Make the first character of the 
##last name lowercase e.g. “Denny D. czejdo”. Display 
##the resulting name.





##         PART Ch4 Tracing Programs      
##          
##Consider different programs below
##and complete the trace table:
## 
##1. Simple Independent Item processing
##listA = [1,2,1,1]
##for item  in listA:
##            print (item,  item +2 )
##
##Complete the Trace table.
##                 item (insert below the values of item in each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3


##2. Conditional Independent Item processing
##listA = [1,2,1,1]
##for item  in listA:
##              if item == 1:
##                              print( item -1)
##
##Complete the Trace table.
##                 item (insert below the values of item in each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3
##
##
##3. Simple Counting
##
##listA = [1,2,1,1]
##count=0
##for item  in listA:
##            count=count+1
##            print(count)
##print(count)
##
##Complete the Trace table.
##                 count (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3
##
##4. Conditional Counting
##listA = [1,2,1,1]
##count=0
##for item  in listA:
##      print item
##      if item >1:
##        count=count+1
##print(count)
##
##Complete the Trace table.
##                 count (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3
##
##5. Simple Aggregation
##listA = [1,2,3,1]
##sum=0
##for item in listA:
##     sum=sum + item*item
##print(sum)
##
##Complete the Trace table.
##                 sum (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3
##
##6. Conditional Aggregation
##listA = [1,2,0,1]
##sum=0
##for item  in listA:
##  	 if item != 0:
##        	sum=sum + item+1
## 	 print(sum)
##print(sum)
##
##Complete the Trace table.
##                 sum (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##After Cycle 3
##
##7. Current & Next Item processing + Simple Processing
##listA = [2,4,16,0]
##for index in range(len(listA)-1):
##		specialValue = (listA[index] + listA[index+1])/2
##   		print(specialValue)
##
##Complete the Trace table.
##                 specialValue (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##
##8. Current & Next Item processing + Conditional  
##
##listA = [2, 8, 6, 10]
##sorted = True
##for i in range(len(listA)-1):
##        if listA[i] > listA [i+1]:
##                sorted = False
##        print (sorted)
##print (sorted)
##
##Complete the Trace table.
##                 sorted (insert below the appropriate values for each cycle)
##Before   loop
##After Cycle 0
##After Cycle 1
##After Cycle 2
##
##              PART Ch 5.1
##
##1. Write a non-recursive function getGrades1() to input 
##John’s scores (e.g. 90, 70, 10) using an explicit prompt 
##YES/NO to continue. Increase all entered scores by 10%. 
##Provide function call and print the list of scores after 
##they were increased by 10% i.e. for our example display 
##[99, 77, 11]. Assume the following interactions with the user:
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




##2. Write a non-recursive function getGrades2() to input 
##John’s scores (e.g. 90, 70, 10) terminated by a blank 
##as the list of integers. Increase all entered scores by 
##10%.  Provide function call and print the list of scores 
##after they were increased by 10% i.e. for our example 
##display [99, 77, 11]. Assume the following interactions 
##with the user:
## 
##Input Initial Values
##What is the next score? 90
##What is the next score? 70
##What is the next score? 10
##What is the next score? 
##Result: ['99', '77', '11'] 




##3. Write a recursive function getGradesNoNegatives() to 
##input John’s scores (e.g. 90 and 10) using explicit 
##prompt YES/NO to continue. Skip all negative numbers 
##(display the WRONG SCORE TRY AGAIN  message). Provide 
##function call and print the list of all entered scores 
##(except negative numbers!!!) after the function call 
##had returned the results. Assume the following interactions 
##with the user:
##
##Input Initial Values
##Would you like to start entering scores? (Y/N)Y
##What is the next score? 90
##Would you like to enter more grades? (Y/N)y
##What is the next score? -70
##WRONG NUMBER TRY AGAIN
##Would you like to enter more grades? (Y/N)y
##What is the next score? 10
##Would you like to enter more grades? (Y/N)n
##Result: ['90', '10'] 




##4. Write a recursive function getGradesNoNegatives() 
##to input sequence of John’s scores (e.g. 90 and 10) 
##terminated by an empty string but skipping all 
##negative numbers (print error message). Provide 
##function call and print the list of all entered 
##scores (except negative numbers!!!) after the 
##function call had returned the results.
##
##Input Initial Values
##What is the next score? 90
##What is the next score? -70
##WRONG NUMBER TRY AGAIN
##What is the next score? 10
##What is the next score? 
##Result: ['90', '10'] 




##5. Write two non-recursive functions: (a)  getNames() to 
##input names according to the below interactions with the 
##user; (b)  shortestName (aList) to accept a list of names 
##while calling it and find the shortest name. In the main 
##program provide the appropriate function calls and print 
##the longest name.
##
##Input Initial Values 
##Enter the sequence of names one in each line terminated by an empty string   
##Enter the name to add to the list (terminate by return key): Jo
##Enter the item to add to the list (terminate by return key):  Mary
##Enter the item to add to the list (terminate by return key):  Li
##Enter the item to add to the list (terminate by return key):  
##Result:
##The shortest name in ['Jo', 'Mary', 'Li'] is ‘Jo’




##6. Write a  non-recursive function (use the for loop) to 
##describe the ball movement along the straight line with 
##the ball size decreasing when it gets closer to the edge. 
##Provide the appropriate function call.




##7. Write a  recursive function (use the for loop) to 
##describe the ball movement along the straight line with 
##the ball size decreasing when it gets closer to the edge. 
##Provide the appropriate function call.



##
##                     PART Ch 6.1
##
##Modify the Television program menu and the class definition 
##to reflect the following changes:
##a) Volume is changed only by the dial control
##b) There is one favorite channel there can be set by a dial 
##c) Channel can be changed also by
##ChannelDoubleUP  and ChannelDoubleDown controls
##d) Channel can be changed also by
##ChannelFavorite  control
##
class Television:
    def __init__(self):
        self._powerOn = False
        self._muted = False
        self._volume = 5
        self._channel = 2
        self._prevChan = 2
    def __str__(self):
        return 'Power is On: '+str(self._powerOn)+'  Muted is :   '+str(self._muted)
		
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
print myTV
