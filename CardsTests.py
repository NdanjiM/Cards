import unittest
import Cards
import HandClass

class HandClassTestCase(unittest.TestCase):
	def test_cards_five_of_a_kind_successful(self):
		cards = {"AS","AC","AH","AD","Jkr"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Five of a kind")

if __name__ == '__main__':
	unittest.main()