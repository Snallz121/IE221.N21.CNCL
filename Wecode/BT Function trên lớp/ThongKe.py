InputText = input()

def ThongKe(InputText):
    NumberOfWord = len(InputText)
    NumberOfUpperWord = 0
    NumberOfLowerWord = 0
    for i in InputText:
        if(i.isupper() == True):
            NumberOfUpperWord += 1
        elif(i.islower()):
            NumberOfLowerWord += 1
    print(InputText.strip())
    return NumberOfWord, NumberOfUpperWord, NumberOfLowerWord


print(ThongKe(InputText))