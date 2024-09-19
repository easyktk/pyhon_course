from random import randrange


def display_board(board):
    line = ("+" + "-" * 7) * 3 + "+"
    print(line)
    for ind1, row in enumerate(board):
        print(("|" + " " * 7) * 4)
        print("|", end="")
        for ind2, cell in enumerate(row):
            print(f"   {cell}   |", end="")
        print()
        print(("|" + " " * 7) * 4)
        print(line)
    # Функція приймає один параметр, що містить поточний статус дошки
    # і виводить його на консоль.


def enter_move(board):
    # Функція приймає поточний статус дошки, запитує користувача про його хід,
    # перевіряє введення та оновлює дошку відповідно до рішення користувача.
    move = input("Введіть свій хід: ")
    try:
        move = int(move)
        if 1 > move > 9:
            raise ValueError
        move -= 1
        row = move // 3
        col = move % 3
        if type(board[row][col]) is not int:
            raise ValueError
        board[row][col] = "O"
    except ValueError:
        print("Невірний ввід")
        enter_move(board)
    return board


def make_list_of_free_fields(board):
    # Функція перевіряє дошку та створює список усіх вільних квадратів;
    # список складається з кортежів, так що кожен кортеж є парою номерів рядка і стовпчика.
    for ind1, row in enumerate(board):
        res = []
        for ind2, cell in enumerate(row):
            if type(cell) is int:
                res.append((ind1, ind2))
    return res


def winner_for(board, sign):
    # Функція аналізує стан дошки, щоб перевірити, чи
    # э в грі переможець
    for line in board:
        if line.count(sign) == 3:
            return True
    lines = []
    for coll in range(3):
        res = []
        for row in range(3):
            res.append(board[row][coll])
        lines.append(res)
    lines.append([board[i][3 - 1 - i] for i in range(3)])
    lines.append([board[i][i] for i in range(3)])
    for line in lines:
        if line.count(sign) == 3:
            return True


def draw_move(board):
    # Функція малює хід комп'ютера та оновлює дошку.
    if board[1][1] == 5:
        board[1][1] = "X"
        return board
    move = randrange(8)
    row = move // 3
    col = move % 3
    while type(board[row][col]) is not int:
        move = randrange(8)
        row = move // 3
        col = move % 3
    board[row][col] = "X"
    return board

# board = [[(i + 1) + (3 * j) for i in range(3)] for j in range(3)]
