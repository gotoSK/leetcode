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

def win_check(grid: list, total_moves: int) -> str:
    pass

def tic_tac_toe(moves: list) -> str:
    play = "X" # (X/O) initial player is A playing 'X'
    total_moves = 0 # counts the total moves played [0,9]
    grid = [[""] * 3 for _ in range(3)] # initializing an empty 3x3 grid
    
    for row, col in moves:
        grid[row][col] = play # update the play on grid
        play = "O" if play=="X" else "X" # switch between X/O in each turn
        total_moves += 1

    display_grid(grid)

if __name__ == "__main__":
    moves = [[0,0], [2,0], [1,1], [2,1], [2,2]]
    print(tic_tac_toe(moves))