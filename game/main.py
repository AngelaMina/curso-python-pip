#!/usr/bin/env python3

import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if user_option not in options:
        print('Esa opción no es válida')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('¡El usuario ganó!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('¡La computadora ganó!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('¡El usuario ganó!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('¡La computadora ganó!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('¡El usuario ganó!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('¡La computadora ganó!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0  
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None:
            continue

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break

if __name__ == "__main__":
    run_game()
