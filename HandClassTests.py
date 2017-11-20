import unittest
import HandClass

class HandClassTestCase(unittest.TestCase):
	def test_handclass_correctrank_successful(self):
		cards = {"AS","10C","10H","3D","3S"}
		hand = HandClass.Hand(cards)
		self.assertEqual(set(hand.Rank),set(["A","10","10","3","3"]))

	def test_handclass_correctsuit_succesfful(self):
		cards = {"AS","10C","10H","3D","3S"}
		hand = HandClass.Hand(cards)
		self.assertEqual(set(hand.Suits), set(["S","C","H","D","S"]))

	def test_handclass_rank_successful_sorted(self):
		cards = {"AS","10C","10H","3D","3S"}
		hand = HandClass.Hand(cards)
		self.assertEqual(hand.Rank,["A","3","3","10","10"])

	def test_handclass_suit_succesfful_sorted(self):
		cards = {"AS","10C","10H","3D","3S"}
		hand = HandClass.Hand(cards)
		self.assertEqual(hand.Suits, ["C","D","H","S","S"])

if __name__ == '__main__':
	unittest.main()