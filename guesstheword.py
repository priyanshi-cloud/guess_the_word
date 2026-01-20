import random
#list of guessed words(fruits)
words=["apple","banana","grape","orange","peach","melon","kiwi","mango","pear"]
#slecting a random word from the list
chosen_word=random.choice(words)
hint_letter=random.choice(chosen_word)

selected_word=[]
selected_word.append(hint_letter)
attempts=3
print("Welcome to Guess The Word!🤩🍎,guess the fruit.....")
while attempts>0:
    display_word=""
    for letter in chosen_word:
        if letter in selected_word:
            display_word+=letter
        else:
            display_word+="_"
    print("\nwords:",display_word)
    print("attempts left:",attempts)     
    guess=input("guess a letter ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.")
        continue
    selected_word.append(guess)
    if guess not in chosen_word:
        attempts-=1
        print("Wrong guess. Try again!")
    if all(letter in selected_word for letter in chosen_word):
        print(f"Congratulations! You guessed the word: {chosen_word} 🎉")
        break   
    if attempts==0:
        print(f"Sorry, you've run out of attempts. The word was: {chosen_word} 😞")     