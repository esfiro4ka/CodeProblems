# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


nums = [1, 3, 5, 6]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)
print(result)
