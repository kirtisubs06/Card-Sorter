"""
Assignment 10: "Sorting Cards"

Author: Kirti Subramanian
CWID: 20531478
Date: 12/4/2022

Program Description: This program has a class defined from which a playing card object can
be created. If the object's rank and suit is given, then the full name of the card will be
returned in word form. The user will be able to compare two cards, and the program can tell
whether they are the same card or not. The class also has a method defined where given two cards,
they can be compared and the smaller/greater one can be identified (based on the orderings of
the bridge card game). There is also a pickle file created from one of the card objects.
"""

from functools import total_ordering
import pickle


@total_ordering
class PlayingCard:
    def __init__(self, rank, suit):
        """
        Constructs an instance of the PlayingCard class given the rank and suit.
        It also initializes a dictionary for the translations.
        :param rank: rank of the card
        :param suit: suit of the card
        """
        self.rank = rank
        self.suit = suit
        self.translations = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                             8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King",
                             "d": "Diamonds", "s": "Spades", "h": "Hearts", "c": "Clubs"}

    def get_rank(self):
        """
        Returns the rank of the card as an integer.
        :return: rank of the card
        """
        # Returns the rank of the card as a number, example 3
        return self.rank

    def get_suit(self):
        """
        Returns the suit of the card as a word after applying translations.
        :return: returns the suit of the card
        """
        return self.translations[self.suit]

    def bj_value(self):
        """
        Returns the blackjack value of the card as an integer.
        :return: the blackjack value of the card
        """
        # Returns the Blackjack value of a card. Ace has a blackjack value of 1,
        # face cards all have blackjack value 10. The rest of the cards have blackjack
        # values that are the same as their rank. The returned value from this method
        # will always be a number.
        return self.rank if self.rank <= 10 else 10

    def __str__(self):
        """
        Returns a string containing the full name of the card.
        :return: full name of card in words
        """
        # Returns a string containing the full name of the card. For example. "Ace of Spades".
        return "{} of {}".format(self.translations[self.rank], self.get_suit())

    def __eq__(self, other):
        """
        Returns True if an existing playing card has the same rank and suit as the object
        "other" that is sent in as a parameter. Otherwise, it returns False.
        :param other: the other card object
        :return: True or False
        """
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """
        Returns True is an existing object is less than the object "other" that is sent
        in as a parameter. Otherwise, it returns False.
        :param other: the other card object
        :return: True or False
        """
        self_rank_bridge = self.rank
        other_rank_bridge = other.rank
        if self.rank == 1:
            self_rank_bridge = 14
        if other.rank == 1:
            other_rank_bridge = 14
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        return self_rank_bridge < other_rank_bridge

    def __repr__(self):
        return str(self)


def main():
    # construct 5 different card objects
    c1 = PlayingCard(5, "h")
    c2 = PlayingCard(13, "c")
    c3 = PlayingCard(11, "s")
    c4 = PlayingCard(9, "d")
    c5 = PlayingCard(1, "c")
    # create a list of the card objects and sort the list
    cards_list = [c1, c2, c3, c4, c5]
    cards_list.sort()
    # store one of the cards as a pickle file and read it back as a new playing card object
    card = open('card.txt', 'wb')
    pickle.dump(c1, card)
    card.close()
    card = open("card.txt", "rb")
    c1_2 = pickle.load(card)
    card.close()
    print(c1_2)


if __name__ == "__main__":
    main()


# test cases for the individual methods
"""
# testing for __eq__ method
card_1 = PlayingCard(4, "c")
card_2 = PlayingCard(4, "c")
print(card_1 == card_2)

# output
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment10.py 
True

Process finished with exit code 0

# testing for __lt__ method
card_3 = PlayingCard(5, "s")
card_4 = PlayingCard(2, "s")
print(card_3 < card_4)

# output
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment10.py 
False

Process finished with exit code 0
"""

# output for the main program
# this is the playing card object that was stored as a pickle file and is
# now read back as a new playing card object
# new card.txt file was created (this is the pickle file for this playing card object)
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment10.py 
5 of Hearts

Process finished with exit code 0
"""