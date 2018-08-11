# Casey Murphy
# Group 5, Project 6
# Discrete Mathematics
# 4 Oct 17

import random

# k - number of items in the set
# top - upper limit for number generation
# returns a set of randomized integers
def irand(k, top):
    return random.sample(range(top + 1), k)

# st - a set of integers
# insertion sorts set into ascending order
def isort(st):
    # steps through set
    for i in range(1, len(st)):
        currVal = st[i]
        pos = i
        # checks if left value (pos - 1) is greater than current
        # value (pos) until left value is no longer larger
        while pos > 0 and st[pos - 1] > currVal:
            # performs insertion
            st[pos] = st[pos - 1]
            pos = pos - 1
        # resets to current value in outer loop
        st[pos] = currVal

# label - name of set
# set - set to format
# returns a readable string containing label and set
def formatSet(label, set):
    temp = '\n' + label + ':\n'
    for i, item in enumerate(set):
        # new line every 10 elements
        if i % 10 == 0: temp += '\n'
        # aligns and pads element
        temp += '{:>5}'.format(str(item))
    temp += '\n'
    return temp

def main():
    x = irand(100, 200)
    print(formatSet("Unsorted", x))
    isort(x)
    print(formatSet("Sorted", x))

main()
