# https://etutor2.itsa.org.tw/mod/topics/view.php?id=42594
# 參考 https://medium.com/程式乾貨/python-round-四捨五入-的小坑-7ef8accad931

from decimal import Decimal, ROUND_HALF_UP
x = int(input())
y = []
for i in range(x):
    y.append(input())

for i in range(x):
    print((Decimal(y[i])**2).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))