#!/usr/bin/python
# -*- coding: UTF-8 -*-


def threeSum(nums):
    """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
            
    res = []
    nums.sort()
        
    for k in range(len(nums)):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue
            
        i, j = k + 1, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < - nums[k]:
                i += 1
            else:
                j -= 1


    return res

nums = [-1, 0, 1, 2, -1, -4]
print threeSum(nums)
