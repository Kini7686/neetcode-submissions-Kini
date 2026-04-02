class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j]==target:
        #             return [i+1,j+1]
        l=0
        r=len(numbers)-1
        while l<r:
            mid=(l+r)//2
            curr_sum=numbers[l]+numbers[r]
            if curr_sum>target:
                r-=1
            elif curr_sum<target:
                l+=1
            else:
                return [l+1,r+1]
        