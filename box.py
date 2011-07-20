#!/usr/bin/python
import sys
BOX_SIZE=15 if (len(sys.argv) < 2) else int(sys.argv[1])

def inner(line,count):
    if line > 0:
        toReturn = '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n' + inner(line-2,count+1) + '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n'
    else:
        toReturn = '* X' + (' '*count) + 'X' + (' '*count) + 'X *\n'
    return toReturn  

toPrint = ''
for i in range(0,BOX_SIZE):
    toPrint += '*'
toPrint += '\n*' + (' '*(BOX_SIZE-2)) + '*\n* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n' + inner(BOX_SIZE-8,0) + '* '
for i in range(0,BOX_SIZE-4):
    toPrint += 'X'
toPrint += ' *\n*' + (' '*(BOX_SIZE-2)) + '*\n'
for i in range(0,BOX_SIZE):
    toPrint += '*'
print toPrint
