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
    # Ensuring no repeats occur
    while len(random_array) < (2 * numberOfUsers + 5):
        r = random.randint(0, 51)
        if r not in random_array:
            random_array.append(r)
    return random_array


# Initialising the blinds distribution
blindsArray = numpy.zeros(shape=(numberOfUsers, 3), dtype='bool')
for i in range(3):
    blindsArray[i][i] = True
# print(blindsArray)

# Creating the game loop
running = True
while running:
    # Assigning all values to people and storing in a list using object "User"
    currentCards = random_cards()
    playerValues = []
    for i in range(numberOfUsers):
        playerValues.append(User(
            userName[i], buyIn,
            deckOfCards[(currentCards[3 + 2*i])], deckOfCards[(currentCards[4 + 2*i])],
            blindsArray[i][0], blindsArray[i][1], blindsArray[i][2], True
        ))

    # Loop to play a round
    while running:
        pot = 0
        # Making all players with blinds place their bets in the round
        for i in playerValues:
            if i.big_blind:
                pot = pot + bigBlind
                i.money_calculation(bigBlind)
            elif i.small_blind:
                pot = pot + smallBlind
                i.money_calculation(smallBlind)


        #
        #
        # # Showing and asking each player if they want to check, raise, or fold
        # for i in range(3): # Since each round can only have 3 iterations
        #     for j in range(numberOfUsers): # Asking input and action from each user
        #         # Checking if the player is currently playing
        #         if playerValues[j][7]:
        #             #
        #

        # for i in playerValues:
        #     print(i.name, i.money, i.card1, i.card2, i.big_blind, i.small_blind, i.dealer)
        # break
    break


