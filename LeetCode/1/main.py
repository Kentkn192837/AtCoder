from typing import List
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i, val in enumerate(nums):
            complentement = target - val
            if complentement in dic:
                return [dic[complentement], i]
            dic[val] = i


print(Solution().twoSum(list(map(int, input().split(","))), int(input())))
