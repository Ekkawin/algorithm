numbers = []
plus = 0
for i in range(9):
    x = int(input())
    numbers.append(x)
    plus = plus+x

left = plus - 100

for i in numbers:
    for j in numbers:
        if i == j:
            continue
        if i + j == left:
            numbers.remove(i)
            numbers.remove(j)



for i in numbers:
    print(i)



