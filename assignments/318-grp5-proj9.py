# Casey Murphy
# Group 5, Project 9
# Discrete Mathematics
# 25 Oct 17

# uses Euclid's algorithm to find the
# greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

# finds the least common multiple of a and b
# calls gcd
# a, b - terms to calculate on
def lcm(a, b):
    return a * b // gcd(a, b)

# finds the greatest common divisor of a
# collection of numbers of n length
# calls gcd
# items - collection of numbers
def gcdList(items):
    a = items[0]
    # skips first element bc of pre-loop assignment
    for item in items[1:]:
        # assign current element
        b = item
        # calculate gcd and assign new value to a
        a = gcd(a, b)
        # loop through list until comprehensive
        # gcd has been calculated
    return a

# finds the least common multiple of a
# collection of numbers of n length
# calls lcm
# items - collection of numbers
def lcmList(items):
    a = items[0]
    # skips first element bc of pre-loop assignment
    for item in items[1:]:
        # assign current element
        b = item
        # calculate lcm and assign new value to a
        a = lcm(a, b)
        # loop through list until comprehensive
        # lcm has been calculated
    return a

def main():
    data = [9720, 4158, 594, 612]
    print('\nGCD and LCM of 2+ numbers\n')
    print('Data Set: ' + ', '.join(str(d) for d in data))
    print('GCD: ' + str(gcdList(data)))
    print('LCM: ' + str(lcmList(data)))

main()

"""
Prime Factorizations of Data Set
---------------------------------------------------------------
9720            4158            594             612
 /\              /\              /\              /\
2  4860         2  2079         2  297          2  306
    /\              /\              /\              /\
   2  2430         3  693          3  99           2  153
        /\             /\              /\              /\
       2  1215        3 231           3  33           3  51
            /\           /\               /\              /\
           3  405       3  77            3  11           3  17
               /\           /\
              3  135       7  11
                  /\
                 3  45
                     /\
                    5  9
                       /\
                      3  3
---------------------------------------------------------------
9720 = 2^3 * 3^3 * 5
4158 = 2 * 3^3 * 7 * 11
594  = 2 * 3^3 * 11
612  = 2^2 * 3^2 * 17
---------------------------------------------------------------
"""
