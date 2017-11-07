# Casey Murphy
# Group 5, Project 11
# Discrete Mathematics
# 7 Nov 17

# returns greatest common divisor of a and b
# a, b - terms to calculate on
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

# returns true if l and x are coprime
# l, x - determining factors
def coprime(l, x):
    return gcd(l, x) == 1

# returns encryption key (e) such that
# e is coprime with l and within 1 - l
# l - totient of RSA modulus
def choosee(l):
    srl = int(l ** (1/2))
    for i in range(1, l):
        low, high = srl - i, srl + i
        if low > 0 and coprime(l, low): return low
        if high < l and coprime(l, high): return high
    return 0

# returns decryption key (d) | e(d) ≡ 1 mod l
# finds modular inverse of e with respect to the totient (l)
# a(x) [from Bezout's Identity] = e(d) ≡ 1 mod l
# (e * d) mod l = 1
def modinv(e, l):
    g, x, _ = egcd(e, l)
    if g == 1: return x % l

# extended euclidean algorithm (recursive)
# essentially, euclid's algorithm backwards
# a, b - positive integers
# returns a tuple (g, x, y)
#   g - gcd(a, b)
#   x, y - Bezout's coefficients
#   such that ax + by = g (Bezout's Identity)
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# returns ascii code of plaintext
# takes a plaintext string and encodes it
# into a continuous (no spaces) ascii sequence
# plaintext - plain text message
def toAscii(plaintext):
    temp = ''
    for c in plaintext:
        n = ord(c)
        if n < 100: temp += '0'
        temp += str(n)
    return int(temp)

# returns plain text message from ascii
# decodes ascii code into plaintext
# asciicode - collection of ascii codes
def toText(asciicode):
    m, asciiAry = '', format(asciicode, ',').split(',')
    for n in asciiAry: m += chr(int(n))
    return m

# returns a tuple containing n, e, d
# uses hard-coded primes to generate values
#   n - RSA modulus
#   e - encryption key
#   d - decryption key
def genKeys():
    p, q = 10174093, 10176827 # original 8 digits
    #p, q = 101741023, 101742617 # 9 digits
    #p, q = 1017411377, 1017410291 # 10 digits
    n = p * q
    # totient of n
    l = (p - 1) * (q - 1)
    e, d = 0, 0
    # coprime check
    while (e == 0 or d == 0):
        e = choosee(l)
        d = modinv(e, l)
    return (n, e, d)

# returns encrypted message (C) | C = M^e mod n
# m - plain text message
# e - encryption key
# n - RSA modulus
def encrypt(m, e, n):
    return binexp(m, e, n)

# returns decrypted message (M) | M = C^d mod n
# c - cipher text message
# d - decryption key
# n - RSA modulus
def decrypt(c, d, n):
    return binexp(c, d, n)

# returns result of b^e mod m
# using binary exponentiation
# b - base number
# e - positive exponent
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
