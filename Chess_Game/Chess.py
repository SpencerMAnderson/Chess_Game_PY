import sys, pygame
from init import init_board, init_game, init_moves, dimension
from board import draw_board
from inputs import handle_click

player = 'w' # White or black player. Syntax is 'w' or 'b'

screen = init_game() # Initialize game window
board = init_board() # Initialize the board
moves = init_moves(board) # Keep track of how many times each piece has moved

# Main game loop
def game():
    running = True
    game_over = False
    while running:
        draw_board(screen, board, player)  # Display the board
        x, y = pygame.mouse.get_pos()
        half = dimension / 2
        
        if player == 'b':  # If the player is black, mirror coordinate inputs
            mirrored_x = half - (x - half)
            mirrored_y = half - (y - half)
            coords = (abs(int(mirrored_x)), abs(int(mirrored_y)))
        else:
            coords = (x, y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if event.button in [1, 3]:  # Check for left (1) and right (3) mouse buttons
                    game_over = handle_click(coords, board, screen, event.button, moves, player)
        pygame.display.flip()
game()
