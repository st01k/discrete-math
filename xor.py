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

# a - a set of integers
# sorts set into ascending order by insertion
def iSort(a):
    for i in range(1, len(a)):
        currVal = a[i]
        pos = i
        while pos > 0 and a[pos - 1] > currVal:
            a[pos] = a[pos - 1]
            pos = pos - 1
        a[pos] = currVal

# a - sorted set
# tgt - target to search for
# performs a binary search of a sorted set
# returns position of match or -1 if not found
def binSearch(a, tgt):
    min, cnt = 0, 0
    max = len(a) - 1
    while min <= max:
        p = (min + max) // 2
        if a[p] == tgt: return p
        elif a[p] > tgt: max = p - 1
        else: min = p + 1
    return -1

# a,b - sorted sets
# returns the symmetric difference of a and b
# A XOR B = (A U B) - (A ∩ B)
def symDiff(a,b):
    result = list()
    # iterate through set A
    for ela in a:
        # search set B for element ela
        if binSearch(b, ela) == -1:
            # add element ela to result if not found
            result.append(ela)
    # iterate through set B
    for elb in b:
        # search set A for element elb
        if binSearch(a, elb) == -1:
            # add element elb to result if not found
            result.append(elb)
    # return symmetric difference of sets A and B
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
    lim, card = 200, 100
    a = iRand(card, lim)
    b = iRand(card, lim)
    print(formatSet('A Unsorted', a))
    print(formatSet('B Unsorted', b))
    iSort(a)
    iSort(b)
    print(formatSet('A Sorted', a))
    print(formatSet('B Sorted', b))
    x = symDiff(a,b)
    iSort(x)
    print(formatSet('A XOR B', x))
main()
