InputNumber = int(input())
res = 1
if(InputNumber % 2 == 0):
    for i in range(2, InputNumber + 2, 2):
        res *= i
else:
    for i in range(1, InputNumber + 2, 2):
        res *= i
print(res)