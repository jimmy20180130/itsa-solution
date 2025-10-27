# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43038

ppl = int(input())
rank = list()
completed = {
  'b': [],
  'g': []
}

for i in range(ppl):
  row = list(map(int, input().split(' ')))
  
  for j in range(ppl):
    rank.append([row[j], i+1, j+1])
    
rank.sort(reverse=True)
    
for score, i, j in rank:
  if i in completed['b'] or j in completed['g']:
    continue
  
  print(f'boy {i} pair with girl {j}')
  
  completed['b'].append(i)
  completed['g'].append(j)
