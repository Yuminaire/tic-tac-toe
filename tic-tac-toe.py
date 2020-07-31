import random
import os

nbToLtr = {'0': 'A', '1': 'B', '2': 'C'}
ltrToNb = {'A': 0, 'B': 1, 'C': 2}
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
signs = ['O', 'X']
players = ['player', 'bot']
free_cases = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
player = signs[random.randint(0, 1)]
bot = 'O' if player == 'X' else 'X'


def print_grid():
    print('\n    1    2    3')
    print('A', grid[0])
    print('B', grid[1])
    print('C', grid[2], '\n')


def start_game():
    os.system('cls')
    print('You will play as ' + player +
          ' and your opponent will play as ' + bot + '.')
    first_turn = players[random.randint(0, 1)]
    play_turn(first_turn)


def play_turn(turn):
    if not check_win():
        if turn == 'bot':
            row, col = random.randint(0, 2), random.randint(0, 2)
            grid[row][col] = bot if grid[row][col] == ' ' else play_turn('bot')
            update_free_cases(str(row) + str(col))
            print('The computer played ' + nbToLtr[str(row)] + str(col+1) + '.')
            play_turn('player')
        else:
            print_grid()
            print('Available cases: ' + ", ".join(free_cases) + '.')
            choice = input('Where do you want to play ? (eg. A3) ').upper()
            if choice not in free_cases:
                os.system('cls')
                play_turn('player')
            else:
                grid[ltrToNb[choice[0]]][int(choice[1])-1] = player
                update_free_cases(choice)
                os.system('cls')
                play_turn('bot')
    else:
        quit()


def update_free_cases(case):
    nb = ['0', '1', '2']
    if case[0] in nb:
        case = nbToLtr[case[0]] + str(int(case[1]) + 1)
    free_cases.remove(case)


def check_win():
    if (grid[0][0] == grid[1][1] == grid[2][2] != ' ' or grid[0][2] == grid[1][1] == grid[2][0] != ' '):
        win(grid[0][0])
        return True
    else:
        for i in range(len(grid)):
            if grid[i].count(grid[i][0]) == 3 and grid[i][0] != ' ':
                win(grid[i][0])
                return True
            elif grid[0][i] == grid[1][i] == grid[2][i] != ' ':
                win(grid[0][i])
                return True
    if not free_cases:
        draw()
        return True


def draw():
    print_grid()
    print('It\'s a draw, no one wins.')


def win(winner):
    print_grid()
    if winner == player:
        print('Congratulations, you won!')
    else:
        print('Looser, your opponent won!')


start_game()
