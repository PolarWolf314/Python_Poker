# Poker in python
# Created by Aaron Guo on 17/08/2021

import random
import numpy
from user import User
from cards import deckOfCards

numberOfUsers = int(input("Please enter the number of users: "))

# Making sure there aren't too many users
while numberOfUsers > 10 | numberOfUsers < 3:
    print("Sorry, that is too many users. Max number of users is 8.")
    numberOfUsers = int(input("Please enter the number of users: "))

# Getting and storing the names of all the users
userName = []
for i in range(numberOfUsers):
    userName.append(input("Please enter player " + str(i + 1) + "'s name: "))

# Getting the initial game variables
buyIn = abs(int(input("What would you like the buy in to be: ")))
bigBlind = abs(int(input("What would you like the big blind to be: ")))
smallBlind = abs(int(input("What would you like the small blind to be: ")))

# Making sure small blind is smaller than big blind
while smallBlind >= bigBlind:
    print("Please enter a value of small blind that is smaller than the big blind.")
    smallBlind = abs(int(input("What would you like the small blind to be: ")))


# Making a function that creates a random array for cards
def random_cards():
    random_array = []
    card_array = []
    # Ensuring no repeats occur
    while len(random_array) < (2 * numberOfUsers + 5):
        r = random.randint(0, 51)
        if r not in random_array:
            random_array.append(r)
    # Extracting cards from deckOfCards
    for i in range(len(random_array)):
        card_array.append(deckOfCards[random_array[i]])
    return card_array


# Initialising the blinds distribution
blindsArray = numpy.zeros(shape=(numberOfUsers, 3), dtype='bool')
for i in range(3):
    blindsArray[i][i] = True

# # Test code to test random_cards()
# r = random_cards()
# print(r)


# Assigning all values to people and storing in a list using object "User"
currentCards = random_cards()
playerValues = []
for i in range(numberOfUsers):
    playerValues.append(User(
        userName[i], buyIn,
        currentCards[3 + 2 * i], currentCards[4 + 2 * i],
        blindsArray[i][0], blindsArray[i][1], blindsArray[i][2], 3, (i + 1), 0
    ))


# A function that sorts out the moves player order by one
def reorder():
    for j in playerValues:  # Reorders the players inside the class
        j.reorder_player()
        if j.player_order == (numberOfUsers + 1):
            j.player_order = 1
    playerValues.sort(key=lambda x: x.player_order)


# A function that updates the pot and player status
def askPlayer(player, betAmount, pot):
    pot += betAmount
    player.status = 2  # Means the current player has checked
    player.bet_amount += betAmount  # Updating current player bet
    return pot


# # Test code to test askPlayer()
# for i in playerValues:
#     askPlayer(i, 50)
#     print(i.money)

# Test code to rest reorder()
# for i in range(3):
#     for j in playerValues:
#         print(j.name, j.card1, j.card2, j.player_order)
#     reorder()

# # Test code to work out indexing a list with objects
# playerIndex = 0
# currentPlayer = playerValues[playerIndex]
# print(currentPlayer.money)

# Creating the game loop
running = True
while running:
    # Loop to play a round
    while running:
        pot = 0
        # Setting player order
        reorder()
        # Making all players with blinds place their bets in the round
        for i in playerValues:
            if i.big_blind:
                if i.money <= bigBlind:  # Forcing all-in if not enough money
                    pot = pot + i.money
                    i.all_in()
                else:  # Otherwise, force add big blind amount
                    pot = pot + bigBlind
                    i.money_calculation(bigBlind)  # fix this
            elif i.small_blind:  # Forcing all in
                if i.money <= smallBlind:
                    pot = pot + i.money
                    i.all_in()
                else:  # Otherwise, force add small blind amount
                    pot = pot + smallBlind
                    i.money_calculation(smallBlind)

        for i in range(3):  # There are only 3 steps in 1 round of poker
            counter = 0
            max_bet = bigBlind
            playerIndex = 0
            currentPlayer = playerValues[playerIndex]

            # While loop that checks 2 conditions before moving out of loop
            while not (currentPlayer.bet_amount == max_bet & currentPlayer.status != 3):

                # Printing the name, balance, and game status for the current player
                print("Hello " + currentPlayer.name + ", the money in the pot right now is " + str(pot))
                print("You currently have $" + str(currentPlayer.money))
                if currentPlayer.big_blind:
                    print("You are currently the big blind")
                elif currentPlayer.small_blind:
                    print("You are currently the small blind")
                elif currentPlayer.dealer:
                    print("You are currently the dealer")

                # Asking what the player wants to do
                status = input("Do you want to raise, check, or fold? (type your answer, no spaces please) \n")
                status = status.lower()

                # Checking if the input is valid
                while not (status == "raise" or status == "check" or status == "fold"):
                    print("man can u even spell or read")
                    status = input("Do you want to raise, check, or fold? (type your answer, no spaces please) \n")

                # What happens if the player wants to raise
                if status == "raise":
                    betAmount = int(input("How much would you like to bet: "))

                    # If the amount bet is too high, ask again
                    while betAmount > currentPlayer.money or betAmount < max_bet:
                        print("try again")  # fix this
                        betAmount = int(input("How much would you like to bet: "))
                        if betAmount == currentPlayer.money and betAmount <= currentPlayer.money:
                            currentPlayer.all_in()
                            pot = askPlayer(currentPlayer, betAmount, pot)
                            max_bet = max_bet + betAmount
                        elif betAmount <= currentPlayer.money:
                            currentPlayer.money_calculation(betAmount)
                            pot = askPlayer(currentPlayer, betAmount, pot)
                            max_bet = max_bet + betAmount

                    # Adding the bet to the pot and subtracting from the player
                    if betAmount == currentPlayer.money and currentPlayer.status == 3:
                        currentPlayer.all_in()
                        pot = askPlayer(currentPlayer, betAmount, pot)
                    elif currentPlayer.status == 3:
                        currentPlayer.money_calculation(betAmount)
                        pot = askPlayer(currentPlayer, betAmount, pot)
                    max_bet = max_bet + betAmount

                # Iterating through all players until both conditions are met
                playerIndex = playerIndex + 1
                if playerIndex >= numberOfUsers:
                    playerIndex = 0
                currentPlayer = playerValues[playerIndex]

        # remember to give new cards

        # for i in playerValues:
        #     print(i.name, i.money, i.card1, i.card2,
        #           i.big_blind, i.small_blind, i.dealer,
        #           i.status, i.player_order)
        break
    break
