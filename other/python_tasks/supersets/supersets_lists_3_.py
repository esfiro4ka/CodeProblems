def list_superset(list_set_1, list_set_2):
    if len(list_set_1) > len(list_set_2):
        superset, subset = list_set_1, list_set_2
    else:
        superset, subset = list_set_2, list_set_1

    all_elements_present = True

    for elem in subset:
        if elem not in superset:
            all_elements_present = False
            break

    if all_elements_present:
        if len(superset) == len(subset):
            return 'Наборы равны.'
        else:
            return f'Набор {superset} - супермножество.'
    else:
        return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))  # 'Набор [1, 3, 5, 7] - супермножество.'
print(list_superset(list_set_2, list_set_3))  # 'Набор [5, 3, 7, 1] - супермножество.'
print(list_superset(list_set_1, list_set_3))  # 'Наборы равны.'
print(list_superset(list_set_2, list_set_4))  # 'Супермножество не обнаружено.'
