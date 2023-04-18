import sys
m, n = map(int, sys.stdin.readline().split())

def MyPow(m, n):
    if(n == 0):
        return 1
    if(n % 2 == 0):
        return MyPow(m, n // 2) ** 2
    else:
        return MyPow(m, n - 1) * m
sys.stdout.write(str(MyPow(m, n) % 1000000007))