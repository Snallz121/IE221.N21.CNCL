count = 3;
NeedSortList = [];

while(count > 0):
    inputText = float(input())
    NeedSortList.append(inputText)
    count -= 1
NeedSortList.sort()

for i in NeedSortList:
    print('{0:g}'.format(i), end=" ")
