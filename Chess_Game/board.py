import pygame
from init import dimension 
from resources import piece_images

# Draw the chess board
def draw_board(screen, board, mouse_pos):
    light = (228, 233, 235) # Light squares
    dark = (153 , 191, 209) # Dark squares

    mouse_x, mouse_y = mouse_pos
    highlight = (190, 190, 190) # Highlight color

    colors = [light,dark]
    tile_size = dimension // 8 
    
    # Print the board
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size))

            # Draw pieces
            piece = board[row][col]
            if piece:
                screen.blit(piece_images[piece], (col * tile_size, row * tile_size))

            if mouse_pos:
                row_x = mouse_x // tile_size
                row_y = mouse_y // tile_size
                screen.blit(highlight, (col * tile_size, row * tile_size))
                print(row_x, row_y)

    