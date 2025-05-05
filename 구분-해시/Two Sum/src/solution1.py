class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums[:-1]):
            find = target-num
            remain = nums[i+1:]
            if find in remain:
                return [i, i+1+remain.index(find)]


if __name__ == '__main__':
    solution = Solution()
    output = solution.twoSum([2, 7, 11, 15], 9)
    print(output)
