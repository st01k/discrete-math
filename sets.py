import random
import string

# Casey

maxDomain = 0
def genSets(k, pop):
    global maxDomain
    maxDomain = pop
    sets = []
    numSets = 2
    for i in range(numSets):
        sets.append(random.sample(range(pop), k))
    return sets

def complement(set):
    uni = list(range(maxDomain + 1))
    for item in set:
        if item in uni: uni.remove(item)
    return uni

def difference(A, B):
    diff = []
    for item in A:
        if item not in B: diff.append(item)
    return diff

def union(A, B):
    union = []
    for i in A: union.append(i)
    for i in B:
        if i not in union: union.append(i)
    union.sort()
    return union

def intersection(A, B):
    intersection = []
    for i in A:
        if i in B: intersection.append(i)
    intersection.sort()
    return intersection

# prints greeting
def greeting(s):
    print()
    print(s)
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
        elif i == 'eval':
            sets = dialog()
            printResult(sets)
        else: print('invalid command')
        print()

def dialog():
    k = input('enter cardinality> ')
    pop = input('enter max value> ')
    print()
    return genSets(int(k), int(pop))


def printResult(sets):
    alpha = string.ascii_uppercase
    for i, st in enumerate(sets):
        iden = alpha[i]
        print(formatSet('Set ' + iden, st))
        st.sort()
        print(formatSet('Sorted', st))
        print()

    A, B = sets[0], sets[1]
    print(formatSet('A U B', union(A, B)))
    print(formatSet('A ∩ B', intersection(A, B)))
    print(formatSet('NOT A', complement(A)))
    print(formatSet('A - B', difference(A, B)))

def formatSet(label, set):
    temp = label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    if len(set) == 0: temp += '\n\t\tEmpty Set'
    temp += '\n'
    return temp

# runs test statement
def test():
    #card, limit = 5, 10
    card, limit = 100, 200
    sets = genSets(card, limit + 1)
    printResult(sets)
    return

# prints help menu
def help():
    print('Available Commands')
    print('-------------------------------------------')
    print('help - prints this list')
    print('cls  - clears console screen')
    print('test - test on assignment requirements')
    print('eval - enters set input mode')
    print('quit - exits program')

# clears screen
def clear(): print('\n' * 70)

if __name__ == "__main__":
    greeting('Sets v1')
    prompt()
    print('Goodbye')