# -*- coding: utf-8 -*-

import math

n1 = 255
n2 = 1000

print(hex(n1), (n2))

# ax2 + bx + c = 0 explain x
def quadratic(a, b, c):
    try:
        if a == 0:
            if b == 0:
                print("The parameter a can't be zero, please input other values...")
            else:
                return -c/b
        elif b**2 - 4*a*c < 0:
            print("The function can't be explain, please input other values...")
        else:
            x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
            x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
            return x1, x2
    except ValueError:
        print("The parameter type has error, please check it.")

print (quadratic(0,0,1))
print (quadratic(1,1,1))
print (quadratic(0,1,3))
print (quadratic(2,3,1))
print (quadratic(1,3,-4))