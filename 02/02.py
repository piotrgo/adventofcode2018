from collections import Counter

twos = 0
threes = 0


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

result = twos*threes
print(result)
