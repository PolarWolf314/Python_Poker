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


# A function that gets the cards from the deck using the randomised index
def access_cards(cards):
    card_array = []
    for card in range(len(cards)):
        card_array.append(cards[card])
    return card_array


# Initialising the blinds distribution
blindsArray = numpy.zeros(shape=(numberOfUsers, 3), dtype='bool')
for i in range(3):
    blindsArray[i][i] = True

# Assigning all values to people and storing in a list using object "User"
currentCards = access_cards([random_cards()])
playerValues = []
for i in range(numberOfUsers):
    playerValues.append(User(
        userName[i], buyIn,
        currentCards[3 + 2 * i], currentCards[4 + 2 * i],  # NEED TO FIX THIS
        blindsArray[i][0], blindsArray[i][1], blindsArray[i][2], True, (i + 1), 0
    ))


# A function that sorts out the moves player order by one
def reorder():
    for j in playerValues:  # Reorders the players inside the class
        j.reorder_player()
        if j.player_order == (numberOfUsers + 1):
            j.player_order = 1
    playerValues.sort(key=lambda x: x.player_order)


# Test code
for i in range(3):
    for j in playerValues:
        print(j.name, j.card1, j.card2, j.player_order)
    reorder()


# Creating the game loop
running = False
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
                else:
                    pot = pot + bigBlind
                    i.money_calculation(bigBlind)
            elif i.small_blind:
                if i.money <= smallBlind:
                    pot = pot + i.money
                    i.all_in()
                else:
                    pot = pot + smallBlind
                    i.money_calculation(smallBlind)

        for i in range(3):  # There are only 3 steps in 1 round of poker
            counter = 0
            max_bet = bigBlind

            for player in playerValues:
                while player.bet_amount != max_bet:
                    response = input("Please ")



    # remember to give new cards

        # for i in playerValues:
        #     print(i.name, i.money, i.card1, i.card2,
        #           i.big_blind, i.small_blind, i.dealer,
        #           i.playing, i.player_order)
        break
    break
