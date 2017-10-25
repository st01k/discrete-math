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
    for item in items[1:]:
        b = item
        a = gcd(a, b)
    return a

# finds the least common multiple of a
# collection of numbers of n length
# calls lcm
# items - collection of numbers
def lcmList(items):
    a = items[0]
    for item in items[1:]:
        b = item
        a = lcm(a, b)
    return a

def main():
    data = [9720, 4158, 594, 612]
    print('\nGCD and LCM of 2+ numbers\n')
    print('Data Set: ' + ', '.join(str(d) for d in data))
    print('GCD: ' + str(gcdList(data)))
    print('LCM: ' + str(lcmList(data)))

main()
