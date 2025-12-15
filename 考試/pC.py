n = int(input())
scores = []
for i in range(n):
    scores.append(input().split(' '))

result = {}

sorts = []

for i in scores:
    total = int(i[0])*4 + int(i[1])*3 + int(i[2])*2 + int(i[3])*1
    result[total] = i
    sorts.append(total)

sorts.sort(reverse=True)

for i in sorts:
    b = ' '.join(result[i])
    print(f'{i} {b}')
