# Casey Murphy
# Group 5, Project 8
# Discrete Mathematics
# 20 Oct 17

# k - number of items in the set
# top - upper limit for number generation
# returns a ranged set of randomized integers with top inclusive
def iRand(k, top):
    import random
    return random.sample(range(top + 1), k)

# A - a set of integers
# sorts set into ascending order by insertion
def iSort(A):
    for i in range(1, len(A)):
        currVal = A[i]
        pos = i
        while pos > 0 and A[pos - 1] > currVal:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = currVal

# A - sorted set
# tgt - target to search for
# performs a binary search of a sorted set
# returns index of match or -1 if not found
def binSearch(A, tgt):
    min, max = 0, len(A) - 1
    while min <= max:
        p = (min + max) // 2
        if A[p] == tgt: return p
        elif A[p] > tgt: max = p - 1
        else: min = p + 1
    return -1

# A,B - sorted sets
# returns the symmetric difference of A and B
# A XOR B = (A U B) - (A ∩ B)
def symDiff(A, B):
    result = []
    for val in A:
        if binSearch(B, val) == -1: result.append(val)
    for val in B:
        if binSearch(A, val) == -1: result.append(val)
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
    #lim, card = 200, 100
    lim, card = 10, 5
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
