my_list = []
for i in range(0, 101):
    my_list.append(i)


def func(my_list):
    for i in my_list:
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz", i)
        elif i % 3 == 0:
            print("fizz", i)
        elif i % 5 == 0:
            print("buzz", i)


func(my_list)
