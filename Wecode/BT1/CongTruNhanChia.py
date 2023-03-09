def ReturnResultFunction(a, b):
    a = int(a)
    b = int(b)
    print(str(a) + " + " + str(b) + " = ",a+b)
    print(str(a) + " - " + str(b) + " = ",a-b)
    print(str(a) + " x " + str(b) + " = ",a*b)
    print(str(a) + " / " + str(b) + " = ","{:.2f}".format(a/b))

textInput = str();
secondTextInput = str();

textInput = input().strip().split()
if(len(textInput) == 2):
    a,b = textInput[0],textInput[1]
    ReturnResultFunction(a,b)
else:
    secondTextInput = input().strip()
    ReturnResultFunction(textInput[0], secondTextInput)
