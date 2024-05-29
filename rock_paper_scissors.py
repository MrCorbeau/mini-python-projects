import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

movesList = [rock, paper, scissors]

player = int(input("Write 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

compMove = random.randint(0,2)

if player == 0:
    if compMove == 0:
        print("Your move :\n\n" + rock + "\n\nComputer's move :\n\n" + rock + "\n\nDRAW!!")
    elif compMove == 1:
        print("Your move :\n\n" + rock + "\n\nComputer's move :\n\n" + paper + "\n\nCOMPUTER WİNS!!")
    else:
        print("Your move :\n\n" + rock + "\n\nComputer's move :\n\n" + scissors + "\n\nPLAYER WİNS!!")
elif player == 1:
    if compMove == 0:
        print("Your move :\n\n" + paper + "\n\nComputer's move :\n\n" + rock + "\n\nPLAYER WİNS!!")
    elif compMove == 1:
        print("Your move :\n\n" + paper + "\n\nComputer's move :\n\n" + paper + "\n\nDRAW!!")
    else:
        print("Your move :\n\n" + paper + "\n\nComputer's move :\n\n" + scissors + "\n\nCOMPUTER WİNS!!")
elif player == 2:
    if compMove == 0:
        print("Your move :\n\n" + scissors + "\n\nComputer's move :\n\n" + rock + "\n\nCOMPUTER WİNS!!")
    elif compMove == 1:
        print("Your move :\n\n" + scissors + "\n\nComputer's move :\n\n" + paper + "\n\nPLAYER WİNS!!")
    else:
        print("Your move :\n\n" + scissors + "\n\nComputer's move :\n\n" + scissors + "\n\nDRAW!!")