#!/usr/bin/python

# parses the first argument or defaults to size 15
import sys
BOX_SIZE=15 if (len(sys.argv) < 2) else int(sys.argv[1])

# prints a single line from the inner box
def innerLine(line,count):
    return '* X' + (' '*count) + 'X' + (' '*line) + 'X' + (' '*count) + 'X *\n'

# prints the inner box
def inner(line,count):
    if line > 0:
        return innerLine(line,count) + inner(line-2,count+1) + innerLine(line,count)
    else:
        return '* X' + (' '*count) + 'X' + (' '*count) + 'X *\n'

# print a line of * of width BOX_SIZE
def starLine():
    return ('*'*BOX_SIZE) + '\n'

# print a *, then a line of spaces of width BOX_SIZE-2, then another *
def spaceLine():
    return '*' + (' '*(BOX_SIZE-2)) + '*\n'

# print a *, a space, a line of X's of width BOX_SIZE-4, a space, then a *
def xLine():
    return '* ' + ('X'*(BOX_SIZE-4)) + ' *\n'

# print the boxes
print starLine() + spaceLine() + xLine() + inner(BOX_SIZE-8,0) + xLine() + spaceLine() + starLine()
