# Casey Murphy
# Group 5, Project 5
# Discrete Mathematics
# 15 Sep 17

import random

# global variables
maxDomain = 0

# generates 2 sets of random numbers
# assigns global max inclusive domain value
# k - number of items in the set
# pop - upper limit for number generation
# returns a 2 member array of sets
def genSets(k, pop):
    global maxDomain
    # add 1 for inclusion on upper limit
    maxDomain = pop + 1
    sets = []
    numSets = 2
    for i in range(numSets):
        sets.append(random.sample(range(maxDomain), k))
    return sets

# determines the complement of a set using
# the global max domain value to define
# the universal set from which to compare
# {x | x ∈ U and x ∉ A}
# A - a set of random numbers
# returns the complement (NOT A) as a set
def complement(A):
    # create universal set
    U = list(range(maxDomain))
    for element in A:
        if element in U: U.remove(element)
    return U

# determines the difference between two sets
# {x | x ∈ A and x ∉ B}
# A - minuend set
# B - subtrahend set
# returns the difference of A - B as a set
def difference(A, B):
    diff = []
    for element in A:
        if element not in B: diff.append(element)
    return diff

# determines the union of two sets
# {x | x ∈ A or x ∈ B}
# A - first set
# B - second set
# returns the union of A and B as a set
def union(A, B):
    union = []
    for element in A: union.append(element)
    for element in B:
        if element not in union: union.append(element)
    union.sort()
    return union

# determines the intersection of two sets
# {x | x ∈ A and x ∈ B}
# A - first set
# B - second set
# returns the intersection of A and B as a set
def intersection(A, B):
    inter = []
    for element in A:
        if element in B: inter.append(element)
    inter.sort()
    return inter

# prints dynamic greeting
# s - greeting title
def greeting(s):
    print()
    print(s)
    print('------------------------')
    print('(type help for commands)')
    print('------------------------')

# displays prompt and awaits command input
# validates input and calls function by command
def prompt():
    while(True):
        i = input('main> ')
        print()
        if i == 'quit' or i == 'q': break
        elif i == 'help': help()
        elif i == 'cls' : clear()
        elif i == 'test': test()
        elif i == 'eval': eval()
        else: print('invalid command')
        print()

# runs test statement based on the
# requirements for this project:
# cardinality of 100
# domain of (0 - 200)
# generates sets
# calls printResult to display results
def test():
    card, limit = 100, 200
    sets = genSets(card, limit)
    printResult(sets)

# prompts for and validates user input
# generates sets based on user input
# calls printResult to display results
def eval():
    k = input('enter cardinality> ')
    # ensure cardinality is greater than 0
    if not k.isdigit() or int(k) < 0:
        print('\ninvalid input')
        return
    pop = input('enter max inclusive domain value> ')
    print('domain: (0 - '+ pop +')')
    # ensure max inclusive domain is less than cardinality
    if not pop.isdigit() or int(pop) + 1 < int(k):
        print('\ninvalid input')
        return
    sets = genSets(int(k), int(pop))
    print()
    printResult(sets)

# prints help menu
def help():
    print('Available Commands')
    print('-------------------------------------------')
    print('help - prints this list')
    print('cls  - clears console screen')
    print('test - test on assignment requirements')
    print('eval - prompts for custom set definition')
    print('       ex: 5 and 10 for easy-to-read test')
    print('quit - exits program')

# clears screen
def clear(): print('\n' * 70)

# prints results of operations on defined sets
# calls operation functions and formatSet
# sets - array of 2 sets
def printResult(sets):
    alpha = ['A', 'B']
    for i, st in enumerate(sets):
        iden = alpha[i]
        print(formatSet('Set ' + iden, st))
        st.sort()
        print(formatSet('Sorted', st))
        print()

    A, B = sets[0], sets[1]
    print(formatSet('A U B', union(A, B)))
    print(formatSet('A ∩ B', intersection(A, B)))
    print(formatSet('A - B', difference(A, B)))
    print(formatSet('NOT A', complement(A)))
    print(formatSet('NOT B', complement(B)))

# formats a printable, readable string
# label - name of set
# set - set to format
# returns a string containing label and set
def formatSet(label, set):
    temp = label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    if len(set) == 0: temp += '\n\t\tEmpty Set'
    temp += '\n'
    return temp

def main():
    greeting('Sets v2')
    prompt()
    print('Goodbye')

# program entry
main()
