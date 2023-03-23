n,m,h,w = map(int, input().strip().split())
count = 0
def swap(a,b):
    if(a < b):
        tmp = a
        a = b
        b = tmp
    return a, b
if(h < w):
    h, w = swap(h,w)
while(h < n):
    h = h * 2
    count += 1
while(w < m):
    w = w * 2
    count += 1

print(count)