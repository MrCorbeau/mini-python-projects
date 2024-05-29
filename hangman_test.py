import random

word_list = ["gameboy", "playstation", "nintendo", "mario", "luigi"]
blanks = []
tempList = []

chosen_word = word_list[random.randint(0,len(word_list) - 1)]
life = 6
isGameEnded = False

for letter in chosen_word:
        blank = "_"
        blanks += blank

temp0 = ""
for x in range(0, len(chosen_word)):
    temp0 = chosen_word[x]
    tempList.append(temp0)

while not isGameEnded:
    print(blanks)
    print(f"remaining life points : {life}")

    guess = input("Guess a letter for the word : ").lower()
    print("\n")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess: 
            blanks.pop(position)
            blanks.insert(position, guess)
    if guess not in chosen_word:
        life-=1
    
    if "_" not in blanks:
        print("\n\n")
        print(blanks)
        print("you win!")
        isGameEnded = True
    
    if life == 0:
        print("\n\n")
        print(tempList)
        print("you lost!")
        isGameEnded = True