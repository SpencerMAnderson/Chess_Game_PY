import pygame

# What computer am I on?
computer = "Home"

if computer == "Home":
    width, height = 904, 904
else:
    width, height = 520, 520

# Initialize the game window
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((width, height)) 
    pygame.display.set_caption("Chess Game")
    return screen

# Initialize the PNG images with their associated pieces
def init_images():
    global computer

    # If I am on my Laptop...
    if computer == "Laptop":
        # B&W Pawns
        wp = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Pawn.png')
        wp = pygame.transform.scale(wp, (65, 65))
        bp = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/PawnB.png')
        bp = pygame.transform.scale(bp, (65, 65))

        # B&W Knights
        wkn = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Knight.png')
        wkn = pygame.transform.scale(wkn, (65, 65))
        bkn = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/KnightB.png')
        bkn = pygame.transform.scale(bkn, (65, 65))

        # B&W Bishops
        wb = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Bishop.png')
        wb = pygame.transform.scale(wb, (65, 65))
        bb = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/BishopB.png')
        bb = pygame.transform.scale(bb,(65, 65))

        # B&W Rooks
        wr = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Rook.png')
        wr = pygame.transform.scale(wr, (65, 65))
        br = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/RookB.png')
        br = pygame.transform.scale(br,(65, 65))

        # B&W Queens
        wq = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Queen.png')
        wq = pygame.transform.scale(wq, (65, 65))
        bq = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/QueenB.png')
        bq = pygame.transform.scale(bq, (65, 65))

        # B&W Kings
        wk = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/King.png')
        wk = pygame.transform.scale(wk, (65, 65))
        bk = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/KingB.png')
        bk = pygame.transform.scale(bk, (65, 65))

    # If I am on my Home PC...
    else:
        # B&W Pawns
        wp = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Pawn.PNG')
        wp = pygame.transform.scale(wp, (113, 113))
        bp = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/PawnB.PNG')
        bp = pygame.transform.scale(bp, (113, 113))

        # B&W Knights
        wkn = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Knight.PNG')
        wkn = pygame.transform.scale(wkn, (113, 113))
        bkn = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/KnightB.PNG')
        bkn = pygame.transform.scale(bkn, (113, 113))

        # B&W Bishops
        wb = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Bishop.PNG')
        wb = pygame.transform.scale(wb, (113, 113))
        bb = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/BishopB.PNG')
        bb = pygame.transform.scale(bb,(113, 113))

        # B&W Rooks
        wr = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Rook.PNG')
        wr = pygame.transform.scale(wr, (113, 113))
        br = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/RookB.PNG')
        br = pygame.transform.scale(br,(113, 113))

        # B&W Queens
        wq = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Queen.PNG')
        wq = pygame.transform.scale(wq, (113, 113))
        bq = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/QueenB.PNG')
        bq = pygame.transform.scale(bq, (113, 113))

        # B&W Kings
        wk = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/King.PNG')
        wk = pygame.transform.scale(wk, (113, 113))
        bk = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/KingB.PNG')
        bk = pygame.transform.scale(bk, (113, 113))

    return wp, bp, wkn, bkn, wb, bb, wr, br, wq, bq, wk, bk 
    
# Initialize a 2D array with all starting positions
def init_board():
    # Blank 8x8 board
    board = [[None for _ in range(8)] for _ in range(8)]

    # Initialize the pieces
    for col in range(8):
        board[6][col] = 'wp'  # White pawns
        board[1][col] = 'bp'  # Black pawns

    board[7][0] = board[7][7] = 'wr'  # White rooks
    board[0][0] = board[0][7] = 'br'  # Black rooks

    board[7][1] = board[7][6] = 'wkn' # White knights
    board[0][1] = board[0][6] = 'bkn'  # Black knights

    board[7][2] = board[7][5] = 'wb'  # White bishops
    board[0][2] = board[0][5] = 'bb'  # Black bishops

    board[7][3] = 'wq'  # White queen
    board[0][3] = 'bq'  # Black queen

    board[7][4] = 'wk'  # White king
    board[0][4] = 'bk'  # Black king

    return board
