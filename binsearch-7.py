# Casey Murphy
# Group 5, Project 7
# Discrete Mathematics
# 16 Oct 17

import random

# k - number of items in the set
# top - upper limit for number generation
# returns a set of randomized integers
def irand(k, top):
    return random.sample(range(top + 1), k)

# st - a set of integers
# insertion sorts set into ascending order
def isort(st):
    for i in range(1, len(st)):
        currVal = st[i]
        pos = i
        while pos > 0 and st[pos - 1] > currVal:
            st[pos] = st[pos - 1]
            pos = pos - 1
        st[pos] = currVal

# st - a sorted set
# tgt - target to search for
# performs a binary search of sorted set
# returns position of match
def binsearch(st, tgt):
    min = 0
    max = len(st) - 1
    cnt = 0
    print('searching for ' + str(tgt) + '...')
    while min <= max:
        cnt += 1
        p = (min + max) // 2
        if st[p] == tgt:
            print('search took ' + str(cnt) + ' guesses')
            return p
        elif st[p] > tgt: max = p - 1
        else: min = p + 1
    return -1

# label - name of set
# set - set to format
# returns a readable string containing label and set
def formatSet(label, set):
    temp = '\n' + label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    temp += '\n'
    return temp

def main():
    upLim = 200
    x = irand(100, upLim)
    print(formatSet("unsorted", x))
    isort(x)
    print(formatSet("sorted", x))
    target = random.randrange(upLim)
    result = binsearch(x, target) + 1
    if result == 0: print('number not found')
    else: print(str(target) + ' found at position ' + str(result))

main()
