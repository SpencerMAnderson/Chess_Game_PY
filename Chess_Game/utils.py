#import pygame
'''
blue_tint = (153 , 191, 209) # RGBA color for a blue tint

# Function to tint images
def tint_image(image, tint_color):
    tinted_image = image.copy()
    tint_surface = pygame.Surface(image.get_size()).convert_alpha()
    tint_surface.fill(tint_color)
    tinted_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted_image

def tint_pieces(pieces):
    for piece in pieces:
        tint_image(piece, blue_tint)
'''

# Load chess board coordinates into board_pos dictionary
board_pos = {}
columns = 'abcdefgh'
rows = '87654321'
for i in range(8):
    for j in range(8):
        board_pos[(i, j)] = columns[j] + rows[i]

