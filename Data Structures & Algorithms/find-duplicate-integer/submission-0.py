class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = []
        for i in range(len(nums)):
            if nums[i] in lst:
                return nums[i]
            else:
                lst.append(nums[i])

        