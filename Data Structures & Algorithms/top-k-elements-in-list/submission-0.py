class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable={}
        lst=[]
        for i in range(len(nums)):
            if nums[i] in hashtable:
                hashtable[nums[i]]+=1
            else:
                hashtable[nums[i]]=1
        # print(hashtable)
        sorted_items = sorted(hashtable.items(), key=lambda x: x[1], reverse=True)
        lst = []
        for i in range(k):
            lst.append(sorted_items[i][0])

        return lst

        