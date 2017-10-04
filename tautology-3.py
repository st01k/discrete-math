# Casey Murphy
# Group 5, Project 3
# Discrete Mathematics
# 8 Sep 17

# determines truth value of implication
# p,q: boolean values
# returns false when p is true and q is false
def implies(p, q):
    if (p and not q): return False
    return True

# determines truth value of bi-implication
# p,q: boolean values
# returns true when p and q have the same truth value
def iff(p, q):
    if (p == q): return True
    return False

# builds static header
# returns header as a string
def buildTableHead():
    n = '|'
    for c in range(col): n += '{:^7}|'.format(str(c + 1))
    h = '|   P   |   Q   |  P^Q  |~(P^Q) |  ~P   |  ~Q   | ~Pv~Q |  <->  |'
    return '\n' + div +  '\n' + n +  '\n' + div + '\n' + h + '\n' + div

# builds row
# vals: tuple containing all values in row
# returns row as a string
def buildTableRow(vals):
    row = '|'
    for val in vals: row += '{:^7}|'.format(str(val))
    return row

def main():
    print('Evaluating tautology (from De Morgan\'s Law): ~(P^Q)<->(~P)v(~Q)')
    print(buildTableHead())

    boolAry = [True, False]
    for p in boolAry:
        for q in boolAry:
            # evaluate first part of iff binomial
            bi1 = not (p and q)
            # evaluate second part of iff binomial
            bi2 = not p or not q
            # contruct a tuple containing the results of logical
            # operations on the current value of p and q in the
            # tautological statement: ~(P^Q)<->(~P)v(~Q)
            vals = p, q, p and q, bi1, not p, not q, bi2, iff(bi1, bi2)
            # prints row and divider
            print(buildTableRow(vals) + '\n' + div)

# global variables
col = 8
div = '--------' * col + '-'

# program entry
main()
