LowerBracket = int(input())
UpperBracket = int(input())

if(LowerBracket % 2 != 0):
    LowerBracket = LowerBracket + 1
if(UpperBracket % 2 == 0):
    UpperBracket = UpperBracket + 1
res = ""
for i in range(LowerBracket, UpperBracket, 2):
    res += str(i) + ","
res = res[:-1]
print(res)
