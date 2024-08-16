import pygame
import sys
from pygame import mixer
from init import init_board, init_game
from board import draw_board
from inputs import handle_click

screen = init_game()
board = init_board()

# Main game loop
def game():
    running = True
    while running:
        draw_board(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_click(pygame.mouse.get_pos(),board, screen,1)
                elif event.button == 3:
                    handle_click(pygame.mouse.get_pos(),board, screen,3)
        pygame.display.flip()
game()