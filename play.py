import random


def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')


def make_move(board, row, col, symbol):
    board[row][col] = symbol


def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    return empty_cells


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def play_game(model1, model2, exploration_rate=0.5):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Let's play Tic-Tac-Toe!")
    print_board(board)

    while True:
        empty_cells = get_empty_cells(board)
        model_input = [1 if board[row][col] == 'x' else 2 if board[row][col] == 'o' else 0 for row, col in
                       empty_cells] + [0] * (9 - len(empty_cells))

        if random.random() < exploration_rate:
            random_move = random.choice(range(len(empty_cells)))
            predicted_row, predicted_col = empty_cells[random_move]
        else:
            predicted_move = model1.predict([model_input])[0]
            predicted_row, predicted_col = empty_cells[predicted_move]

        make_move(board, predicted_row, predicted_col, 'X')
        print("Model 1's move:")
        print_board(board)

        if check_winner(board, 'X'):
            print("Model 1 wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        empty_cells = get_empty_cells(board)
        model_input = [1 if board[row][col] == 'x' else 2 if board[row][col] == 'o' else 0 for row, col in
                       empty_cells] + [0] * (9 - len(empty_cells))

        if random.random() < exploration_rate:
            random_move = random.choice(range(len(empty_cells)))
            predicted_row, predicted_col = empty_cells[random_move]
        else:
            predicted_move = model2.predict([model_input])[0]
            predicted_row, predicted_col = empty_cells[predicted_move]

        make_move(board, predicted_row, predicted_col, 'O')
        print("Model 2's move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("Model 2 wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break


def get_human_move(board):
    while True:
        try:
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integers.")


def play_gameAI(model):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Let's play Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        human_row, human_col = get_human_move(board)
        make_move(board, human_row, human_col, 'X')
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # Model's turn
        empty_cells = get_empty_cells(board)
        model_input = [1 if board[row][col] == 'x' else 2 if board[row][col] == 'o' else 0 for row, col in
                       empty_cells] + [0] * (9 - len(empty_cells))

        predicted_move = model.predict([model_input])[0]
        predicted_row, predicted_col = empty_cells[predicted_move]
        make_move(board, predicted_row, predicted_col, 'O')
        print("Model's move:")
        print_board(board)

        # Check if the model wins
        if check_winner(board, 'O'):
            print("Oops! The model wins!")
            break

        # Check if the board is full
        if is_board_full(board):
            print("It's a draw!")
            break
