inputText = input();
inputText.strip();
if(inputText[0] == "-"):
    inputText = inputText[1:]

if(len(inputText) == 1):
    print('true')
else:
    flag = 0;
    for i in range(0, int(len(inputText) / 2) + 1):
        if(inputText[i] != inputText[len(inputText) - 1 - i]):
            flag = 1;
            break;
    if(flag == 1):
        print('false')
    else:
        print('true')
