from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # OK. Let me ask you some questions to confirm my understanging.
        # 与えられる配列の要素は、すべて整数であると考えていいですか？(Can I assume that all elements of the given array are integers?)
        # この配列は、空出ないと考えていいですか？(and can I assume that the array is not empty?)
        # この配列の範囲は、どのくらいですか？(What is the range of this array?)

        # まず、配列をソートしてみましょうか？(First, let's try sorting the array.)
        # ソートした後、先頭から順番に要素を数えてみましょうか？(After sorting, let's count the elements from the beginning in order.)
        sorted_nums = sorted(nums)
        current_num = sorted_nums[0]
        counter = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != current_num:
                current_num = sorted_nums[i]
                counter = 1
            else:
                counter += 1
                return True
        return False

print(Solution().containsDuplicate(list(map(int, input().split()))))
