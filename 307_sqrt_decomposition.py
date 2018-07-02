#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

class NumArray(object):

    def __init__(self, nums):
        """
        l: size of each block
        n: number of block
        s: block sum
        """

        size = len(nums)
        self.item = nums
        if not size == 0:
            self.l = int(math.sqrt(size))
            n = int(math.ceil(size/self.l))

            self.s = [0 for i in range(n+1)]

            for i in range(size):
                self.s[i//self.l] += nums[i]

    def update(self, i, val):
        self.s[i//self.l] = self.s[i//self.l] - self.item[i] + val
        self.item[i] = val

    def sumRange(self, i, j):
        sum = 0
        start = i//self.l
        end = j//self.l

        if start == end:
            for k in range(i, j+1):
                sum += self.item[k]
        else:
            for k in range(i, (start+1)*self.l):
                sum += self.item[k]
                print(self.item[k], 1)
            for k in range(end*self.l, j+1):
                sum += self.item[k]
                print(self.item[k], 2)
            for k in range(start+1, end):
                sum += self.s[k]
                print(self.s[k], 3)

        return sum


"""
test case: 
te = NumArray([9, -8])
te.update(0,3)
print(te.sumRange(1, 1))
print(te.sumRange(0, 1))
te.update(1, -3)
print(te.sumRange(0, 1))
"""
