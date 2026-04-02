class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable={}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                hashtable[nums[i]]+=1
            else:
                hashtable[nums[i]]=1
        
        max_count = max(hashtable.values())
        for key, value in hashtable.items():
            if value == max_count:
                return key

        