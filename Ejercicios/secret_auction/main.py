from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False


def find_highest_bider(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bider(bids)
    elif should_continue == "yes":
        os.system("cls")


# def add_bidders(biders_name, biders_bid):
#     secret_bidders = {}
#     offer_list = []
#     secret_bidders[biders_name] = biders_bid
#     key1 = secret_bidders[biders_name]
#     offer_list.append(key1)
#     print(offer_list)


# add_bidders(first_name, bid)
