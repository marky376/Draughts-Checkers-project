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
    if not (0 <= start_row < 8 and 0 <= start_col < 8 and
            0 <= end_row < 8 and 0 <= end_col < 8):
        return False, False
    
    if board[start_row][start_col] != player or board[end_row][end_col] != " ":
        return False, False
    
    # Check direction of movement
    if player == "W" and end_row <= start_row:  # White moves down (increasing row)
        return False, False
    if player == "B" and end_row >= start_row:  # Black moves up (decreasing row)
        return False, False
    
    # Check for regular move (1 step diagonally)
    if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
        return True, False
    
    # Check for capture move (2 steps diagonally)
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        # Calculate the position of the jumped piece
        jumped_row = (start_row + end_row) // 2
        jumped_col = (start_col + end_col) // 2
        
        # Check if there's an opponent's piece to capture
        opponent = "B" if player == "W" else "W"
        if board[jumped_row][jumped_col] == opponent:
            return True, True
    
    return False, False

def make_move(board, player, start_row, start_col, end_row, end_col):
    # Check if this is a capture move
    is_capture = False
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        # Remove the captured piece
        jumped_row = (start_row + end_row) // 2
        jumped_col = (start_col + end_col) // 2
        board[jumped_row][jumped_col] = " "
        is_capture = True
    
    # Make the move on the board
    board[start_row][start_col], board[end_row][end_col] = " ", player
    return is_capture

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")

def has_valid_moves(board, player):
    # Check if the player has any valid moves
    for start_row in range(8):
        for start_col in range(8):
            if board[start_row][start_col] == player:
                # Check all possible diagonal moves
                for dr in [-2, -1, 1, 2]:
                    for dc in [-2, -1, 1, 2]:
                        end_row, end_col = start_row + dr, start_col + dc
                        valid, _ = is_valid_move(board, player, start_row, start_col, end_row, end_col)
                        if valid:
                            return True
    return False

def count_pieces(board, player):
    # Count the number of pieces a player has
    count = 0
    for row in board:
        for cell in row:
            if cell == player:
                count += 1
    return count

def play_game():
    # Main game loop
    player = "W"
    board = initialize_board()

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn")
        
        # Check win conditions
        opponent = "B" if player == "W" else "W"
        if count_pieces(board, opponent) == 0:
            print(f"Player {player} wins! All opponent pieces captured.")
            break
        
        if not has_valid_moves(board, player):
            print(f"Player {opponent} wins! Player {player} has no valid moves.")
            break
        
        # Get move input with error handling
        start_row = get_valid_input("Enter the row of the piece you want to move: ", 0, 7)
        start_col = get_valid_input("Enter the column of the piece you want to move: ", 0, 7)
        end_row = get_valid_input("Enter the row where you want to move the piece: ", 0, 7)
        end_col = get_valid_input("Enter the column where you want to move the piece: ", 0, 7)

        valid, is_capture = is_valid_move(board, player, start_row, start_col, end_row, end_col)
        if valid:
            make_move(board, player, start_row, start_col, end_row, end_col)
            if is_capture:
                print(f"Player {player} captured a piece!")
        else:
            print("Invalid move. Try again.")
            continue

        # Switch players
        player = "B" if player == "W" else "W"

if __name__ == "__main__":
    play_game()