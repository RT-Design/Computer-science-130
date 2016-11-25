print('assignment: Take Home Quiz 1B')
print('programmer: Ryan Tolentino')
print('date: 9/1/2016\n')

print('Problem 1')
for i in range(1,129):
    print('Number:',i)
    
print('complete\n')
print('Problem 2')
print('Result:', range(10,2,-2)+ range(2,11,2))

print('complete\n')
print('Problem 3')
sum=0
listA=[-1,9,5,-10,9]
for i in range(len(listA)-1):
    sum+=listA[i]
avg=sum/len(listA)
for n in range(len(listA)-1):
    if listA[n]<=avg:
        print('Smaller:' ,listA[n])

print('complete\n')       
print('Problem 4')
Item=0
aList=['A', 'b', 'c', 'D']

for i in range(len(aList)):
    if aList[i].islower()==True:
        Item+=1
        
print(Item)

print('complete\n')

print('Problem 5')
aList=['A', 'b', 'c', 'D']
for i in range(len(aList)-1):
    aList.insert(i+1,aList[i].upper())
    aList.pop(i)
print(aList)

print('complete\n')

print('Problem 6')
occur=0
listA=[-1, 9, 9, 5, -10, 9]
for i in range(len(listA)-1):
    if occur!=2 and listA[i]==9:
        listA.pop(i)
        occur+=1
print(listA)

print('complete\n')

print('Problem 7')

oldList=[1, 3, 3, 5, 7]
newlist= []
toohigh = []
for VARIABLE in oldList:
    if VARIABLE < 4:
        newlist.append(VARIABLE)
    else:
        toohigh.append(VARIABLE)
print('Result:',newlist)

print('complete\n')


print('Problem 8 EXTRA CREDIT')


csc130= [9, 29, 77, 19]

phil100=[99, 97, 100, 98]

csc130.extend(phil100)


newlist = []

for VARIABLE in csc130:
    csc = csc130.pop(0)
    newlist.append(csc)
    phil = phil100.pop(0)
    newlist.append(phil)
       
print('Result:',newlist)
    



