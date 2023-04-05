InputText = input().strip().lower()
letter = 0
number = 0

for i in InputText:
    if(i.isalpha()):
        letter += 1
    if(i.isnumeric()):
        number += 1
print(letter)
print(number)