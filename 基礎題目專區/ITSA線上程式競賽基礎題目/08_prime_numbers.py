# https://etutor2.itsa.org.tw/mod/topics/view.php?id=15908
# 隨便亂寫的

num = int(input())
checked = []

for i in range(num):
    x = i+1
    # 先檢查 i 是否為 checked 裡面的因數
    a = False
    for j in checked:
        if x%j==0 and x!=1 and x!=j+1:
            a = True
            break
        
    if a:
        continue
    
    if num%x == 0 and x!=1 and num!=x:
        print('NO')
        break
    
    if x!=1:
        checked.append(x)

else:
    print('YES')
