
def clear():
    return print(end="\033c")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

list_of_bidders = {}

def find_highest(record):
    highest_bid = 0
    highest_bidder = ""
    for x in list_of_bidders:
        bid_price = record[x]
        if bid_price > highest_bid:
            highest_bid = bid_price
            highest_bidder = x
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

programContinues = True

while programContinues:
    name = input("What is your name :")
    bid = int(input("What is your bid : $"))
    list_of_bidders[name] = bid
    anotherBidder = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    if anotherBidder == "no":
        clear()
        find_highest(list_of_bidders)
        programContinues = False
    elif anotherBidder == "yes":
        clear()
