import math

def bina(a):
    c=[]
    leng = int(math.log(a,2))
    for i in range(leng + 1):
        c.append(a%2)
        a = a // 2
    c.reverse()
    print(c)
    return c

def modexp(base, exponent, modulus):
    ebin = bina(exponent)
    ebin.reverse()
    leng = len(ebin)
    base = base % modulus
    prod = base ** ebin[0]
    for i in range(1, leng):
        base = (base ** 2) % modulus
        prod = (prod * base ** ebin[i]) % modulus
        print(i, base, ebin[i], prod)
    return prod

def memeffmodexp(b, e, m):
    c = 1
    for eprime in range(1, e + 1):
        c = (c * b) % m
        print(eprime, c)
    return c

def main():
    modexp(8, 27, 17)
    print()
    modexp(4, 13, 497)
    print()
    memeffmodexp(4, 13, 297)

main()
