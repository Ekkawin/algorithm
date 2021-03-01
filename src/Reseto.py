x = input().split()

num = int(x[0])
length = int(x[1])
arrX = []
count = 0
ans = 0
divider = 0

for i in range(0, num - 1):
    arrX.append(i + 2)

while count < length:
    divider = arrX[0]
    for j in arrX:
        if j % divider == 0:
            arrX.remove(
            count += 1

            if count == length:
                ans = j

print(ans)
