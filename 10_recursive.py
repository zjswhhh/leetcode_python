#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        # bool(string): "" return false， else return true
        first_char = bool(text) and pattern[0] in [text[0], '.']

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:])) or (first_char and self.isMatch(text[1:], pattern))

        else:
            return first_char and self.isMatch(text[1:], pattern[1:])
