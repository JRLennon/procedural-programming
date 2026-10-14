secret_num = 7
guess_count = 0

def display_guess_count(guess_count: int):
    print(f"You found the secret number in {guess_count} guesses.")

while True:
    guess = int(input("Guess the secret number: "))

    if guess == 7:
        print("Correct! You win!")
        guess_count+=1
        display_guess_count(guess_count)
    elif guess <7:
        print("Too low!")
        guess_count+=1
    elif guess >7:
        print("Too high!")
        guess_count+=1

