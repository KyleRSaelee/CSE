import random
guess_total = 8
guesses_taken = 0
letter_guessed = []  # Displays what letters you've guessed
words_list = ["red", "blue", "white", "cyan", "pink", "black", "orange", "violet",
              "grey", "grapes", "orange", "fruits", "pear"]
word_selected = random.choice(words_list)
hidden_word = []
print(word_selected)  # Remove when finished

for letter in word_selected:
    hidden_word.append(".")
print("".join(hidden_word))
string1 = word_selected


def index_of(word, letter, starting_index):
    try:
        chopped_word = word[starting_index]
        found_index = chopped_word.index(letter)
        return found_index + starting_index
    except ValueError:
        return -1


win = 0


while win == 0:

    for letter in range(len(word_selected)):
        char_guessed = input("Guess a random letter.")
        if char_guessed in word_selected:
            print()
            print("Yep! that letter is in the word.")
            current_index = word_selected.index(char_guessed)
            hidden_word.pop(current_index)
            hidden_word.insert(current_index, char_guessed)
            print("".join(hidden_word))

        elif char_guessed is not word_selected:
            print()
            print("That letter isn't in the word.")
            guess_total -= 1
            print("".join(hidden_word))

        if guess_total == 0:
            win = 1
            print()
            print("You have ran out of guesses.")

        if "." not in hidden_word:
            win = 1
            print("Congrats, you've got the word!")

        letter_guessed.append(char_guessed)
        print()
        print("You have %s guesses left." % guess_total)
