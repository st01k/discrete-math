# Casey Murphy
# Group 5, Project 9
# Discrete Mathematics
# 31 Oct 17

# returns a value that is relatively prime with l
# starts search at square root of l
# l -
def chooseE(l):
    # floor integer square root of l
    srl = int(l ** (1/2))
    # iterate through values from 1 to half of l
    for i in range(l // 2):
        # set high and low values
        high, low = srl + i, srl - i
        # skip values higher than l
        if high > l: continue
        # check if high value is relatively prime with l
        elif relprime(l, high): return high
        # skip values lower than 1
        if low < 1: continue
        # check if low value is relatively prime with l
        elif relprime(l, low): return low
    return 0

# returns 1 if l and x are relatively prime
# returns 0 otherwise
# calls gcd
# l, x - terms to calculate on
def relprime(l, x):
    if gcd(l,x) == 1: return 1
    return 0

# returns greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

def main():
    p, q = 10174093, 10176827
    n = p * q
    l = (p - 1) * (q - 1)
    e = chooseE(l)

    s = '\np = ' + str(p) + '\n'
    s += 'q = ' + str(q) + '\n'
    s += 'n = p * q = ' + str(n) + '\n'
    s += 'l = (p - 1)(q - 1) = ' + str(l) + '\n'
    s += 'e = ' + str(e) + '\n'
    s += 'gcd(' + str(l) + ', ' + str(e) + ') = ' + str(gcd(l, e))

    print(s)
    return

main()
