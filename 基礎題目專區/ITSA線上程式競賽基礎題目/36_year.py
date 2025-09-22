# https://etutor2.itsa.org.tw/mod/topics/view.php?id=15909

num = int(input())

if num%4 == 0 and num%100 !=0:
    print('Bissextile Year')
elif num%400 == 0:
    print('Bissextile Year')
else:
    print('Common Year')
