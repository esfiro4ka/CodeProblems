class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. если создать новый список:
        
        # new_list = [0] * len(nums)
        # index = 0
        # for e in nums:
        #     if e != 0:
        #         new_list[index] = e
        #         index += 1
        # return new_list
        
        
        # 2. если не создавать новый список (в соответствии с условиями задачи):
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1