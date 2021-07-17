import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    # def test_check_card_has_suit(self):
    #     self.ace_of_spades = Card("Spades", 1)
    #     self.assertEqual("Spades", self.ace_of_spades.suit)

    # def test_check_card_has_value(self):
    #     self.ace_of_spades = Card("Spades", 1)
    #     self.assertEqual(1, self.ace_of_spades.value)

    def test_check_for_ace(self):
        self.ace_of_spades = Card("Spades", 1)
        result = CardGame.check_for_ace(self, self.ace_of_spades)
        self.assertEqual(True, result)

    def test_highest_card(self):
        self.card_2 = Card("Hearts", 4)
        self.card_1 = Card("Spades", 7)
        self.higher_card = CardGame.highest_card(self,self.card_1, self.card_2)
        self.assertEqual(7, self.higher_card.value)

    def test_cards_total(self):
        self.card_1 = Card("Hearts", 4)
        self.card_2 = Card("Spades", 7)
        self.card_3 = Card("Clubs", 10)
        self.cards = [self.card_1, self.card_2, self.card_3]
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 21", result)