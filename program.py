def get_valid_moves(player, board):
    opp = 'b'
    if (player == 'b'):
        opp = 'w'
    
    

    for i in range(8):
        for j in range(8):
            if ((board[i][j]==player or board[i][j]==' ') and board[i][j+1] == opp):
                

                
            



def make_move(player, board):
    

def check_winner(board):
    print("check winner\n")

def check_draw(board):
    print("check draw\n")


def print_board(board):
    for row in board:
        print(row)

def game_controller(board):
    players = ['b', 'w']
    i = 0
    while (True):
        print_board(board)
        make_move(players[i], board)
        winner = check_winner(board)
        if (players[i] == winner):
            print(players[i], "won\n")
            break
        elif (check_draw(board)):
            print("Draw\n")
            break
        
        i=(i+1)%2
    



def main():
    rows = 8
    cols = 8
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    board[3][3] = 'w'
    board[3][4] = 'b'
    board[4][4] = 'w'
    board[4][3] = 'b'
    game_controller(board)
    # disks: b or w



# if __name__=="__main__":
#     main()

main()
