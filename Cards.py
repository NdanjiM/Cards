import sys
import HandClass

def CheckHand(suits, ranks):
	#check for 5 of a kind
	ranking = list(ranks)
	suits = list(suits)
	if ranking[0]=="Jk":
		same = True
		for i in range(1, len(ranking)-1):
			if(ranking[i]!=ranking[i+1]):
				same = False
		if same == True:
			return "Five of a kind"


def main():
  userInput = input("Enter cards (comma seperated):")
  cards = userInput.split(',')

  hand = HandClass.Hand(cards)

  result = CheckHand(hand.Suits, hand.Rank)

  print(result)
  
if __name__== "__main__":
  main()