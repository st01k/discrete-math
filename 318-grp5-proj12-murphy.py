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

# returns random encryption key (e) such that
# e is coprime with l and within 1 - l, exclusive
# l - totient of RSA modulus
def choosee(l):
    from random import shuffle
    candidates = []
    for i in range(2, l - 1):
        if coprime(l, i): candidates.append(i)
        if len(candidates) > 10: break
    shuffle(candidates)
    return candidates[0]

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
# into a list of ascii codes
# plaintext - plain text message
def toAscii(plaintext):
    return [ord(c) for c in plaintext]

# returns plain text message from ascii
# decodes ascii code into plaintext
# asciicode - collection of ascii codes
def toText(asciicode):
    m = []
    for n in asciicode: m += chr(int(n))
    return m

# returns a tuple containing n, e, d
# uses hard-coded primes to generate values
#   n - RSA modulus
#   e - encryption key
#   d - decryption key
def genKeys():
    # replaced p, original not prime
    p, q = 10175461, 10176827
    n = p * q
    # l = totient of n = phi = (p-1)*(q-1)
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
        # exponent is even
        if e % 2 == 0:
            # square base, take the mod
            b = (b * b) % m
            # divide exponent in half
            e /= 2
        # exponent is odd
        else:
            # mod result of b * y until exponent is 1
            y = (b * y) % m
            # decrement exponent
            e -= 1
    return y

# returns formatted block of text based on input
# s - list of integers
# length - desired width of text block
def formatList(s, length):
    from textwrap import fill
    string = ''
    for c in s: string += str(c)
    return fill(string, width = length, subsequent_indent = ' ')

def main():
    n, e, d = genKeys()
    msg = 'Math is awesome!'
    # encodes message text to ascii
    amsg = toAscii(msg)
    # encrypts one character at a time
    cipher = [encrypt(c, e, n) for c in amsg]
    # decrypts one character at a time
    plain = [decrypt(c, d, n) for c in cipher]
    # decodes decrypted message from ascii to text
    dmsg = toText(plain)
    # for block size of output, 3 numbers per ascii code
    width = len(amsg) * 3

    print()
    print('Plaintext: \n', msg)
    print('Plaintext ASCII: \n', formatList(amsg, width))
    print('Encrypted ASCII: \n', formatList(cipher, width))
    print('Decrypted ASCII: \n', formatList(plain, width))
    print('Decrypted Plaintext: \n', formatList(dmsg, width))

main()
