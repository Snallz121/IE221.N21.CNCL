age = int(input())
gender = input()
gender = gender.upper()

if(age >= 21):
    if(gender == 'M'):
        print(1)
    elif(gender == 'F'):
        print(2)
    else:
        print("I do not know why")
else:
    if(gender == 'M'):
        print(3)
    elif(gender == 'F'):
        print(4)
    else:
        print("I do not know why")