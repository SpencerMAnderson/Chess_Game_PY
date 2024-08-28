import sys, pygame
from init import init_board, init_game, init_moves
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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_board(screen, board, (mouse_x, mouse_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if event.button == 1:
                    game_over = handle_click(pygame.mouse.get_pos(), board, screen, 1, moves)
                elif event.button == 3:
                    game_over = handle_click(pygame.mouse.get_pos(), board, screen, 3, moves)
        pygame.display.flip()
game() 