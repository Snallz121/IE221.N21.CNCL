import sys
InputText = int(sys.stdin.readline())
sum = 0
for i in range(1, int(InputText ** (1/2)) + 1):
    if InputText % i == 0:
        sum += i
        if(InputText // i != i):
            sum += InputText // i
sum = sum - InputText
print(sum)
