def list_superset(list_set_1, list_set_2):
    set_1 = set(list_set_1)
    set_2 = set(list_set_2)

    # Проверяем, равны ли множества
    if set_1 == set_2:
        return "Наборы равны."
    # Проверяем, является ли set_1 супермножеством set_2
    elif set_1.issuperset(set_2):
        return f"Набор {list_set_1} - супермножество."
    # Проверяем, является ли set_2 супермножеством set_1
    elif set_2.issuperset(set_1):
        return f"Набор {list_set_2} - супермножество."
    else:
        return "Супермножество не обнаружено."


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
