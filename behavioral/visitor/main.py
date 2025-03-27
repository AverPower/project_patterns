from animals import Lion, Elephant, Giraffe
from visitors import SoundVisitor, DescriptionVisitor

animals = [Lion(), Elephant(), Giraffe()]

sound_visitor = SoundVisitor()
desc_visitor = DescriptionVisitor()

print("### Звуки животных ###")
for animal in animals:
    animal.accept(sound_visitor)

print("\n### Описания животных ###")
for animal in animals:
    animal.accept(desc_visitor)