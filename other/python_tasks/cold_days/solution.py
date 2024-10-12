def get_cold_days(temperatures):
    temperatures_list = list(map(int, temperatures.split()))
    results = []
    for i in range(0, len(temperatures_list) - 1):
        if temperatures_list[i] - temperatures_list[i+1] >= 3:
            results.append(i+1)
    if results == []:
        return 'Нет'
    else:
        return sorted(results)


temperatures = '-20 -30 -40'  # temperatures = input()
cold_days = get_cold_days(temperatures)
print(cold_days)  # 1 2

# 0 5 2 7 4 1 => 2 4 5
# 10 8 6 4 2 0 -2 -4 => Нет
# 10 5 0 -5 -10 -15 -20 => 1 2 3 4 5 6
