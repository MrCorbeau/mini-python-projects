from higher_lower_art import logo
from higher_lower_art import bye
from higher_lower_art import vs
from higher_lower_art import game_over
from higher_lower_game_data import data
import random

def clear():
    return print(end="\033c")


gameWorking = True
score = 0

def generate_round():
    global gameWorking
    global gameCont
    global score

    print(logo)
    clear()
    tempA = random.choice(data)
    tempB = random.choice(data)
    if tempA == tempB : tempB = random.choice(data)

    print(f"""
-------------- Celebrity A --------------
    Name : {tempA["name"]}
    Description : {tempA["description"]}
    Country : {tempA["country"]}
              """)
    print(vs)
    print(f"""
-------------- Celebrity B --------------
    Name : {tempB["name"]}
    Description : {tempB["description"]}
    Country : {tempB["country"]}
              """)
        
    guess = input("guess which celebrity has higher follower type 'A' for Celebrity A and type 'B' for Celebrity B : ").title()
    if guess == "A" :
        if tempA["follower_count"] > tempB["follower_count"]:
                gameCont = True
                score += 1
        elif tempA["follower_count"] == tempB["follower_count"]:
                print("DRAW!!!")
                gameCont = True
        elif tempA["follower_count"] < tempB["follower_count"]:
                gameCont = False
                gameWorking = False
                clear()
                print(game_over)
    if guess == "B" :
        if tempB["follower_count"] > tempA["follower_count"]:
                gameCont = True
                score += 1
        elif tempA["follower_count"] == tempB["follower_count"]:
                print("DRAW!!!")
        elif tempB["follower_count"] < tempA["follower_count"]:
                gameCont = False
                gameWorking = False
                clear()
                print(game_over)

while gameWorking :
    clear()
    print(logo)
    user = input("do you want to play the game. type 'y' for yes 'n' for no : ").lower()
    if user == "n":
        gameWorking = False
        clear()
        print(bye)
    else:
        generate_round()
        while gameCont == True:
            generate_round()
print(f"Your score is : {score}")

            

