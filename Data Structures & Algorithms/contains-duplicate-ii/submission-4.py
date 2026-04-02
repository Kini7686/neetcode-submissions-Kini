class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,min(((i+1)+k),len(nums))):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                # elif nums[i]==nums[j] and abs(i-j)>k:
                #     return False
                # else:
                #     continue
        return False
            

        