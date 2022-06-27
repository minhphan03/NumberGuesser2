class Card:
    def __init__(self, group, suit) -> None:
        self._suit = suit
        self._group = group
    
    def get_suit(self):
        return self._suit
    
    def get_group(self):
        return self._group

    def __str__(self) -> str:
        return self._group + " " + self._suit

    def __eq__(self, __o: object) -> bool:
        return self._suit == __o._suit and self._group == __o._group

    