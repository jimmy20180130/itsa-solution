# https://etutor2.itsa.org.tw/mod/topics/view.php?id=42613

x, y = input().split()
x = int(x)
y = int(y)
# 抄維基百科的
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(x, y))
