'''import random

board=[' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
current_player='X'
winner=None
game_running=True

#Game Board
def display_board(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("-----")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("-----")
    print(board[6]+" | "+board[7]+" | "+board[8])

 #Take Player Input
def player_input(board):
    inp=int(input("Select a spot(1 to 9): "))
    if board[inp-1]==" ":
        board[inp-1]=current_player
    else:
        print("Oops! one player is already at that spot.")

#CHECKING FOR WIN OR TIE
def horizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!=" ":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!=" ":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!=" ":
        winner=board[6]
        return True

def vertical(board):
    if board[0]==board[3]==board[6] and board[0]!=" ":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!=" ":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!=" ":
        winner=board[2]
        return True

def diagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!=" ":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!=" ":
        winner=board[2]
        return True
    
def check_win(board):
    global game_running
    if horizontal(board):
        display_board(board)
        print(f"The winner is  {winner}!")
        game_running=False
    elif vertical(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_running=False
    elif diagonal(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_running=False

def check_TIE(board):
    global game_running
    if " " not in board:
        display_board(board)
        print("Oh! It's a TIE !")
        game_running=False

#Switch the player
def switch():
    global current_player
    if current_player=="X":
        current_player=="O"
    else:
        current_player=="X"

def computer(board):
    while current_player=="O":
        position=random.randint(0,8)
        if board[position]==" ":
            board[position]="O"
            switch()

while game_running:
    display_board(board)
    player_input(board)
    check_win(board)
    check_TIE(board)
    switch()
    computer(board)
    check_win(board)
    check_TIE(board) '''
board={1:' ', 2:' ', 3:' ',
            4:' ', 5:' ', 6:' ',
             7:' ', 8:' ', 9:' '}
player1="O"
player2="X"
def display_board(board):
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("------")
    print(board[7]+" | "+board[8]+" | "+board[9])
    print("\n")

def free_space(position):
    if board[position]==' ':
        return True
    else:
        return False
    
def chance(letter, position):
    if free_space(position):
        board[position]=letter
        display_board(board)
        if (draw()):
            print("The match is TIE.")
            exit()
        elif check_win():
            if letter=='X':
                print("X wins :)")
                exit()
            else:
                print("O wins")
                exit()
        return
    else:
        print("It can't insert here.")
        position=int(input("Enter any new position: "))
        chance(letter, position)
        return

def check_win():
    if (board[1] == board[2] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def draw():
    for key in board.keys():
        if (board[key]==' '):
            return False
    return True

def move1():
    position=int(input("Enter the position for O: "))
    chance(player1, position)
    return

def move2():
    position=int(input("Enter the position for X: "))
    chance(player2,position)
    return

display_board(board)

while not check_win():
    move2()
    move1()
