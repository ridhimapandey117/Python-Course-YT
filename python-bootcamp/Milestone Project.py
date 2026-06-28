#Warmup
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

#Make sure to check input before moving on with it



def display_game(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


def position_row():

    row = ''
    acceptable_range = range(0,3)
    within_range = False

    while row.isdigit() == False or within_range == False:
        row = input("Please enter a row value (0-2): ")

        if row.isdigit() == False:
            print("Sorry, that isn't a digit!")

        if row.isdigit() == True:
            if int(row) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-2)")
                within_range = False

    return int(row)

def position_col():
    col = ''
    acceptable_range = range(0,3)
    within_range = False

    while col.isdigit() == False or within_range == False:
        col = input("Please enter a col value (0-2): ")

        if col.isdigit() == False:
            print("Sorry, that isn't a digit!")

        if col.isdigit() == True:
            if int(col) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-2)")
                within_range = False

    return int(col)

def position_place(row, col, mark):
    row, col = check(row, col)

    if row == 0:
        row1[col] = mark
    elif row == 1:
        row2[col] = mark
    else:
        row3[col] = mark

def check(row, col):

    while True:

        if row == 0:
            if row1[col] == ' ':
                return row, col

        elif row == 1:
            if row2[col] == ' ':
                return row, col

        else:
            if row3[col] == ' ':
                return row, col

        print("There's already something there!")

        row = position_row()
        col = position_col()



def isWin(player, mark):
    #vertical win
    if (row1[0] == mark and row2[0] == mark and row3[0] == mark) or (row1[1] == mark and row2[1] == mark and row3[1] == mark) or (row1[2] == mark and row2[2] == mark and row3[2] == mark):
        return player
    #horizontal win
    elif (row1[0] == mark and row1[1] == mark and row1[2] == mark) or (row2[0] == mark and row2[1] == mark and row2[2] == mark) or (row3[0] == mark and row3[1] == mark and row3[2] == mark):
        return player

    #diagonal
    elif (row1[0] == mark and row2[1] == mark and row3[2] == mark) or (row1[2] == mark and row2[1] == mark and row3[0] == mark):
        return player

    else:
        return 'None'

def gameon():
    gameon = True
    current_player = ''
    winner = ''
    turn = 1

    print("Welcome to Tic Tac Toe!")

    while True:
        choice1 = input("Player 1: Do you want to be X or O? ").upper()

        if choice1 in ("X", "O"):
            break

    if choice1 == "X":
        choice2 = "O"
        current_player = "Player 1"
        print("Player 1 will go first!")
    else:
        choice2 = "X"
        current_player = "Player 2"
        print("Player 2 will go first!")


    while gameon:

        if current_player == 'Player 1':
            print("PLAYER 1\n")
            row_one = position_row()
            col_one = position_col()
            #check(row_one,col_one,choice1)
            position_place(row_one,col_one,choice1)
            display_game(row1,row2,row3)
            winner = isWin(current_player, choice1)

            if (winner == 'None'):
                if (turn == 9):
                    print("IT'S A TIE")
                    gameon = False
                else:
                    current_player = "Player 2"
                    turn += 1

            else:
                print(f"The winner is {winner}")
                gameon = False


        elif current_player == 'Player 2':
            print("PLAYER 2\n")
            row_two = position_row()
            col_two = position_col()
            #check(row_two,col_two,choice2)
            position_place(row_two,col_two,choice2)
            display_game(row1,row2,row3)
            winner = isWin(current_player, choice2)

            if (winner == 'None'):
                if (turn == 9):
                    print("IT'S A TIE")
                    gameon = False
                else:
                    current_player = "Player 1"
                    turn += 1
            else:
                print(f"The winner is {winner}")
                gameon = False



#Where everything begins

display_game(row1, row2,row3)
gameon()

'''
Problems:
When player makes an error in typing row and col then fixes it, their turn isn't displayed nor registered

'''