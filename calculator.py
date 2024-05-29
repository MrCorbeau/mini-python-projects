logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

isRunning = True

def add(x,y):    
    return int(x) + int(y)
def sub(x,y):
    return int(x) - int(y)
def divide(x,y):
    return int(x) / int(y)
def mulitply(x,y):
    return int(x) * int(y)

result = input("type a number : ")

while isRunning:
    numb2 = input("type a number again : ")
    calculate_str = """pick an operation :
    type 'a' for adding
    type 's' for substraction
    type 'd' for dividing
    type 'm' for multiply
    """
    action = input(calculate_str)
    if action == "a":
        result = add(result, numb2)
    elif action == "s":
        result = sub(result, numb2)
    elif action == "d":
        result = divide(result, numb2)
    elif action == "m":
        result = mulitply(result, numb2)
    
    print(f"Result : {result}")
    user = input("type 'y' in order to continue or 'n' to end it : ")
    if user == "n":
        isRunning = False