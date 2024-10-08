import random

def guess_number_game(random_number=None):
    if random_number is None:
        random_number = random.randrange(1, 10)

    def get_input(prompt):
        while True:
            user_input = input(prompt)
            try:
                return int(user_input)
            except ValueError:
                print("Invalid number")

    print("***Guess The Number***")
    name = input("What's your name? ")
    print(f"Hello {name}!")

    user_input = get_input("Guess a number between one and ten:")

    if user_input == random_number:
        print("You won!")
        print(f"The number was: {random_number}")
        return True

    i = 0
    while i < 2 and user_input != random_number:
        user_input = get_input(f"Wrong guess! You have {2-i} chance left!")
        i += 1
        if user_input == random_number and i < 3:
            print("You won!")
            print(f"The number was: {random_number}")
            return True
        elif i == 2:
            print("You lost!")
            return False

if __name__ == "__main__":
    guess_number_game()
