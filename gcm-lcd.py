# Casey Murphy
# Group 5, Project 9
# Discrete Mathematics
# 25 Oct 17

import functools

# uses Euclid's algorithm to calculate the
# greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return a

# finds the least common multiple of a and b
# a, b - terms to calculate on
def lcm(a, b):
    return a * b // gcd(a, b)

# finds the greatest common divisor of a
# collection of numbers of n length
# calls euclid
# items - collection of numbers
def gcdList(items):
    return functools.reduce(gcd, items)

# finds the least common multiple of a
# collection of numbers of n length
# calls gcd
# items - collection of numbers
def lcmList(items):
    return functools.reduce(lcm, items)

def main():
    data = {9720,4158,594,612}
    test = {15, 60, 180}
    print(gcdList(test))
    print(lcmList(test))

main()
