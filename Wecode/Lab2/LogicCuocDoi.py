tre_trung, xinh_dep, co_gau, giau_co = map(int,input().split())

flag = bool()

def Logic(a, b):
    if(a == 1 and b == 1):
        return True
    else:
        return False

def BinhLogic(tre_trung, xinh_dep, co_gau, giau_co):
    if(xinh_dep == 0 and Logic(giau_co, co_gau) == True):
        return 1
    flag = Logic(tre_trung, xinh_dep)

    if(flag == False):
        return 0
    else:
        flag = Logic(xinh_dep, co_gau)
        if(flag == False):
            return 0
        else:
            return 1
print(BinhLogic(tre_trung, xinh_dep, co_gau, giau_co))