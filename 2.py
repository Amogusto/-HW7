from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def count(self):
        pass
    

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H > 200:
            self.__H = 200
        elif H < 160:
            self.__H = 160
        else:
            self.__H = H

    def count(self):
        result = self.H * 2 + 0.3
        return f'ткани: {result}'

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V > 65:
            self.__V = 65
        elif V < 46:
            self.__V = 46
        else:
            self.__V = V

    def count(self):
        result = self.V / 6.5 + 0.5
        return f'ткани {result}'

suit1 = Suit(170)
coat1 = Coat(56)
print(suit1.H)
print(coat1.V)
print(suit1.count())
print(coat1.count())