from abc import ABC, abstractmethod


class AnimalVisitor(ABC):
    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_elephant(self, elephant):
        pass

    @abstractmethod
    def visit_giraffe(self, giraffe):
        pass

# Посетитель для генерации звуков
class SoundVisitor(AnimalVisitor):
    def visit_lion(self, lion):
        print("Лев рычит: Рррр!")

    def visit_elephant(self, elephant):
        print("Слон трубит: Тууу!")

    def visit_giraffe(self, giraffe):
        print("Жираф издает тихий звук: Ммм...")

# Посетитель для генерации описаний
class DescriptionVisitor(AnimalVisitor):
    def visit_lion(self, lion):
        print("Лев — король джунглей")

    def visit_elephant(self, elephant):
        print("Слон — огромное млекопитающее")

    def visit_giraffe(self, giraffe):
        print("Жираф — самое высокое животное")