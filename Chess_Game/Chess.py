import pygame
import sys
from init import init_board, init_game
from board import draw_board
from inputs import handle_click

screen = init_game()
board = init_board()

def game():
    # Main game loop
    running = True
    while running:
        draw_board(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos(),board, screen)
        pygame.display.flip()
game()