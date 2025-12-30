board = [[0,0,0], [0,0,0], [0,0,0]]

def print_board(p):
    print()
    for row in p:
        for element in row:
            if element == 0:
                print("|-", end="")
            elif element == 1:
                print("|X", end="")
            else:
                print("|O", end="")
        print("|")
    print()

def is_winner(board):
    for r in range(3):
        for c in range(3):
            if(r == 2):
                if(board[r][c] == board[r-1][c] and board[r-1][c] == board[r-2][c] and board[r][c] != 0):
                    return board[r][c]
            if(c == 2):
                if(board[r][c] == board[r][c-1] and board[r][c-1] == board[r][c-2] and board[r][c] != 0):
                    return board[r][c]
            if(r == 2 and c == 2):
                if(board[r][c] == board[r-1][c-1] and board[r-1][c-1] == board[r-2][c-2] and board[r][c] != 0):
                    return board[r][c]
    return -1

winner = -1
turn = True
count = 0
while winner == -1 and count < 9:
    print_board(board)
    if turn:
        print("Player 1's turn.\n")
        r = int(input("Which row do you to choose from (1,2, or 3?" ))-1
        c = int(input("Which collumn do you to choose from (1,2, or 3?" ))-1
        board[r][c] = 1
        turn = False
    else:
        print("Player 2's turn.\n")
        r = int(input("Which row do you to choose from (1,2, or 3?" ))-1
        c = int(input("Which collumn do you to choose from (1,2, or 3?" ))-1
        board[r][c] = 2
        turn = True
    winner = is_winner(board)
    count += 1

print("Game Over!")
if(winner == 1):
    print("Player 1 Wins!")
elif(winner == 2):
    print("Player 2 Wins!")
else:
    print("It's a Tie!")
print_board(board)