#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len([s for s in S if s in J])
