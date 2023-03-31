InputText = input().strip()

def ChuoiDoiXung(InputText):
    for i in range(0, len(InputText)):
        if(InputText[i] != InputText[len(InputText) - 1 - i]):
            return False
    return True

print(ChuoiDoiXung(InputText))