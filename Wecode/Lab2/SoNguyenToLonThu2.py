InputNum = int(input())
flag = -1
res = int()

def isElement(num):
    for i in range(2, int(num**0.5) + 1):
        if(num % i == 0):
            return False
    return True

for i in range(InputNum, -1, -1):
    if(isElement(i) == True):
        if(flag == 1):
            res = i
            break
        flag = 1
print(res)