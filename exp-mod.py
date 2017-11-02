
b = int(input('base: '))
e = int(input('exponent: '))
m = int(input('mod: '))

#result = (b ** e) % m
result = pow(b,e,m)
print(str(b) + '^' + str(e) + ' (mod ' + str(m) + ') = ' + str(result))
