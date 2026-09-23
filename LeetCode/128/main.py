from typing import List
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_consecutive_length = 0
        num_set = set(nums)
        # 数字一つずつを見ていく
        for num in nums:
            if num not in num_set:
                continue
            num_set.remove(num)
            current_consecutive_length = 1
            # 探索中の値に対して、＋方向に連続している値があるかどうかを確認する
            i = 1
            while num + i in num_set:
                num_set.remove(num + i) # 探索した値はnum_setから削除することで、同じ連続列を複数回確認することを防ぐ
                current_consecutive_length += 1
                i += 1
            # 同様に、－方向にも探索する
            i = 1
            while num - i in num_set:
                num_set.remove(num - i) # 探索した値はnum_setから削除することで、同じ連続列を複数回確認することを防ぐ
                current_consecutive_length += 1
                i += 1
            max_consecutive_length = max(max_consecutive_length, current_consecutive_length) # ある値に対する探索が終わったら、最大連続長を更新する
        return max_consecutive_length
"""
ポイント:
1. 探索自体は愚直に配列の値を一個ずつ取り出すが、探索済みの値はnum_setから削除することで、同じ連続列を複数回確認することを防ぐ
"""

print(Solution().longestConsecutive(list(map(int, input().split(",")))))
