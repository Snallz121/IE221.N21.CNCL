count = 5
InputArray = []
while(count > 0):
    InputArray.append(input().strip().split())
    count -= 1

center = [2,2]
pos = []
for i in range(0,5):
    for j in range(0,5):
        if(InputArray[i][j] == "1"):
            pos.append(i)
            pos.append(j)
res = 0
while(pos[0] != center[0]):
    if(pos[0] > center[0]):
        pos[0] -= 1
        res += 1
    else:
        pos[0] += 1
        res += 1

while(pos[1] != center[1]):
    if(pos[1] > center[1]):
        pos[1] -= 1
        res += 1
    else:
        pos[1] += 1
        res += 1

print(res)