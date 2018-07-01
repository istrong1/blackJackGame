# -*- coding: utf-8 -*-
# using import future because Python 2.7 doesn't recognize end =" "
from __future__ import print_function
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

class Player:

    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0


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

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount # money 100; bet(20)
        self.bet += amount # money 100->80 bet 0->20

    def win(self, result):
        if result == True:
            if self.score == 21 and  len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(House):
    for card in range(len(House.hand)): # hides first card
        if card == 0:
            print("X", end =" ")
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card], end =" ")


cardDeck = createDeck()
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
Player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = createDeck()

while(True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(), cardDeck.pop()]
    secondHand = [cardDeck.pop(), cardDeck.pop()]
    Player1.play(firstHand)
    House.play(secondHand)
    Bet = int(raw_input("Please enter your bet: "))

    print(cardDeck)
    Player1.betMoney(Bet)
    printHouse(House)
    print(Player1)

    if Player1.hasBlackJack():
        if House.hasBlackJack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        while(Player1.score < 21): #while(True==True), keeps going forever
            action = str(raw_input("Do you want another card? (y/n): "))
            if action == "y":
                Player1.hit(cardDeck.pop()) #whichever card is popped gets put into this line
                print(Player1)
                printHouse(House)
            else:
                break
        while(House.score < 16):
            print(House)
            House.hit(cardDeck.pop())

        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
            else:
                Player1.win(False)

        elif Player1.score > House.score:
            Player1.win(True)

        elif Player1.score == House.score:
            Player1.draw()

        else:
            if House.score > 21:
                Player1.win(True)
            else:
                Player1.win(False)

    print(Player1.money)
    print(House)
