from resources import pieces
import copy

# Function to check if the move can be played
def logic(selected_piece, selected_pos, end_pos, board, pieces):
    x1, y1 = selected_pos
    x2, y2 = end_pos
    
    if selected_piece == 'wp':  # White pawn logic
        # Move one step forward
        if y1 == y2 and x2 == x1 - 1 and board[x2][y2] is None:
            return True
        # Move two steps forward from the starting position
        if y1 == y2 and x1 == 6 and x2 == x1 - 2 and board[x2][y2] is None and board[x1 - 1][y1] is None:
            return True
        # Capture diagonally
        if abs(y2 - y1) == 1 and x2 == x1 - 1 and board[x2][y2] is not None and "Black" in pieces[board[x2][y2]]:
            return True  

    elif selected_piece == 'bp':  # Black pawn logic
        # Move one step forward
        if y1 == y2 and x2 == x1 + 1 and board[x2][y2] is None:
            return True
        # Move two steps forward from the starting position
        if y1 == y2 and x1 == 1 and x2 == x1 + 2 and board[x2][y2] is None and board[x1 + 1][y1] is None:
            return True
        # Capture diagonally
        if abs(y2 - y1) == 1 and x2 == x1 + 1 and board[x2][y2] is not None and "White" in pieces[board[x2][y2]]:
            return True

    # Knight logic 
    if selected_piece == 'wkn' or selected_piece == 'bkn':
        # All possible moves of a knight
        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(8):
            # Position of the knight after the move
            x = x1 + X[i]
            y = y1 + Y[i]
            # Check if the move is within the board boundaries
            if 0 <= x < 8 and 0 <= y < 8:
                # If the end position matches the knight's move...
                if end_pos == (x, y):
                    # Check if the destination is empty or contains an opponent's piece
                    if board[x][y] is None or (selected_piece == 'wkn' and "Black" in pieces[board[x][y]]) or (selected_piece == 'bkn' and "White" in pieces[board[x][y]]):
                        return True

    # Bishop logic
    if selected_piece == 'wb' or selected_piece == 'bb':
        if abs(x2 - x1) == abs(y2 - y1) and check_diagonal(x1, y1, x2, y2, board):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True

    # Rook logic
    if selected_piece == 'wr' or selected_piece == 'br': 
        if (x1 == x2 or y1 == y2) and check_straight_line(x1, y1, x2, y2, board):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
            
    # Queen logic
    if selected_piece == 'wq' or selected_piece == 'bq':
        if ((x1 == x2 or y1 == y2) and check_straight_line(x1, y1, x2, y2, board)) or (abs(x2 - x1) == abs(y2 - y1) and check_diagonal(x1, y1, x2, y2, board)):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
    
    # King logic
    if selected_piece == 'wk' or selected_piece == 'bk':
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Check if the king is moving only one square in any direction
        if (dx <= 1 and dy <= 1) and ((check_straight_line(x1, y1, x2, y2, board)) or (check_diagonal(x1, y1, x2, y2, board))):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True

    return False

# Check if there is any pieces obscuring a diagonal
def check_diagonal(x1, y1, x2, y2, board):
    dx = 1 if x2 > x1 else -1  # Determine direction of movement in x-axis
    dy = 1 if y2 > y1 else -1  # Determine direction of movement in y-axis

    x, y = x1 + dx, y1 + dy  # Start from the next square along the diagonal

    while x != x2 and y != y2:
        if board[x][y] is not None:  # Check if the square is occupied
            return False  # Path is blocked
        x += dx
        y += dy
    return True  

# Check if there is any pieces obscuring a rank/file
def check_straight_line(x1, y1, x2, y2, board):
    # Vertical movement
    if x1 == x2:
        dy = 1 if y2 > y1 else -1
        for y in range(y1 + dy, y2, dy):
            if board[x1][y] is not None:  # Check if the square is occupied
                return False 
    # Horizontal movement        
    elif y1 == y2: 
        dx = 1 if x2 > x1 else -1
        for x in range(x1 + dx, x2, dx):
            if board[x][y1] is not None:  # Check if the square is occupied
                return False  
    return True

# Return the king's position
def king_position(board, king_color):
    king_piece = 'wk' if king_color == 'w' else 'bk'
    for row in range(8):
        for col in range(8):
            if board[row][col] == king_piece:
                return (row, col)
    return None  
    
# Check if a king is in check
def is_in_check(board, king_pos, is_white):
    opponent_color = 'b' if is_white else 'w'
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece.startswith(opponent_color):
                # If the piece's logic can move to the king...
                if logic(piece, (row, col), king_pos, board, pieces):
                    return True  # The king is in check
    return False

# Determine if it is checkmate
def is_checkmate(king_pos, board, pieces):
    king_x, king_y = king_pos
    king_color = 'w' if 'w' in board[king_x][king_y] else 'b'
    opponent_color = 'b' if king_color == 'w' else 'w'
    
    # Check if the king can move to any adjacent square without being in check
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = king_x + dx, king_y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:  # Ensure new position is within bounds
                if board[new_x][new_y] is None or board[new_x][new_y].startswith(opponent_color):
                    # Temporarily move the king to the new position
                    original_piece = board[new_x][new_y]
                    board[new_x][new_y] = board[king_x][king_y]
                    board[king_x][king_y] = None
                    
                    # Check if the king would still be in check at the new position
                    if not is_in_check(board, (new_x, new_y), king_color == 'w'):
                        # Restore the original board state
                        board[king_x][king_y] = board[new_x][new_y]
                        board[new_x][new_y] = original_piece
                        return False
                    
                    # Restore the original board state
                    board[king_x][king_y] = board[new_x][new_y]
                    board[new_x][new_y] = original_piece
    
    # If the king cannot move, check if any other piece can block the check or capture the attacking piece
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece.startswith(king_color):
                for x in range(8):
                    for y in range(8):
                        if logic(piece, (x, y), (row, col), board, pieces):
                            # Simulate the move
                            simulated_board = copy.deepcopy(board)
                            simulated_board[x][y] = simulated_board[row][col]
                            simulated_board[row][col] = None
                            
                            # Check if the king is still in check after the move
                            if not is_in_check(simulated_board, king_pos, king_color == 'w'):
                                return False  # If any piece can prevent checkmate
    
    # If no valid moves can prevent check, it's checkmate
    return True



