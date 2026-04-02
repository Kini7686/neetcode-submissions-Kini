class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]

        count=0
        numset=set(nums)
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                length=0
                while (nums[i] + length) in numset:
                    length+=1
                if count<length:
                    count=length
        return count
