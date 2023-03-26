n,m,h,w = map(int, input().strip().split())
count = 0
def swap(a,b):
    if(a < b):
        tmp = a
        a = b
        b = tmp
    return a, b

if(h > w):
    if(n < m):
        n,m = swap(n,m)
else:
    if(n > m):
        n,m = swap(n,m)

while(True):
    if(n <= h and m <= w):
        break;
    if(n < m):
        n, m = swap(n, m)
    while(n > h):
        n /= 2
        count += 1
    while(m > w):
        m /= 2
        count += 1
print(count)