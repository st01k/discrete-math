# Casey Murphy
# Group 5, Project 7
# Discrete Mathematics
# 16 Oct 17

import random

# k - number of items in the set
# top - upper limit for number generation
# returns a ranged set of randomized integers
def irand(k, top):
    return random.sample(range(top + 1), k)

# st - a set of integers
# sorts set into ascending order by insertion
def isort(st):
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
def binsearch(st, tgt):
    min, cnt = 0, 0
    max = len(st) - 1
    print('searching for ' + str(tgt) + '...')
    while min <= max:
        # increment guess counter
        cnt += 1
        # current position gets middle element of set (for guess)
        p = (min + max) // 2
        # if found return position
        if st[p] == tgt:
            print('search took ' + str(cnt) + ' guesses')
            return p
        # if target is lower than guess,
        # max gets current position - 1
        # reduces set in half by ignoring higher half
        elif st[p] > tgt: max = p - 1
        # if target is higher than guess
        # min gets current position + 1
        # reduces set in half by ignoring lower half
        else: min = p + 1
    # if target is not found
    return -1

# label - name of set
# set - set to format
# returns a formatted set with label for readability
def formatSet(label, set):
    temp = '\n' + label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    temp += '\n'
    return temp

def main():
    upLim = 200
    card = 100
    x = irand(card, upLim)
    print(formatSet("unsorted", x))
    isort(x)
    print(formatSet("sorted", x))
    # picks a random number within range to search for
    target = random.randrange(upLim)
    # plus one adjustment for 0 based array index
    result = binsearch(x, target) + 1
    # print result
    if result == 0: print('number not found')
    else: print(str(target) + ' found at position ' + str(result))

main()
