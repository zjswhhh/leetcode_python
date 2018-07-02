#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

# two-pass hashmap

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        ans = []
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            if map.has_key(target - nums[i]) and map[target - nums[i]] != i:
                ans.append(i)
                ans.append(map[target-nums[i]])
                break

        return ans

