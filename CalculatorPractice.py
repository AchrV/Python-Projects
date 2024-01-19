import os
import math
import secrets
import string

# Function for performing addition
def addition():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    # Initialize variable to control the continuation of calculation
    continue_calc = 'y'

    # Take two numbers as input from the user
    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 + num_2  # Perform addition
    values_entered = 2
    print(f'The Current result: {ans}')  # Display the result

    # Loop to allow user to continue adding more numbers
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ')

        # Validate user's choice to continue or not
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

        # Break out of the loop if user chooses not to continue
        if continue_calc.lower() == 'n':
            break

        # Take another number as input and add to the current result
        num = float(input('Enter another number: '))
        ans += num  # Update the result with the new number
        print(f'Current result: {ans}')
        values_entered += 1  # Track the number of values entered

    # Return the final result and the count of values entered
    return [ans, values_entered]

# Function for performing subtraction
def subtraction():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    # Initialize variable to control the continuation of calculation
    continue_calc = 'y'

    # Take two numbers as input from the user
    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 - num_2  # Perform subtraction
    values_entered = 2
    print(f'The Current result: {ans}')  # Display the result

    # Loop to allow user to continue subtracting more numbers
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ')

        # Validate user's choice to continue or not
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

        # Break the loop if user chooses not to continue
        if continue_calc.lower() == 'n':
            break

        # Take another number as input and subtract from the current result
        num = float(input('Enter another number: '))
        ans -= num  # Update the result with the new number
        print(f'Current result: {ans}')
        values_entered += 1  # Track the number of values entered

    # Return the final result and the count of values entered
    return [ans, values_entered]

# Function for performing multiplication
def multiplication():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')

    # Initialize variable to control the continuation of calculation
    continue_calc = 'y'

    # Take two numbers as input from the user
    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))
    ans = num_1 * num_2  # Perform multiplication
    values_entered = 2
    print(f'The Current result: {ans}')  # Display the result

    # Loop to allow user to continue multiplying more numbers
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ')

        # Validate user's choice to continue or not
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

        # Break the loop if user chooses not to continue
        if continue_calc.lower() == 'n':
            break

        # Take another number as input and multiply with the current result
        num = float(input('Enter another number: '))
        ans *= num  # Update the result with the new number
        print(f'Current result: {ans}')
        values_entered += 1  # Track the number of values entered

    # Return the final result and the count of values entered
    return [ans, values_entered]

# Function for performing division
def division():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')

    # Initialize variable to control the continuation of calculation
    continue_calc = 'y'

    # Take two numbers as input from the user
    num_1 = float(input('Please Enter a number: '))
    num_2 = float(input('Please Enter another number: '))

    # Ensure the second number is not zero to avoid division by zero
    while num_2 == 0.0:
        print('Please enter a second number > 0')
        num_2 = float(input(' Please Enter another number: '))

    ans = num_1 / num_2  # Perform division
    values_entered = 2
    print(f'The Current result: {ans}')  # Display the result

    # Loop to allow user to continue dividing more numbers
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ')

        # Validate user's choice to continue or not
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

        # Break the loop if user chooses not to continue
        if continue_calc.lower() == 'n':
            break

        # Take another number as input for division, ensuring it's not zero
        num = float(input('Enter another number: '))
        while num == 0.0:
            print('Please enter a number > 0')
            num = float(input('Enter another number: '))
        ans /= num  # Perform the division and update the result
        print(f'Current result: {ans}')
        values_entered += 1  # Track the number of values entered

    # Return the final result and the count of values entered
    return [ans, values_entered]

# Function for performing exponentiation
def exponentiation():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exponentiation')

    # Take the base and exponent as input from the user
    num_base = float(input('Enter the base number: '))
    exponent = float(input('Enter the exponent: '))
    ans = num_base ** exponent  # Perform exponentiation
    print(f'Current result: {ans}')

    return [ans, 2]

# Function for calculating square root
def square_root():
    # Clear the console screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Square Root')

    # Take a number as input, ensuring it's non-negative
    num = float(input('Please Enter a number: '))
    while num < 0:
        print('Please enter a non-negative number')
        num = float(input('Enter a number: '))

    ans = math.sqrt(num)  # Calculate the square root
    print(f'Current result: {ans}')

    return [ans, 1]

# Main calculator function
def calculator():
    quit = False
    while not quit:
        results = []
        # Display the menu options
        print('Simple Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'e\' for exponentiation')
        print('Enter \'r\' for square root')
        print('Enter \'q\' to quit')

        choice = input('Selection: ')

        # Handle user's choice and call the appropriate function
        if choice == 'q':
            quit = True
            continue

        if choice == 'a':
            results = addition()
        elif choice == 's':
            results = subtraction()
        elif choice == 'm':
            results = multiplication()
        elif choice == 'd':
            results = division()
        elif choice == 'e':
            results = exponentiation()
        elif choice == 'r':
            results = square_root()
        else:
         print('Sorry,  thats an ainvalid character')

        print('Ans = ', results[0], ' total inputs: ', results[1])

if __name__ == '__main__':
    calculator()

    
