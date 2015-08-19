import sys


def main(file_arg):
    with open(file_arg) as f:
        # Set up a grid, a list of lists. Each internal list is a row, and
        # each tile in the row has the value True or False; True for life,
        # False for empty
        grid = []
        for line in f:
            row = []
            for char in line.strip():
                if char == '.':
                    row.append(False)
                else:
                    row.append(True)
            grid.append(row)

        # Now we go through each iteration (10 in this case) and get the next
        # generation. Once the new generation is computed, it replaces the old
        # generation.
        iterations = 10

        for each_iteration in range(iterations):
            next_generation = []

            for y, each_row in enumerate(grid):
                next_generation_row = []
                for x, each_cell in enumerate(each_row):
                    surrounding_cells = get_surrounding_cells((x, y), grid)
                    next_generation_row.append(
                        get_new_cell_status((x, y), grid, surrounding_cells))

                next_generation.append(next_generation_row)

            grid = next_generation

        print_grid(grid)


def get_new_cell_status(cell, grid, surrounding_cells):
    # First, get the number of live neighbors
    live_neighbors = surrounding_cells.count(True)

    if grid[cell[0]][cell[1]]:
        # The cell is currently alive, so check if it survived
        if live_neighbors < 2:
            # Under-population, leading to death
            return False
        elif (live_neighbors == 2) or (live_neighbors == 3):
            # It lives!
            return True
        else:
            # Over-population, death
            return False
    else:
        # The cell is dead, so we only need to check if there is 3 neighbors
        if live_neighbors == 3:
            # 3 neighbors, so reproduction occurs
            return True


def get_surrounding_cells(cell, grid):
    surrounding_cells = []

    on_left_edge = False
    on_right_edge = False
    on_top_edge = False
    on_bottom_edge = False

    if cell[0] == 0:
        # Cell is on the left edge of the grid
        on_left_edge = True
    elif cell[0] == len(grid[0]) - 1:
        # Cell is on the right edge of the grid
        on_right_edge = True
    if cell[1] == 0:
        # Cell is on the top edge of the grid
        on_top_edge = True
    elif cell[1] == len(grid) - 1:
        # Cell is on the bottom edge of the grid
        on_bottom_edge = True

    if (not on_left_edge):
        if (not on_top_edge):
            surrounding_cells.append(grid[cell[0]-1][cell[1]-1])
        if (not on_bottom_edge):
            surrounding_cells.append(grid[cell[0]-1][cell[1]+1])
        surrounding_cells.append(grid[cell[0]-1][cell[1]])
    if (not on_right_edge):
        if (not on_top_edge):
            surrounding_cells.append(grid[cell[0]+1][cell[1]-1])
        if (not on_bottom_edge):
            surrounding_cells.append(grid[cell[0]+1][cell[1]+1])
        surrounding_cells.append(grid[cell[0]+1][cell[1]])
    if (not on_top_edge):
        surrounding_cells.append(grid[cell[0]][cell[1]-1])
    if (not on_bottom_edge):
        surrounding_cells.append(grid[cell[0]][cell[1]+1])

    return surrounding_cells


def print_grid(grid):
    for each_row in grid:
        row_string = ''
        for each_cell in each_row:
            if each_cell:
                row_string += '*'
            else:
                row_string += '.'

        print(row_string)


if __name__ == '__main__':
    main(sys.argv[1])
