import pygame
import copy
from init import width, init_sounds
from resources import pieces
from utils import board_pos
from logic import logic, king_position, is_in_check, is_checkmate
from board import draw_board

selected_piece = None
selected_pos = None
move_piece_sound, piece_captured, check, invalid_move, victory, game_start = init_sounds()

# Logic for handling user click inputs
def handle_click(pos,board,screen,click):
    if click == 1:
        global selected_piece, selected_pos
        x,y = pos
        tile_size = width // 8
        row = y // tile_size
        col = x // tile_size
        clicked_pos = (row,col)

        if selected_piece: # If a piece is clicked on
            move_piece(clicked_pos,board,screen) # Send the end pos to move_piece method
            selected_piece = None
            selected_pos = None
        else: # Select a piece
            if board[row][col]:
                selected_piece = board[row][col] # This is the piece clicked on
                selected_pos = (row, col) # This is the pos of the piece clicked on
    elif click == 3:
        selected_piece = None

player_turn = 0 # Global variable to keep track of which player's turn it is

def move_piece(end_pos, board, screen):
    global player_turn
    x1, y1 = selected_pos
    x2, y2 = end_pos

    # Determine current player's pieces and opponent's king color
    if player_turn % 2 == 0:
        current_player = "White"
        current_king = 'w'
        opponent_king = 'b'
        opponent = "Black"
    else:
        current_player = "Black"
        current_king = 'b'
        opponent_king = 'w'
        opponent = "White"

    # Ensure the piece being moved belongs to the current player
    if current_player in pieces[selected_piece]:  
        if not logic(selected_piece, selected_pos, end_pos, board, pieces):
            pygame.mixer.Sound.play(invalid_move)
            print("Invalid move")
        else:
            # Simulate the move on a copied board
            simulated_board = copy.deepcopy(board)
            simulated_board[x2][y2] = simulated_board[x1][y1]
            simulated_board[x1][y1] = None

            if is_in_check(simulated_board, king_position(simulated_board, current_king), current_king == 'w'):
                pygame.mixer.Sound.play(invalid_move)
                print(f"Invalid move: The {current_player.lower()} king would be in check!")
            else:
                # Execute the move on the actual board
                execute_move(board, x1, y1, x2, y2, screen)

                # Check if the opponent's king is now in check
                if is_in_check(board, king_position(board, opponent_king), current_king != 'w'):
                    if is_checkmate(king_position(board, opponent_king), board, pieces):
                        print(f"Game over! {current_player} wins!")
                        pygame.mixer.Sound.play(victory)
                    else:
                        pygame.mixer.Sound.play(check)
                        print(f"The {opponent.lower()} king is in check!")
    else:
        pygame.mixer.Sound.play(invalid_move)
        print(f"{current_player} to move")


def execute_move(board, x1, y1, x2, y2, screen):
    global player_turn
    captured = True if board[x2][y2] is not None else False

    print(pieces[selected_piece], board_pos[(x1, y1)], "to", board_pos[(x2, y2)])
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = None 
    draw_board(screen,board)
    pygame.display.flip()
    if captured:
        pygame.mixer.Sound.play(piece_captured)
    else:
        pygame.mixer.Sound.play(move_piece_sound)
    player_turn += 1