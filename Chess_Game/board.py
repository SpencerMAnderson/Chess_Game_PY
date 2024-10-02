import pygame, numpy as np
from init import dimension 
from resources import piece_images

# Draw the chess board
def draw_board(screen, board, player):
    light = (228, 233, 235) # Light squares
    dark = (153 , 191, 209) # Dark squares

    colors = [light,dark]
    tile_size = dimension // 8 
    
    # Print the board
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size))

            if player == 'b': # Flip the piece positions if player is black
                mirrored_board = np.fliplr(np.flipud(board))
                mirrored_board = mirrored_board.tolist()

                # Draw pieces
                piece = mirrored_board[row][col]
                if piece:
                    screen.blit(piece_images[piece], (col * tile_size, row * tile_size))
            else:
                # Draw pieces
                piece = board[row][col]
                if piece:
                    screen.blit(piece_images[piece], (col * tile_size, row * tile_size))

    