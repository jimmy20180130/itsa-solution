# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43088

a = list(map(int, input().split(' ')))
if a[0] <= 100 and a[1] <= 100:
    print('inside')
else:
    print('outside')
