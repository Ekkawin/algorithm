sort = input()
x = 1


def swap(method, x):
    if method == 'A':
        if (x == 1):
            return 2
        if (x == 2):
            return 1
    elif method == 'B':
        if (x == 2):
            return 3
        if (x == 3):
            return 2
    else:
        if (x == 3):
            return 1
        if (x == 1):
            return 3
    return x


for i in sort:

    if (sort.index(i) + 1 == len(sort)):
        print(swap(i, x))
    else:
        y = swap(i, x)
        x = y

print(x)
