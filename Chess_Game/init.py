import pygame, copy, sys
from pygame import mixer

# What computer am I on?
computer = "Laptop"

def init_dimensions():
    pygame.init()
    screen_info = pygame.display.Info()
    screen_h = screen_info.current_h
    scale = 0.85
    height = int(screen_h * scale)
    return height

height = init_dimensions()

height -= height % 8

# Initialize the game window
def init_game():
    global height
    pygame.init()
    screen = pygame.display.set_mode((height, height)) 
    pygame.display.set_caption("Chess")
    return screen

# Initialize the PNG images with their associated pieces
def init_images():
    global computer, height
    square_dimensions = (height // 8, height // 8)

    # If I am on my Laptop...
    if computer == "Laptop":
        # B&W Pawns
        wp = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Pawn.png')
        wp = pygame.transform.scale(wp, square_dimensions)
        bp = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/PawnB.png')
        bp = pygame.transform.scale(bp, square_dimensions)

        # B&W Knights
        wkn = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Knight.png')
        wkn = pygame.transform.scale(wkn, square_dimensions)
        bkn = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/KnightB.png')
        bkn = pygame.transform.scale(bkn, square_dimensions)

        # B&W Bishops
        wb = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Bishop.png')
        wb = pygame.transform.scale(wb, square_dimensions)
        bb = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/BishopB.png')
        bb = pygame.transform.scale(bb,square_dimensions)

        # B&W Rooks
        wr = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Rook.png')
        wr = pygame.transform.scale(wr, square_dimensions)
        br = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/RookB.png')
        br = pygame.transform.scale(br,square_dimensions)

        # B&W Queens
        wq = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/Queen.png')
        wq = pygame.transform.scale(wq, square_dimensions)
        bq = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/QueenB.png')
        bq = pygame.transform.scale(bq, square_dimensions)

        # B&W Kings
        wk = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/King.png')
        wk = pygame.transform.scale(wk, square_dimensions)
        bk = pygame.image.load('C:/Users/socce/source/repos/Chess_Game_PY/Chess_Game/Pieces/KingB.png')
        bk = pygame.transform.scale(bk, square_dimensions)

    # If I am on my Home PC...
    else:
        # B&W Pawns
        wp = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Pawn.PNG')
        wp = pygame.transform.scale(wp, square_dimensions)
        bp = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/PawnB.PNG')
        bp = pygame.transform.scale(bp, square_dimensions)

        # B&W Knights
        wkn = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Knight.PNG')
        wkn = pygame.transform.scale(wkn, square_dimensions)
        bkn = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/KnightB.PNG')
        bkn = pygame.transform.scale(bkn, square_dimensions)

        # B&W Bishops
        wb = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Bishop.PNG')
        wb = pygame.transform.scale(wb, square_dimensions)
        bb = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/BishopB.PNG')
        bb = pygame.transform.scale(bb, square_dimensions)

        # B&W Rooks
        wr = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Rook.PNG')
        wr = pygame.transform.scale(wr, square_dimensions)
        br = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/RookB.PNG')
        br = pygame.transform.scale(br, square_dimensions)

        # B&W Queens
        wq = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/Queen.PNG')
        wq = pygame.transform.scale(wq, square_dimensions)
        bq = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/QueenB.PNG')
        bq = pygame.transform.scale(bq, square_dimensions)

        # B&W Kings
        wk = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/King.PNG')
        wk = pygame.transform.scale(wk, square_dimensions)
        bk = pygame.image.load('C:/Users/First Build/source/repos/Chess_Game_PY/Chess_Game/Pieces/KingB.PNG')
        bk = pygame.transform.scale(bk, square_dimensions)

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

def init_moves(board):
    moves = copy.deepcopy(board)
    for row in range(8):
        for col in range(8):
            if moves[row][col]:
                moves[row][col] = 0
    return moves

# Initilaize sound effects
def init_sounds():
    pygame.mixer.init()

    if computer == "Laptop":
        move_piece_sound = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\piece_moved.mp3')
        piece_captured = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\piece_captured.mp3')
        check = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\check.mp3')
        invalid_move = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\invalid_move.mp3')
        victory = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\victory.mp3')
        game_start = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\game_start.mp3')
        castle = pygame.mixer.Sound(r'C:\Users\socce\source\repos\Chess_Game_PY\Chess_Game\sounds\castle.mp3')
    else:
        move_piece_sound = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\piece_moved.mp3')
        piece_captured = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\piece_captured.mp3')
        check = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\check.mp3')
        invalid_move = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\invalid_move.mp3')
        victory = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\victory.mp3')
        game_start = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\game_start.mp3')
        castle = pygame.mixer.Sound(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\sounds\castle.mp3')
    
    # Set the volume of sound effects
    pygame.mixer.Sound.set_volume(move_piece_sound, 0.5)
    pygame.mixer.Sound.set_volume(piece_captured, 0.4)
    pygame.mixer.Sound.set_volume(check, 0.3)
    pygame.mixer.Sound.set_volume(invalid_move, 0.3)
    pygame.mixer.Sound.set_volume(victory, 0.3)
    pygame.mixer.Sound.set_volume(game_start, 0.3)
    pygame.mixer.Sound.set_volume(castle, 1)

    return move_piece_sound, piece_captured, check, invalid_move, victory, game_start, castle
