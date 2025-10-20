# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43018

a = int(input())
b = list(map(int, input().split()))
print(*[b[i] - b[i-1] if i > 0 else b[0] for i in range(a)])
