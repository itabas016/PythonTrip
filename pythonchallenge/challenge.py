__author__ = 'Roger'


def add(a, b):
    print "ADDING %d + %d" % (a, b)
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
	if a < 0:
		return -1
	elif a == 0:
		return 1
	else:
		if b > 0:
			s = 1
			for i in range(1, b - 1):
				s = s * a
				i = i + 1
			return s
		elif b == 0:
			return 1
		else:
			t = 1
			for j in range(1, b + 1):
				t = t * 1 / a
				j = j + 1
			return t


power(2, 1)
power(2, -3)
power(2, 38)
"""274877906944"""

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def move(list, n):
	if isinstance(list) & len(list) > 0:
		dest_array = array
		for i in list:
			dest_array[i] = array[array.index(list[i]) + n]
			i = i + 1
		return dest_array
	else:
		return ""