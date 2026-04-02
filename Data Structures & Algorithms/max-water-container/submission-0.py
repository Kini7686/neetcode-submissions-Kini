class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        arr=[]
        while l<r:
            a=min(heights[l],heights[r])*(r-l)
            arr.append(a)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max(arr)
        