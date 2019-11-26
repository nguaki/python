import random

class Card(object):
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank  = rank
        
    def show(self):
        print( "{} of {}".format(self.suite, self.rank) )


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for suite in ['spades', 'heart', 'club', 'diamond']:
            
            #Appends Card object.
            for rank in range(1,14):
                self.cards.append(Card(suite, rank))
                
    def show(self):
        
        print('There are ', len(self.cards), ' cards.')
        for card in self.cards:
            card.show()
                
    def shuffle(self):
        
        for i in range(len(self.cards)-1, 0, -1):
            
            r = random.randint(0, i)
            
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def draw(self):
        
        return self.cards.pop()
        
        #card1.show()
        
    def howManyCardsLeft(self):
        
        return(len(self.cards))
        
class player(object):
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    #returns the entire object s.t. calling draw() again is possible.
    def draw(self, deck):
        self.hand.append(deck.draw())
        
        
    def showHand(self):
        print(self.name)
        for card in self.hand:
            card.show()
            
        
            
        
#acard = Card('Club', 10)
#acard.show()

deck = Deck()
#deck.show()
deck.shuffle()
#card = deck.draw()
#card.show()

#player = player('Danny')
#player.draw(deck).draw(deck)
#player.showHand()


numPlayers = 13

if 52 % numPlayers !=0 :
    print('not an even players')

for i in range(1,53):
    card = deck.draw()
    card.show()
    print(deck.howManyCardsLeft())
    
deck = Deck()
deck.shuffle()

#playerCards = {}
playerCards = dict()
#playerCards = defaultDict(list)

for i in range(0,13):
    playerCards[i] = []



for cardNum in range(0, 52):
    print('cardNum=', cardNum)
    #for playerID in range(1, 14):
    playerID = cardNum % numPlayers
    card = deck.draw()
    print(deck.howManyCardsLeft())
    playerCards[playerID].append(card)
        
uniqCards = []
for playerID in playerCards.keys():
    print(playerID, ' has')
    for card in playerCards[playerID]:
        if card not in uniqCards:
            uniqCards.append(card)
        card.show()
        
print('uniq card count = ', len(uniqCards))
