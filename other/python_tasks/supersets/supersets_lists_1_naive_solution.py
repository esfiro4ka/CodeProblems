def list_superset(list_set_1, list_set_2):
    common_list = []
    max_list = []
    if len(list_set_1) > len(list_set_2):
        max_list = list_set_1
    else:
        max_list = list_set_2
    for element in list_set_1:
        if element in list_set_2:
            common_list.append(element)
    if len(list_set_1) == len(list_set_2) == len(common_list):
        return 'Наборы равны.'
    elif (len(list_set_1) == len(list_set_2)
          and len(list_set_1) != len(common_list)):
        return 'Супермножество не обнаружено.'
    elif common_list == []:
        return 'Супермножество не обнаружено.'
    return f'Набор {max_list} - супермножество.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
