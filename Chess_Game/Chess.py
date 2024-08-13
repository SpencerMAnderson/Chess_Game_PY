import pygame
import sys

pygame.init()

# Window dimensions:
width, height = 520, 520
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
blue_tint = (153 , 191, 209, 0) # RGBA color for a blue tint

# B&W Pawns
wp = pygame.image.load(r'C:\Users\socce\Chess_Game\PawnM.JPG')
wp = pygame.transform.scale(wp, (65, 65))
bp = pygame.image.load(r'C:\Users\socce\Chess_Game\PawnM.JPG')
bp = pygame.transform.scale(bp, (65, 65))
bp = tint_image(bp, blue_tint)

# B&W Knights
wkn = pygame.image.load(r'C:\Users\socce\Chess_Game\KnightM.JPG')
wkn = pygame.transform.scale(wkn, (65, 65))
bkn = pygame.image.load(r'C:\Users\socce\Chess_Game\KnightM.JPG')
bkn = pygame.transform.scale(bkn, (65, 65))
bkn = tint_image(bkn, blue_tint)

# B&W Bishops
wb = pygame.image.load(r'C:\Users\socce\Chess_Game\BishopM.JPG')
wb = pygame.transform.scale(wb, (65, 65))
bb = pygame.image.load(r'C:\Users\socce\Chess_Game\BishopM.JPG')
bb = pygame.transform.scale(bb,(65,65))
bb = tint_image(bb, blue_tint)

# B&W Rooks
wr = pygame.image.load(r'C:\Users\socce\Chess_Game\RookM.JPG')
wr = pygame.transform.scale(wr, (65, 65))
br = pygame.image.load(r'C:\Users\socce\Chess_Game\RookM.JPG')
br = pygame.transform.scale(br,(65,65))
br = tint_image(br, blue_tint)

# B&W Queens
wq = pygame.image.load(r'C:\Users\socce\Chess_Game\QueenM.JPG')
wq = pygame.transform.scale(wq, (65, 65))
bq = pygame.image.load(r'C:\Users\socce\Chess_Game\QueenM.JPG')
bq = pygame.transform.scale(bq, (65, 65))
bq = tint_image(bq, blue_tint)

# B&W Kings
wk = pygame.image.load(r'C:\Users\socce\Chess_Game\KingM.JPG')
wk = pygame.transform.scale(wk, (65, 65))
bk = pygame.image.load(r'C:\Users\socce\Chess_Game\KingM.JPG')
bk = pygame.transform.scale(bk, (65, 65))
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

# On player turn, record the coordinates of the player's mouse click
    # Triangulate the coordinates of the mouse click to the corresponding square in the 'board' array
# Which ever piece is selected, upon the player's next click, triangulate the corrdinates of the mouse click to 'board' array
    # If it is a valid move, over write the piece in 'board' with selected piece
    # if not a valid move, try again

def handle_click(coordinates):
    selected_piece = None
    x = coordinates[0]
    y = coordinates[1]
    print("X:",x,"Y:",y)



# Detect checks/en passant

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
    