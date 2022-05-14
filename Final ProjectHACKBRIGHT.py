from random import randint
from time import sleep


def style():
    print('-=' * 11)


def instructions():
    print("In rock-paper-scissors, two players will each randomly choose one of three hand signs: rock, paper, or "
          "scissors. "
          "Here are the rules that determine which sign beats another")
    print("- Rock wins over scissors (because rock smashes scissors)"
         "\n- Scissors wins over paper (because scissors cut paper)"
          "\n- Paper wins over rock (because paper covers rock)")
    ready = input("Press ENTER when ready to move forward >")


def welcoming_message():
    print("\033[1;35;40m**** Hi! Welcome to Rock, Paper, Scissors! ****\033[m")
    instructions_input = (input("Would you like to see the instructions? [YES] or [No]")).strip().lower()
    if instructions_input.startswith("y"):
        instructions()
    else:
        print("Ok!")
        ready2 = input("Press ENTER when ready to move forward >")


welcoming_message()

user_name = input("What's your name?").title()

itens = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)


def rock_paper_scissors():

    user_wins = 0
    computer_wins = 0

    while True:
        print("Ready to play? \n [YES] or [NO]")
        user_choice = input(">").strip().lower()

        if user_choice.startswith("y"):
            print('''Options:
            [ 0 ] ROCK
            [ 1 ] PAPER
            [ 2 ] SCISSORS''')

            player = int(input('What is your play?'))
            if player == 0 or player == 1 or player == 2:

                print('\033[1;34mROCK')
                sleep(1)
                print('PAPER')
                sleep(1)
                print('SCISSORS')
                sleep(1)
                print('SHOOT\033[m')
                sleep(1)
                style()
                print(f'Computer played {(itens[computer])}.')
                print(f'{user_name} played {(itens[player])}.')
                style()
                print()
                if computer == 0:  # rock
                    if player == 0:
                        print('\033[4;36mTIE\033[m')
                    elif player == 1:
                        print(f'\033[4;32m{user_name} wins!\033[m')
                        user_wins += 1
                    elif player == 2:
                        print('\033[4;31mComputer wins!\033[m')
                        computer_wins += 1
                    else:
                        print('Invalid! Try again!')
                elif computer == 1:  # paper
                    if player == 0:
                        print('\033[4;31mComputer wins!\033[m')
                        computer_wins += 1
                    elif player == 1:
                        print('\033[4;36mTIE\033[m')
                    elif player == 2:
                        print(f'\033[4;32m{user_name} wins!\033[m')
                        user_wins += 1
                    else:
                        print('Invalid! Try again!')
                elif computer == 2:  # scissors
                    if player == 0:
                        print(f'\033[4;32m{user_name} wins!\033[m')
                        user_wins += 1
                    elif player == 1:
                        print('\033[4;31mComputer wins!\033[m')
                        computer_wins += 1
                    elif player == 2:
                        print('\033[4;36mTIE\033[m')
                    else:
                        print('Invalid, try again!')
            else:
                print('''\033[4;33mInvalid! Only\033[m:
                \033[4;33m[ 0 ] ROCK\033[m
                \033[4;33m[ 1 ] PAPER\033[m
                \033[4;33m[ 2 ] SCISSORS\033[m''')

        elif user_choice.startswith("n"):
            break
        else:
            print("Invalid. Try again.")
        print()
        print('-=' * 11)
        print(f'You have {user_wins} wins')
        print(f'Computer has {computer_wins} wins')
        print('-=' * 11)


rock_paper_scissors()

print("Good bye! Thanks for playing with me.")
