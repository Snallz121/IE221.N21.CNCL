InputNum = int(input())

InputArr = list(map(float,input().split()))
InputArr.sort()
max = InputArr[len(InputArr) - 1]
res = 1
while(res < max):
    res *= 2
print(res)
