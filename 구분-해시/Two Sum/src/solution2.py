from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, n in enumerate(nums):
            complement = target - n
            if n in need:
                return [need[n], i]
            need[complement] = i
            