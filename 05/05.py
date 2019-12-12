# load data from file
with open('input') as f:
    polymer = f.read()

polymer_list = list(polymer)
size = len(polymer_list)
new_size = len(polymer_list) - 1
unit_types = []
results = []


def react(input_list):
    """ react polymer """
    for pos, unit in enumerate(input_list):
        if pos < len(input_list)-1:
            if unit != input_list[pos+1]:
                if unit == input_list[pos+1].lower():
                    del input_list[pos]
                    del input_list[pos]
                elif unit == input_list[pos+1].upper():
                    del input_list[pos]
                    del input_list[pos]
    return input_list


while new_size < size:
    size = new_size
    react(polymer_list)
    new_size = len(polymer_list)

# solution part 1
print(len(polymer_list))


# get the list of unit types to evaluate
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


for c in char_range('a', 'z'):
    unit_types.append(c)

for u in unit_types:
    print(u)
    polymer_list = list(polymer)
    polymer_list = [x for x in polymer_list if x != u]
    polymer_list = [x for x in polymer_list if x != u.upper()]
    size = len(polymer_list)
    new_size = len(polymer_list) - 1
    while new_size < size:
        size = new_size
        react(polymer_list)
        new_size = len(polymer_list)
    results.append(new_size)

# solution part 2
print(min(results))
