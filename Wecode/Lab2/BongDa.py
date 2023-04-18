import sys
count = 6
InputText = []
while(count > 0):
    InputText.append(list(map(int,sys.stdin.readline().split(" "))))
    count -= 1

count = 1
Team1 = [0, 0, 0, 0]
Team2 = [0, 0, 0, 0]

def DiemSo(SoBanThang, SoBanThua):
    if(SoBanThang > SoBanThua):
        return 3
    if(SoBanThang == SoBanThua):
        return 1
    return 0

def GoalDifference(SoBanThang, SoBanThua):
    return SoBanThang - SoBanThua

def CompareTwoTeam(Team1, Team2):
    Mark1 = Team1[0] - Team2[0]
    Mark2 = Team1[1] - Team2[1]
    Mark3 = Team1[2] - Team2[2]
    Mark4 = Team1[3] - Team2[3]
    Record = (Mark1, Mark2, Mark3, Mark4)
    for i in Record:
        if(i > 0):
            return list(map(str,Team1))
        elif(i < 0):
            return list(map(str,Team2))
        else:
            continue

for i in InputText:
    if(count <= 3):
        Team1[0] += DiemSo(i[0], i[1]) 
        Team1[1] += GoalDifference(i[0], i[1]) 
        Team1[2] += i[0]
        Team1[3] += i[2]
    else:
        Team2[0] += DiemSo(i[0], i[1]) 
        Team2[1] += GoalDifference(i[0], i[1]) 
        Team2[2] += i[0]
        Team2[3] += i[2]
    count += 1

sys.stdout.write(' '.join(CompareTwoTeam(Team1, Team2)))