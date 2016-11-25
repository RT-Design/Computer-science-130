filename = raw_input('What is the filename?')
source = file(filename)
text = source.read()
numchars = len(text)
numwords = len(text.split())
numlines = len(text.split('\n'))

print (numlines,numwords,numchars,numlines)

source.close()
               
