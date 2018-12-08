import re

# load data from file
with open('input_data') as f:
    lines = f.read().splitlines()

# assume 1000 inches is max in terms of width/height for starters
side_length = 1000
total_area = [["?" for x in range(side_length)] for y in range (side_length)]
overlaping_claims = []
claims_ids = []

expr_ID = re.compile('^#(\d+)')
expr_coords = re.compile('@.(\d+.+):')
expr_area = re.compile('(\d+x\d+)')
for claim in lines:
    overlap_indicator = 0
    ID = re.match(expr_ID, claim).group(1)
    claims_ids.append(ID)
    coords = re.search(expr_coords, claim).group(1).split(',')
    area = re.search(expr_area, claim).group(1).split('x')
    width = range(int(coords[0]),int(coords[0])+int(area[0]))
    height = range(int(coords[1]), int(coords[1])+int(area[1]))
    for x in width:
        for y in height:
            field = total_area[x][y]
            if field == "?":
                total_area[x][y] = "X"
            else:
                total_area[x][y] = "*"
                overlap_indicator = 1
            if field == "X":
                overlap_indicator = 0
    if overlap_indicator == 1:
        overlaping_claims.append(ID)

# this is so bad :
for claim in lines:
    overlap_indicator = 0
    ID = re.match(expr_ID, claim).group(1)
    coords = re.search(expr_coords, claim).group(1).split(',')
    area = re.search(expr_area, claim).group(1).split('x')
    width = range(int(coords[0]),int(coords[0])+int(area[0]))
    height = range(int(coords[1]), int(coords[1])+int(area[1]))
    for x in width:
        for y in height:
            field = total_area[x][y]
            if field == "*":
                overlap_indicator = 1
    if overlap_indicator == 1:
        overlaping_claims.append(ID)


claims = []
for i in range(side_length):
    claims.append(total_area[i].count('*'))


# result for part 1
print(sum(claims))

# part 2: find claim that doesn't overlap

print((list(set(claims_ids) - set(overlaping_claims))))
