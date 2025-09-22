# https://etutor2.itsa.org.tw/mod/topics/view.php?id=42612

num = int(input())
days = num//86400
hours = (num%86400)//3600
minutes = (num%86400)%3600//60
seconds = (num%86400)%3600%60

print(f'{days} days\n{hours} hours\n{minutes} minutes\n{seconds} seconds')
