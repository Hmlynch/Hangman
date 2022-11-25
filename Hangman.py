import random_generator
from word_library import word_list

def Random_Word():
    word = random_generator.choice(word_list)
    return word.upper()

def Game_Ruels(word): 
    word_selction = "_" * len(word) 
    guesses = False
    guess_letters = [] 
    guess_words = [] 
    attempts = 7 
    print("Hangman")
    print(f"You have {attempts} attempts left...") 
    print(word_selction) 
    print("\n")

    while not guesses and attempts > 0: 
        guess = input("Guess a letter or a word: ").upper()

        if len(guess) == 1 and guess.isalpha(): 
            if guess in guess_letters: 
                print("This letter has already been used...", guess)
            elif guess not in word: 
                print(f"{guess} is not in the word.")
                attempts -= 1
                guess_letters.append(guess)
            else: 
                print(f"Correct, {guess} is in the word!")
                guess_letters.append(guess) 
                guess_word_list = list(word_selction)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    guess_word_list[index] = guess 
                word_selction = "".join(guess_word_list) 
                if "_" not in word_selction: 
                    guess = True 

        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in guess_words:
                print(f"{guess} has already been guessed!") 
            elif guess != word: 
                print(f"{guess} is not the word")
                attempts -= 1 
                guess_words.append(guess) 
            else:
                guesses = True 
                word_selction = word 

        else: 
            print("This is not a valid guess, try again!")
        print(f"You have {attempts} attempts left...")
        print(word_selction)
        print("\n")

    if guesses:
        print("Congragulatios, you guessed the word correctly! You win the game!") 
    else: 
        print(f"Sorry, you ran out of attempts. The word was {word}.") 

def Play_Game(): 
    word = Random_Word()
    Game_Ruels(word)
    while input("Would you like to play again? (Y)es | (N)o").upper() == "Y":
        word = Random_Word()
        Game_Ruels(word)

if __name__ == "__main__":
    Play_Game()