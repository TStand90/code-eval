var fs  = require("fs");

var grid = [];
var iterations = 10;

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {

        var row = [];
        for (var i = 0; i < line.length; i++) {
            if (line[i] == '.') {
                row.push(false);
            }
            else {
                row.push(true);
            }
        }

        grid.push(row);
    }
});

for (var i = 0; i < iterations; i++) {
    var next_generation = [];

    for (var y = 0; y < grid.length; y++) {
        next_generation_row = [];
        for (var x = 0; x < grid[y].length; x++) {
            var current_cell = [x, y];
            var surrounding_cells = get_surrounding_cells(current_cell, grid);
            next_generation_row.push(get_new_cell_status(current_cell, grid, surrounding_cells));
        }
        next_generation.push(next_generation_row);
    }
    grid = next_generation;
}

print_grid(grid);

function get_new_cell_status(cell, grid, surrounding_cells) {
    // First, get the number of live neighbors
    // var live_neighbors = surrounding_cells.count(true);
    var live_neighbors = 0;

    for (var i = 0; i < surrounding_cells.length; i++) {
        if (surrounding_cells[i]) {
            live_neighbors++;
        }
    }

    if (grid[cell[0]][cell[1]]) {
        // The cell is currently alive, so check if it survived
        if (live_neighbors < 2) {
            // Under-population, leading to death
            return false
        }
        else if ((live_neighbors == 2) || (live_neighbors == 3)) {
            // It lives!
            return true
        }
        else {
            // Over-population, death
            return false
        }
    }
    else {
        // The cell is dead, so we only need to check if there is 3 neighbors
        if (live_neighbors == 3) {
            // 3 neighbors, so reproduction occurs
            return true;
        }
    }
}

function get_surrounding_cells(cell, grid) {
    var surrounding_cells = [];

    var on_left_edge = false;
    var on_right_edge = false;
    var on_top_edge = false;
    var on_bottom_edge = false;

    if (cell[0] == 0) {
        // Cell is on the left edge of the grid
        on_left_edge = true;
    }
    else if (cell[0] == grid[0].length - 1) {
        // Cell is on the right edge of the grid
        on_right_edge = true;
    }
    if (cell[1] == 0) {
        // Cell is on the top edge of the grid
        on_top_edge = true;
    }
    else if (cell[1] == grid.length - 1) {
        // Cell is on the bottom edge of the grid
        on_bottom_edge = true;
    }

    if (!on_left_edge) {
        if (!on_top_edge) {
            surrounding_cells.push(grid[cell[0]-1][cell[1]-1]);
        }
        if (!on_bottom_edge) {
            surrounding_cells.push(grid[cell[0]-1][cell[1]+1]);
        }
        surrounding_cells.push(grid[cell[0]-1][cell[1]]);
    }
    if (!on_right_edge) {
        if (!on_top_edge) {
            surrounding_cells.push(grid[cell[0]+1][cell[1]-1]);
        }
        if (!on_bottom_edge) {
            surrounding_cells.push(grid[cell[0]+1][cell[1]+1]);
        }
        surrounding_cells.push(grid[cell[0]+1][cell[1]]);
    }
    if (!on_top_edge) {
        surrounding_cells.push(grid[cell[0]][cell[1]-1]);
    }
    if (!on_bottom_edge) {
        surrounding_cells.push(grid[cell[0]][cell[1]+1]);
    }

    return surrounding_cells;
}

function print_grid(grid) {
    for (var i = 0; i < grid.length; i++) {
        var row_string = '';
        for (var x = 0; x < grid[i].length; x++) {
            if (grid[i][x]) {
                row_string += '*';
            }
            else {
                row_string += '.';
            }
        }

        console.log(row_string);
    }
}