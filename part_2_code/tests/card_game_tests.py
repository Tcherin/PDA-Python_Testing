import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 6)
        self.card2 = Card("Spaces", 4)
        self.card3 = Card("Clubs", 1)
        self.card4 = Card("Diamonds", 8)
        self.card_list = [self.card1, self.card2, self.card3, self.card4]
        self.card_game = CardGame()
    
    def test_check_for_ace(self):
        ace_result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, ace_result)

    def test_highest_card(self):
        highest_result = self.card_game.highest_card(self.card2, self.card4)
        self.assertEqual(self.card2, highest_result)

    def test_cards_total(self):
        total_result = self.card_game.cards_total(self.card_list)
        self.assertEqual("You have a total of 10", total_result)




   

