#!/usr/bin/python
BOX_SIZE=15

def inner(line, size):
    if line != (size-1):
        toReturn = '* X' + (' '*line) + 'X' + (' '*(size-(line*2))) + 'X' + (' '*line) + 'X *\n'
        toReturn += inner(line+1, size)
        toReturn += '* X' + (' '*line) + 'X' + (' '*(size-(line*2))) + 'X' + (' '*line) + 'X *\n'
    else:
        toReturn = '* X' + (' '*(size-1)) + 'X' + (' '*(size-1)) + 'X *\n'
    return toReturn  

toPrint = ''
for i in range(0,BOX_SIZE):
    toPrint += '*'
toPrint += '\n* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n' + inner(0,(BOX_SIZE-4)/2) + '* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n'
for i in range(0,BOX_SIZE):
    toPrint += '*'
print toPrint
