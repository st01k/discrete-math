# Casey Murphy
# Group 5, Project 10
# Discrete Mathematics
# 1 Nov 17

# returns greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

# returns true if l and x are coprime
# calls gcd
# l, x - terms to calculate on
def coprime(l, x):
    return gcd(l, x) == 1

# returns a value that is coprime with l
# and within the range of 1 - l
# calls coprime
# l - totient of RSA modulus
def choosee(l):
    # floor integer square root of l
    srl = int(l ** (1/2))
    for i in range(1, l):
        # set high and low values
        low, high = srl - i, srl + i
        # checks low range limit and tests co-primality
        if low > 0 and coprime(l, low): return low
        # checks high range limit and tests co-primality
        if high < l and coprime(l, high): return high
    return 0

def main():
    p, q = 10174093, 10176827
    n = p * q
    l = (p - 1) * (q - 1)
    e = choosee(l)

    s = '\np = ' + str(p) + '\n'
    s += 'q = ' + str(q) + '\n'
    s += 'n = p * q = ' + str(n) + '\n'
    s += 'l = (p - 1)(q - 1) = ' + str(l) + '\n'
    s += 'e = ' + str(e) + '\n'
    s += 'gcd(' + str(l) + ', ' + str(e) + ') = ' + str(gcd(l, e))

    print(s)

main()
