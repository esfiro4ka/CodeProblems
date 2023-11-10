class Solution:
    def reverse(self, x: int) -> int:
        
        minimum = -2**31
        maximum = 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x *= sign

        reversed_str = str(x)[::-1]

        reversed_x = int(reversed_str) * sign

        if reversed_x < minimum or reversed_x > maximum:
            return 0
        
        return reversed_x
