# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43022

a = input().split(',')
print(int(''.join(sorted(a, reverse=True))) - int(''.join(sorted(a))))
