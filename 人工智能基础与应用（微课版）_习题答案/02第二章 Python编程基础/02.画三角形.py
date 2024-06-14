i = 1
while i < 10:
    print(' ' * (10 - i) + '*' * (2 * i - 1))
    i+=1

for j in range(1,10):
    if j < 10:
        print((' ' * (9 - j)) + '*' *(2 * j - 1))