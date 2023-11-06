# https://dmoj.ca/problem/wc17c3j3

password = input()

ll_count = 0
ul_count = 0
d_count = 0

for i in password:
    if i.islower():
        ll_count = ll_count + 1
    if i.isupper():
        ul_count = ul_count + 1
    if i.isdigit():
        d_count = d_count + 1
    if not (i.islower() or i.isupper() or i.isdigit()):
        print('Invalid')

if 8 <= len(password) <= 12 and ll_count >=3 and ul_count >= 2 and d_count >= 1:
    print('Valid')
else:
    print('Invalid')
