# Временная сложность:
# Создание и обновление словаря: O(n), где n — суммарное количество элементов
# в items1 и items2.
# Сбор результатов в список: O(m), где m — количество уникальных ключей.
# Сортировка списка: O(m log m), где m — количество уникальных ключей.
# Общая временная сложность алгоритма составляет O(n + m log m), где
# n — общее количество элементов в items1 и items2,
# а m — количество уникальных ключей.

class Solution:
    def mergeSimilarItems(self, items1, items2):
        count = {}
        for item in items1:
            count[item[0]] = item[1]
        for item in items2:
            if item[0] not in count.keys():
                count[item[0]] = item[1]
            else:
                count[item[0]] += item[1]
        result = []
        for key, value in count.items():
            new_element = [key, value]
            result.append(new_element)
        result.sort()
        return result

# Если нужно избежать сортировки в конце, можно использовать структуру данных,
# которая хранит элементы отсортированными, например, collections.OrderedDict.
# Но такие структуры могут усложнить код и в данном случае не дадут большого
# выигрыша в производительности.


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
solution = Solution()
result = solution.mergeSimilarItems(items1, items2)
print(result)
# result = [[1, 6], [3, 9], [4, 5]]
