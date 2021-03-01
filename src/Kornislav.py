x = input().split()
maxx =0
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])

newX = [a,b,c,d]
newX.sort()
print(newX[0] * newX[2])
