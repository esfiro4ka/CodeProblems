class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # output = []
        # for i in range(len(nums)):
        #     if nums[i] not in output:
        #         output.append(nums[i])
        # return len(output)
        count = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:                
                continue
            nums[count] = nums[i]
            count += 1
        return count