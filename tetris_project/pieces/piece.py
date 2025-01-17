class Piece:
    def __init__(self, piece_column):
        if piece_column > self.max_column():
            raise IndexError("Column index " + str(piece_column) + " out of bounds for piece " + str(self.get_piece_type()))
        self.coordinates = [[r, c + piece_column] for r, c in self.piece_shape()]

    def max_column(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def piece_shape(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def get_coordinates(self):
        return self.coordinates
    
    def get_columns_indexes(self):
        return list(set(coordinate[1] for coordinate in self.coordinates))
    
    def get_rows_indexes(self):
        return list(set(coordinate[0] for coordinate in self.coordinates))
    
    def adujst_row_height(self, row_height, lowest_column):
        # find min value on the column
        min_val = min([r for r, c in self.coordinates if c == lowest_column])
        height_modification = row_height - min_val
        # Adjust the coordinates
        self.coordinates = [[r + height_modification, c] for r, c in self.coordinates]
        
        # Find the minimum row value after adjustment, if negative, shift rows to have min value 0
        min_row_after_adjustment = min(r for r, _ in self.coordinates)
        
        if min_row_after_adjustment < 0:
            self.coordinates = [[r + abs(min_row_after_adjustment), c] for r, c in self.coordinates]

    def increase_row_height(self, row_height):
        self.coordinates = [[r + row_height, c] for r, c in self.coordinates]