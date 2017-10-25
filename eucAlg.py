def euc():
    go = 1
    while go == 1:
        a = int(input('enter first int: '))
        b = int(input('enter second int: '))
        c = list(range(2))
        if a > b: c[0], c[1] = a, b
        if b > a: c[0], c[1] = b, a
        while c[1] > 0:
            d = c[0] % c[1]
            c[0] = c[1]
            c[1] = d
            print(c[0], c[1])
            if c[1] == 1:
                print('no common divisiors')
                break
        go = int(input('continue? 1, 0: '))

def lcm(a,b):
    product = a * b
    c = list(range(2))
    if a > b: c[0], c[1] = a, b
    if b > a: c[0], c[1] = b, a
    while c[1] > 0:
        d = c[0] % c[1]
        c[0] = c[1]
        c[1] = d
        lcm = product / c[0]
        print('lcm: ', lcm)
        return lcm

def golden(a, b):
    stop = .2
    g = 2 / (1 + 5 ** .5)
    lam = a + (b - a) * (1 - g)
    mu = a + (b - a) * g
    foflam = fun(lam)
    fofmu = fun(mu)
    print(line)
    print('+---A---+---B---+-LAMBDA-+-FOFLAM-+---MU---+--FOFMU-+')
    while b - a > stop:
        if foflam > fofmu:
            a = lam
            lam = mu
            foflam = fofmu
            mu = a + (b - a) * g
            fofmu = fun(mu)
        else:
            b = mu
            mu = lam
            fofmu = foflam
            lam = a + (b - a) % (1 - g)
            foflam = fun(lam)
        print('+', f.format(a),'|', f.format(b),'|', f.format(lam), '|', f.format(foflam), '|', f.format(mu), '|', f.format(fofmu), '+')
        print(line)
    return

def fun(a):
    return a ** 2 + 2 * a

def main():
    euc()
    # a,b = -3,5
    # golden(a,b)

main()
