"""
Игра 'Крестики-нолики'.
"""

import random

PLAY_BOARD = [str(num) if num > 9 else '0'+str(num) for num in range(100)]
PLAYERS_MARKS = ['X', 'O']
X_POSITIONS = list()
Y_POSITIONS = list()
EMPTY_POSSITIONS_LIST = [int(el) for el in PLAY_BOARD]
LOSE_CHECK_LIST = \
    [[i + ln + al for i in range(5)] for ln in range(6) for al in range(0, 91, 10)] + \
    [[i*10 + gn + al for i in range(5)] for gn in range(10) for al in range(0, 51, 10)] + \
    [[i + ln + al for i in range(0, 45, 11)] for ln in range(6) for al in range(0, 51, 10)] + \
    [[i + ln + al for i in range(4, 41, 9)] for ln in range(6) for al in range(0, 51, 10)]
    # все пятерки по горизонтали
    # все пятерки по вертикали
    # все пяторои по диаганали слево на прово
    # все пяторои по диаганали справо на лево


def display_board(board_list):
    """Генерация игрового поля"""

    for i, el in enumerate(board_list):
        if i % 10 == 0:
            print('\n\033[36m' + '+' + '----+'*10, end='\n| \033[0m')
        print(el, end=' \033[36m|\033[0m ')
    print('\n\033[36m' + '+' + '----+'*10, end='\n\033[0m')


def player_input():
    """Выбор игровой роли: крестик или нолик"""

    player_first = ""
    while player_first not in ('X', 'O'):
        player_first = input('Вы хотите играть за X или O? ').upper()

    if player_first == 'X':
        player_second = 'O'
    else:
        player_second = 'X'

    return player_first, player_second


def place_marker(board, marker, position):
    """Установка маркера игрока в указанную позицию"""
    added_str = f'\033[31m{marker}\033[0m ' if marker == 'X' else f'\033[33m{marker}\033[0m '
    board[position] = added_str


def lose_check(mark):
    """Проверка выиграл ли игрок с указанным маркером игру"""

    chenge_passitions = X_POSITIONS if mark == 'X' else Y_POSITIONS
    if len(chenge_passitions) < 5:
        return False
    return any(all(x in chenge_passitions for x in lst) for lst in LOSE_CHECK_LIST)



def choose_first():
    """Определение случайным образом игрока, который будет ходить первым"""

    return PLAYERS_MARKS[random.choice((0, 1))]


def full_board_check(board):
    """Определяет имеется ли на игровой доске оба маркера: X и O"""

    return len(set(board)) == 2


def player_choice(board, player_mark, second_player):
    """Выбор игроком следующей ячейки для хода и проверка того можно ли поставить маркер в эту ячейку"""

    position = -1

    if player_mark ==  second_player[1]:
        position = random.choice(EMPTY_POSSITIONS_LIST)
    else:

        while position not in [num for num in range(100)]:
            try:
                position = int(input(f'\nИгрок "{player_mark}", введите адрес ячейки для хода.\nВвод осуществляется числом в диапазоне от 0 до 99: '))
                if position not in EMPTY_POSSITIONS_LIST:
                    position = -1
                    raise ValueError
            except ValueError:
                print(f'\033[31mНеверное значение. Пожалуйста, введите числом адрес пустой ячейки.\033[0m')

    X_POSITIONS.append(position) if player_mark == 'X' else Y_POSITIONS.append(position)
    EMPTY_POSSITIONS_LIST.remove(position)
    return position


def replay():
    """Предложение игрокам начать игру заново"""

    decision = ""
    while decision not in ('да', 'нет'):
        decision = input(
            'Вы бы хотели поиграть еще раз? Напишите "да" или "нет"'
        ).lower()

    return decision == 'да'


def clear_screen():
    """Очищение игрового экрана добавлением пустых строк"""

    print('\n' * 100)


def switch_player(mark):
    """Переключение роли игрока для смены очереди для хода"""

    return 'O' if mark == 'X' else 'X'


def check_game_finish(mark):
    """Проверка того, завершена ли игра"""

    if lose_check(mark):
        print(f'\033[31mИгрок "{mark}" проиграл!\033[0m')
        return True

    if full_board_check(PLAY_BOARD):
        print('Игра завершилась вничью.')
        return True

    return False


print('Добро пожаловать в игру "Крестики-нолики"!')

PLAYER_MARKS = player_input()
CURRENT_PLAYER_MARK = choose_first()

print(f'Игрок "{CURRENT_PLAYER_MARK}" ходит первым.')

while True:
    display_board(PLAY_BOARD)

    print(f'Очередь игрока "{CURRENT_PLAYER_MARK}":')

    PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_MARKS)
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD = [str(num) if num > 9 else '0'+str(num) for num in range(100)]
            X_POSITIONS = list()
            Y_POSITIONS = list()
            EMPTY_POSSITIONS_LIST = [int(el) for el in PLAY_BOARD]
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()