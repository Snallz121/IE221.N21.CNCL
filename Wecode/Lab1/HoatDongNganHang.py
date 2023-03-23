count = int(input())
sum = 0
for i in range(0, count):
    InputText = input().strip().split()
    if(InputText[0] == "D"):
        sum += int(InputText[1])
    else:
        sum -= int(InputText[1])
print(sum)