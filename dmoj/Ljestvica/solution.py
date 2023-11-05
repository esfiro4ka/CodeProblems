# https://dmoj.ca/problem/coci12c5p1

notes = input()

C_count = 0
A_count = 0

for i in range(len(notes)):
    if i == 0 or notes[i-1] == '|':
        if notes[i] in ['C', 'F', 'G']:
            C_count = C_count + 1
        if notes[i] in ['A', 'D', 'E']:
            A_count = A_count + 1

if C_count > A_count or C_count == A_count and notes[len(notes)-1] == 'C':
    print('C-dur')
else:
    print('A-mol')
