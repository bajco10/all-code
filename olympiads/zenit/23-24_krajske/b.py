def transform_letter(char, letters):
    return '.' if char == '.' else letters[(int(char) - 1) % 9]

num_rows, num_cols = map(int, input().split())
characters = input().split()

result_output = ""

for _ in range(num_cols):
    numbers_input = input()
    transformed_line = ''.join(transform_letter(num, characters) for num in numbers_input)
    result_output += transformed_line + ("\n" if _ != num_cols - 1 else "")

print(result_output)
