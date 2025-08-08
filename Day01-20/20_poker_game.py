"""
扑克游戏
"""

from enum import Enum
import random


class Suite(Enum):
    """花色枚举类，定义扑克牌的四种花色"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """扑克牌类，表示一张扑克牌

    Attributes:
        suite: 花色，Suite枚举类型
        face: 点数，整数类型，1-13分别表示A,K,Q,J,10-2
    """

    def __init__(self, suite, face):
        """初始化扑克牌对象

        Args:
            suite (Suite): 花色枚举值
            face (int): 点数，范围1-13
        """
        self.suite = suite
        self.face = face

    def __repr__(self):
        """返回扑克牌的字符串表示，格式为花色符号+点数

        Returns:
            str: 扑克牌的可视化字符串表示
        """
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
    def __lt__(self, other):
        """比较两个牌大小，按照花色和点数进行比较

        Args:
            other (Card): 另一张牌

        Returns:
            bool: 当前牌是否比另一张牌小
        """
        if self.suite == other.suite:
            return self.face < other.face
        else:
            return self.suite.value < other.suite.value


# card1 = Card(Suite.SPADE, 5)
# card2 = Card(Suite.HEART, 13)
# print(card1)
# print(card2)


class Poker:
    """扑克牌类，表示一副牌

    Attributes:
        cards: 牌列表，Card对象列表
    """

    def __init__(self):
        """初始化一副牌对象"""
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌，随机打乱牌的顺序"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌，返回当前牌，并移动到下一张牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_more_card(self):
        """判断牌是否还有剩余"""
        return self.current < len(self.cards)

# poker = Poker()
# print(poker.cards)  # 洗牌前的牌
# poker.shuffle()
# print(poker.cards)  # 洗牌后的牌
# print(poker.deal())
# print(poker.has_more_card)

class Player:
    """玩家类，表示一个玩家

    Attributes:
        name: 玩家名称，字符串类型
    """

    def __init__(self, name):
        """初始化玩家对象

        Args:
            name (str): 玩家名称
        """
        self.name = name
        self.cards = []

    def get_card(self, card):
        """摸牌，从牌堆中摸"""
        self.cards.append(card)

    def sort_card(self):
        """排序，按照牌面大小排序"""
        self.cards.sort()

poker = Poker()
poker.shuffle()
players  = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_card(poker.deal())

for player in players:
    player.sort_card()
    print(f'{player.name}', end=': ')
    print(player.cards)

