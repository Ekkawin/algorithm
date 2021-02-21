a = int(input(""))
b = int(input(""))
c = int(input(""))


def grading(x, y, z):
    score = 0
    if x <= 30:
        score += x
    else:
        score += 30
    if y <= 30:
        score += y
    else:
        score += 30

    if z <= 40:
        score += z
    else:
        score += 40

    if (score >= 80):
        print("A")
    elif (score > 75):
        print("B+")
    elif (score >= 70):
        print("B")
    elif (score >= 65):
        print("C+")
    elif (score >= 60):
        print("C")
    elif (score >= 55):
        print("D+")
    elif (score >= 50):
        print("D")
    else:
        print("F")


grading(a, b, c)
