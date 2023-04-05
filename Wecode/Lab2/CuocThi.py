n, k = map(int,input().split())
InputArr = list(map(int,input().split()))

pos = InputArr[k - 1]
count = 0

for i in InputArr:
    if(i > 0):
        if(i >= pos):
            count += 1
print(count)