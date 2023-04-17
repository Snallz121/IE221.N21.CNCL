import sys

InputText = sys.stdin.readline().split("\n")[0]
a = float(InputText.split()[0])
n = int(InputText.split()[1])

print('%.10g' % (round(a * n) / n))
