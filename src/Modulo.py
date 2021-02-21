x= []
ans = []
for i in range(0,10):
    x.append(int(input()))

for j in range(0,10):
    mod = x[j] % 42
    if(mod not in ans):
        ans.append(mod)
print(len(ans))