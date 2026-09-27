from typing import List
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i, val in enumerate(nums):
            complentement = target - val
            if complentement in dic:
                return [dic[complentement], i]
            dic[val] = i
"""
問題の制約から、解は必ず一つ存在することが保証されているので、見つかった時点で返すようにしている。
"""

print(Solution().twoSum(list(map(int, input().split(","))), int(input())))
