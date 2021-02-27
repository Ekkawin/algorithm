length = int(input())
pattern = []
ans = list(input())
i = 0
name = [[ 'Adrian',  0], ['Bruno', 0], [ 'Goran', 0]]
# while i < length:
#     pattern.append(input())
#     i += 1


def andiran(index):
    if (index % 3 == 0):
        return 'A'
    elif (index % 3 == 1):
        return ('B')
    else:
        return 'C'

def bruno(index):
    if (index % 2 == 0):
        return 'B'
    elif (index % 4 == 1):
        return 'A'
    elif (index % 4 == 3):
        return 'C'


def goran(index):
    if (index % 6 == 0 or index % 6 == 1):
        return 'C'
    elif (index % 6 == 2 or index % 6 == 3):
        return 'A'
    elif (index % 6 == 4 or index % 6 == 5):
        return 'B'




for i in range(0,len(ans)):

    if(ans[i] == andiran(i)):
        name[0][1] += 1
    if (ans[i] == bruno(i)):
        name[1][1] += 1
    if (ans[i] == goran(i)):
        name[2][1] += 1




maxScore = max(map(lambda x: x[1], name))
print(maxScore)
for j in range(3):
    if (name[j][1] == maxScore):
        print(name[j][0])









