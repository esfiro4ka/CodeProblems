class Solution:
    def mostFrequentEven(self, nums):
        count = {}
        for num in nums:
            if num % 2 == 0:
                if num not in count:
                    count[num] = 1
                else:
                    count[num] += 1
        print(count)
        most_frequent_key = 0
        most_frequent_value = 0

        for key, value in count.items():
            if value > most_frequent_value:
                most_frequent_value = value
                most_frequent_key = key
            elif value == most_frequent_value:
                if key < most_frequent_key:
                    most_frequent_key = key
        if most_frequent_value == 0:
            return -1
        # если print(most_frequent_key),
        # функция вернет None
        else:
            return most_frequent_key


nums = [0, 1, 4, 4, 2, 2, 1]
# nums = [29, 47, 21, 41, 13, 37, 25, 7]
solution = Solution()
result = solution.mostFrequentEven(nums)
print(result)
