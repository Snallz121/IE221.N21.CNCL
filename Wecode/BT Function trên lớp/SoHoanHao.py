import sys
InputText = int(sys.stdin.readline())
def isPerfectNumber(InputText):
    sum = 0
    for i in range(1, int(InputText ** (1/2)) + 1):
        if InputText % i == 0:
            sum += i
            if(InputText // i != i):
                sum += InputText // i
    sum -= InputText
    if(sum == InputText):
        return True
    return False
print(isPerfectNumber(InputText))