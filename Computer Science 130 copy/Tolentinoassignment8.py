print('Assignment 8')
print('Ryan Tolentino')
print('October 29,2016\n')


print('Problem 1')
#Problem 1
#Create and test the openFileReadRobust() function to open file (for reading) whose name is provided from the standard input (keyboard) ﾖ the name is requested until it is correct (slide 17)
def openFileReadRobust():
  source = None
  while not source:
        filename = raw_input('Input filename: ')
        try:
            source = file(filename)
        except IOError:
           print ('Sorry, unable to open file', filename)
  return source

print('Complete\n')


print('Problem 2')
#Problem 2
#Create and test the openFileWriteRobust () function to open file (for writing) whose name is provided from the standard input (keyboard) ﾖ the name is requested until is correct (slide 18)
def openFileWriteRobust(defaultName):
    writable = None
    while not writable:
        prompt = 'Output filename [%s]?:  '%(defaultName)
        filename = raw_input(prompt)
        if not filename:
            filename = defaultName
        try:
           writable = file(filename,)
        except IOError:
            print ('Sorry, unable to write to file', filename)
    return writable

print('Complete\n')


print('Problem 3')
#Problem 3
def ReadFile(filename):
    openFile=file(filename)
    text=source.read()
    numchars=len(text)
    numwords=len(text.split())
    numlines=len(text.split('\n'))
    print ("Number of lines:"+str(numlines)+"\nNumber of Words:"+str(numwords))
    source.close()
ReadFile(filename)
