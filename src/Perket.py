length = int(input())
x = []

min_dif = 1000000

for i in range(length):
    x.append(input().split())
length = len(x)
k = 0
while k < length:
    s = 1
    b = 0
    for j in range(len(x)):
        s = s * int(x[j][0])
        b += int(x[j][1])
        # print("s", s)
        # print("b", b)
        if b - s < min_dif and b-s >= 0:
            min_dif = b - s
    val = x[k]
    x.remove(val)
    x.append(val)
    k += 1

print(min_dif)
