# Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.



import sys

def isValidSudoku(board: list, check_type: str) -> bool:
    # valid row & col    
    if check_type != "sub-box":
        for i in range(9):
            availables = "123456789"
            for j in range(9):
                if check_type != "col": val = board[i][j] # while validating row
                else: val = board[j][i] # while validatin col

                if val != ".": # skip the empty boxes else do this
                    if val in availables: # if unique value has been encountered
                        availables = availables.replace(val, "")
                    else: # if the same value has been encountered, invalidate
                        return False

    # valid sub-box
    else:
        # do for all 9 sub-boxes
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):

                availables = "123456789"
                # select a sub-box and check each of its boxes
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if board[i][j] != ".":
                            if board[i][j] in availables:
                                availables = availables.replace(board[i][j], "")
                            else:
                                return False
    
    return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    if isValidSudoku(board, "row"):
        if isValidSudoku(board, "col"):
            if isValidSudoku(board, "sub-box"):
                print("Valid")
                sys.exit()
    print("Invalid")