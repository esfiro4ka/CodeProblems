def func(my_tuple):
    result = 0
    for i in range(0, len(my_tuple)):
        if type(my_tuple[i]) is str:
            return i
        else:
            result += my_tuple[i]
    return result


print(func((1, 2, 3, 4, 5)))
print(func((1, 2, 3.0, 4, 5)))
print(func((1, 2, "a", 4, 5)))


# 1 альтернативный вариант:
# def func(my_tuple):
#     result = 0
#     for i in range(0, len(my_tuple)):
#         if type(my_tuple[i]) is str:
#             print(f"Индекс элемента, являющегося строкой: {i}")
#             return
#         else:
#             result += my_tuple[i]
#     print(f"Сумма элементов равна {result}")


# 2 альтернативный вариант:
# def func(my_tuple):
#     result = 0
#     for i, item in enumerate(my_tuple):
#         if type(item) is str:
#             print(f"Индекс элемента, являющегося строкой: {i}")
#             return
#         elif isinstance(item, (int, float)):
#             result += item
#     print(f"Сумма элементов равна {result}")
#     return result

# func((1, 2, 3, 4, 5))
# func((1, 2, 3.0, 4, 5))
# func((1, 2, "a", 4, 5))
