class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=(x+1)//2
        max_ans = float('-inf')
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                max_ans = max(max_ans,mid)
                l = mid + 1
        
        return max_ans
        
            
        