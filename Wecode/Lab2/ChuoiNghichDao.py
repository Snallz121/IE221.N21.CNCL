String1 = input().strip()
String2 = input().strip()

def PalindromeStr(String1, String2):
    for i in range(0, len(String1)):
        if(String1[i] != String2[len(String1) - 1 - i]):
            print("NO")
            return
    print("YES")
    return

PalindromeStr(String1, String2)
