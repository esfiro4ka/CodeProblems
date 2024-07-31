# Временная сложность: буквально O(2n), так как два цикла, или упрощенно O(n)
# при сокращении констант для обоих циклов.
# Пространственная сложность: O(n) для словаря count.


class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key in count.keys():
            if count[key] >= len(nums)/2:
                return key


nums = [2, 2, 1, 1, 1, 2, 2]

solution = Solution()
result = solution.majorityElement(nums)
print(result)
