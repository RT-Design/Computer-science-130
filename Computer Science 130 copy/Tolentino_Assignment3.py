print('\nProgrammer: Ryan Tolentino\n')
print('\nAssignment 3\n')
print('\n9/16/16\n')



print('\nGet grades\n')

def getGrades():
    grade=input("Enter score:")
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

print('\nGet no zeros\n')
def getGradesNoZeros():
    grade=input("Enter score: ")
    if grade=="" or grade=="0":
        return []
    else:
        head=list()
        head.append(int(grade))
        rest=getGradesNoZeros()
        return head+rest
print("Input John's scores")
print("Result: the list of all John's scores is", getGradesNoZeros())       

print('End')
print('\nGet names\n')

def GetNames():
    name=input("Enter names:")
    if name=="":
        return []
    else:
        head=list()
        head.append(name)
        rest=GetNames()
        return head+rest
print("Input names")
print("Result: the list of all names is", GetNames())
    
print('End')
print('\nCountA = \n')


def countA():

    rest=countAß()
    return head+rest
    print(rest)



print('End')
print('\nNext letter in alphabet\n')

def isAlphabetic(current_string, previous_character = ""):
    if current_string == "":
        return True         
    if previous_character and previous_character > current_string[0]:
        return False        
    return isAlphabetic(current_string[1:], current_string[0]) 

