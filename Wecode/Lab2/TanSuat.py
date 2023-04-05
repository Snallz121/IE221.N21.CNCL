WorkCount = int(input())

while(WorkCount > 0):
    n, k = map(int, input().split())
    InputArr = list(map(float,input().split()))
    count = 0
    for i in InputArr:
        if(i == k):
            count += 1
    print(count)
    WorkCount -= 1
