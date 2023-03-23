n = int(input())
InputArray = list(map(int, input().strip().split()))

InputArray.sort()
Possible1, Possible2 = abs(InputArray[n-1] - InputArray[1]), abs(InputArray[n-2] - InputArray[0])

if(Possible1 < Possible2):
    print(Possible1)
else:
    print(Possible2)
