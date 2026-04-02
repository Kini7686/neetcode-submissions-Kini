class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=int(k %len(nums) )
        nums[:] = nums[::-1]
        nums[0:k]=nums[0:k][::-1]
        # return nums
        nums[k:]=nums[k:][::-1]
        # return nums
        

        