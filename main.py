import random
from colorama import init, Fore, Style
init(autoreset=True)

X = Fore.CYAN + 'X' + Style.RESET_ALL
O = Fore.RED + 'O' + Style.RESET_ALL

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

is_running = True

while is_running:
    print("\n 0 1 2")
    for row_index, row in enumerate(board):
        colored_row = '|'.join(X if v == 'X' else O if v == 'O' else v for v in row)
        print(f"{row_index}{colored_row}")
        if row_index < 2:
            print("----------")

    print(f"\n Зараз твій хід ({X})")
    try:
        row = int(input("Вибери номер рядка "))
        col = int(input("Введіть номер стовбця "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Error, You cannot do it")
            continue

    except (ValueError, IndexError):
        print("Error, You wrote it false")
        continue

    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]

    if winner:
        print("\n 0 1 2")
        for row_index, row in enumerate(board):
            colored_row = '|'.join(X if v == 'X' else O if v == 'O' else v for v in row)
            print(f"{row_index}{colored_row}")
            if row_index < 2:
                print("----------")
        print(f"{X if winner == 'X' else O} won!")
        is_running = False
        continue
    elif all(board[r][c] != ' ' for r in range(3) for c in range(3)):
        print("Draw!")
        is_running = False
        continue

    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    r, c = random.choice(empty_cells)
    board[r][c] = 'O'
    print(f"\n Комп'ютер ({O}) поставив на {r},{c}")
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]

    if winner:
        print("\n 0 1 2")
        for row_index, row in enumerate(board):
            colored_row = '|'.join(X if v == 'X' else O if v == 'O' else v for v in row)
            print(f"{row_index}{colored_row}")
            if row_index < 2:
                print("----------")
        print(f"{X if winner == 'X' else O} won!")
        is_running = False
    elif all(board[r][c] != ' ' for r in range(3) for c in range(3)):
        print("Draw!")
        is_running = False
