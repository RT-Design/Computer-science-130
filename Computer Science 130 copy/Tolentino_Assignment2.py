print('Assignment 2\n')
print('Ryan Tolentino\n')
print('9/6/2016\n')

print('Problem 1\n')

print('Assume that the requirements for the username are to have first two letters followed by a sequence of 4 digits. Check if the given usernames JD1234 and J12345 are correct usernames.')
username1 = 'JD1234'

username2 = 'J12345'

print('initial value:',username1)
print('initial value',username2)

if username1[:2].isalpha() and username1[3:].isdigit():
    print ('Username 1 is True')
if username2[:2].isalpha() and username2[3:].isdigit():
    print ('user name 2 is True')

print('Complete\n')
print('Problem 2\n')

print('Write a coding program to code a three letter string into another string with each letter converted to the next letter in the\n alphabetical order e.g. converting “cat” into “dbu”')
str1='cat'
split1=''
for k in str1:
    k=ord(k)
    k+=1
    k=chr(k)
    split1 = split1 +str(k)
    
print('\n',split1)

print('Complete\n')
print('Problem 3\n')

print('Write a decoding program for problem 2 i.e. e.g. converting dbu” into “cat”.')
str1='dbu'
split1=''
for k in str1:
    k=ord(k)
    k-=1
    k=chr(k)
    split1 = split1 + str(k)
    
print('\n',split1)
    
print('Complete\n')
print('Problem 4\n')

print('Convert the string representing the birthday in the format mm-dd-yyyy into an European format with only two digits for the\n year dd-mm-yy i.e. convert “05-19-1971” into “19-05-71”.')
america= '05-19-1971'
euro=america[3:6] + america[0:3] + america[8:10]
print(euro)

print('Complete\n')
print('Problem 5\n')

print('Convert the string representing the birthday in the European format with only two digits for the year dd-mm-yy into format\n mm-dd-yyyy i.e. convert “19-05-71” back into “05-19-1971”.')
european = '19-05-71'
merica = european[3:6] + european[0:3] + '19' + european[6:8]
print(merica)

print('Complete\n')
print('Problem 6\n')

print('Create an empty list. Populate the list with the sequence of numbers 5, 7, 9, …, 111, 113 using the range function.')
listA=list(range(5,115,2))
print(listA)


print('Complete\n')
print('Problem 7\n')

print('Check if the last score for John (assume scores 98, 77,99, and 100) is the same as his first score.')
score=[98,77,99,100]
if score[0] == score[-1]:
    print('True')
else:
    print('False')

print('Complete\n')
print('Problem 8\n')

print('Create an empty list. Populate the list with the sequence of numbers 1, 2, 3, 4, …, 18, 19, 18, 17, …, 4, 3, 2, 1 using the range\n function and the extend method.')
listB=list(range(1,20,1))
listB.extend(list(range(18,0,-1)))

print(listB)

print('Complete\n')
print('Problem 9\n')

print('Create the list numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1. Based on this list create a new list containing only odd numbers.')
listC=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

listD=[]
for i in listC:
    if i % 2 == 1:
        listD.append(i)
print(listD)

print('Complete\n')


