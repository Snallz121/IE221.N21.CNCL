Can = ["CANH", "TAN", "DINH", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]

Giap = ["THAN", "DAU", "TUAT", "HOI", "TY'", "SUU", "DAN", "MEO", "THIN", "TY.", "NGO", "MUI"]

InputYear = int(input())
if(InputYear < 0):
    InputYear *= -1
    IndexOfCan = InputYear % 10
    IndexOfGiap = InputYear % 12
    print(Can[len(Can)- IndexOfCan], Giap[len(Giap)-IndexOfGiap])
else:
    IndexOfCan = InputYear % 10
    IndexOfGiap = InputYear % 12

    print(Can[IndexOfCan], Giap[IndexOfGiap]) 