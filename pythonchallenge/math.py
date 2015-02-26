__author__ = 'Roger'


def add(a, b):
    print 'ADDING %d + %d' % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


def power(a, b):
    print "POWERING %d ** %d" % (a, b)
    return a ** b


'''
def power(a, b):
    print "POWERING %d ** %d" % (a, b)
    if a < 0:
        if b > 0:
            s = 1
            for k in range(b):
                s = s * a
                k += 1
            if b % 2 == 0:
                return -s
            else:
                return s
        elif b == 0:
            return 1
        else:
            t = 1
            for h in range(b):
                t = t * (1 / a)
                h += 1
            return t
    elif a == 0:
        return 0
    else:
        if b > 0:
            s = 1
            for i in range(b):
                s = s * a
                i += 1
            return s
        elif b == 0:
            return 1
        else:
            t = 1
            for j in range(-b):
                t = t * divide(1, a)
                j += 1
            return t
'''
print add(1, 2)
print subtract(3, 1)
print multiply(2, 3)
print divide(8, 2)
print power(-2, 3)
print power(-2, 4)
print power(0, 2)
print power(2, 4)
print power(2, -3)
print power(-2, -3)
print power(2, 0)
