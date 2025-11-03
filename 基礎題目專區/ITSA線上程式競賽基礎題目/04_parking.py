# https://etutor2.itsa.org.tw/mod/topics/view.php?id=15904

start = list(map(int, input().split(' ')))
end = list(map(int, input().split(' ')))

# 10 23
# 15 20

timePassed = 60*(end[0]-start[0]) + (end[1] - start[1])
if end[1] - start[1] < 0:
    timePassed = 60*(end[0]-start[0]) - (start[1] - end[1])

amount = 0
# 297
if timePassed > 240:
    amount += ((timePassed-240)//30)*60
    timePassed = 240

if timePassed > 120:
    amount += ((timePassed-120)//30)*40
    timePassed = 120

amount += ((timePassed)//30)*30

print(amount)
