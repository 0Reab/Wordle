import json, random
from termcolor import colored

wordlist = "common.json" # 1000 most common English words
# thank you to dariusk for wordlist
# https://github.com/dariusk/corpora/blob/master/data/words/common.json

with open(wordlist, 'r') as file:
    words = json.load(file)

words = words['commonWords']
wordlist_length = len(words)

# game loop
running = True


while running:
    char = '_ '
    tries = 5
    validity = {} # for guesses

    word = words[random.randint(1, wordlist_length)] # find random word
    hidden_word = char * len(word) # ex: '_ _ _ _' for word 'abcd'

    print(hidden_word, f' {len(word)} letters')

    for _ in range(tries):
        while True: # guess validation
            user_guess = input('Your guess:\n')
            print("\033[A\033[K", end="")  # clear the input() stdout in terminal

            # check if guess is same len() of word
            if len(user_guess) == len(word):
                break
            else:
                print(f'{user_guess} is {len(user_guess)} letters\n')

        # {char_idx : 'result_color'} // green, yellow, grey
        validity = {idx:'green' if char == word[idx] else 'grey' for idx, char in enumerate(user_guess)}

        unused_letters = [word[c[0]] for c in validity.items() if c[1] != 'green']
        
        # Second pass: Check for yellows
        for idx, char in enumerate(user_guess):
            if validity[idx] == 'grey' and char in unused_letters:
                validity[idx] = 'yellow'  # Wrong position, but letter exists
                unused_letters.remove(char)  # Mark this letter as used
        # Debug output      
        # print(word)
        # print(unused_letters)
        # print(validity)

        for key, value in validity.items():
            print(colored(user_guess[key], value), end='')
        print('\n')

    q = input('Do you want to exit?\ny/n\n')

    if q == 'y': running = False































