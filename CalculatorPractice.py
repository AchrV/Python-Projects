import os
import math
import secrets
import string

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continue_calc = 'y'

    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'The Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 - num_2
    values_entered = 2
    print(f'The Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans -= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')

    continue_calc = 'y'

    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans *= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')

    continue_calc = 'y'

    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    while num_2 == 0.0:
        print('Please enter a second number > 0')
        num_2 = float(input(' Please Enter another number: '))

    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        while num == 0.0:
            print('Please enter a number > 0')
            num = float(input('Enter another number: '))
        ans /= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def exponentiation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exponentiation')

    num_base = float(input('Enter the base number: '))
    exponent = float(input('Enter the exponent: '))
    ans = num_base ** exponent
    print(f'Current result: {ans}')

    return [ans, 2]

def square_root():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Square Root')

    num = float(input('Please Enter a number: '))
    while num < 0:
        print('Please enter a non-negative number')
        num = float(input('Enter a number: '))

    ans = math.sqrt(num)
    print(f'Current result: {ans}')

    return [ans, 1]

def calculator():
    quit = False
    while not quit:
        results = []
        print('Simple Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for substraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'e\' for exponentiation')
        print('Enter \'r\' for square root')
        print('Enter \'q\' to quit')

        choice = input('Selection: ')

        if choice == 'q':
            quit = True
            continue

        if choice == 'a':
            results = addition()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'e':
            results = exponentiation()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'r':
            results = square_root()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        else:
            print('Sorry,  thats an ainvalid character')

if __name__ == '__main__':
    calculator()
    