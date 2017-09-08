# Casey Murphy
# Group 5, Project 2
# Discrete Mathematics
# 25 Aug 17

# determines truth value of implication
# returns false when p is true and q is false
def implies(p, q):
    if (p and not q): return False
    return True

# determines truth value of bi-implication
# returns true when p and q have the same truth value
def iff(p, q):
    if (p == q): return True
    return False

# dynamically prints statement and result
# calls implies and iff
def testPrint(p, q):
    pStr, qStr = 'F', 'F'

    if (p): pStr = 'T'
    if (q): qStr = 'T'

    print()
    print('p(' + pStr + ') --> q(' + qStr + '): ' + str(implies(p, q)))
    print('p(' + pStr + ') <-> q(' + qStr + '): ' + str(iff(p, q)))

# runs test loop to check all possible values
def main():
    vals = [True, False]
    for x in vals:
        p, q = x, x
        testPrint(p, q)
        q = not x
        testPrint(p, q)

# program entry
if __name__ == '__main__':
  main()
