import requests, random, os.path

def generate_secret_word():
    return (requests.get("https://random-word-api.herokuapp.com/word?number=1").text).replace('["', "").replace('"]', "")

def generate_hint_letter_list(word):
    return list(word)

def add_best_score(score: int): # pass a score, and then if it's better than the previous best score, then it will set it to be the new best score.
    with open("bestscore.txt", "w") as f:
        f.write(f"{score}")

def view_best_score():
    if os.path.isfile("bestscore.txt") == False:
        os.mknod("bestscore.txt")
        print("There is currently no best score saved.")
    elif os.path.getsize("bestscore.txt") == 0:
            print("There is currently no best score saved.")
    else: # it should exist
        f = open("bestscore.txt")
        print(f"Current best score: {f.read()}")

def main():
    word = generate_secret_word()
    #print(word)
    guess_count = 0
    hint_list = generate_hint_letter_list(word)
    word_guessed = False
    while guess_count <=10 and word_guessed == False:
        guess = input("Guess the word: ")
        if guess_count == 10:
            print(f"You have run out of guesses! The word was '{word}'.")
        if guess != word:
            guess_count += 1
            print(f"Failure, the word is not {guess} - You are on attempt #{guess_count}")
            # give a hint, user got it incorrect
            print(f"Hint: The word contains the letter {random.choice(hint_list)}")
            continue
        elif guess == word:
            print(f"Correct! You guessed the word correctly within {guess_count} guesses. - The word was {word}")
            word_guessed = True
            add_best_score(guess_count)


try:
    while True:
        print("Welcome to the secret word guessing game!")
        userchoice = input("1. Play game\n2. See best score\n3. Exit\nWhat would you like to do: ")
        if userchoice == "1": # play game
            main()
        elif userchoice == "2": # see best score
            view_best_score()
        elif userchoice == "3": # exit
            break
        else:
            print("Wrong input!") # 
except Exception as e:
    print(f"Something went wrong - Error: {e}")
