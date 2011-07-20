#!/usr/bin/python
BOX_SIZE=11

def outer(size):
    toPrint = ''
    for i in range(0,size):
        toPrint += '*'
    toPrint += '\n* '
    for i in range(0,size-4):
        toPrint += 'X'
    toPrint += ' *\n' + inner(0,(size-4)/2) + '* '
    for i in range(0,size-4):
        toPrint += 'X'
    toPrint += ' *\n'
    for i in range(0,size):
        toPrint += '*'
    print toPrint

def inner(line, size):
    if line != (size-1):
        toReturn = '* X' + (' '*line) + 'X' + (' '*(size-(line*2))) + 'X' + (' '*line) + 'X *\n'
        toReturn += inner(line+1, size)
        toReturn += '* X' + (' '*line) + 'X' + (' '*(size-(line*2))) + 'X' + (' '*line) + 'X *\n'
    else:
        toReturn = '* X' + (' '*2) + 'X' + (' '*2) + 'X *\n'
    return toReturn  

outer(BOX_SIZE)
