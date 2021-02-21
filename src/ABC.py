inputs = input().split()
sorter = input()

for i in range(0, len(inputs) - 1):
    for j in range(0, len(inputs) - 1):
        if (int(inputs[j]) > int(inputs[j + 1])):
            new = inputs[j]
            inputs[j] = inputs[j + 1]
            inputs[j + 1] = new



for x in sorter:
    index = sorter.index(x)
    endWord = " "
    if (index == 2):
        endWord = ""
    
    if (x == 'A'):
        print(inputs[0], end=endWord)
    elif (x == 'B'):
        print(inputs[1], end=endWord)
    else:
        print(inputs[2], end=endWord)
