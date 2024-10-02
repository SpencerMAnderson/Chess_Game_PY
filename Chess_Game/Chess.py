import sys, pygame
from init import init_board, init_game, init_moves, dimension
from board import draw_board
from inputs import handle_click

player = 'w' # White or black player

screen = init_game() # Initialize game window
board = init_board(player) # Initialize the board
moves = init_moves(board) # Keep track of how many times each piece has moved

# Main game loop
def game():
    running = True
    game_over = False
    while running:
        draw_board(screen, board, player) # Display the board
        x, y = pygame.mouse.get_pos()
        half = dimension / 2

        if player == 'b':
            # Calculate mirrored coordinates
            mirrored_x = half - (x - half)
            mirrored_y = half - (y - half)
            
            # Create a tuple for the mirrored coordinates
            mirrored_coords = (abs(int(mirrored_x)), abs(int(mirrored_y)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 'b':
                if event.button == 1:
                    game_over = handle_click(mirrored_coords, board, screen, 1, moves, player)
                elif event.button == 3:
                    game_over = handle_click(mirrored_coords, board, screen, 3, moves, player)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if event.button == 1:
                    game_over = handle_click((x,y), board, screen, 1, moves, player)
                elif event.button == 3:
                    game_over = handle_click((x,y), board, screen, 3, moves, player)
        pygame.display.flip()
game() 