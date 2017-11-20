import sys
import HandClass

def CheckHand(suits, ranks):
	ranking = list(ranks)
	uniqueRanks = []
	numberRankOccurences = []

	handSuits = list(suits)
	uniqueSuits = []
	numberSuitOccurrences = []

	for i in ranking:
		if i not in uniqueRanks:
			uniqueRanks.append(i)

	for i in uniqueRanks:
		numberRankOccurences.append(ranking.count(i))

	for i in handSuits:
		if i not in uniqueSuits:
			uniqueSuits.append(i)

	for i in uniqueSuits:
		numberSuitOccurrences.append(handSuits.count(i))


	#check for 5 or 4 of a kind
	if "Jk" in ranking and len(uniqueRanks)==2 and (4 in numberRankOccurences):
		return "Five of a kind"
	elif "JK" not in ranking and len(uniqueRanks)==2 and (4 in numberRankOccurences):
		return "Four of a kind"

	#check if straight flush
	if len(uniqueSuits)==1 and IsSequential(ranking):
		return "Straight flush"
	elif len(uniqueSuits)==1 and not IsSequential(ranking):
		return "Flush"
		
def IsSequential(ranks):
	isSequen = True
	#special cases
	if "K" in ranks and "A" in ranks:
		if "Q" not in ranks or "J" not in ranks or "10" not in ranks:
			isSequen = False
	elif "K" in ranks and "A" not in ranks:
		if "Q" not in ranks or "J" not in ranks or "10" not in ranks or "9" not in ranks:
			isSequen = False
	elif "Q" in ranks:
		if "J" not in ranks or "10" not in ranks or "9" not in ranks or "8" not in ranks:
			isSequen = False
	elif "J" in ranks:
		if "7" not in ranks or "10" not in ranks or "9" not in ranks or "8" not in ranks:
			isSequen = False
	elif "A" in ranks:
		if "2" not in ranks or "3" not in ranks or "4" not in ranks or "5" not in ranks:
			isSequen = False
	else:
		counter = 0
		if not IsNumber(ranks[0]):
			counter = int(len(ranks))
			for i in range(len(ranks)-1,0,-1):
				counter = counter + 1
				if ranks[i] != counter:
					isSequen = False
		else:
			counter = int(ranks[len(ranks)-1])
			
			for i in range(len(ranks)-1,-1,-1):
				
				if int(ranks[i]) != counter:
					isSequen = False
				counter = counter + 1

	return isSequen

def IsNumber(rank):
	try:
		int(rank)
		return True
	except ValueError:
		return False


def main():
  userInput = input("Enter cards (comma seperated):")
  cards = userInput.split(',')

  hand = HandClass.Hand(cards)

  print(hand.Rank)

  result = CheckHand(hand.Suits, hand.Rank)

  print(result)
  
if __name__== "__main__":
  main()