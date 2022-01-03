# Engeto Bulls and Cows project
import random


def create_list_of_numbers(num):
    return [int(i) for i in str(num)]


def check_for_duplicity(num):
    num_li = create_list_of_numbers(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def generate_number():
    while True:
        num = random.randint(1000, 9999)
        if check_for_duplicity(num):
            return num


def number_of_bulls_and_cows(num, guess):
    bull_or_cow = [0, 0]
    num_li = create_list_of_numbers(num)
    guess_li = create_list_of_numbers(guess)

    # Deciding bull or cow using if else and enumerate
    for index, number in enumerate(guess_li):
        if number in num_li:
            if number == num_li[index]:
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
    loopend = "no"
    while loopend == "no":
        try:
            guess = int(guess)
            if not check_for_duplicity(guess):
                guess = input("Number should not have repeated digits. Try again:")
            if len(str(guess)) != 4:
                guess = input("Number should have 4 digits. Try again:")
            if isinstance(guess, int):
                loopend = "yes"
        except ValueError:
            guess = input("You entered incorrect value. Please enter a integer:")
        except guess < 1000 or guess > 9999:
            guess = input("Enter 4 digit number only. Try again:")
    return int(guess)


def main():
    # variable and loop for possible replay
    want_to_continue = "yes"
    while want_to_continue == "yes":
        # Secret Code
        tries = check_tries_input_validity()
        num = generate_number()
        # Game
        while tries > 0:
            guess = check_guess_input_validity()

            bull_cow = number_of_bulls_and_cows(num, guess)
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
            tries -= 1

            if bull_cow[0] == 4:
                print("You guessed right!")
                break
        else:
            print(f"You ran out of tries. Number was {num}")
        want_to_continue = check_continue_input_validity()
main()