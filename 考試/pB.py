o = [
    '_OOO_',
    'O___O',
    'O___O',
    'O___O',
    '_OOO_',
]

x = [
    'X___X',
    '_X_X_',
    '__X__',
    '_X_X_',
    'X___X',
]

a = list(input())
one = []
two = []
three = []
four = []
five = []

for j in a:
    if j == 'O':
        one.append(o[0])
    else:
        one.append(x[0])

for j in a:
    if j == 'O':
        two.append(o[1])
    else:
        two.append(x[1])

for j in a:
    if j == 'O':
        three.append(o[2])
    else:
        three.append(x[2])

for j in a:
    if j == 'O':
        four.append(o[3])
    else:
        four.append(x[3])

for j in a:
    if j == 'O':
        five.append(o[4])
    else:
        five.append(x[4])

print(''.join(one))    
print(''.join(two))    
print(''.join(three))    
print(''.join(four))    
print(''.join(five))    
