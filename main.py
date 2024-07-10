import random

words = ['python', 'java', 'kotlin', 'javascript', 'swift', 'ruby']

print("The Word Was: python', 'java', 'kotlin', 'javascript', 'swift', 'ruby' ")

# Randomly choose a word from the list
chosen_word = random.choice(words)

# Create a list of underscores
word_display = ["-" for _ in chosen_word]

print(word_display)
attempts = 8 # Number of allowed attempts

print("Welcome To Hangman!")

while attempts > 0 and '-' in word_display:
    print("\n" + ''.join(word_display))
    guess = input("Guess a Letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
                
    else:
        print("The letter doesn't appear in the word ")
        attempts -= 1
        
# Game Conclusion

if '-' not in word_display:
    print("You guessed the word!")
    print(''.join(word_display))
    print("You Survived")
    
else:
    print("You ran out of attempts, The Word was: " + chosen_word)
    print("You Lost")                     
