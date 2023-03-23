InputText = int(input())
res = ""

for i in range(1, InputText + 1):
    res += str(i)
print(res[InputText - 1])