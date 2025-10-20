# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43017

a = int(input())
b = list(map(int, input().split()))

for i in range(1, len(b)):
    b[i] += b[i-1]

print(*b)
