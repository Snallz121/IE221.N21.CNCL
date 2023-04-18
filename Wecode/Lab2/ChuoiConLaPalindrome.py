import sys
def isPalindrome(InputText):
    for i in range(0, len(InputText)):
        if(InputText[i] != InputText[len(InputText) - 1 - i]):
            return False
    return True;

count = 0
InputText = sys.stdin.readline().strip()

for i in range(0, len(InputText)):
    for j in range(i+1, len(InputText) + 1):
        if(isPalindrome(InputText[i:j]) == True):
            count += 1
print(count) 