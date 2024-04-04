import random

words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

stages = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   / \\
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\
    |
    ------------
    """
]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = len(stages) - 1

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(stages[len(stages) - attempts - 1])
            print(f"Remaining attempts: {attempts}")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

play_hangman()
