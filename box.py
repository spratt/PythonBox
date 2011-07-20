#!/usr/bin/python
BOX_SIZE=15

def inner(line,count):
    if line > 0:
        toReturn = '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n'
        toReturn += inner(line-2,count+1)
        toReturn += '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n'
    else:
        toReturn = '* X' + (' '*count) + 'X' + (' '*count) + 'X *\n'
    return toReturn  

toPrint = ''
for i in range(0,BOX_SIZE):
    toPrint += '*'
toPrint += '\n* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n' + inner(BOX_SIZE-8,0) + '* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n'
for i in range(0,BOX_SIZE):
    toPrint += '*'
print toPrint
