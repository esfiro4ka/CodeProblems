# https://dmoj.ca/problem/ccc11s1

count = int(input())

char_t = 0

char_s = 0

for i in range(count):
    line = input()
    for char in line:
        if char == 'T' or char == 't':
            char_t = char_t + 1
        if char == 'S' or char == 's':
            char_s = char_s + 1
if char_t > char_s:
    print('English')
if char_t <= char_s:
    print('French')
