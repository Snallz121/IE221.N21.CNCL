NumberOfPapers = int(input())
ArrayOfIndex = list(map(int, input().strip().split()))

ArrayOfIndex.sort(reverse=True)
count = 0
for i in range(0, NumberOfPapers):
    if(ArrayOfIndex[i] > i):
        count += 1
    else:
        break

print(count)