class Hand:
	def __init__(self, cards):
		self.Rank = self.SplitRanks(cards)
		self.Suits = self.SplitSuits(cards)

	def SplitRanks(self, cards):
		ranks = []
		for card in cards:
			rank = card[:-1]
			ranks.append(rank)
		return ranks

	def SplitSuits(self, cards):
		suits = []
		for card in cards:
			suit = card[-1:]
			suits.append(suit)
		return suits