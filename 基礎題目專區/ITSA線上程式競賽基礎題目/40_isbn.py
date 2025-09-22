# https://etutor2.itsa.org.tw/mod/topics/view.php?id=15951

isbn = input().split(' ')
sum = 0
temp = []

for i in range(len(isbn)):
    if isbn[i] == 'X':
        isbn[i] = 10
        
    sum += int(isbn[i])
    temp.append(sum)

sum = 0

for i in temp:
    sum += i

if sum%11 == 0:
    print('YES')
else:
    print('NO')
