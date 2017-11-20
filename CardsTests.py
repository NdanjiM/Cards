import unittest
import Cards
import HandClass

class HandClassTestCase(unittest.TestCase):
	def test_cards_five_of_a_kind_successful(self):
		cards = {"AS","AC","AH","AD","Jkr"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Five of a kind")

	def test_cards_four_of_a_kind_successful(self):
		cards = {"AS","AC","AH","AD","KH"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Four of a kind")

	def test_cards_special_straight_flush_successful(self):
		cards = {"AH","KH","QH","JH","10H"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Straight flush")

	def test_cards_straight_flush_successful(self):
		cards = {"8D","7D","6D","5D","4D"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Straight flush")

	def test_cards_special_flush_successful(self):
		cards = {"AH","3H","QH","7H","10H"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Flush")

	def test_cards_Flush_successful(self):
		cards = {"8D","2D","6D","9D","4D"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Flush")

if __name__ == '__main__':
	unittest.main()