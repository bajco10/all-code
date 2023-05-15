input_str = """10010
10000
00110
10000
01000"""

input_lines = input_str.split('\n')

# Initialize the lists for each column
columns = []
for i in range(len(input_lines[0])):
    columns.append([])

# Iterate through the input lines and add each character to the appropriate column list
for line in input_lines:
    for i, char in enumerate(line):
        columns[i].append(char)

# Print the vertical lists
for col in columns:
    print(col)