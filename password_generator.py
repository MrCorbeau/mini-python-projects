import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordBasic = ""
passwordShuffeled = ""
tempList = []

for x in range(1, nr_letters + 1):
    randLetter = random.choice(letters)
    temp0 = random.randint(0,1)
    if temp0 == 1:
        randLetter.capitalize
    passwordBasic += randLetter
for x in range(1, nr_symbols + 1):
    randSymbol = random.choice(symbols)
    passwordBasic += randSymbol
for x in range(1, nr_numbers + 1):
    randNumber = random.choice(numbers)
    passwordBasic += randNumber

print(f"Here is a basic version of your password : {passwordBasic}. If you make it more complex write 'continue'. If you are satisfied with your password write 'end'")
makeItComplex = input().lower()

if makeItComplex == "continue":
    for y in range(0, len(passwordBasic)):
        temp1 = passwordBasic[y]
        tempList.append(temp1)

    random.shuffle(tempList)

    for y in range(0, len(tempList)):
        temp2 = tempList[y]
        passwordShuffeled += temp2

print(f"\nHere is a complex version of your password : {passwordShuffeled}\n")