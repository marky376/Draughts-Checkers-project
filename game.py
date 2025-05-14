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
    # Check if the move is valid (non-capture move)
    if (
        0 <= start_row < 8 and 0 <= start_col < 8 and
        0 <= end_row < 8 and 0 <= end_col < 8 and
        board[start_row][start_col] == player and
        board[end_row][end_col] == " " and
        abs(end_col - start_col) == 1
    ):
        # White moves down (row increases), Black moves up (row decreases)
        if player == "W" and end_row - start_row == 1:
            return True
        if player == "B" and end_row - start_row == -1:
            return True
    return False

def is_valid_capture(board, player, start_row, start_col, end_row, end_col):
    # Check if a capture move is valid
    opponent = "B" if player == "W" else "W"
    if (
        0 <= start_row < 8 and 0 <= start_col < 8 and
        0 <= end_row < 8 and 0 <= end_col < 8 and
        board[start_row][start_col] == player and
        board[end_row][end_col] == " " and
        abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2
    ):
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        if board[mid_row][mid_col] == opponent:
            # White captures down, Black captures up
            if player == "W" and end_row > start_row:
                return True
            if player == "B" and end_row < start_row:
                return True
    return False

def make_move(board, player, start_row, start_col, end_row, end_col):
    # Make the move on the board, handling both regular moves and captures
    if is_valid_capture(board, player, start_row, start_col, end_row, end_col):
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[start_row][start_col] = " "
        board[mid_row][mid_col] = " "  # Remove captured piece
        board[end_row][end_col] = player
    else:
        board[start_row][start_col], board[end_row][end_col] = " ", player

def has_valid_moves(board, player):
    # Check if the player has any valid moves (regular or capture)
    for r in range(8):
        for c in range(8):
            if board[r][c] == player:
                # Check all possible diagonal moves
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                for dr, dc in directions:
                    if is_valid_move(board, player, r, c, r + dr, c + dc):
                        return True
                    # Check capture moves (2 steps)
                    if is_valid_capture(board, player, r, c, r + 2*dr, c + 2*dc):
                        return True
    return False

def count_pieces(board, player):
    # Count the number of pieces for a player
    return sum(row.count(player) for row in board)

def play_game():
    # Main game loop
    player = "W"
    board = initialize_board()

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn")

        while True:
            try:
                start_row = int(input("Enter the row of the piece you want to move: "))
                start_col = int(input("Enter the column of the piece you want to move: "))
                end_row = int(input("Enter the row where you want to move the piece: "))
                end_col = int(input("Enter the column where you want to move the piece: "))
                if not (0 <= start_row <= 7 and 0 <= start_col <= 7 and
                        0 <= end_row <= 7 and 0 <= end_col <= 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 7.")

        if (is_valid_move(board, player, start_row, start_col, end_row, end_col) or
            is_valid_capture(board, player, start_row, start_col, end_row, end_col)):
            make_move(board, player, start_row, start_col, end_row, end_col)
        else:
            print("Invalid move. Try again.")
            continue

        # Check win conditions
        opponent = "B" if player == "W" else "W"
        if count_pieces(board, opponent) == 0 or not has_valid_moves(board, opponent):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch players
        player = "B" if player == "W" else "W"

if __name__ == "__main__":
    play_game()