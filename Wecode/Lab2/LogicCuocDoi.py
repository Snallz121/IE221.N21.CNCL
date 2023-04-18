tre_trung, xinh_dep, co_gau, giau_co = map(int,input().split())

if(xinh_dep == 0 and co_gau == 1 and giau_co == 1):
    if(tre_trung == 0):
        print(0)
    else:
        print(1)
else:
    if(tre_trung == 1 and xinh_dep == 1):
        print(1)
    elif(xinh_dep == 1 and co_gau == 1):
        print(1)
    else:
        print(0)