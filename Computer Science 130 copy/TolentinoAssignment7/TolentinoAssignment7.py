from sys import argv

print('assignment: Assignment 2.1')
print('programmer: Denny Czejdo')
print('date: 8/16/2016')
print('Correct Answers')
print

print('Problem 0 - an example with solution')
print('Display the first character a first name e.g. "Denny" as "D"')
firstName ='Denny'
print 'Initial Value: ', firstName
firstLetter=firstName[0] # INSERTED HERE MISSING PART OF THE PROGRAM
print 'Result: ', firstLetter # INSERTED HERE MISSING PART OF THE PROGRAM 
print 

print('Problem 1')
print('Display a first name e.g "Denny" with a last name "Czejdo" in one line ')
print('with one blank between the first and the last name i.e. as "Denny Czejdo" ')
firstName='Denny'
lastName='Czejdo'
print 'Initial Value: ' , firstName 
print 'Initial Value: ' , lastName 
combinedName= firstName + ' ' + lastName# INSERT HERE MISSING PART OF THE PROGRAM
print 'Result: ' , combinedName
print 

print('Problem 2')
print('Display the first character of a first name e.g. "Denny" with a last name e.g "Czejdo"')
print('as "D. Czejdo"')
firstName='Denny'
lastName='Czejdo'
print 'Initial Value: ' , firstName 
print 'Initial Value: ' , lastName 
firstLetter=firstName[0]# INSERT HERE MISSING PART OF THE PROGRAM
combinedName=firstLetter+'.'+' ' +lastName
print 'Result: ' , combinedName
print 

print('Problem 3')
print('Check if the length of a first name e.g. ‘Denny’ is the same as a last name e.g. ‘Czejdo’ ')
##firstName='Denny'
##lastName='Czejdo'
isItTrue = False
f = open('myFile1.txt', 'r+')

line1 = raw_input("Line 1:")
f.write(line1)
f.write("\n")
line2 = raw_input("Line 2:")
f.write(line2)
f.write("\n")
line3 = raw_input("Line 3:")
f.write(line3)
f.write("\n")

print line1
print line2
print line3
f.close
print 'Initial Value: ' , firstName 
print 'Initial Value: ' , lastName

if len(firstName) == len(lastName):
                         isItTrue= True
print 'Result: ' , isItTrue  
print 

print('Problem 4')
print('A list of John’s scores is given e.g. 99, 77, 19, and 100.') 
print('John took a next quiz and got a score e.g. 98. Update the list.')
scores = [99,77,19,100]
newScore = 98
print 'Initial Value: ' , newScore 
print 'Initial Value: ' , scores
# INSERT HERE MISSING PART OF THE PROGRAM
scores.append(newScore)
print 'Result: ' , scores
print

print('Problem 5')
print('A list of John’s scores is given e.g. 99, 77, 19,  100 and 98.')
print('John took a makeup quiz to replace the third score i.e. the score with index 2,')
print('and got a new score e.g. 90. Update the list.')
scores=[99,77,19,100,98]
scoreIndex= 2
newScore = 90
print 'Initial Value: ' , scores
print 'Initial Value: ' , scoreIndex 
print 'Initial Value: ' , newScore 
# INSERT HERE MISSING PART OF THE PROGRAM
print 'Result: ' 
print




