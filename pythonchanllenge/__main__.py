__author__ = 'cuir'


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
				t = t * 1/a
				j = j + 1
			return t

power(2, 1)
power(2, -3)