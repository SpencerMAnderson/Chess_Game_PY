# Function to check if the move can be played
def logic(selected_piece, selected_pos, end_pos, board, pieces):
    x1, y1 = selected_pos
    x2, y2 = end_pos
    
    # Pawn logic
    # Need to handle enpessant
    if selected_piece == 'wp' or selected_piece == 'bp':
        # Pawns move one step forward
        if (y1 == y2 and x2 == x1 - 1 and board[x2][y2] is None) or (y1 == y2 and x2 == x1 + 1 and board[x2][y2] is None):
            return True
        # Pawns move two steps forward from the starting position
        if (y1 == y2 and x1 == 6 and x2 == x1 - 2 and board[x2][y2] is None and board[x1 - 1][y1] is None) or (y1 == y2 and x1 == 1 and x2 == x1 + 2 and board[x2][y2] is None and board[x1 + 1][y1] is None):
            return True
        # Pawns capture diagonally
        if (abs(y2 - y1) == 1 and x2 == x1 - 1 and board[x2][y2] is not None and "Black" in pieces[board[x2][y2]]) or (abs(y2 - y1) == 1 and x2 == x1 + 1 and board[x2][y2] is not None and "White" in pieces[board[x2][y2]]):
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
    
    # Check if there is any pieces obscuring a diagonal
    def check_diagonal(x1, y1, x2, y2, board):
        dx = 1 if x2 > x1 else -1  # Determine direction of movement in x-axis
        dy = 1 if y2 > y1 else -1  # Determine direction of movement in y-axis

        x, y = x1 + dx, y1 + dy  # Start from the next square along the diagonal

        # Loop until you reach the destination
        while x != x2 and y != y2:
            if board[x][y] is not None:  # Check if the square is occupied
                return False  # Path is blocked
            x += dx
            y += dy
        return True  

    # Bishop logic
    if selected_piece == 'wb' or selected_piece == 'bb':
        if abs(x2 - x1) == abs(y2 - y1) and check_diagonal(x1, y1, x2, y2, board):
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
            
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

    # Rook logic
    if selected_piece == 'wr' or selected_piece == 'br':  # Rook can be either white or black
        if (x1 == x2 or y1 == y2) and check_straight_line(x1, y1, x2, y2, board):
            # Check if the destination square has a piece of the same color
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
            
    # Queen logic
    if selected_piece == 'wq' or selected_piece == 'bq':
        if ((x1 == x2 or y1 == y2) and check_straight_line(x1, y1, x2, y2, board)) or (abs(x2 - x1) == abs(y2 - y1) and check_diagonal(x1, y1, x2, y2, board)):
            # Check if the destination square has a piece of the same color
            if board[x2][y2] is None or ("White" in pieces[selected_piece] and "Black" in pieces[board[x2][y2]]) or ("Black" in pieces[selected_piece] and "White" in pieces[board[x2][y2]]):
                return True
    
    # King logic
    if selected_piece == 'wk':
        
        dx = 1 if x2 > x1 else -1  # Determine direction of movement in x-axis
        dy = 1 if y2 > y1 else -1  # Determine direction of movement in y-axis

        x, y = x1 + dx, y1 + dy  # Start from the next square along the diagonal
            


    return False