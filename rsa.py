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

# returns a value that is coprime with l
# and within the range of 1 - l
# calls coprime
# l - totient of RSA modulus
def choosee(l):
    srl = int(l ** (1/2))
    for i in range(1, l):
        low, high = srl - i, srl + i
        if low > 0 and coprime(l, low): return low
        if high < l and coprime(l, high): return high
    return 0

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
    if a == 0: return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def toAscii(plaintext):
    temp = ''
    for c in plaintext:
        n = ord(c)
        if n < 100: temp += '0'
        temp += str(n)
    return int(temp)

def toText(asciicode):
    asciiAry = format(asciicode, ',').split(',')
    m = ''
    for n in asciiAry: m += chr(int(n))
    return m

def genKeys():
    p, q = 10174093, 10176827
    n = p * q
    l = (p - 1) * (q - 1)
    e = choosee(l)
    d = modinv(e, l)
    return (n, e, d)

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

# implementation of pow(b,e,m)
# with binary exponentiation
def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

def main():
    msg = 'Mathi'
    m = toAscii(msg)
    n, e, d = genKeys()
    c = encrypt(m, e, n)
    cm = toText(c)
    p = decrypt(c, d, n)
    dm = toText(p)

    print('Plaintext: ', msg)
    print('Plaintext ASCII: ', str(m))
    print('Ciphertext ASCII: ', str(c))
    print('Ciphertext: ', cm)
    print('Decrypted Plaintext ASCII: ', str(p))
    print('Decrypted Plaintext: ', dm)

main()
