#PAO system practise

import random
import os
import time

withHint = True

class Card:
    def __init__(self, type, pao):
        self.type = type
        self.pao = pao

    def __str__(self):
        return (str(self.type))

    def get_pao(self):
        return self.pao
    def get_type(self):
        return self.type

class Deck:
    def __init__(self):
        pao = {
            "Ace of Clubs": ["a","b","c"],
            "2 of Clubs": ["a","b","c"],
            "3 of Clubs": ["a","b","c"],
            "4 of Clubs": ["a","b","c"],
            "5 of Clubs":["a","b","c"],
            "6 of Clubs":["a","b","c"],
            "7 of Clubs":["a","b","c"],
            "8 of Clubs":["a","b","c"],
            "9 of Clubs":["a","b","c"],
            "10 of Clubs":["a","b","c"],
            "Jack of Clubs":["a","b","c"],
            "Queen of Clubs":["a","b","c"],
            "King of Clubs":["a","b","c"],
            "Ace of Hearts":["a","b","c"],
            "2 of Hearts":["a","b","c"],
            "3 of Hearts":["a","b","c"],
            "4 of Hearts":["a","b","c"],
            "5 of Hearts":["a","b","c"],
            "6 of Hearts":["a","b","c"],
            "7 of Hearts":["a","b","c"],
            "8 of Hearts":["a","b","c"],
            "9 of Hearts":["a","b","c"],
            "10 of Hearts":["a","b","c"],
            "Jack of Hearts":["a","b","c"],
            "Queen of Hearts":["a","b","c"],
            "King of Hearts":["a","b","c"],
            "Ace of Diamonds":["a","b","c"],
            "2 of Diamonds":["a","b","c"],
            "3 of Diamonds":["a","b","c"],
            "4 of Diamonds":["a","b","c"],
            "5 of Diamonds":["a","b","c"],
            "6 of Diamonds":["a","b","c"],
            "7 of Diamonds":["a","b","c"],
            "8 of Diamonds":["a","b","c"],
            "9 of Diamonds":["a","b","c"],
            "10 of Diamonds":["a","b","c"],
            "Jack of Diamonds":["a","b","c"],
            "Queen of Diamonds":["a","b","c"],
            "King of Diamonds":["a","b","c"],
            "Ace of Spades": ["a","b","c"],
            "2 of Spades": ["a","b","c"],
            "3 of Spades": ["a","b","c"],
            "4 of Spades": ["a","b","c"],
            "5 of Spades":["a","b","c"],
            "6 of Spades":["a","b","c"],
            "7 of Spades":["a","b","c"],
            "8 of Spades":["a","b","c"],
            "9 of Spades":["a","b","c"],
            "10 of Spades":["a","b","c"],
            "Jack of Spades":["a","b","c"],
            "Queen of Spades":["a","b","c"],
            "King of Spades":["a","b","c"]
        }
        self.deckList = []
        for card in pao.keys():
            c = Card(card, pao[card])
            self.deckList.append(c)

        self.shuffle_deck(time.time)

    def shuffle_deck(self, seed):
        random.seed = seed
        random.shuffle(self.deckList)

    def get_card_at_index(self,index):
        return self.deckList[index]
        
class Game:
    def __init__(self):
        self.deck = Deck()


    def play(self):
        print("Starting in 5")
        time.sleep(5)
        os.system('cls')
        startTime = time.time()
        #Memorization phase:
        #for each card of 52
        i = 0
        while( i < 52 ):
            print("Press j to go back one card")
            print("Press k to go to the next card")
            print("Press h to get a hint\n")
        
            threeCounter = i % 3

            #progress bar
            print("[" + i*'=' + (52-i) * '-' +  "]")

            card = self.deck.get_card_at_index(i)
            print(card)

            correctInput = False
            while(correctInput != True):
                x = input()
                if(x == 'j'):
                    i -= 1
                    correctInput = True
                elif(x == 'h'):
                    os.system('cls')
                    print("Press j to go back one card")
                    print("Press k to go to the next card")
                    print("Press h to get a hint\n")
                    print("[" + i*'=' + (52-i) * ' ' +  "]")
                    print(card)
                    pao = card.get_pao()
                    for g,r in enumerate(pao):
                        if(g == threeCounter):
                            print(" *"+str(r)+"* ", end="", flush=True)
                        else:
                            print(" -" + str(r) + "- ", end="", flush=True)
                elif(x == 'k'):
                    correctInput = True
                    i += 1

            if(i<0):
                i = 0
            os.system('cls')
        endTime = time.time()

        print("Begining memory palace run through")
        print("Prepare for the first three cards")
        print("Time taken for memorization = "+str(endTime-startTime)+" seconds")
        time.sleep(4)
        numCorrect = 0
        wrongCardList = []
        wrongPAOList = []
        rightCardList = []
        
        i=0
        while(i<52):
            print("Prepare for the first three cards")
            print("Press y if correct")
            print("Press n if incorrect\n")
            threeCounter = i % 3

            #progress bar
            print("[" + i*'=' + (52-i) * '-' +  "]")
            card = self.deck.get_card_at_index(i)
            print(card)
            pao = card.get_pao()
            for g,r in enumerate(pao):
                if(g == threeCounter):
                    print(" *"+str(r)+"* ", end="", flush=True)
                else:
                    print(" -" + str(r) + "- ", end="", flush=True)
                    
            correctInput = False
            while(correctInput != True):   
                x = input()
                if(x == 'y'):
                    numCorrect += 1
                    rightCardList.append( card)
                    i+=1
                    correctInput = True
                elif(x == 'n'):
                    wrongCardList.append( card)
                    wrongPAOList.append( card.get_pao()[threeCounter])
                    i+=1
                    correctInput = True


            os.system('cls')

        print("You got these cards with their respective pao wrong:")
        for k,c in enumerate(wrongCardList):
            print(c.get_type() + " = " + c.get_pao()[0] +"-"+ c.get_pao()[1] +"-"+ c.get_pao()[2] +" --- *"+ wrongPAOList[k] + "*")

        print("You got these cards right:")
        for k,c in enumerate(rightCardList):
            print(c.get_type() + " = " + c.get_pao()[0] +"-"+ c.get_pao()[1] +"-"+ c.get_pao()[2] +" --- *")
        print("With %d being the number correct\n" % numCorrect)


        print("\n\nIt took me "+str(endTime-startTime)+" seconds to memorize with "+str((len(rightCardList)/52)*100)+" percent accuracy")
        print("Press anything to restart")
        if(input()):
            self.deck.shuffle_deck(time.time)
            self.play()
            

        


g = Game()
g.play()
