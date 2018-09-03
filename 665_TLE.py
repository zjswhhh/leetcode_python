#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def checkPossibility(nums):
    """
        :type nums: List[int]
        :rtype: bool
        """
    def nonDecrease(a):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                return False
        return True

        if nonDecrease(nums):
            return True
    
    for i in range(len(nums)):
        old = nums[i]
        nums[i] = nums[i-1] if i > 0 else float("-inf")
        if nonDecrease(nums):
            return True
        nums[i] = old

    return False

test = [4,2,1]
print checkPossibility(test)
