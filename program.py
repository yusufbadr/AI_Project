def is_valid_move(i, j, player, board):
    # dx = 1, 0, -1, 0
    # dy = 0, -1, 0, 1
    # r, b, l, u

    opp = 'b'
    if (player == 'b'):
        opp = 'w'

    if (board[i][j]!=' '):
        return False
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    

    for k in range(4):
        r =  i + dx[k]
        c = j + dy[k]

        if (r<0 or r >=8 or c<0 or c>=8):
            continue

        if board[r][c] == opp:
            while 0<=r<8 and 0<=c<8 and board[r][c]==opp:
                r = r + dx[k]
                c = c + dy[k]

            if 0<=r<8 and 0<=c<8 and board[r][c]==player:
                return True
    
    return False




def outflank(i, j, player, board):
    # dx = 1, 0, -1, 0
    # dy = 0, -1, 0, 1


    opp = 'b'
    if (player == 'b'):
        opp = 'w'

    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    

    for k in range(4):
        r =  i + dx[k]
        c = j + dy[k]

        if (r<0 or r >=8 or c<0 or c>=8):
            continue

        if board[r][c] == opp:
            while 0<=r<8 and 0<=c<8 and board[r][c]==opp:
                r = r + dx[k]
                c = c + dy[k]

            if 0<=r<8 and 0<=c<8 and board[r][c]==player:
                while (r!=i or c!=j):
                    r-=dx[k]
                    c-=dy[k]
                    board[r][c] = player


def get_valid_moves(player, board):
    valid_moves = []
    for i in range(8):
        for j in range(8):
            if is_valid_move(i, j, player, board):
                valid_moves.append([i, j])

    return valid_moves


def make_move(i, j, player, board):
    valid_moves = get_valid_moves(player, board)
    if ([i, j] in valid_moves):
        board[i][j] = player
        outflank(i, j, player, board)
        return True
    
    return False
    
    

def check_winner(board):
    valid_b = get_valid_moves('b', board)
    valid_w = get_valid_moves('w', board)

    if (len(valid_b) == 0 and len(valid_w) == 0):
        b_score = 0
        w_score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j]=='b':
                    b_score+=1
                elif board[i][j]=='w':
                    w_score+=1

        if b_score>w_score:
            return 'b'
        elif w_score>b_score:
            return 'w'
        else:
            return 'd'
    
    else:
        return 'x'
        

def print_board(board):
    for row in board:
        print(row)

def game_controller(board):
    players = ['b', 'w']
    i = -1
    while (True):
        i=(i+1)%2
        print_board(board)
        print(i)
        print(players[i], "'s turn\n")
        print("Valid moves:\n")
        valid_moves = get_valid_moves(players[i], board)
        if (len(valid_moves)!=0):
            print(get_valid_moves(players[i], board))
            print("Enter valid move [i, j]:\n")
            r = int(input("i:"))
            c = int(input("j:"))
            while not make_move(r, c, players[i], board):
                print("Incorrect Move")
                r = int(input("i:"))
                c = int(input("j:"))

        winner = check_winner(board)
        
        if winner == 'd':
            print("Draw\n")
            break
        elif winner == 'x':
            
            continue
        else:
            print("Winner is: ", winner)
     
    



def main():
    rows = 8
    cols = 8
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    board[3][3] = 'w'
    board[3][4] = 'b'
    board[4][4] = 'w'
    board[4][3] = 'b'
    game_controller(board)
    # print(get_valid_moves('b', board))

    # disks: b or w



# if __name__=="__main__":
#     main()

main()
