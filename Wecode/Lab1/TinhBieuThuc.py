import math

InputText = list(map(int, input().strip().split()))
x = InputText[0] ** 5 - 2 * abs(InputText[1])** (1/2) + InputText[0] * InputText[1] * InputText[2] 

print('{:.2f}'.format(x));