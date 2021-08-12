from random import *
from math import *
print('Welcome to the number prediction game ')
ans = input('Do you want to continue?').lower()
if ans == 'yes':
    l = int(input('Enter a lower limit '))
    u = int(input('Enter a upper limit '))
    a = randrange(l, u, 1)
    n = ceil(log(u-l, 2))
    print('You have ',n,'chances to predict the number,Lets start')
    for i in range(n):
        b = int(input('Enter a number '))
        if b < a:
            print('The entered number is less than the target number ')
        elif b > a:
            print('The entered number is greater than the target number ')
        else:
            print('Congratulations!!! YOU WON the Game')
            break
    else:
        print('Oh NO! You lost the Game!')
else:
    print('Ok Bye')