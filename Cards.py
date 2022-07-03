"""
to_str() возвращает строковое представление карты в виде строки, формата:4♦
 .equal_suit(card) - проверяет, одинаковые ли масти у карт
Пример:
card1.more(card2) → True, при card1(J♦) card2(10♦).

.more(card) - возвращает True, если карта, у которой вызван метод, больше, чем карта,
которую передали в качестве параметра.
Пример:
card1.more(card2) → True, при card1(J♦) card2(10♦). Валет больше(старше) 10-ки
card1.more(card2) → False, при card1(4♦) card2(10♦). 4-ка не старше 10-ки
 .less(card) - проверяет является ли карта младше, чем карта в параметре
"""
import random

class Card:
    def __init__(self, type, suit):
        self.type = type
        self.suit = suit

    def _set_image(self):
        card_suit_image = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
        self.image = card_suit_image[self.suit]

    def _card_priority(self):
        card_type_priority = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        card_suite_priority = {'Hearts': 10, 'Diamonds': 9, 'Clubs': 8, 'Spades': 7}
        return card_type_priority[self.type], card_suite_priority[self.suit]

    def to_str(self):
        self._set_image()
        return (str(self.type)+str(self.image))

    def equal_suit(self, card):
        return self.suit == card.suit

    def more(self, card):
        first_card = self._card_priority()
        second_card = card._card_priority()
        if self.equal_suit(card):
            return first_card[1] > second_card[1]
        else:
            return first_card[0] > second_card[0]

    def less(self, card):
        first_card = self._card_priority()
        second_card = card._card_priority()
        if self.equal_suit(card):
            return first_card[1] < second_card[1]
        else:
            return first_card[0] < second_card[0]


def test():
    one = Card('2', 'Diamonds')
    two = Card('2', 'Hearts')
    three = Card('J', 'Spades')
    four = Card('J', 'Hearts')

    print(one.to_str())
    print(three.equal_suit(one))
    print(three.less(four))
    a = 0

test()

class Desk:
    def __init__(self):
        self.desk = []
        self.init_desk()

    def init_desk(self):
        cards_priority = ['Hearts','Diamonds','Clubs','Spades']
        cards_priority_type = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in cards_priority:
            for card in cards_priority_type:
                value = card+suit
                self.desk.append(Card(card, suit))

    def show(self):
        print('desk['+str(len(self.desk))+']', end=': ')
        for card in self.desk:
            print(card.to_str(), end=', ')

    def draw(self, x):
        new_desk = Desk()
        new_desk.desk = self.desk[0: x]
        self.desk = self.desk[x: ]
        return new_desk.show()

    def shuffle(self):
        random.shuffle(self.desk)



desk = Desk()

desk.show()
print('\n')
desk.draw(10)
print('\n')
desk.shuffle()
desk.show()
