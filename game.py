# Simple Text-Based Checkers/Draughts Game

def initialize_board():
    # Initialize an 8x8 board
    return [
        [" ", "W", " ", "W", " ", "W", " ", "W"],
        ["W", " ", "W", " ", "W", " ", "W", " "],
        [" ", "W", " ", "W", " ", "W", " ", "W"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["B", " ", "B", " ", "B", " ", "B", " "],
        [" ", "B", " ", "B", " ", "B", " ", "B"],
        ["B", " ", "B", " ", "B", " ", "B", " "]
    ]

def print_board(board):
    # Print the current state of the board
    print("   0  1  2  3  4  5  6  7")
    for i, row in enumerate(board):
        print(f"{i} ", end="")
        for cell in row:
            print(f"| {cell}", end=" ")
        print("|")

def is_valid_move(board, player, start_row, start_col, end_row, end_col):
    # Check if the move is valid
    if (
        0 <= start_row < 8 and 0 <= start_col < 8 and
        0 <= end_row < 8 and 0 <= end_col < 8 and
        board[start_row][start_col] == player and
        board[end_row][end_col] == " " and
        abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1
    ):
        return True
    return False

def make_move(board, player, start_row, start_col, end_row, end_col):
    # Make the move on the board
    board[start_row][start_col], board[end_row][end_col] = " ", player

def play_game():
    # Main game loop
    player = "W"
    board = initialize_board()

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn")

        start_row = int(input("Enter the row of the piece you want to move: "))
        start_col = int(input("Enter the column of the piece you want to move: "))
        end_row = int(input("Enter the row where you want to move the piece: "))
        end_col = int(input("Enter the column where you want to move the piece: "))

        if is_valid_move(board, player, start_row, start_col, end_row, end_col):
            make_move(board, player, start_row, start_col, end_row, end_col)
        else:
            print("Invalid move. Try again.")
            continue

        # Switch players
        player = "B" if player == "W" else "W"

if __name__ == "__main__":
    play_game()

