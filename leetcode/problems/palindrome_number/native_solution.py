class Solution:
    def isPalindrome(self, x):
        x = str(x)
        y = len(x)
        for i in range(0, len(x)):
            if x[i] == x[y-1]:
                y = y - 1
            else:
                return False
        return True


x = 121
solution = Solution()
result = solution.isPalindrome(x)
print(result)
