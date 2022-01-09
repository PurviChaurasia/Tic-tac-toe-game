import random

# SETTING UP THE BOARD
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''

    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Choose X or O: ")

    # ASSIGN PLAYER 2, the opposite marker
    playerfirst = marker

    if playerfirst == 'X':
        playersecond = 'O'
    else:
        playersecond = 'X'

    return (playerfirst, playersecond)


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):
    win = 0
    # CHECKING FOR WINNERS

    # Checking rows

    if board[7] == board[8] == board[9] == mark:
        win = 1
    elif board[4] == board[5] == board[6] == mark:
        win = 1
    elif board[1] == board[2] == board[3] == mark:
        win = 1

    # Checking columns

    elif board[1] == board[4] == board[7] == mark:
        win = 1
    elif board[2] == board[5] == board[8] == mark:
        win = 1
    elif board[3] == board[6] == board[9] == mark:
        win = 1

    # Checking Diagnols

    elif board[1] == board[5] == board[9] == mark:
        win = 1
    elif board[3] == board[5] == board[7] == mark:
        win = 1

    if win == 1:
        return True
    else:
        return False


def choose_first():
    # Assigning a number to each player
    player1 = 1
    player2 = 2

    firstplayer = random.randint(1, 2)

    if firstplayer == 1:
        print("Player 1 will go first")
        return player1
    else:
        print("Player 2 will go first")
        return player2


def space_check(board, position):
    for i in range(1, 10):
        if board[position] == ' ':
            return True
        else:
            return False


def full_board_check(board):
    flag = 0

    for i in range(1, 10):
        if board[i] == ' ':
            flag = 1
            break
    if flag == 1:
        return False
    else:
        return True


def player_choice(board, turn):
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    position = 0

    # While the choice is not a digit, keep asking for input.
    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not space_check(board, position):

        # we shouldn't convert here, otherwise we get an error on a wrong input
        print("\n")
        print(turn)
        choice = input("Pick a position to replace (1-9): ")
        position = int(choice)

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            print("Sorry, but you did not choose a valid position (1-9)")
            print('\n')

        if not space_check(board, position):
            print("Sorry, space not available for move!")
            print('\n')

    print("Space available for move!")
    return position


def replay():
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y', 'N']:

        choice = input("Would you like to keep playing? Y or N:  ")

        if choice not in ['Y', 'N']:

            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False


print('Welcome to Tic Tac Toe!')

FIRST = input("Enter first player's name: ")
SECOND = input("Enter second player's name: ")

while True:
    test_board = [' '] * 10

    # Assigning markers
    player1_marker, player2_marker = player_input()

    # Deciding who goes first
    FirstPlayer = choose_first()
    if FirstPlayer == 1:
        turn = FIRST
    else:
        turn = SECOND

    play_game = input("Are you ready to play?(yes/no): ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == FIRST:
            print('\n')
            display_board(test_board)

            # Asking the position
            position = player_choice(test_board, FIRST)

            # Positioning the marker
            place_marker(test_board, player1_marker, position)

            if win_check(test_board, player1_marker):
                print("Congratulations ", FIRST, " has won!")
                display_board(test_board)
                game_on = False

            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = SECOND
        else:
            # Player 2's turn
            print('\n')
            display_board(test_board)

            # Asking the position
            position = player_choice(test_board, SECOND)

            # Positioning the marker
            place_marker(test_board, player2_marker, position)

            if win_check(test_board, player2_marker):
                print("Congratulations ", SECOND, " has won!")
                display_board(test_board)
                game_on = False

            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = FIRST

    if not replay():
        print('Thank you for playing this game!!')
        break
