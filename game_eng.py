import random


def bot():
    action = int(random.randrange(1, 4))
    print(f'BOT :: {action}')
    return action


def player():
    while True:
        action = str(input('YOU :: '))
        if action == '1' or action == '2' or action == '3':
            return int(action)
        else:
            print('! Enter 1, 2 or 3 !\n')


def info():
    print('''Symbols:
     1 - STONE
     2 - SCISSORS
     3 - PAPER''')
    print('Start the game? Y/N')
    start = input('> ').lower()
    if start == 'y' or start == 'yes':
        return True
    elif start == 'n' or start == 'no':
        return False


def logic(action_player, action_bot):
    """
1 - STONE \n
2 - SCISSORS \n
3 - PAPER \n
1 -> 2 \n
2 -> 3 \n
3 -> 1
"""
    rules = {1: 2, 2: 3, 3: 1}
    if action_player == action_bot:
        print('! Draw !')
        status = 'draw'
    elif rules[action_player] == action_bot:
        print('! You win !')
        status = 'win'
    else:
        print('! You lost !')
        status = 'lost'
    return status


def statistic(score):
    """
    score = [ win, win, --- ] \n
    score = [ win, draw, draw ] \n

    score = [ lost, lost, --- ] \n
    score = [ lost, draw, draw ] \n

    score = [ win, lost, draw ] \n
    score = [ draw, draw, draw ] \n
    """
    winner = None

    if 'win' in score:
        if score.count('win') == 2:
            winner = 'YOU'
        elif score.count('draw') == 2:
            winner = 'YOU'

    if 'lost' in score:
        if score.count('lost') == 2:
            winner = 'BOT'
        elif score.count('draw') == 2:
            winner = 'BOT'

    if score.count('win') == score.count('lost') or score.count('draw') == 3:
        winner = 'DRAW'

    print('\n|=== Statistic ===|')
    print(f'Tour #1 :: {score[0]}')
    print(f'Tour #2 :: {score[1]}')
    print(f'Tour #3 :: {score[2]}')
    print('::: RESULT :::')
    print(f'! Win {winner} !')
    print('|=================|\n')


def main():
    if info():
        score = []
        print('--- Start ---')
        for i in range(3):
            action_player = player()
            action_bot = bot()
            score.append(logic(action_player, action_bot))
            if i != 2:
                print()
        print('---- End ----')
        statistic(score)


if __name__ == '__main__':
    while True:
        main()
        print('\n-------------------')
        print('Play again? Y/N')
        repeat = str(input('> ')).lower()
        print('-------------------\n\n')
        if repeat != 'y' and repeat != 'yes':
            break
