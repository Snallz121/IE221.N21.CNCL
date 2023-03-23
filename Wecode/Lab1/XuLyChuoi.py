InputText = input().lower()
res = ""
for i in range(0, len(InputText)):
    if(InputText[i] == "a" or InputText[i] == "o" or InputText[i] == "y" or InputText[i] == "e" or InputText[i] == "u" or InputText[i] == "i"):
        continue
    else:
        res += "." + InputText[i]
print(res)
