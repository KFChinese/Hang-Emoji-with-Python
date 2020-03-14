import random
import time
from os import system, name
from random_word import RandomWords


# define our clear function
def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


r = RandomWords()


def get_word():

    randomword = r.get_random_words(hasDictionaryDef="true", limit=1, maxLength=12)
    word = random.choice(randomword)
    return word.upper()


def play(word):
    word_completion = "*" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hang Emoji!")
    time.sleep(0.8)
    print("Let's play a game.")
    print(display_hangman(tries))
    print("The word has", len(word), "letters.")
    print("Answer:", word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear()
                print('You already guessed the letter "' + guess + '".')
            elif guess not in word:
                clear()
                print('"' + guess + '" is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear()
                print('Good job, "' + guess + '" is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "*" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                clear()
                print('You already guessed the word: "' + guess + '".')
            elif guess != word:
                clear()
                print('"' + guess + '" is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            clear()
            print('"' + guess + '" is Not a valid guess.')
        print(display_hangman(tries))
        #print("Answer Key:",word)
        # ^Uncomment("#") above to get answer Key.
        print("The word has", len(word), "letters.")
        print("Answer:", word_completion)
        print("Letters Guessed:", guessed_letters)
        print("Words Guessed:", guessed_words)
        if tries == 1:
            print("You have", tries, "valid try left. Choose Wisely!")
        elif tries != 0:
            print("You have", tries, "valid tires left.")
        print("\n")
    if guessed:
        clear()
        print(" 🥰 -My Hero!")
        print("\\|/")
        print(" |")
        print("/ \\")
        print("Congrats, you guessed", word, "You win!")
        time.sleep(4.5)
        clear()
    else:
        clear()
        print(" 💀 -Mission Failed. We'll get them next time.")
        print("\\|/")
        print(" |")
        print("/ \\")
        print(
            'Sorry, you ran out of tries. The word was "' + word + '". Maybe next time!'
        )
        time.sleep(4.5)
        clear()


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   ==========
                   ||      |
                   ||      💀
                   ||     \\|/
                   ||      |
                   ||     / \\
                   ----------
                """,
        # head, torso, both arms, and one leg
        """
                   ==========
                   ||      |   
                   ||      🥺 -Help!
                   ||     \\|/
                   ||      |
                   ||     /
                   ----------
                """,
        # head, torso, and both arms
        """
                   ==========
                   ||      |
                   ||      😭
                   ||     \\|/
                   ||      |
                   ||    
                   ----------
                """,
        # head, torso, and one arm
        """
                   ==========
                   ||      |
                   ||      😑
                   ||     \\|
                   ||      |
                   ||    
                   ----------
                """,
        # head and torso
        """
                   ==========
                   ||      |
                   ||      🙃
                   ||      |
                   ||      |
                   ||    
                   ----------
                """,
        # head
        """
                   ==========
                   ||      |
                   ||      😕
                   ||      
                   ||      
                   ||    
                   ----------
                """,
        # initial empty state
        """
                   ==========
                   ||      |
                   ||      
                   ||      
                   ||      
                   ||    
                   ----------
                """,
    ]
    return stages[tries]


def main():
    clear()
    word = get_word()
    clear()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        clear()
        clear()
        word = get_word()
        play(word)


if __name__ == "__main__":
    clear()
    main()
