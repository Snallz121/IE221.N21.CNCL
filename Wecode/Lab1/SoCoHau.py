InputText = input().strip().split()
count = 0
for i in range(1, int(InputText[1]) + 1):
    tmp = str(i)
    if(tmp.rfind(InputText[0], len(tmp) - len(InputText[0])) != -1):
        count += 1
print(count)