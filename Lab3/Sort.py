Require = "1, 6, 7, 14, 8, 20, 11, 15, 16, 23, 21, 27, 4, 9, 10, 17, 18, 19, 22, 24, 25"
Additional = "29, 30, 31"
All = Require + ", " + Additional
Require = list(map(int, Require.split(", ")))
All = list(map(int, All.split(", ")))
All.sort()
Require.sort()
Remain = [];

for i in range(1, 32):
    if i not in All:
        Remain.append(i)
print("Require:")
for i in Require:
    print(i, end=" ")
print()
print("Remain:")
for i in Remain:
    print(i, end=" ")