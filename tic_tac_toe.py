# Find Winner on a Tic Tac Toe Game

# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

#     Players take turns placing characters into empty squares ' '.
#     The first player A always places 'X' characters, while the second player B always places 'O' characters.
#     'X' and 'O' characters are always placed into empty squares, never on filled ones.
#     The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
#     The game also ends if all squares are non-empty.
#     No more moves can be played if the game is over.

# Given a 2D integer array moves where moves[i] = [row_i, col_i] indicates that the ith move will be played on grid[row_i][col_i], return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

def display_grid(grid: list):
    for row in grid:    print(row)


def tic_tac_toe(moves: list) -> str:
    play = "X" # (X/O) initial player is A playing 'X'
    grid = [[""] * 3 for _ in range(3)] # initializing an empty 3x3 grid
    
    # Place moves in grid
    for row, col in moves:
        grid[row][col] = play # update the play on grid
        play = "O" if play=="X" else "X" # switch between X/O in each turn

    display_grid(grid)

    for i in range(3):
        # check rows
        if grid[i][0] == grid[i][1] == grid[i][2]: # when all cells of the row is same
            if grid[i][0] == "X":
                return "A"
            elif grid[i][0] == "O":
                return "B"
            
        # check columns
        if grid[0][i] == grid[1][i] == grid[2][i]: # when all cells of the col is same
            if grid[0][i] == "X":
                return "A"
            elif grid[0][i] == "O":
                return "B"

    # check left-to-right diagonal
    if grid[0][0] == grid[1][1] == grid[2][2]: # when all cells of the diagonal is same
            if grid[0][0] == "X":
                return "A"
            elif grid[0][0] == "O":
                return "B"
            
    # check right-to-left diagonal
    if grid[0][2] == grid[1][1] == grid[2][0]: # when all cells of the diagonal is same
            if grid[0][2] == "X":
                return "A"
            elif grid[0][2] == "O":
                return "B"
    
    return "Draw" if len(moves)==9 else "Pending"


if __name__ == "__main__":
    # draw
    # moves = [[0,0], [0,1], [1,1], [2,2], [1,2], [1,0], [0,2], [2,0], [2,1]]
    # pending
    # moves = [[0,0], [0,2], [1,2], [1,1], [2,1]]
    # diagonal-2
    # moves = [[0,0], [0,2], [1,2], [1,1], [2,1], [2,0]]
    # diagonal-1
    # moves = [[0,0], [0,1], [1,1], [1,2], [2,2]]
    # cols
    # moves = [[0,2], [0,1], [1,2], [1,1], [2,2]]
    # rows
    # moves = [[2,0], [1,0], [2,1], [1,1], [2,2]]
    
    # moves = [[0,0], [2,0], [1,1], [2,1], [2,2]]
    moves = [[0,0], [1,1], [0,1], [0,2], [1,0], [2,0]]
    print(tic_tac_toe(moves))