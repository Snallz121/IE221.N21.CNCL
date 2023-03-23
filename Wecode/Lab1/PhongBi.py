n,m,h,w = map(int, input().strip().split())
count = 0
def swap(a,b):
    if(a < b):
        tmp = a
        a = b
        b = tmp
    return a, b

while(True):
    if(n >= h and m >= w):
        break;
    while(n < h):
        h *= 2
        count += 1
    while(m < w):
        w *= 2
        count += 1
print(count)
