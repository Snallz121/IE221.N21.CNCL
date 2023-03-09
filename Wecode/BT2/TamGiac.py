import math
def ReturnResultFunction(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    p = (a+b+c) / 2
    res = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("{:.2f}".format(res))

textInput = str();
secondTextInput = str();
thirdTextInput = str();

textInput = input().strip().split()
if(len(textInput) == 3):
    a,b,c = textInput[0],textInput[1], textInput[2]
    ReturnResultFunction(a,b,c)
else:
    secondTextInput = input().strip()
    thirdTextInput = input().strip()
    ReturnResultFunction(textInput[0], secondTextInput, thirdTextInput)