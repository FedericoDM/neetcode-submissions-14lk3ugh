class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dot = "."
        grid_size = 3
        transposed_board = [list(row) for row in zip(*board)]

        for row, column in zip(board, transposed_board):
            complete_row = [num for num in row if num != dot]
            complete_column = [num for num in column if num != dot]
            
            print("Row: ",complete_row)
            print("Column: ",complete_column)

            if len(complete_row) != len(set(complete_row)):
                return False 

            if len(complete_column) != len(set(complete_column)):
                return False
        
        # Grid logic goes here
        for index in range(0, len(board), grid_size):
            # First n // 3 rows
            grid_rows = [row for row in board[index:index + grid_size]]
            # Build grid blocks
            for index in range(0, len(board), grid_size):
                grid = [grid_row[index: index + grid_size] for grid_row in grid_rows]
                flattened_grid = [item for row in grid for item in row if item != dot]
                if len(flattened_grid) != len(set(flattened_grid)):
                    return False

        return True