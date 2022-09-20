# Assignment: TicTacToe Game
# Author: Marc Rollins
# tictactoe-solution.py by Bro. Manley was used as a reference


def main():
    """
    This is the main function of the TicTacToe game.
    Parameters: None
    Returns: Nothing
    """
    try:
        restart_game = True
        while restart_game == True:
            game_win = False
            board = create_board()
            display_board(board)
            game_round = 1
            player_turn = "O"

            while game_win == False:    
                player_turn = determine_turn(player_turn)

                player_input = int(input(f"It is {player_turn}'s turn to choose a square (1-9): "))
                board = update_board(board, player_input, player_turn)
                display_board(board)

                game_win = game_over(board, game_round)
                game_round += 1

            print("Good Game. Thanks for playing!")
        
        
            # Asks the users if they would like to play again and allows the program to loop as necessary.
            continue_game = str(input("Would you like to play again? (yes/no) "))
            if continue_game.lower == "yes":
                restart_game = True
            elif continue_game.lower() == "no":
                restart_game = False

            print("\nPlease come play again soon!")

    except ValueError as val_error:
        print(f"Error: {val_error}\n You must enter a whole number between 1 and 9. Closing the program now.")

def determine_turn(player_turn):
    """
    Determines who's turn it is to mark the board.

    Parameters:
        player_symbol: a string containing the letter 'X' or 'O'
    Return: player_symbol
    """
    if player_turn.lower() == "x":
        player_symbol = "O"
    else: player_symbol = "X"

    return player_symbol


def create_board():
    """
    Prints out the board for a visual representation of the game's progress.

    Parameters: None

    Returns: 
        board: A list containing the value of each square
    """
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def update_board(board, player_input, player_symbol):
    """
    Determines who's turn it is and updates the board accordingly.

    Parameters: 
        board: a list containing the value of each square
        player_input: the square that the user chose
        player_symbol: either an 'X' or an 'O'
    Returns: 
        board: an updated version of the same list given in parameters
    """
    square_index = player_input-1
    board[square_index] = player_symbol

    return board

def game_over(board, game_round):
    """
    Determines whether the game is a victory for one of the players or a draw.
    Parameters: 
        board: a list containing the value of each square
        game_round: a number tracking the number of times the board has been marked
    Returns: Boolean
    """
    def game_draw(board):
        if game_round == 9:
            return True
        elif game_round != 9:
            return False
    def game_winner(board):

        if board[0] == board[1] == board[2]:
            return True
        elif board[3] == board[4] == board[5]:
            return True
        elif board[6] == board[7] == board[8]:
            return True
        elif board[0] == board[3] == board[6]:
            return True
        elif board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:
            return True
        elif board[0] == board[4] == board[8]:
            return True
        elif board[2] == board[4] == board[6]:
            return True
        else:
            return False

    if game_draw(board) == True:
        return True
    elif game_winner(board) == True:
        return True
    else: return False


if __name__ == "__main__":
    main()