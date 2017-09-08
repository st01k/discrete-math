# Casey Murphy
# Group 5, Project 3
# Discrete Mathematics
# 1 Sep 17

import sys

IMP = '-->'
IFF = '<->'

# determines truth value of implication
# returns false when p is true and q is false
def implies(p, q):
    if (p and not q): return False
    return True

# determines truth value of bi-implication
# returns true when p and q have the same truth value
def iff(p, q):
    if (p == q): return True
    return False

# prints greeting
def greeting():
    print()
    print('Statement Solver v1')
    print('------------------------')
    print('(type help for commands)')
    print('------------------------')

# displays prompt and awaits command input
# calls function by command
def prompt():
    while(True):
        i = input('main> ')
        print()
        if i == 'quit' or i == 'q': break
        elif i == 'help': help()
        elif i == 'cls': clear()
        elif i == 'test': test()
        elif i == 'solve':
            print('example form: p^q-->~q')
            s = input('solve> ')
            solve(s)
        else: print('invalid command')
        print()

# prints help menu
def help():
    print('Statement Solver Help')
    print('------------------------------------')
    print('help  - prints this list')
    print('cls   - clears console screen')
    print('test  - evaluates test statement')
    print('solve - enters statement input mode')
    print('quit  - exits program')
    print('\nsolver mode:')
    print(' use any letter except \'v\' \n as a statement symbol')
    print(' ~  = NOT')
    print(' ^  = AND')
    print(' v  = OR')
    print('--> = IMPLIES')
    print('<-> = IFF')

# clears screen
def clear(): print('\n' * 70)

# runs test statement
def test():
    ts = '~(P^Q)<->(~P)v(~Q)'
    print('test statement: ', ts)
    solve(ts)

# solves statement
# s - statement input from user
def solve(s):
    holder = addParen(s)
    stack = parseNestedParen(holder)

    sym = list()
    for char in s:
        if char.isalpha() and char != 'v':
            if char in sym:
                break
            else: sym.append(char)
    print(sym)
    print(truthtable(len(sym)))

    rows = 2 ** len(sym)
    # build divider
    div = '\n' + '|---' * len(sym) + '|'

    # build and print table
    print(div)

    for item in stack:
        print('evaluating: ' + str(item))
        print(evaluate(item[1]))

def truthtable (n):
  if n < 1:
    return [[]]
  subtable = truthtable(n-1)
  return [ row + [v] for row in subtable for v in [1,0] ]

def addParen(s):
    temp = s
    imp, iff = False, False
    x, holder = '', ''

    if IMP in temp:
        x = temp.split(IMP)
        imp = True

    if IFF in temp:
        x = temp.split(IFF)
        iff = True

    if len(x) == 2:
        for i, item in enumerate(x):
            item = '(' + item + ')'
            holder += item
            if i < 1:
                if imp: holder += '@'
                if iff: holder += '$'
    elif len(x) < 2:
        holder = temp
    else: print('cannot currently handle 2+ implications')

    temp = '(' + holder + ')'
    return temp

def parseNestedParen(s):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield (len(stack), s[start + 1: i])
    return stack

def evaluate(statement):
    x,y,op = '', '', ''
    for char in statement:
        print(char)
        if char == '(' or char == ')': continue
        if char == '~': op = '~'
        if char == '^': op = '^'
        if char == 'v': op = 'v'
        if char == '@': op = '@'
        if char.isalpha():
            if x == '': x = char
            else: y = char

    print(x + op + y + ' =', end = ' ')

    if op == '~': return not x
    elif op == '^': return x and y
    elif op == 'v': return x or y
    elif op == '@': return implies(x, y)
    elif op == '$': return iff(x, y)
    else: print('no operation found')

# program entry point
def main():
    greeting()
    prompt()
    print('Goodbye')

# import (as lib) entry point
if __name__ == '__main__':
  main()
