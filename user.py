# A class for the user with some other parameters
# Created by Aaron Guo on 17/09/2021

class User:
    def __init__(self, name, money, card1, card2, big_blind, small_blind, dealer, playing):
        self.name = name
        self.money = money
        self.card1 = card1
        self.card2 = card2
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.dealer = dealer
        self.playing = playing

    # Calculates the money that goes into a bet
    def money_calculation(self, bet):
        self.money = self.money - bet
        if self.money < 0:
            print("Sorry, your balance is too low. Please try again")
            self.money = self.money + bet
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

    def fold(self):
        self.playing = False


# test1 = User("Aaron", 500, "Ace of spades", "Ace of queens", False, False, False, True)
# test1.money_calculation(300)
# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')
# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')
# test1.blind_change()
# print(test1.money, test1.big_blind, test1.small_blind, test1.dealer, sep=' ')
# test1.fold()
# print(test1.playing)
