
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

# finds modular inverse of e with respect
# to the totient
# x = modinv(b) mod n, (x * b) % n == 1
def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1: return x % n

# extended euclidean algorithm (recursive)
# take positive integers a, b as input, and
# return a tuple (g, x, y), such that
# ax + by = g = gcd(a, b)
def egcd(a, b):
    # base case
    if a == 0: return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def main():
    p, q, e = 11, 5, 7
    n = p * q
    l = (p - 1) * (q - 1)
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
