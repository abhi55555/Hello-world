n = 20
t = n // 2
for i in range(1, t + 1, 2):
    print(' ' * ((t - i) // 2) + '*' * i)

for i in range(n // 4 - 1):
    print(' ' * ((t - 1) // 2) + '@')

for i in range(n // 4 + 1):
    print(' ' * ((t - 1) // 2) + '@' + ' ' * (t - 1) + '*' * i)

print(' ' * ((t - 1) // 2) + '@', end='')

for i in range(n // 2 - 1):
    print('@', end='')

print('*' * (t // 2 + 1))

for i in range(t // 2, 0, -1):
    print(' ' * ((t - 1) // 2) + ' ' * (n // 2) + '*' * i)
