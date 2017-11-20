import sys
import HandClass

def CheckHand(suits, ranks):
	#check for 5 of a kind
	ranking = list(ranks)
	uniqueRanks = []
	numberOccurences = []

	for i in ranking:
		if i not in uniqueRanks:
			uniqueRanks.append(i)

	for i in uniqueRanks:
		numberOccurences.append(ranking.count(i))

	if "Jk" in ranking and len(uniqueRanks)==2 and (4 in numberOccurences):
		return "Five of a kind"
		
			


def main():
  userInput = input("Enter cards (comma seperated):")
  cards = userInput.split(',')

  hand = HandClass.Hand(cards)

  result = CheckHand(hand.Suits, hand.Rank)

  print(result)
  
if __name__== "__main__":
  main()