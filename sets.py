import random
import string

# Casey
# intersection
# union
# both lists in ascending order
# U = {x | x is a whole number 0-200 (inclusive)}
# print NOT A (asc)
# print A-B (asc)

def genSets(k, pop, numSets):
    sets = []
    for i in range(numSets):
        sets.append(random.sample(range(pop), k))
    return sets

def complement(u, set):
    uni = list(range(u))
    for item in set:
        if item in uni:
            uni.remove(item)
    return uni

def difference(A, B):
    diff = []
    for item in A:
        if item not in B: diff.append(item)

    return diff


def union(sets):
    union = []
    # for i in A: union.append(i)
    # for i in B:
    #     if i not in union: union.append(i)

    for set in sets:
        for item in set:
            if item not in union: union.append(item)

    union.sort()
    return union

def intersection(sets):
    intersection = []
    # for i in A:
    #     if i in B: intersection.append(i)

    for set in sets:
        for item in set:
            for otherSet in sets:
                if otherSet != set:
                    if item in otherSet:
                        if item not in intersection:
                            intersection.append(item)


    intersection.sort()
    return intersection

# prints greeting
def greeting():
    print()
    print('Sets v1')
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
            sets = dialog()
            printResult(sets)
        else: print('invalid command')
        print()

def dialog():
    n = input('enter number of sets> ')
    k = input('enter cardinality> ')
    pop = input('enter max value> ')
    print()
    return genSets(int(k), int(pop), int(n))


def printResult(sets):
    alpha = string.ascii_uppercase
    for i, st in enumerate(sets):
        iden = alpha[i]
        print('Set  ' + iden + ': { ' + str(st).strip('[]') + ' }')
        st.sort()
        print('Sorted: { ' + str(st).strip('[]') + ' }')
        print()

    u = union(sets)
    i = intersection(sets)
    print('Union : { ' + str(u).strip('[]') + ' }')
    print('Inter : { ' + str(i).strip('[]') + ' }')

# prints help menu
def help():
    print('Available Commands')
    print('-------------------------------------------')
    print('help  - prints this list')
    print('cls   - clears console screen')
    print('test  - test run on assignment requirements')
    print('solve - enters set input mode')
    print('quit  - exits program')

# clears screen
def clear(): print('\n' * 70)

# runs test statement
def test():
    card, limit, sets = 5, 10, 2
    sets = genSets(card, limit, sets)
    printResult(sets)
    A = sets[0]
    B = sets[1]
    comp = complement(limit, A)
    diff = difference(A, B)
    print('NOT A : { ' + str(comp).strip('[]') + ' }')
    print('A - B : { ' + str(diff).strip('[]') + ' }')

    return

if __name__ == "__main__":
    greeting()
    prompt()
    print('Goodbye')
