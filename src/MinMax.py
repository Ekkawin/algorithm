a = int(input())

min = 0
max = 0
initialMin = 0
for i in range(0, a):
    newVal = int(input())
    if i == 0:
        min = newVal
        max = newVal
    else:
        if newVal > max:
            max = newVal
        if newVal < min:
            min = newVal

print(min)
print(max)
