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


