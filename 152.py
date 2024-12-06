from random import shuffle
def deck():
    sign = ['diamonds', 'clubs', 'hearts', 'spades']
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for x in range(2, 11):
        for y in sign:
            deck.append(str(x)+' '+y)
    for y in sign:
        for x in ['J', 'Q']:
            deck.append(str(x)+' '+y)
    deck_start = []
    deck_end = []
    for x in sign:
        deck_start.append('A'+' '+x)
    for x in sign:
        deck_end.append('K'+' '+x)
    shuffle(deck_start)
    shuffle(deck_end)
    shuffle(deck)
    for x in deck_start+deck+deck_end:
        yield x
gen = deck()
for x in range(52):
    print(next(gen))
