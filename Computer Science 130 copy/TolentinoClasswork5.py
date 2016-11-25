print('Programmer: Ryan Tolentino')
print('Assignment Classwork Chapter 5')
print('Date: 9/17/16')

print('get Grades')
def getGrades():
    grade=input("Enter score:")
    if grade=="":
        return []
    else:
        head=list()
        head.append(int(grade))
        rest=getGrades()
        return head + rest
print("Result: the list of all John's scores is", getGrades())

print('get Grades')
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
    
print('get names')
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
print("Result: the list of all John's scores is", GetNames())
    
#Count
def count100():

    rest=count100()
    return head+rest

def gradesImproving(previousGrade=0):
    grade=input("What is next score:")
    if grade=="":
        return True
    else:
        if int(grade) <=previousGrade:
            head=False
            return False
        else:
            previousGrade=int(grade)
            rest=gradesImproving(previousGrade)
            return rest
