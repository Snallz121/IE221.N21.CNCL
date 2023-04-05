InputText = input().strip().lower().split()

NormalizeName = ""

for i in InputText:
    NormalizeName += i.capitalize() + " "
print(NormalizeName)

