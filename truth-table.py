# Casey Murphy
# Discrete Math (318)
# Project 1, Group 5
# 25 Aug 17

# greeting with border
print('\n' + '{:-^98}'.format('\n Lexicographical Truth Table v3 \n'))

# stSym = representative statement symbol array
stSym = 'p q r s t u v w x y z'.split()

# program loop
while True:
    # input validation loop
    while True:
        i = input('\nEnter number of statements (q to quit): ')
        if (i.isdigit() and 2 <= int(i) and int(i) <= len(stSym)):
            numSts = int(i)
            break
        elif (i == 'q'):
            exit()
        else:
            print('Invalid Input\nEnter a value between 2 and', len(stSym))

    # calculate and print number of rows
    numRows = 2 ** numSts
    print('Total Rows:', numRows, '\n')

    # print table head
    for x in range(numSts):
        print(' ', stSym[x], end=' ')

    # build divider
    div = '\n' + '|---' * numSts + '|'

    # build and print table
    print(div)
    # decrements row value with each iteration
    for row in reversed(range(numRows)):
        # converts row number to the binary value of row
        # when binary value digits < number of statements, fills with 0
        temp = "{0:b}".format(row).rjust(numSts,'0')
        # replaces 1 with T, 0 with F
        val = ' ' + temp.replace('1', ' T  ').replace('0', ' F  ')
        # prints row values and divider
        print (val + div)
