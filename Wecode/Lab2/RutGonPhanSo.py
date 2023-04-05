import math
WorkCount = int(input())

while(WorkCount > 0):
    tu, mau = map(int, input().split())
    k = math.gcd(tu,mau)
    tu /= k
    mau /= k
    tu = int(tu); mau = int(mau)
    if(mau > 1):
        print(tu, mau)
    else:
        print(tu)
    WorkCount -= 1
    