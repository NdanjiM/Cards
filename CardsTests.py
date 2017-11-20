import unittest
import Cards
import HandClass

class HandClassTestCase(unittest.TestCase):
	def test_cards_high_card_successful(self):
		cards = {"KH","JH","8C","7D","4S"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"High card")

	def test_cards_five_of_a_kind_successful(self):
		cards = {"AS","AC","AH","AD","JKR"}

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

	def test_cards_flush_successful(self):
		cards = {"8D","2D","6D","9D","4D"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Flush")

	def test_cards_full_house_successful(self):
		cards = {"KC","KS","KD","5C","5H"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Full house")

	def test_cards_special_straight_successful(self):
		cards = {"AC","KC","QD","JS","10S"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Straight")

	def test_cards_straight_successful(self):
		cards = {"9C","8C","7C","6D","5D"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Straight")

	def test_cards_three_of_a_kind_successful(self):
		cards = {"2D","2C","2S","KS","6H"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Three of a kind")

	def test_cards_two_pair_successful(self):
		cards = {"JH","JC","4C","4S","9H"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"Two pair")

	def test_cards_one_pair_successful(self):
		cards = {"6H","6S","KS","7H","4C"}

		hand = HandClass.Hand(cards)

		result = Cards.CheckHand(hand.Suits, hand.Rank)
		self.assertEqual(result,"One pair")

if __name__ == '__main__':
	unittest.main()