for count in range(10,0,-1):
    print count
print ('Blastoff!')


groceries = ['milk','cheese','bread','cereal']

for position in range(len(groceries)):
    label = str(1+position) + '.'
    print label + groceries[position]


x = 3

if x == 3:
    x = 2 * x

print (x)

if x == 3:
    x = 2 * x

print (x)

x = 3
if x < 3:
    print('x less than 3')
else:
    print(x,'greater than or equal to 3')



"""
numA = numC = numG = numT = 0

for base in dna:
    if base == 'A':
        numA += 1
    elif base == 'C':
        numC +=1
    elif base == 'G':
        numG += 1
    else:
        numT +=1
"""


