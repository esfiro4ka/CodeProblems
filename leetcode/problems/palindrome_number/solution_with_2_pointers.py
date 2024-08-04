class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        x = str(x)
        left_pointer, right_pointer = 0, len(x) - 1

        while left_pointer < right_pointer:
            if x[left_pointer] != x[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True


x = 1211
solution = Solution()
result = solution.isPalindrome(x)
print(result)
