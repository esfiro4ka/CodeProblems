def digital_root(n):
    str_n = str(n)
    if len(str_n) > 1:
        sum_n = 0
        for i in str_n:
            sum_n += int(i)
        return digital_root(sum_n)
    else:
        return n


input_string = '511'  # input_string = input()
result = digital_root(int(input_string))
print(result)

# '511' => 7
# '942' => 9 + 4 + 2 => 15 => 1 + 5 => 6
# '760301' => 8
# '132189' => 6
