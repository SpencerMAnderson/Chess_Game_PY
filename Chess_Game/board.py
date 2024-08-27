import pygame
from init import dimension 
from resources import piece_images

# Draw the chess board
def draw_board(screen, board):
    light = (228, 233, 235)
    dark = (153 , 191, 209)
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