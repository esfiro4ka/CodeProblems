# Проход по элементам в обоих списках: O(n), где n — общее количество
# элементов в items1 и items2.
# Преобразование словаря в список и его сортировка: O(m log m),
# где m — количество уникальных ключей.

class Solution:
    def mergeSimilarItems(self, items1, items2):
        from collections import defaultdict
        count = defaultdict(int)

        for item in items1:
            count[item[0]] = item[1]

        # (defaultdict автоматически создает запись с начальным значением
        # по умолчанию, если ключ еще не существует в словаре. поэтому
        # в отличие обычного словаря, существование ключа проверять не надо)

        for item in items2:
            count[item[0]] += item[1]

        result = sorted([[key, value] for key, value in count.items()])

        return result


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
solution = Solution()
result = solution.mergeSimilarItems(items1, items2)
print(result)
# Ожидаемый результат: [[1, 6], [3, 9], [4, 5]]
