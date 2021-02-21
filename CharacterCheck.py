isHasUpper = False
isHasLower = False

word = input()

for i in word:
    if (isHasUpper and isHasLower):
        break
    if (i.isupper()):
        isHasUpper = True
    if (i.islower()):
        isHasLower = True


def characterCheck() :
    if (isHasUpper and isHasLower):
        print("Mix")
    elif (isHasUpper):
        print("All Capital Letter")
    else:
        print("All Small Letter")

characterCheck()