import pygame
import sys
from Logic import logic
from init import width, init_board, init_game
from utils import board_pos
from board import draw_board
from resources import pieces

screen = init_game()
board = init_board()

selected_piece = None
selected_pos = None

# Logic for handling user click inputs
def handle_click(pos):
    global selected_piece, selected_pos
    x,y = pos
    tile_size = width // 8
    row = y // tile_size
    col = x // tile_size
    clicked_pos = (row,col)

    if selected_piece: # If a piece is clicked on
        move_piece(clicked_pos) # Send the end pos to move_piece method
        selected_piece = None
        selected_pos = None
    else: # Select a piece
        if board[row][col]:
            selected_piece = board[row][col] # This is the piece clicked on
            selected_pos = (row, col) # This is the pos of the piece clicked on

player_turn = 0 # Global variable to keep track of which player's turn it is

# Logic for how each piece can move
def move_piece(end_pos):
    global player_turn
    x1,y1 = selected_pos
    x2,y2 = end_pos

    if player_turn % 2 == 0 and "White" in pieces[selected_piece]:  # If it is white's turn...
        if not logic(selected_piece, selected_pos, end_pos, board, pieces):
            print("Invalid move")
        else:
            print(pieces[selected_piece], board_pos[(x1, y1)], "to", board_pos[(x2, y2)])
            # Update the board
            board[x2][y2] = board[x1][y1]
            board[x1][y1] = None 
            draw_board(screen,board)
            pygame.display.flip()
            player_turn += 1

    elif player_turn % 2==1 and "Black" in pieces[selected_piece]: # If it is black's turn...
        if not logic(selected_piece, selected_pos, end_pos, board, pieces):
            print("Invalid move")
        else:
            print(pieces[selected_piece],board_pos[(x1,y1)],"to",board_pos[(x2,y2)])
            # Update the board
            board[x2][y2] = board[x1][y1]
            board[x1][y1] = None 
            draw_board(screen,board)
            pygame.display.flip()
            player_turn +=1

    else:
        if player_turn % 2==0:
            print("White to move")
        else:
            print("Black to move")

 
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
                handle_click(pygame.mouse.get_pos())
        pygame.display.flip()
game()