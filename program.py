#check winner not working correct

# ['b', 'b', 'b', 'b', 'b', 'b', 'b', ' ']
# ['b', 'w', 'b', 'b', 'b', 'b', 'b', 'w']
# ['b', 'w', 'b', 'w', 'w', 'b', 'b', 'w']
# ['b', 'w', 'b', 'b', 'b', 'b', 'b', 'w']
# ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'w']
# ['b', 'w', 'w', 'b', 'b', 'b', 'b', 'w']
# ['b', 'b', 'w', 'b', 'b', 'b', 'b', 'w']
# ['b', 'b', 'b', 'b', 'b', 'b', 'b', ' ']


import copy
# b-w
def evaluate_state(board):
    # max
    # b w diff_in_#ofvalid
    diff_bw = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'b':
                diff_bw+=1
            elif board[i][j] == 'w':
                diff_bw-=1

    diff_valid_moves = len(get_valid_moves('b', board)) - len(get_valid_moves('w', board))
    winner = check_winner(board)

    if winner=='b':
        return diff_bw+diff_valid_moves+1000
    elif winner=='w':
        return diff_bw+diff_valid_moves-1000

    return diff_bw+diff_valid_moves


def get_best_move(board, player, difficulty):
    
    if player == 'b':
        max_score = -float("inf")
        best_move = None

        for [i, j] in get_valid_moves(player, board):
            
            board[i][j] = player
            score = minimax(board, difficulty, -float("inf"), float("inf"), 'w')
            board[i][j] = ' '
            if (score>max_score):
                max_score = score
                best_move = [i, j]

        return best_move
    
    else:
        min_score = float("inf")
        best_move = None

        for [i, j] in get_valid_moves(player, board):
            
            board[i][j] = player
            score = minimax(board, difficulty, -float("inf"), float("inf"), 'b')
            board[i][j] = ' '
            if (score<min_score):
                min_score = score
                best_move = [i, j]

        return best_move


def get_all_valid_new_states(board, player):
    new_boards = []
    valid_moves = get_valid_moves(player, board)

    for [i, j] in valid_moves:
        new_board = copy.deepcopy(board)
        make_move(i, j, player, new_board)
        new_boards.append(new_board)

    return new_boards


def minimax(board, depth, alpha, beta, player):
    if depth == 0 or check_winner(board)!='x':
        return evaluate_state(board)

    if player == 'b':
        max_score = -float("inf")
        for child in get_all_valid_new_states(board, player):
            score = minimax(child, depth - 1, alpha, beta, 'w')
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float("inf")
        for child in get_all_valid_new_states(board, player):
            score = minimax(child, depth - 1, alpha, beta, 'b')
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score


def is_valid_move(i, j, player, board):
    # if (board == True):
    #     raise Exception
    
    # dx = 1, 0, -1, 0
    # dy = 0, -1, 0, 1
    # r, b, l, u
    # print(board)
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
        if i==1:
            best_move = get_best_move(board, players[i], 5)
            if (best_move is not None):
                [x, y] = get_best_move(board, players[i], 5)
                make_move(x, y, players[i], board)
            
        else:
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
            break
     
    



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
