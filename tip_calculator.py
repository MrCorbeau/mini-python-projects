print("Wlecome to the tip calculator.\n")
bill = float(input("What was the total bill : "))
percentage = int(input("What percentage tip would you like to give ?10, 12, 15 : "))
party = int(input("How many people to split the bill : "))

billWithTheTip = bill + (bill * percentage)/100
result = billWithTheTip/party

print(f"Each person should pay : {round(result,2)}$")