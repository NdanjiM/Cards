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

if __name__ == '__main__':
	unittest.main()