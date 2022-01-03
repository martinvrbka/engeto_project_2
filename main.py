# Engeto Bulls and Cows project
import random


# Returns list of digits
def create_list_of_numbers(num):
    return [int(i) for i in str(num)]


# Checks duplicity of number
def check_for_duplicates(num):
    num_li = create_list_of_numbers(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


# Generates a unique 4 digit number
def generate_number():
    while True:
        num = random.randint(1000, 9999)
        if check_for_duplicates(num):
            return num


# compares two lists to decide bulls and cows
def number_of_bulls_and_cows(num, guess):
    bull_cow = [0, 0]
    num_li = create_list_of_numbers(num)
    guess_li = create_list_of_numbers(guess)
    for index, number in enumerate(guess_li):

        # common digit present
        if number in num_li:

            # common digit exact match
            if number == num_li[index]:
                bull_cow[0] += 1

            # common digit match but in wrong position
            else:
                bull_cow[1] += 1

    return bull_cow

def user_valid_continue_input():
    user_input = input("Do you want to play again? yes/no:")
    acceptable_values = ["yes", "no", "y", "n", "YES", "NO", "Y", "N"]
    while user_input not in acceptable_values:
        user_input = input("You have used unsupported value. Please try to use yes or no:")
    else:
        return user_input

def user_valid_tries_input():
    tries = input('Enter number of tries: ')
    while not isinstance(tries, int):
        try:
            tries = int(tries)
            return tries
        except ValueError:
            tries = input("You entered incorrect value. Please enter a integer:")

def user_valid_guess_input():
    guess = input("Enter your guess: ")
    loopend = "no"
    while loopend == "no":
        try:
            guess = int(guess)
            if not check_for_duplicates(guess):
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
        tries = user_valid_tries_input()
        num = generate_number()
        # Game
        while tries > 0:
            guess = user_valid_guess_input()

            bull_cow = number_of_bulls_and_cows(num, guess)
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
            tries -= 1

            if bull_cow[0] == 4:
                print("You guessed right!")
                break
        else:
            print(f"You ran out of tries. Number was {num}")
        want_to_continue = user_valid_continue_input()
main()