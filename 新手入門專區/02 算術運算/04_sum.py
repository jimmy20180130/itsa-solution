# https://etutor2.itsa.org.tw/mod/topics/view.php?id=42595

x = int(input())
y = []

for i in range(x):
    a, b = [int(item) for item in input().split()]
    y.append([a, b])

for i in range(x):
    print(y[i][0] + y[i][1])