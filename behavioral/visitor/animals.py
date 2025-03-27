from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Lion(Animal):
    def accept(self, visitor):
        visitor.visit_lion(self)

class Elephant(Animal):
    def accept(self, visitor):
        visitor.visit_elephant(self)

class Giraffe(Animal):
    def accept(self, visitor):
        visitor.visit_giraffe(self)