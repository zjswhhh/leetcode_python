#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

class NumArray(object):
    def __init__(self, nums):
        self.item = nums
        if(len(nums)>0):
            self.n = len(nums)
            self.tree = [ 0 for i in range(self.n*2)]
            for i in range(self.n, self.n*2):
                self.tree[i] = nums[i-self.n]
            for i in range(self.n-1, 0, -1):
                self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, i, val):
        index = i + self.n
        self.tree[index] = val
        while index > 0 :
            left = index
            right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index/2] = self.tree[left] + self.tree[right]
            index /= 2

    def sumRange(self, i, j):
        l = i + self.n
        r = j + self.n
        sum = 0
        while l <= r:
            if l % 2 == 1:
                sum += self.tree[l]
                l += 1
            if r % 2 == 0:
                sum += self.tree[r]
                r -= 1
            l /= 2
            r /= 2
        return sum




"""
test case: 
"""
te = NumArray([9, -8])
te.update(0,3)
print(te.sumRange(1, 1))
print(te.sumRange(0, 1))
te.update(1, -3)
print(te.sumRange(0, 1))
