from words import words
import random
import string
def valid_word(words):
    word = random.choice(words)

    return word
def hangman():
    word = valid_word(words)
    letters = set(word)
    alphabet = set(letters)
    used_letters = set()
    lives = 7
    while len(letters) > 0 and lives >0 :
        print('You are left with', lives, 'lives and You have used these letters yet that are in the word : ',' '.join(used_letters))
        words_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word ::",' '.join(words_list))
        player = input('Enter your letter : ')

        if player in alphabet - used_letters :
            used_letters.add(player)
            if player in letters:
                letters.remove(player)

        elif player in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("You have entered character that is not in the word. Please try again.")
    print(word.upper(),"\nYESS !! You have guessed right letter...")

hangman()

