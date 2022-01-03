# Engeto Bulls and Cows project
import random


def create_list_of_numbers(generated_number):
    return [int(i) for i in str(generated_number)]


def check_for_duplicity(num):
    generated_list = create_list_of_numbers(num)
    if len(generated_list) == len(set(generated_list)):
        return True
    else:
        return False


def generate_number():
    while True:
        generated_number = random.randint(1000, 9999)
        if check_for_duplicity(generated_number):
            return generated_number


def number_of_bulls_and_cows(generated_number, guess):
    bull_or_cow = [0, 0]
    generated_list = create_list_of_numbers(generated_number)
    guess_li = create_list_of_numbers(guess)

    # Deciding bull or cow using if else and enumerate
    for index, number in enumerate(guess_li):
        if number in generated_list:
            if number == generated_list[index]:
                bull_or_cow[0] += 1
            else:
                bull_or_cow[1] += 1

    return bull_or_cow


def check_continue_input_validity():
    user_input = input("Do you want to play again? yes/no:")
    acceptable_values = ["yes", "no", "y", "n", "YES", "NO", "Y", "N"]
    while user_input not in acceptable_values:
        user_input = input("You have used unsupported value. Please try to use yes or no:")
    else:
        return user_input


def check_tries_input_validity():
    tries = input('Enter number of tries: ')
    while not isinstance(tries, int):
        try:
            tries = int(tries)
            return tries
        except ValueError:
            tries = input("You entered incorrect value. Please enter a integer:")


def check_guess_input_validity():
    guess = input("Enter your guess: ")
    while not isinstance(guess, int):
        try:
            guess = int(guess)
            if not check_for_duplicity(guess):
                guess = input("Number should not have repeated digits. Try again:")
            guess = int(guess)
            if len(str(guess)) != 4:
                guess = input("Number should have 4 digits. Try again:")
        except ValueError:
            guess = input("You entered incorrect value. Please enter a integer:")
        except TypeError:
            guess = input("You entered incorrect value. Please enter a integer:")
    return int(guess)


def main():
    delimiter = 40*"-"
    want_to_continue = "yes"
    while want_to_continue == "yes":
        tries = check_tries_input_validity()
        generated_number = generate_number()

        while tries > 0:
            guess = check_guess_input_validity()
            bull_cow = number_of_bulls_and_cows(generated_number, guess)
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
            print(delimiter)
            tries -= 1

            if bull_cow[0] == 4:
                print("You guessed right!")
                print(delimiter)
                break
        else:
            print(f"You ran out of tries. Number was {generated_number}")
        want_to_continue = check_continue_input_validity()
main()