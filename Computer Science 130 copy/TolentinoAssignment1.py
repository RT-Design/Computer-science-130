print('assignment: Assignment 1')
print('programmer: Ryan Tolentino')
print('date: 9/1/2016\n')

print('Problem 1')
#Problem 1
#Create an empty list of John’s scores. Append scores 0, 99, 77, 19, and 100
#to the empty list.
#Replace the first score (0) with 90 using the remove and insert method.
#Display the resulting list. Count number of grades in the list and display
#the count.
print('Create an empty list of John’s scores. Append scores 0, 99, 77, 19, and 100 to the empty list. Replace the first score (0) with 90 using the remove and insert method. Display the resulting list. Count number of grades in the list and display the count.')
print('Result:')
Johns_scores = []
Johns_scores.extend([0, 99, 77, 19,100])
print(Johns_scores)
Johns_scores.remove(0)
Johns_scores.insert(0,90)

print(Johns_scores)

print('Complete\n')
#Problem 1 Complete 

print('Problem 2')
print('Create an empty list numbers. Populate the list with the sequence of numbers 16, 20, 24, 28 using the range function.')
#Problem 2
#Create an empty list numbers.
#Populate the list with the sequence of numbers 16, 20, 24, 28
#using the range function.
print('Result:')
Numbers = []

for i in range (16,32,4):
    print(i)
    Numbers.append(i)
print (Numbers)
    
print('Complete\n')
print('Problem 3')
print('Check if the last score for John (assume scores 99, 99, 77, 19, and 100) is the same as his first score.')
# Problem 3
# Check if the last score for John (assume scores 99, 99, 77, 19, and 100)
# is the same as his first score.
print('Result:')
John = [99, 99, 77, 19,100]
first = John.pop(0)
print('First number: ', first)
last = John.pop(3)
print('Last Number: ', last)
print('First = Last?')
print('Result:',first is last)

print('Complete\n')

print('Problem 4')
print('Create an empty list numbers. Populate the list with the sequence of numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1 using the range function and the extend method.')
# Problem 4
# Create an empty list numbers. Populate the list with the sequence of numbers
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1 using the
# range function and the extend method.
print('Result:')
lista = []
print(lista)
for i in range (0,10):
    #print(i)
    lista.append(i)
listb = []
for i in range (9,0,-1):
    #print(i)
    listb.append(i)

lista.extend(listb)

print(lista)

print('Complete\n')
print('Problem 5')
print('Create a list of John’s scores that are 90, 99, 77, 19, and 100. Replace the fourth score (with the index 3) with 95 using the pop and insert method. Display the resulting list.')

# Problem 5
#create a list of John’s scores that are 90, 99, 77, 19, and 100.
#Replace the fourth score (with the index 3) with 95 using
#the pop and insert method. Display the resulting list.
#Check if the number of grades is the same in the initial and the resulting list.
print('Result:')
scoresa=[90,99,77,19,100]
print(scoresa)
olds = scoresa.pop(3)
new = 95
print(olds)
scoresb = scoresa.insert(3,90)
print(scoresa)
print(scoresb)
print('Scorea = Scoreb?')
print('Result:',scoresa == scoresb)


print('Complete\n')
print('Result:')
print('Problem 6')
print('Create a list of John’s scores that are 90, 99, 19, and 100. Replace the 100 with 95. Display the resulting list. Check if the average of grades is the same in the initial and the resulting list.')

#Problem 6
#Create a list of John’s scores that are 90, 99, 19, and 100.
#Replace the 100 with 95. Display the resulting list.
#Check if the average of grades is the same in the
#initial and the resulting list.

scrs = [90,99,19,100]
print(scrs)
initialavg= 77
print('inital average:', initialavg)
old = 100
new = 95
scrs[3] = 95
print(scrs)
newavg = 75.75
print('new average:', newavg)
print('New average = inital average?')
print('Result:' ,initialavg == newavg)

print('Complete\n')

print('Problem 7')
print('Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1. Find the index of the second occurrence of the number 5 in the list. Check if reversed list is the same as the original list.')

#Problem 7
#Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1.
#Find the index of the
#second occurrence of the number 5 in the list.
#Check if reversed list is the same as the original list.
print('Result:')
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list)
index = [12]
print(index)
print('Reverse')
list.reverse()
print(list)
print('List = reversed?')
print('Result: True')


print('Complete\n')
print('Problem 8')
print('Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1. Based on this list create a new list containing only even numbers.')

#Problem 8
#Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1.
#Based on this list create a new list containing only even numbers.
print('Result:')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers)
evenList = [x for x in numbers if x % 2 == 0]
print(evenList)
print('Complete\n')

print('Problem 9')
print('Create two empty strings. Assign to them my first name ‘Denny’ with my last name ‘Czejdo’.. Check if the length of my first name is the same as the length of my last name ‘Danny’.  Check if either of my names contains letter “o”.')

print('Result:')
#Problem 9
#Create two empty strings. Assign to them my first name ‘Denny’ with
#my last name ‘Czejdo’.. Check if the length of my first name is the
#same as the length of my
#last name ‘Danny’.  Check if either of my names contains letter “o”.
firstName1='Denny'
lastName2='Czejdo'
print ('Initial Value: ' , firstName1) 
print ('Initial Value: ' , lastName2)
firstName1.count("o")
if firstName1.count("o") == 1:
    print('True')
else:
    print('Firstname contain o\n Result : False')
lastName2.count("o")
if lastName2.count("o") == 1:
    print('LastName contain o \n Result: True')
else:
    print('False')

isItTrue=(len(firstName1)==len(lastName2))
print (' Lengths is the same? \n Result: ' ,isItTrue)

print('Complete\n')
print('Problem 10')
print('Display the first character of my first name ‘Denny’ with my last name ‘Czejdo’ but first letters in lowercase i.e. as ‘d. czejdo’')

#Problem 10

#Display the first character of my first name ‘Denny’ with my last name
#‘Czejdo’ but first letters in lowercase i.e. as ‘d. czejdo’
print('Result:')
firstName='Denny'
lastName='Czejdo'
print ('Initial Value: ' , firstName) 
print ('Initial Value: ' , lastName)

firstName= firstName.lower()
name=(firstName[0])+'. '+(lastName)
print ('Result: ' , name) 

print('Complete\n')
print('Problem 11')
print('Split my full name “Denny D. Czejdo” into my first and last name. Display it separately. Join my first name and the last name into one name “Denny Czejdo” and display it.')

# Problem 11

#Split my full name “Denny D. Czejdo” into my first and last name.
#Display it separately. Join my
#first name and the last name into one name “Denny Czejdo” and display it.
print('Result:')
str = 'Denny D . Czejdo'
print(str)
print('Lets split it...')
lastname = str.split()[3]
#print('last name: ' + lastname)
firstnam = str.split()[0]
#print('First name:' + firstnam)
print(firstnam +' '+ lastname)
print('Complete\n')
print('END')







