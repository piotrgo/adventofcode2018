# load data from file
with open('input') as f:
    polymer = f.read()

polymer_list = list(polymer)
size = len(polymer_list)
new_size = len(polymer_list) - 1


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

# solution
print(len(polymer_list))
