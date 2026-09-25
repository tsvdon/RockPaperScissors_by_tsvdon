import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_score = 0
computer_score = 0
unfair_advantage_player = False

while True:
    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid input. Try again.')

    computer_move = None

    if unfair_advantage_player:
        computer_random_number = random.randint(1, 5)
        if player_move == rock:
            if computer_random_number == 1 or computer_random_number == 2:
                computer_move = scissors
            elif computer_random_number == 3 or computer_random_number == 4:
                computer_move = rock
            elif computer_random_number == 5:
                computer_move = paper
        elif player_move == paper:
            if computer_random_number == 1 or computer_random_number == 2:
                computer_move = rock
            elif computer_random_number == 3 or computer_random_number == 4:
                computer_move = paper
            elif computer_random_number == 5:
                computer_move = scissors
        elif player_move == scissors:
            if computer_random_number == 1 or computer_random_number == 2:
                computer_move = paper
            elif computer_random_number == 3 or computer_random_number == 4:
                computer_move = scissors
            elif computer_random_number == 5:
                computer_move = rock
    else:
        computer_random_number = random.randint(1, 3)
        if computer_random_number == 1:
            computer_move = rock
        elif computer_random_number == 2:
            computer_move = paper
        elif computer_random_number == 3:
            computer_move = scissors

    print(f'\033[95mYou chose \033[1m\033[4m{player_move}\033[0m')
    print(f'\033[94mThe computer chose \033[1m\033[4m{computer_move}\033[0m')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('\033[92mYou win!\033[0m')
        player_score += 1
    elif player_move == computer_move:
        print('\033[93mDraw!\033[0m')
    else:
        print('\033[91mYou lose!\033[0m')
        computer_score += 1

    print(f'\033[95mYour score: {player_score}\033[0m')
    print(f'\033[94mComputer score: {computer_score}\033[0m')

    next_game = input('Do you want to play again? [y/n]: ')

    if next_game == 'y':
        unfair_advantage = input('Do you want to use an unfair advantage against the computer in the next round? [y/n]: ')
        if unfair_advantage == 'y':
            unfair_advantage_player = True
        elif unfair_advantage == 'n':
            unfair_advantage_player = False
        else:
            raise SystemExit('Invalid input. Try again.')
        continue
    elif next_game == 'n':
        print('Thank you for playing!')
        break
    else:
        raise SystemExit('Invalid input. Try again.')


