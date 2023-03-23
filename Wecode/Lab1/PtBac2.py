a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c
if(a == 0):
    print("PTVN")
else:
    if(delta < 0):
        print("PTVN")
    elif(delta == 0):
        x = -b / (2*a)
        print("PT co nghiem kep: x1 = x2 = %g" % x)
    else:
        print("PT co hai nghiem phan biet:")
        x1 = (-b + delta ** (1/2)) / (2*a)
        x2 = (-b - delta ** (1/2)) / (2*a)
        print("x1 = %g" % x1)
        print("x2 = %g" % x2)