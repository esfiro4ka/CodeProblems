# https://dmoj.ca/problem/coci18c4p1

wizard = input()

number_of_duels = int(input())

number_of_wizards = 1

wizards_list = []

wizards_list.append(wizard)

for i in range(number_of_duels):
    defeats = input()
    if wizard != defeats[0] and wizard == defeats[2]:
        wizard = defeats[0]
        if wizard not in wizards_list:
             wizards_list.append(wizard)

print(f'{wizard}')
print(len(wizards_list))
