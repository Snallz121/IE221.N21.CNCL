InputText = input()

def ThongKe(InputText):
    NumberOfWord = len(InputText)
    NumberOfUpperWord = 0
    NumberOfLowerWord = 0
    InputText = InputText.split("")
    for i in InputText:
        if(i.isupper() == True):
            NumberOfUpperWord += 1
        elif(i.islower()):
            NumberOfLowerWord += 1
    
    return NumberOfWord, NumberOfUpperWord, NumberOfLowerWord, InputText


print(ThongKe(InputText))