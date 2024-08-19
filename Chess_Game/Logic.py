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

        # Regular king move: one square in any direction
        if (dx <= 1 and dy <= 1) and ((check_straight_line(x1, y1, x2, y2, board)) or (check_diagonal(x1, y1, x2, y2, board))):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
        
        # Castling logic
        if dy == 2 and dx == 0:  # Castling move is two squares horizontally
            if selected_piece == 'wk':
                # White king castling
                if y2 == 6 and board[7][7] == 'wr':  # Castling kingside with h1 rook
                    if (check_straight_line(7, 4, 7, 7, board) and 
                        not is_in_check(board, (7, 4), True) and
                        not is_in_check(board, (7, 5), True) and 
                        not is_in_check(board, (7, 6), True)):
                        return True
                elif y2 == 2 and board[7][0] == 'wr':  # Castling queenside with a1 rook
                    if (check_straight_line(7, 0, 7, 2, board) and 
                        not is_in_check(board, (7, 4), True) and 
                        not is_in_check(board, (7, 3), True) and 
                        not is_in_check(board, (7, 2), True)):
                        return True

            elif selected_piece == 'bk':
                # Black king castling
                if y2 == 6 and board[0][7] == 'br':  # Castling kingside with h8 rook
                    if (check_straight_line(0, 4, 0, 6, board) and 
                        not is_in_check(board, (0, 4), False) and 
                        not is_in_check(board, (0, 5), False) and 
                        not is_in_check(board, (0, 6), False)):
                        return True
                elif y2 == 2 and board[0][0] == 'br':  # Castling queenside with a8 rook
                    if (check_straight_line(0, 0, 0, 2, board) and 
                        not is_in_check(board, (0, 4), False) and 
                        not is_in_check(board, (0, 3), False) and 
                        not is_in_check(board, (0, 2), False)):
                        return True

    return False  # Move is not valid

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
    
    # Check if any pieces can block the check or capture the attacking piece
    for x1 in range(8):
        for y1 in range(8):
            # For every piece on the board
            piece = board[x1][y1]
            # If the piece is the same color as the king in check
            if piece and piece.startswith(king_color):
                for x2 in range(8):
                    for y2 in range(8):
                        # Check if that piece can move to a random square on the board
                        if logic(piece, (x1, y1), (x2, y2), board, pieces):
                            # Simulate the move
                            simulated_board = copy.deepcopy(board)
                            simulated_board[x2][y2] = simulated_board[x1][y1]
                            simulated_board[x1][y1] = None
                            new_king_pos = (x2,y2) if piece.endswith('k') else king_pos
                    
                            # Check if the king is still in check after the move
                            if not is_in_check(simulated_board, new_king_pos, king_color == 'w'):
                                return False  # If any piece can prevent checkmate
                            
    # If no valid moves can prevent check, it's checkmate
    return True

def en_passant():
    return True



