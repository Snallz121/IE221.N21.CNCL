from math import factorial
 
# input n
n = int(input())
for i in range(n):
    print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()