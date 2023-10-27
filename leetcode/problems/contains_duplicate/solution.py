class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}

        for index, value in enumerate(nums):
            if value in count_dict:
                count_dict[value] += 1
            else:
                count_dict[value] = 1

        for value in count_dict.values():
            if value > 1:
                return True
        return False
    
        # unique_set = set(nums)
        # return len(unique_set) < len(nums)






        