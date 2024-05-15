import pygame
from program import *

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BRIGHT_COLOR = (255, 255, 0)


SCALE_FACTOR = 1

SCREEN_WIDTH = int(400 * SCALE_FACTOR)
SCREEN_HEIGHT = int(400 * SCALE_FACTOR)

BOARD_SIZE = 8
CELL_SIZE = int(SCREEN_WIDTH // (BOARD_SIZE * SCALE_FACTOR))

DISC_B = pygame.image.load('D:/FCAI/AI/AI_Project/black_disc.png')
DISC_W = pygame.image.load('D:/FCAI/AI/AI_Project/white_disc.png')

board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
board[3][3] = 'w'
board[3][4] = 'b'
board[4][4] = 'w'
board[4][3] = 'b'

player_discs = {'b': 30, 'w': 30}  # Both players start with 30 discs

def draw_board(screen):
    screen.fill(GREEN)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if board[row][col] == 'b':
                screen.blit(DISC_B, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))
            elif board[row][col] == 'w':
                screen.blit(DISC_W, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))

def highlight_valid_moves(screen, player):
    screen.fill(GREEN)  
    draw_board(screen)  
    valid_moves = get_valid_moves(player, board)
    for move in valid_moves:
        row, col = move
        pygame.draw.circle(screen, BRIGHT_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 5)



def animate_disc_flip(screen, row, col, player):
    disc_image = DISC_B if player == 'b' else DISC_W
    for i in range(1, CELL_SIZE // 2):
        pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(disc_image, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))
        pygame.display.flip()
        pygame.time.wait(50)




def no_valid_moves(board):
    b_valid_moves = get_valid_moves('b', board)
    w_valid_moves = get_valid_moves('w', board)
    if len(b_valid_moves) == 0 and len(w_valid_moves) == 0:
        return True
    if len(b_valid_moves) == 0 and  player_discs['w'] == 0:
        return True
    if len(w_valid_moves) == 0 and  player_discs['b'] == 0:
        return True
    else:
        return False

def game_controller(board, player, screen, player_discs, difficulty):  
    if no_valid_moves(board):
        print("No valid moves remaining for either players\nGame Over!")
        winner = check_winner(board)
        if winner == 'b':
            print("Player B wins!")
        elif winner == 'w':
            print("Player W wins!")
        else:
            print("It's a draw!")
        pygame.quit()

    if player == 'b':  # Human player
        if player_discs[player] == 0:
            print("no disks for player",player)
            return
        valid_moves = get_valid_moves(player, board)
        if len(valid_moves) == 0:
            print("No valid moves for player B")
            return
        
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the row and column of the clicked cell
                    row = event.pos[1] // CELL_SIZE
                    col = event.pos[0] // CELL_SIZE

                    if is_valid_move(row, col, player, board):
                        make_move(row, col, player, board)
                        player_discs[player] -= 1  
                        return
                        
    else:  
        if player_discs[player] == 0:
            print("no disks for player",player)
            return

        valid_moves = get_valid_moves(player, board)
        if len(valid_moves) == 0:
            print("No valid moves for player W")
            return
        
        best_move = get_best_move(board, player, difficulty)
        if best_move is not None:
            [x, y] = best_move
            make_move(x, y, player, board)
            player_discs[player] -= 1  
            animate_disc_flip(screen, x, y, player)  
  



def main():
    print("what difficulty you wanna experience? \nchoose from 1 to 5: ")
    difficulty = int (input())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Othello")

    running = True
    current_player = 'b'
    draw_board(screen)
    highlight_valid_moves(screen, current_player) 
    pygame.display.flip()
    
    while running:
        no_moves_made = True  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        draw_board(screen)
        if current_player == 'b':
            highlight_valid_moves(screen, current_player) 
        
        game_controller(board, current_player, screen, player_discs,difficulty) 

        current_player = 'w' if current_player == 'b' else 'b'

        draw_board(screen)
        if current_player == 'b':
            highlight_valid_moves(screen, current_player) 

        pygame.display.flip()

        valid_moves = get_valid_moves(current_player, board)
        if len(valid_moves) > 0:
            no_moves_made = False
            
        
        if no_moves_made and player_discs['b'] == 0 and player_discs['w'] == 0:
            break

    print("Game Over!")
    winner = check_winner(board)
    if winner == 'b':
        print("Player B wins!")
    elif winner == 'w':
        print("Player W wins!")
    else:
        print("It's a draw!")

    pygame.quit()

if __name__ == "__main__":
    main()
