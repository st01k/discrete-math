import random

def irand(k, top):
    return random.sample(range(top + 1), k)

def isort(st):
    print(str(st[0]) + ' at position 1 moved to sorted list')
    for i in range(1, len(st)):
        currVal = st[i]
        pos = i
        print('evaluating ' + str(currVal) + ' at position ' + str(pos + 1))
        while pos > 0 and st[pos - 1] > currVal:
            st[pos] = st[pos - 1]
            pos = pos - 1
            print('inserting ' + str(currVal) + ' into position ' + str(pos + 1))
            if pos > 0: print('evaluating ' + str(currVal) + ' at position ' + str(pos + 1))
        st[pos] = currVal

def formatSet(label, set):
    temp = '\n' + label + ':\n'
    for i, item in enumerate(set):
        if i % 10 == 0: temp += '\n'
        temp += '{:>5}'.format(str(item))
    temp += '\n'
    return temp

def main():
    x = irand(5, 200)
    print(formatSet("Unsorted", x))
    isort(x)
    print(formatSet("Sorted", x))

main()
