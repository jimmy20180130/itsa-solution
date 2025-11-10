# https://etutor2.itsa.org.tw/mod/topics/view.php?id=15923

str1 = input()
str2 = input()
step = range(len(str2) - len(str1) + 1)
count = 0

for i in step:
  if str1 == str2[i:i+len(str1)]:
    count+=1
    
print(count)
