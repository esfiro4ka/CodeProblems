class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''  
        s = s.strip()  # or s = s.replace(' ', '')
        
        for i in s:
            if (i == '-' or i == '+') and not result:
                result += i
            elif i.isdigit():
                result += i
            else:
                break

        if result in ('', '-', '+'):
            return 0

        result = int(result)
        int_min, int_max = -2**31, 2**31 - 1
        result = max(int_min, min(result, int_max))
        return result