#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Score(object):

    def __init__(self, num):
        self.num = num

    def double(self):
        return self.num * self.num


s = Score(10)
d = s.double()
print(s.num)
print(d)
# print(d.__self__)
# print(d.__self__.num)