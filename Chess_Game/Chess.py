import pygame
import sys

pygame.init()

# Window dimensions:
width, height = 904, 904
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Chess Game")

# Initialize the colors of light/dark tiles
light = (228, 233, 235)
dark = (153 , 191, 209)

# Function to tint images
def tint_image(image, tint_color):
    # Create a copy of the image to apply the tint
    tinted_image = image.copy()
    
    # Create a surface with the same size as the image
    tint_surface = pygame.Surface(image.get_size()).convert_alpha()
    
    # Fill the surface with the tint color
    tint_surface.fill(tint_color)
    
    # Blit the tint surface onto the original image using the special flag BLEND_RGBA_MULT
    tinted_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
    return tinted_image

grey_tint = (150, 150, 150, 0)  # RGBA color for a grey tint
blue_tint = (153 , 191, 209) # RGBA color for a blue tint

# B&W Pawns
wp = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Pawn.PNG')
wp = pygame.transform.scale(wp, (113, 113))
bp = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Pawn.PNG')
bp = pygame.transform.scale(bp, (113, 113))
bp = tint_image(bp, blue_tint)

# B&W Knights
wkn = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Knight.PNG')
wkn = pygame.transform.scale(wkn, (113, 113))
bkn = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Knight.PNG')
bkn = pygame.transform.scale(bkn, (113, 113))
bkn = tint_image(bkn, blue_tint)

# B&W Bishops
wb = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Bishop.PNG')
wb = pygame.transform.scale(wb, (113, 113))
bb = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Bishop.PNG')
bb = pygame.transform.scale(bb,(113,113))
bb = tint_image(bb, blue_tint)

# B&W Rooks
wr = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Rook.PNG')
wr = pygame.transform.scale(wr, (113, 113))
br = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Rook.PNG')
br = pygame.transform.scale(br,(113,113))
br = tint_image(br, blue_tint)

# B&W Queens
wq = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Queen.PNG')
wq = pygame.transform.scale(wq, (113, 113))
bq = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\Queen.PNG')
bq = pygame.transform.scale(bq, (113, 113))
bq = tint_image(bq, blue_tint)

# B&W Kings
wk = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\King.PNG')
wk = pygame.transform.scale(wk, (113, 113))
bk = pygame.image.load(r'C:\Users\First Build\source\repos\Chess_Game_PY\Chess_Game\King.PNG')
bk = pygame.transform.scale(bk, (113, 113))
bk = tint_image(bk, blue_tint)

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

# Link the images of the pieces to their respective vairables
piece_images = {
    'wp': wp,
    'bp': bp,
    'wkn': wkn,
    'bkn': bkn,
    'wb': wb,
    'bb': bb,
    'wr': wr,
    'br': br,
    'wq': wq,
    'bq': bq,
    'wk': wk,
    'bk': bk
}

# Names of pieces
pieces = {
    'wp': "White Pawn",
    'bp': "Black Pawn",
    'wkn': "White Knight",
    'bkn': "Black Knight",
    'wb': "White Bishop",
    'bb': "Black Bishop",
    'wr': "White Rook",
    'br': "Black Rook",
    'wq': "White Queen",
    'bq': "Black Queen",
    'wk': "White King",
    'bk': "Black King"
}

# Load chess board coordinates into board_pos dictionary
board_pos = {}
columns = 'abcdefgh'
rows = '87654321'
for i in range(8):
    for j in range(8):
        board_pos[(i, j)] = columns[j] + rows[i]

# Draw the chess board
def draw_board():
    colors = [light,dark]
    tile_size = width // 8 

    # Print the board
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size))

            # Draw pieces
            piece = board[row][col]
            if piece:
                screen.blit(piece_images[piece], (col * tile_size, row * tile_size))

# On player turn, record the pos of the player's mouse click
    # Triangulate the pos of the mouse click to the corresponding square in the 'board' array
# Which ever piece is selected, upon the player's next click, triangulate the corrdinates of the mouse click to 'board' array
    # If it is a valid move, over write the piece in 'board' with selected piece
    # if not a valid move, try again
# Detect checks/en passant

selected_piece = None
selected_pos = None

# Logic for handling user click inputs
def handle_click(pos):
    global selected_piece, selected_pos
    x,y = pos
    tile_size = width // 8
    row = y // tile_size
    col = x // tile_size
    clicked_pos = (row,col)

    if selected_piece: # If a piece is clicked on
        move_piece(clicked_pos) # Send the end pos to move_piece method
        selected_piece = None
        selected_pos = None
    else: # Select a piece
        if board[row][col]:
            selected_piece = board[row][col] # This is the piece clicked on
            selected_pos = (row, col) # This is the pos of the piece clicked on

player_turn = 0 # Global variable to keep track of which player's turn it is

# Logic for how each piece can move
def move_piece(end_pos):
    global player_turn
    x1,y1 = selected_pos
    x2,y2 = end_pos

    if player_turn % 2==0 and "White" in pieces[selected_piece]: # If it is white's turn...
        print(pieces[selected_piece],board_pos[(x1,y1)],"to",board_pos[(x2,y2)])
        # Update the board
        board[x2][y2] = board[x1][y1]
        board[x1][y1] = None 
        draw_board()
        pygame.display.flip()
        player_turn +=1

    elif player_turn % 2==1 and "Black" in pieces[selected_piece]: # If it is black's turn...
        print(pieces[selected_piece],board_pos[(x1,y1)],"to",board_pos[(x2,y2)])
        # Update the board
        board[x2][y2] = board[x1][y1]
        board[x1][y1] = None 
        draw_board()
        pygame.display.flip()
        player_turn +=1

    else:
        if player_turn % 2==0:
            print("White to move")
        else:
            print("Black to move")
 
def game():
    # Main game loop
    running = True
    while running:
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
        pygame.display.flip()
game()