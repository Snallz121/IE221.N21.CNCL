SoNguyenTo = int(input())

def isElementaryNumber(number):
    for i in range(2, int(number**0.5) + 1):
        if(number % i == 0):
            return 0
    return 1

def findSecondElementaryNumber(number):
    for i in range(number - 1, 1, -1):
        if(isElementaryNumber(i) == 1):
            return i
    return -1
print("pos: ", isElementaryNumber(SoNguyenTo))
print("Second Ele: ", findSecondElementaryNumber(SoNguyenTo))