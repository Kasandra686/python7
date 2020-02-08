from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани для пошива пальто : {round(self.param/6.5)+0.5}"

class Costume(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани для костюма : {2* self.param +0.3}"

coat = Coat(44)
costume = Costume(168)
print(coat.consumption)
print(costume.consumption)
