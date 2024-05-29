import random

def clear():
    return print(end="\033c")

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

gameStarts = True

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J" ,"Q" ,"K"]

players_hand = []
computers_hand = []
player_point = 0
computer_point = 0

def generate_card():
    card = cards[random.randint(0,11)]

    return card

def generate_point(card):
    point = 0
    if card == "A":
        x = random.randint(0,1)
        if x == 0:
            point = 1
        else:
            point = 11
    elif card == "J" or card == "Q" or card == "K":
        point+=10
    else:
        point = card

    return point
    
def generate_round_forP():
    P_starting_card = generate_card()
    player_point = generate_point(P_starting_card)

    players_hand.append(P_starting_card)

    return player_point

def generate_round_forC():
    C_starting_card = generate_card()
    computer_point = generate_point(C_starting_card)

    computers_hand.append(C_starting_card)

    return computer_point

print(logo)
while gameStarts:
    gameRuns = input("if you want to play the game type 'y' otherwise type 'n' : ").lower()
    if gameRuns == "n":
        clear()
        print("You made a right choise. Gambling is addictive.")
        gameStarts = False
    else:
        player_point = generate_round_forP()
        computer_point = generate_round_forC()

        print(f"""player's hand : {players_hand}
player's point : {player_point}

computer's hand : {computers_hand}
computer's hand : {computer_point}\n\n""")

        gameCont = True

        while gameCont :
            draw_or_stay = input("if you want to draw a card type 'd' or if you want to stay type 's' : ").lower()
#if player draws a card
            if draw_or_stay == "d":
                clear()
                print(logo)
                player_point += generate_round_forP()
                comp_draw_chance = random.randint(0,100)
                if comp_draw_chance <= 63 :
                    computer_point += generate_round_forC()
                print(f"""player's hand : {players_hand}
player's point : {player_point}

computer's hand : {computers_hand}
computer's point : {computer_point}\n\n""")
            
                if player_point > 21 :
                    print("Computer Wins!!")
                    gameCont = False
                    gameStarts = False
                elif computer_point > 21 :
                    print("Player Wins!!")
                    gameCont = False
                    gameStarts = False
                elif player_point == 21:
                    print("Player Wins!!")
                    gameCont = False
                    gameStarts = False
                elif computer_point == 21:
                    print("Computer Wins!!")
                    gameCont = False
                    gameStarts = False
                elif player_point == 21 and computer_point == 21 :
                    print("Draw!!")
                    gameCont = False
                    gameStarts = False
#if player stays
            elif draw_or_stay == "s" :
                clear()
                print(logo)
                comp_draw_chance = random.randint(0,100)
                if comp_draw_chance <= 36 :
                    computer_point += generate_round_forC()
                print(f"""player's hand : {players_hand}
player's point : {player_point}

computer's hand : {computers_hand}
computer's point : {computer_point}\n\n""")
                if computer_point == 21:
                        print("Computer Wins!!")
                        gameCont = False
                        gameStarts = False    
                elif computer_point > 21 :
                        print("Player Wins!!")
                        gameCont = False
                        gameStarts = False