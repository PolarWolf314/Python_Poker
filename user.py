# A class for the user with some other parameters
# Created by Aaron Guo on 17/09/2021

class User:
    def __init__(self, name, money, card1, card2,
                 big_blind, small_blind, dealer,
                 playing, player_order, bet_amount):
        self.name = name
        self.money = money
        self.card1 = card1
        self.card2 = card2
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.dealer = dealer
        self.playing = playing
        self.player_order = player_order
        self.bet_amount = bet_amount

    # Calculates the money that goes into a bet
    def money_calculation(self, bet):
        if bet <= self.money:
            self.money = self.money - bet
            self.bet_amount = self.bet_amount + bet
        else:
            print("Sorry, your balance is too low. Please try again")
        return

    # Function that changes blinds around
    def blind_change(self):
        if self.big_blind:
            self.small_blind = True
            self.big_blind = False
        elif self.small_blind:
            self.small_blind = False
            self.dealer = True
        elif self.dealer:
            self.dealer = False
        else:
            self.big_blind = True
        return self.big_blind, self.small_blind, self.dealer

    # Function that fold the player
    def fold(self):
        self.playing = False

    # Function that gives a player big blind
    def give_big_blind(self):
        self.big_blind = True

    # Function that does all in
    def all_in(self):
        self.bet_amount = self.bet_amount + self.money
        self.money = 0
        print(self.name + " has gone all in. Good luck!")

    # Function that orders the players
    def reorder_player(self):
        self.player_order = self.player_order + 1


# test1 = User("Aaron", 500, "Ace of spades", "Ace of queens",
#              False, False, False, True, 1, 50)
#
# test1.money_calculation(500)

# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')
# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')
# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')

# test1.fold()
# print(test1.playing)
# test1.all_in()
# print(test1.money)
