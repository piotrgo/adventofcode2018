from collections import Counter
from difflib import SequenceMatcher

twos = 0
threes = 0
difference = []
best_pair = []

with open('input_data') as f:
    lines = f.read().splitlines()

for line in lines:
    pair = Counter(line).most_common(2)
    a = pair[0][1]*pair[1][1]
    if a == 6:
        twos += 1
        threes += 1
    if a in [4, 2]:
        twos += 1
    if a in [9, 3]:
        threes +=1

#for part one
result = twos*threes
print(result)

# part two:

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


i = 0
while i < len(lines):
    j = 0
    while j < len(lines):
        difference.append([similar(lines[i], lines[j]), i, j])
        j += 1
    i += 1

best_pair = sorted(difference)[:-(len(lines))][len(best_pair)-2:-1]
print(''.join([i for i, j in zip(lines[best_pair[0][1]], lines[best_pair[0][2]]) if i == j]))
