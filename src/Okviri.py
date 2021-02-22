word = input()
length = len(word)


def firstLine():
    for i in range(0, length):
        if (i == 0):
            print(".", end='')

        if (i % 3 == 2):
            print(".*..", end='')
        else:
            print(".#..", end='')
    print()


def secondLine():
    for i in range(0, length):
        if (i == 0):
            print(".", end='')
        if (i % 3 == 2):
            print("*.*.", end='')
        else:
            print("#.#.", end='')
    print()


def midLine():
    for i in range(0, length):
        if (i == 0):
            print("#."+word[i]+'.#', end='')
        if (i % 3 == 2):
            print("*." + word[i] + ".*", end='')
        elif (i != 0 and i % 3 == 0):
            print("." + word[i] + ".#", end='')
        elif( i != 0  and i % 3 == 1 ):
            print("."+word[i]+".", end='')
        if (length % 3 == 2 and i == length-1 and i % 3 == 1):
            print("#", end='')
    print()


firstLine()
secondLine()
midLine()
secondLine()
firstLine()
