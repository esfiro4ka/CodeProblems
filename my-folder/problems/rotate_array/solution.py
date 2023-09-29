class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(0, k):
        #     nums [:] = [nums[-1]] + nums[:-1]
            
        k = k % len(nums)
        if k > 0 :
            nums[:] = nums[-k:] + nums[:-k]