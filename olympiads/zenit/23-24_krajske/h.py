n = 5
dosky = [1, 2, 8, 2, 1]

def horizontalny_tah(dosky):
    nove = []
    for i in dosky:
        nove.append(i-1)
    """for j in nove:
        if j==0:
            nove.remove(j)"""
    return nove

# vertikalne tahy budu len pocet dosiek, ktore mi ostanu
# ktore sa uz nebudu dat spolu skratit horizontalnym tahom
def find_consecutive_numbers(lst):
    
    consecutive_groups = []
    current_group = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            current_group.append(lst[i])
        else:
            consecutive_groups.append(current_group)
            current_group = [lst[i]]

    consecutive_groups.append(current_group)

    return consecutive_groups

# Example usage:
numbers = [1, 2, 3, 5, 6, 8, 9, 10]
result = find_consecutive_numbers(dosky)
print(result)










