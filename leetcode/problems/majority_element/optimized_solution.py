# Для нахождения элемента, который встречается более чем ⌊n/2⌋ раз,
# можно использовать алгоритм Boyer-Moore Voting Algorithm, который работает за
# O(n) времени и O(1) пространства.

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            # if num == candidate:
            #     count += 1
            # else:
            #     count -= 1

        return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
result = solution.majorityElement(nums)
print(result)
