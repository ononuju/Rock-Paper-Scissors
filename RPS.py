
import random

possible_actions = ['R', 'P', 'S']

# get user input and handle invalid inputs
while True:
    print('R is for rock, Pis for paper, S is for scissors')
    user_action = input('Enter a choice between R, P, and S: ')
    while user_action not in possible_actions:
        user_action = input('Eror! Enter a valid selection\n')
    cpu_action = random.choice(possible_actions)
    print(f'\nPlayer - {user_action} : CPU - {user_action}.\n')
    while user_action == cpu_action:
        user_action = input(f"Both players selected {user_action}. it's s tie! \
            \nWould you like to restart? y/n: ")
        if user_action != 'y':
            break

    if user_action == 'R':
        if cpu_action == 's':
            print('Rock smashes scissors! Yon win!')
        else:
            print('Paper cover rock! You lose')
    elif user_action == 'P':
        if cpu_action == 'R':
            print('Paper cover rock! You win!')
        else:
            print('Scissors cuts paper! You Lose.')
    elif user_action == 'S':
        if cpu_action == 'P':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose.')

        break
