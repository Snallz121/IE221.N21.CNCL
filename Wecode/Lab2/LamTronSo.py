a,n = input().split()
a = float(a)
n = int(n)
a = round(a*n) / n
print({'%.10g'}%a)