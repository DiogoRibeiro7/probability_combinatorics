from math import comb

# Define the total cells to be covered (since it's a 9x9 grid and we start from 0)
total_vertical_cells = 8
total_horizontal_cells = 8

# Function to find the number of ways
def find_number_of_ways():
    ways = 0
    # Try different numbers of 'up' moves
    for up_moves in range(total_vertical_cells // 2 + 1):
        vertical_covered = up_moves * 2
        if (total_vertical_cells - vertical_covered) % 3 == 0:
            right_moves = (total_horizontal_cells - vertical_covered) // 3
            if right_moves * 3 == total_horizontal_cells - vertical_covered:
                total_moves = up_moves + right_moves
                # Calculate combinations
                ways += comb(total_moves, up_moves)
    return ways

# Calculate and print the number of ways
number_of_ways = find_number_of_ways()
print(number_of_ways)


from math import comb

# Define the total cells to be covered (since it's a 13x13 grid and we start from 0)
total_cells = 12

# Function to find the number of ways
def find_number_of_ways_13(total_cells):
    ways = 0
    # Try different numbers of 'up' moves
    for up_moves in range(total_cells // 2 + 1):
        vertical_covered = up_moves * 2
        if (total_cells - vertical_covered) % 3 == 0:
            right_moves = (total_cells - vertical_covered) // 3
            if right_moves * 3 + vertical_covered == total_cells:
                total_moves = up_moves + right_moves
                # Calculate combinations
                ways += comb(total_moves, up_moves)
    return ways

# Calculate and print the number of ways
number_of_ways = find_number_of_ways_13(total_cells)
print(number_of_ways)

