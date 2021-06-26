board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()
    print()

def play_game(board):
    while True:
        print_board(board)
        line = int(input('Selecione uma linha: '))
        column = int(input('Selecione uma coluna: '))
        board[line + 1].insert(column + 1, 'X')
        if board[line] == ['X', 'X','X'] or (board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X') or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
            print('X venceu')
            break
        else:
            print_board(board)
            line = int(input('Selecione uma linha: '))
            column = int(input('Selecione uma coluna: '))
            board[line + 1].insert(column + 1, 'O')
            if board[line] == ['O', 'O','O'] or (board[0][column] == 'O' and board[1][column] == 'O' and board[2][column] == 'O') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
                print('O venceu')
                break        
play_game(board)