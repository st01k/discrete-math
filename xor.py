# Casey Murphy
# Group 5, Project 8
# Discrete Mathematics
# 20 Oct 17

import random

# k - number of items in the set
# top - upper limit for number generation
# returns a ranged set of randomized integers
def iRand(k, top):
    return random.sample(range(top + 1), k)

# st - a set of integers
# sorts set into ascending order by insertion
def iSort(st):
    for i in range(1, len(st)):
        currVal = st[i]
        pos = i
        while pos > 0 and st[pos - 1] > currVal:
            st[pos] = st[pos - 1]
            pos = pos - 1
        st[pos] = currVal

# st - sorted set
# tgt - target to search for
# performs a binary search of a sorted set
# returns position of match or -1 if not found
def binSearch(st, tgt):
    min, cnt = 0, 0
    max = len(st) - 1
    while min <= max:
        p = (min + max) // 2
        if st[p] == tgt: return p
        elif st[p] > tgt: max = p - 1
        else: min = p + 1
    return -1

# x,y - sorted sets
# returns the symmetric difference of x and y
# (X U Y) - (X int Y)
def symDiff(x,y):
    result = list()
    for elx in x:
        if binSearch(y, elx) == -1:
            result.append(elx)
    for ely in y:
        if binSearch(x, ely) == -1:
            result.append(ely)
    return result


# label - name of set
# set - set to format
# returns a formatted set with label for readability
def formatSet(label, set):
    temp = '\n' + label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    if len(set) == 0: temp += '\n\t\tEmpty Set'
    temp += '\n'
    return temp

def main():
    upLim = 200
    card = 100
    a = iRand(card, upLim)
    b = iRand(card, upLim)
    print(formatSet('A Unsorted', a))
    print(formatSet('B Unsorted', b))
    iSort(a)
    iSort(b)
    print(formatSet('A Sorted', a))
    print(formatSet('B Sorted', b))
    x = symDiff(a,b)
    iSort(x)
    print(formatSet('A XOR B', x))
    #l=[[ x for x in range(5) ] for y in range(4)]
    #myList=[i*i for i in range(10)]
main()
