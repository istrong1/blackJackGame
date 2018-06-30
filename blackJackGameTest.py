# -*- coding: utf-8 -*-


from random import shuffle

def createDeck():
    Deck = []
    
    faceValues = ["A", "J", "Q", "K"]
    for i in range(4): #there are 4 different suits
        for card in range(2,11): #adding numbers 2 through 10, non-face
            Deck.append(str(card))
            
        for card  in faceValues:
            Deck.append(card)
            
    shuffle(Deck)
    return Deck

cardDeck = createDeck()

#print(cardDeck)

class Player:
    
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        print(self.score)
        self.money = money
        
        
    def __str__(self): #allows us to call print(player)
        currentHand = "" #self.hand = ["A", "10"]
                        #the loop changes loop to "A 10", much prettier
        for card in self.hand:
            currentHand += str(card) + " "
            
        finalStatus = currentHand + "score: " + str(self.score)
        #"A 10 score: 21", what finalStatus looks like print(player) is called
        return finalStatus
    
    def setScore(self):
        self.score = 0 #" 3 4 " -> "3 4 10"
                        # 7 -> 7 + 10, so we don't add 10 to the net draw
        print(self.score)
        faceCardsDict = {"A":11, "J":10, "Q":10, "K":10, 
                         "2":2, "3":3, "4":4, "5":5, "6":6,
                         "7":7, "8":8, "9":9, "10":10}
        aceCounter = 0
        for card in self.hand: #"10", want to convert this to and int
                self.score += faceCardsDict[card]
                if card == "A":
                    aceCounter += 1
                if self.score > 21 and aceCounter != 0: 
                    self.score -= 10
                    aceCounter -= 1
        return self.score

Player1 = Player(["3", "7", "5"])
print(Player1)
