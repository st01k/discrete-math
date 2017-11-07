# Casey Murphy
# Group 5, Project 11
# Discrete Mathematics
# 6 Nov 17

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

# returns encryption key,
# a value that is coprime with l and within 1 - l
# l - totient of RSA modulus
def choosee(l):
    # floor integer square root of l
    srl = int(l ** (1/2))
    for i in range(1, l):
        # set high and low values
        low, high = srl - i, srl + i
        # checks low range limit and tests coprimality
        if low > 0 and coprime(l, low): return low
        # checks high range limit and tests coprimality
        if high < l and coprime(l, high): return high
    return 0

# returns d (decryption key) | e(d) ≡ 1 mod l
# finds modular inverse of e with respect to the totient (l)
# a(x) [from Bezout's Identity] = e(d) ≡ 1 mod l
# (e * d) mod l = 1
def modinv(e, l):
    # g = gcd(e, l) - used to determine coprimality
    # x = modular inverse(e) mod l
    # _ is not used in this function,
    # used for recursion in egcd function
    g, x, _ = egcd(e, l)
    # if coprime, return d as x mod l
    # also handles negative values for x
    if g == 1: return x % l
    # if e is not a coprime candidate
    return 0

# extended euclidean algorithm (recursive)
# essentially, euclid's algorithm backwards
# a, b - positive integers
# returns a tuple (g, x, y)
# g - gcd(a, b)
# x, y - Bezout's coefficients
# such that ax + by = g (Bezout's Identity)
# ref: https://www.youtube.com/watch?v=6KmhCKxFWOs
def egcd(a, b):
    # base case
    if a == 0: return (b, 0, 1)
    else:
        # recursively finds g, x, y for a, b
        # by reducing the problem each time in terms
        # of the remainder b / a or b mod a
        g, x, y = egcd(b % a, a)
        # general case (return gcd, x, y)
        return (g, y - (b // a) * x, x)

def main():
    p, q = 10174093, 10176827
    n = p * q
    # totient of n
    l = (p - 1) * (q - 1)
    e, d = 0, 0
    # coprime check
    while (d == 0):
        e = choosee(l)
        d = modinv(e, l)

    s = '\np = ' + str(p) + '\n'
    s += 'q = ' + str(q) + '\n'
    s += 'n = p * q = ' + str(n) + '\n'
    s += 'l = (p - 1)(q - 1) = ' + str(l) + '\n'
    s += 'e = ' + str(e) + '\n'
    s += 'd = ' + str(d) + '\n'
    s += 'd * e (mod l) = ' + str((d * e) % l) + '\n'

    print(s)

main()
