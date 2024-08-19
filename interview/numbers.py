def func():
    for i in range(0, 1001):
        if i % 3 == 0 and i % 5 != 0:
            str_number = str(i)
            summa = 0
            for j in str_number:
                summa += int(j)
            if summa < 10:
                print(i)


func()
