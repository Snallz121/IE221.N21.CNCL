n,x = map(int,input().split())
count = 0

if(n**2 < x):
    print(0)
else:
    if(n >= x):
        start = 1
    else: 
        start = 2
    end = n + 1
    for i in range(start, end):
        if(x / i < 1):
            break
        if(x % i == 0):
            if(x / i <= n):
                count += 1
    print(count)