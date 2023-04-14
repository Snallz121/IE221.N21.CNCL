m, n = map(int, input().split())
res = 1

def MyPow(m, n):
    if(n == 0):
        return 1
    if(n % 2 == 0):
        return MyPow(m, n // 2) ** 2
    else:
        return MyPow(m, n - 1) * m
    
print(MyPow(m, n))