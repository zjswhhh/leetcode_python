#!/usr/bin/python
# -*- coding: UTF-8 -*-

class KthLargest(object):
    
    def __init__(self, k, nums):
        """
            :type k: int
            :type nums: List[int]
        """
        self.k = k
        self.pool = nums
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1


    def add(self, val):
        """
            :type val: int
            :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif self.pool[0] < val:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
