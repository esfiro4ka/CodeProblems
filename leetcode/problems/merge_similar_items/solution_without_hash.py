# Этот подход позволяет обойтись без использования словарей, но он требует
# сортировки списка и дополнительного прохода по нему, что увеличивает
# временную сложность до O(n log n), где n — это сумма длин двух входных
# списков.
# В то время как использование словаря позволяло решить задачу за O(n).

class Solution:
    def mergeSimilarItems(self, items1, items2):
        combined = items1 + items2
        combined.sort()
        result = []
        current_key = combined[0][0]
        current_value = combined[0][1]

        for i in range(1, len(combined)):
            key, value = combined[i]
            if key == current_key:
                current_value += value
            else:
                result.append([current_key, current_value])
                current_key = key
                current_value = value

        # Добавляем последний элемент
        result.append([current_key, current_value])

        return result


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
solution = Solution()
result = solution.mergeSimilarItems(items1, items2)
print(result)
# result = [[1, 6], [3, 9], [4, 5]]
