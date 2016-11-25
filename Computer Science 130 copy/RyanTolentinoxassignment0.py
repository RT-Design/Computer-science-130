#Ryan Tolentino
#8-18-2016
#Assignment 0 

print('assignment: Assignment 0')
print('programmer: Ryan Tolentino')
print('date: 8/16/2016')
print('Correct Answers')

print('Problem 1')
print('Check if the first character of my first name "Denny" is the same as') 
print('the first character of your name "Ryan"')

firstName1 ='Denny'
firstName2 ='Ryan'
print ('Initial Value: ' , firstName1)
print ('Initial Value: ' , firstName2)

isItTrue=(firstName1[0]==firstName2[0])
print ('Result: ' , isItTrue)

print('Problem 2')
print('Display my first name "Ryan" with my last name "Tolentino" i.e. as "Ryan Tolentino" ')

firstName='Ryan'
lastName='Tolentino'
print ('Initial Value: ' , firstName) 
print ('Initial Value: ' , lastName)

name=(firstName+' '+lastName)
print ('Result: ' , name) 

print('Problem 3')
print('Display the first character of my first name "Ryan" with my last name "Tolentino" i.e. as "D. Czejdo" initial and the last name')

firstName='Ryan'
lastName='Tolentino'
print ('Initial Value: ' , firstName) 
print ('Initial Value: ' , lastName)

name=(firstName[0]+'. '+lastName)
print ('Result: ' , name )

print('Problem 4')
print('Check if the length of my first name ‘Denny’ is the same as the length of your name ‘Ryan’ ')

firstName='Denny'
lastName='Ryan'
print ('Initial Value: ' , firstName) 
print ('Initial Value: ' , lastName)

isItTrue=(len(firstName1)==len(firstName2))
print ('Result: ' ,isItTrue )

print('Problem 5')
print('Display your age next year assuming that you are now twenty years old ')

currentAge=20
print ('Initial Value: ' , currentAge)

futureAge=currentAge+1
print ('Result: ' , futureAge) 


print('Problem 6')
print('Create a list of John’s scores that are 99, 77, 19, 80, and 100. John took a next test and got 98. ')
print('Update the list.')

scores=[99,77,19,80,100]
score1=98
print ('Initial Value: ' , scores )
print ('Initial Value: ' , score1)

scores.append(score1)
print ('Result: ' , scores)

print('Problem 7')
print('Create a list of John’s scores that are 99, 77, 19, 80, 100 and 98.')
print('John took a makeup for third quiz and got 90. Update the list.')

scores=[99,77,19,80,100,98]
score2=80
print ('Initial Value: ' , scores)
print ('Initial Value: ' , score2)

scores[2]=score2
print ('Result: ' , scores)
