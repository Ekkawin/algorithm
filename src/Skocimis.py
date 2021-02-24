x, y, z = input().split()

xy = int(y) - int(x)
yz = int(z) - int(y)

print(max(xy, yz) - 1)
