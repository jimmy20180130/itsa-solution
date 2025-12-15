a = int(input())

if a == 1:
    print('#')
else:
    for i in range(1, a+1):
        #first: 2# and 1* and 2# 
        plusarr = ["+" for j in range((2* a-1 -(2*i-1))//2)]

        barr = ["#" for j in range((2*i-1))]

        print(''.join(plusarr) + ''.join(barr) + ''.join(plusarr))
