rowcols = input().split()
row = int(rowcols[0])
col = int(rowcols[1])
mat1 = []
mat2 = []
sum = []
for i in range(0, int(row)):
    mat1.append([])
    mat2.append([])
    sum.append([0] * col)

for i in range(0, int(row)):
    newVals = input().split()
    mat1[i] = newVals

for i in range(0, int(row)):
    newVals = input().split()
    mat2[i] = newVals

for i in range(0, int(row)):
    for j in range(0, int(col)):
        sum[i][j] = int(mat1[i][j]) + int(mat2[i][j])
        print(sum[i][j], end=" ")
    print("\n", end="")


