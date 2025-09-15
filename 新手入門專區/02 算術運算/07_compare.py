# sol 1
a = [int(x) for x in input().split(' ')]
a.sort(reverse=True)
print(a[0])

# sol 2
a = [int(x) for x in input().split(' ')]
b = a[0]

for n in a[1:]:
    if n > b:
        b = n
        
print(b)
