import sys

def isValidSudoku(board: list, check_type: str) -> bool:
    if check_type == "sub-box":
        availables = "123456789"
        size = 3
    else:
        size = 9
    
    for i in range(size):
        
        if check_type != "sub-box":
            availables = "123456789"
        
        for j in range(size):
            if check_type != "col": val = board[i][j]
            else: val = board[j][i]

            if val != ".":
                if val in availables:
                    availables = availables.replace(val, "")
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