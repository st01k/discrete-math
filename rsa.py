# Casey Murphy
# Group 5, Project 9
# Discrete Mathematics
# 31 Oct 17

def chooseE(l):
    # floor integer square root of l
    srl = int(l ** (1/2))
    for i in range(l // 2):
        high, low = srl + i, srl - i
        if high > l: continue
        elif relprime(l, high): return high
        if low < 1: continue
        elif relprime(l, low): return low
    return 0

def relprime(l, x):
    if gcd(l,x) == 1: return 1
    return 0

# uses Euclid's algorithm to find the
# greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

def main():
    p = 10174093
    q = 10176827
    n = p * q
    l = (p - 1) * (q - 1)
    e = chooseE(l)
    d = (1 % l) / e

    s = 'p = ' + str(p) + '\n'
    s += 'q = ' + str(q) + '\n'
    s += 'n = p * q = ' + str(n) + '\n'
    s += 'l = (p - 1)(q - 1) = ' + str(l) + '\n'
    s += 'e = ' + str(e) + '\n'
    s += 'd = (1 mod l) / e = ' + str(d) + '\n'

    print(s)
    return

main()
