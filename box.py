#!/usr/bin/python
import sys
BOX_SIZE=15 if (len(sys.argv) < 2) else int(sys.argv[1])

def inner(line,count):
    return '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n' + inner(line-2,count+1) + '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n' if line > 0 else '* X' + (' '*count) + 'X' + (' '*count) + 'X *\n'

print '' + ('*'*BOX_SIZE) + '\n*' + (' '*(BOX_SIZE-2)) + '*\n* ' + 'X'*(BOX_SIZE-4) + ' *\n' + inner(BOX_SIZE-8,0) + '* ' + 'X'*(BOX_SIZE-4) + ' *\n*' + (' '*(BOX_SIZE-2)) + '*\n' + ('*'*BOX_SIZE)
