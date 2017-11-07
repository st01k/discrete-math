# Casey Murphy
# Group 5, Project 11
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

# returns encryption key,
# a value that is coprime with l and within 1 - l
# l - totient of RSA modulus
def choosee(l):
    srl = int(l ** (1/2))
    for i in range(1, l):
        low, high = srl - i, srl + i
        if low > 0 and coprime(l, low): return low
        if high < l and coprime(l, high): return high
    return 0

# returns d (decryption key) | e(d) ≡ 1 mod l
# finds modular inverse of e with respect to the totient (l)
# a(x) [from Bezout's Identity] = e(d) ≡ 1 mod l
# (e * d) mod l = 1
def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1: return x % n

# extended euclidean algorithm (recursive)
# essentially, euclid's algorithm backwards
# a, b - positive integers
# returns a tuple (g, x, y)
# g - gcd(a, b)
# x, y - Bezout's coefficients
# such that ax + by = g (Bezout's Identity)
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# takes a plaintext string and encodes it
# into non-breaking (no spaces) ascii
# returns ascii code of plaintext
# plaintext - plain message
def toAscii(plaintext):
    temp = ''
    for c in plaintext:
        n = ord(c)
        if n < 100: temp += '0'
        temp += str(n)
    return int(temp)

# takes an ascii string and decodes it
# into a plaintext message
# returns plain text message
# asciicode - collection of ascii codes
def toText(asciicode):
    m, asciiAry = '', format(asciicode, ',').split(',')
    for n in asciiAry: m += chr(int(n))
    return m

# uses hard-coded primes to generate RSA modulus (n),
# encryption key (e), and decryption key (d)
# returns a tuple containing n, e, d
def genKeys():
    p, q = 10174093, 10176827
    n = p * q
    # totient of n
    l = (p - 1) * (q - 1)
    e, d = 0, 0
    # coprime check
    while (d == 0):
        e = choosee(l)
        d = modinv(e, l)
    return (n, e, d)

# C = M^e mod n
def encrypt(m, e, n):
    return pow(m, e, n)

# M = C^d mod n
def decrypt(c, d, n):
    return pow(c, d, n)

# implementation of pow(b,e,m)
# with binary exponentiation
# returns b^e mod m
# b - base number
# e - exponent
# m - modulus
def binexp(b, e, m):
    y = 1
    while e > 0:
        if e % 2 == 0:
            b = (b * b) % m
            e = e/2
        else:
            y = (b * y) % m
            e = e - 1
    return y

def main():
    msg = 'Math'
    m = toAscii(msg)
    n, e, d = genKeys()
    c = encrypt(m, e, n)
    cm = toText(c)
    p = decrypt(c, d, n)
    dm = toText(p)

    print()
    print('{:<20}'.format('Plaintext: ' + '{:>20}'.format(msg)))
    print('{:<20}'.format('Plaintext ASCII: ' + '{:>21}'.format(str(m))))
    print('{:<20}'.format('Encrypted ASCII: ' + '{:>24}'.format(str(c))))
    print('{:<20}'.format('Ciphertext: ' + '{:>20}'.format(cm)))
    print('{:<20}'.format('Decrypted ASCII: ' + '{:>21}'.format(str(p))))
    print('{:<20}'.format('Plaintext: ' + '{:>20}'.format(dm)))

main()
