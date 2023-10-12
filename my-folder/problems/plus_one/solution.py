class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        # из списка сделать число
        for digit in digits:
            result = result * 10 + digit
        result +=1
        # из числа сделать список
        digits = []
        while result > 0:
            digit = result % 10  # Получаем последнюю цифру
            digits.insert(0, digit)  # Добавляем цифру в начало списка
            result //= 10  # Удаляем последнюю цифру
        return digits