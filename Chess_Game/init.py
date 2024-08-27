import pygame, copy, os

# Load file directories
base_path = os.path.dirname(__file__)
pieces_path = os.path.join(base_path, 'Pieces')
sounds_path = os.path.join(base_path, 'sounds')

# Initialize the dimension of the window 
def init_dimension():
    pygame.init()
    screen_info = pygame.display.Info()
    screen_h = screen_info.current_h
    screen_w = screen_info.current_w
    lowest = screen_h if screen_h < screen_w else screen_w # Base the size of the screen off of the lowest width or dimension value
    scale = 0.85
    dimension = int(lowest * scale)
    return dimension

dimension = init_dimension()
dimension -= dimension % 8 # Make the dimension divisible by 8 to properly display the board

# Initialize the game window
def init_game():
    global dimension
    pygame.init()
    screen = pygame.display.set_mode((dimension, dimension)) 
    pygame.display.set_caption("Chess")
    return screen

# Initialize the PNG images with their associated pieces
def init_images():
    global dimension
    square_dimension = (dimension // 8, dimension // 8)

    # B&W Pawns
    wp = pygame.image.load(os.path.join(pieces_path, 'Pawn.png'))
    wp = pygame.transform.scale(wp, square_dimension)
    bp = pygame.image.load(os.path.join(pieces_path, 'PawnB.png'))
    bp = pygame.transform.scale(bp, square_dimension)

    # B&W Knights
    wkn = pygame.image.load(os.path.join(pieces_path, 'Knight.png'))
    wkn = pygame.transform.scale(wkn, square_dimension)
    bkn = pygame.image.load(os.path.join(pieces_path, 'KnightB.png'))
    bkn = pygame.transform.scale(bkn, square_dimension)

    # B&W Bishops
    wb = pygame.image.load(os.path.join(pieces_path, 'Bishop.png'))
    wb = pygame.transform.scale(wb, square_dimension)
    bb = pygame.image.load(os.path.join(pieces_path, 'BishopB.png'))
    bb = pygame.transform.scale(bb,square_dimension)

    # B&W Rooks
    wr = pygame.image.load(os.path.join(pieces_path, 'Rook.png'))
    wr = pygame.transform.scale(wr, square_dimension)
    br = pygame.image.load(os.path.join(pieces_path, 'RookB.png'))
    br = pygame.transform.scale(br,square_dimension)

    # B&W Queens
    wq = pygame.image.load(os.path.join(pieces_path, 'Queen.png'))
    wq = pygame.transform.scale(wq, square_dimension)
    bq = pygame.image.load(os.path.join(pieces_path, 'QueenB.png'))
    bq = pygame.transform.scale(bq, square_dimension)

    # B&W Kings
    wk = pygame.image.load(os.path.join(pieces_path, 'King.png'))
    wk = pygame.transform.scale(wk, square_dimension)
    bk = pygame.image.load(os.path.join(pieces_path, 'KingB.png'))
    bk = pygame.transform.scale(bk, square_dimension)

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

# Inizialize a 2D array of the board to keep track of the number of moves a piece has made
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

    # Create sound effect variables
    move_piece_sound = pygame.mixer.Sound(os.path.join(sounds_path, 'piece_moved.mp3'))
    piece_captured = pygame.mixer.Sound(os.path.join(sounds_path, 'piece_captured.mp3'))
    check = pygame.mixer.Sound(os.path.join(sounds_path, 'check.mp3'))
    invalid_move = pygame.mixer.Sound(os.path.join(sounds_path, 'invalid_move.mp3'))
    victory = pygame.mixer.Sound(os.path.join(sounds_path, 'victory.mp3'))
    game_start = pygame.mixer.Sound(os.path.join(sounds_path, 'game_start.mp3'))
    castle = pygame.mixer.Sound(os.path.join(sounds_path, 'castle.mp3'))
   
    # Set the volume of sound effects
    pygame.mixer.Sound.set_volume(move_piece_sound, 0.5)
    pygame.mixer.Sound.set_volume(piece_captured, 0.4)
    pygame.mixer.Sound.set_volume(check, 0.3)
    pygame.mixer.Sound.set_volume(invalid_move, 0.3)
    pygame.mixer.Sound.set_volume(victory, 0.3)
    pygame.mixer.Sound.set_volume(game_start, 0.3)
    pygame.mixer.Sound.set_volume(castle, 1)

    return move_piece_sound, piece_captured, check, invalid_move, victory, game_start, castle
