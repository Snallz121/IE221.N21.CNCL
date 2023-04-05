dong = int(input())
cot = int(input())
OfficialMatrix = []
for i in range(dong):
    tmpMatrix = []
    for j in range(cot):
        tmpMatrix.append(i * j)
    OfficialMatrix.append(tmpMatrix)
print(OfficialMatrix)
