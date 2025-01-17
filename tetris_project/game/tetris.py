from utils.constants import GRID_WIDTH

class Tetris:
    def __init__(self):
        # The grid’s initial state is empty
        self.grid = []
        self.lowest_available_row_in_column = [0] * GRID_WIDTH

    def get_grid_height(self):
        return len(self.grid)
    
    def add_row(self):
        self.grid.append([0] * GRID_WIDTH)

    def is_out_of_bound(self, r):
        # We only check rows because columns are fixed size
        return False if 0 <= r <= len(self.grid) - 1 else True
    
    def is_space_available(self, piece):
        for coordinate in piece.get_coordinates():
            while self.is_out_of_bound(coordinate[0]):
                self.add_row()
            if self.grid[coordinate[0]][coordinate[1]] == 1:
                return False
        return True

    def add_piece_in_grid(self, piece_coordinates):
        for coordinate in piece_coordinates:
            self.grid[coordinate[0]][coordinate[1]] = 1
            self.lowest_available_row_in_column[coordinate[1]] = coordinate[0]
            
    def get_lowest_fitting_row(self, piece):
        row_start = 0
        lowest_column = 0
        for col in piece.get_columns_indexes():
            r_s = self.lowest_available_row_in_column[col]
            if r_s >= row_start:
                row_start = r_s
                lowest_column = col
        return row_start, lowest_column
    
    def remove_complete_rows(self, piece):
        # Check if any row got completed and remove it
        removed_row = 0
        for row in sorted(piece.get_rows_indexes(), reverse=True):
            if all(item == 1 for item in self.grid[row]):
                removed_row += 1
                self.grid.pop(row)
        
        # Update the lowest availble row
        self.lowest_available_row_in_column = [
            max(0, row - removed_row) for row in self.lowest_available_row_in_column
        ]

    def add_piece(self, piece):

        # If grid is empty add original row
        if not self.grid:
            self.add_row()

        # Adujst row height for piece to "fall" on the other pieces
        row_start, lowest_column = self.get_lowest_fitting_row(piece)
        piece.adujst_row_height(row_start, lowest_column)

        # Check availability, if space not available, move the piece up
        while not self.is_space_available(piece):
            piece.increase_row_height(1)

        # Add piece 
        self.add_piece_in_grid(piece.get_coordinates())

        # Remove full lines
        self.remove_complete_rows(piece)