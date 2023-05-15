vyska, sirka = input().split()

l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

input_lines=[]
for i in range(int(vyska)):
    input_lines.append(input())

columns = []
for i in range(len(input_lines[0])):
    columns.append([])

# Iterate through the input lines and add each character to the appropriate column list
for line in input_lines:
    for i, char in enumerate(line):
        columns[i].append(char)

# Print the vertical lists
for col in columns:
    index = col.index("0")
    """if col[index+1] == "1":
        l1 +=1
    elif col[index+1] == """
    print(find_indices(col, "0"))
    print(col)







