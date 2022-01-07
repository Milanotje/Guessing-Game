import random

def generate_random_number():
    return random.randint(1, 10)

def get_user_input():
    return int(input("Enter a random number between 1 and 10: "))

def check_user_input(user_input, random_number):
    if user_input == random_number:
        return True
    else:
        return False
    
def play_game():
    random_number = generate_random_number()
    user_input = get_user_input()
    result = check_user_input(user_input, random_number)
    print_result(result)

play_game()

def play_game_repeatedly():
    while True:
        play_game()
        user_input = input("Do you want to play again? (y/n): ")
        if user_input == "n":
            break

play_game_repeatedly()
