from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for val in s:
            if val in dic_s:
                dic_s[val] += 1
            else:
                dic_s[val] = 1
        for val in t:
            if val in dic_t:
                dic_t[val] += 1
            else:
                dic_t[val] = 1
        return dic_s == dic_t


print(Solution().isAnagram(input(), input()))
