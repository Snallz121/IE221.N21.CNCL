InputText = list(map(int, input().strip().split()))

if(InputText[0] < InputText[1]):
    print("max =",InputText[1],"\nmin =",InputText[0])
else:
    print("max =",InputText[0],"\nmin =",InputText[1])