class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                suma=sum(nums[i:j+1])
                if suma> maxi:
                    maxi=suma
        return maxi

        