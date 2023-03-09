import math
InputArray = list(map(int, input().split()))
Max = 1
MaxNegative = -math.inf;
StoreData = []
print(type(Max))
for i in InputArray:
    if i == 0:
        continue
    elif i < 0:
        if(MaxNegative < i):
            MaxNegative = i
        Max *= i
        StoreData.append(i)
    else:
        Max *= i
        StoreData.append(i)
if(Max < 0):
    Max = int(Max / MaxNegative)
    StoreData.remove(MaxNegative)

print(Max)
for i in StoreData:
    print(i, end= " ")

