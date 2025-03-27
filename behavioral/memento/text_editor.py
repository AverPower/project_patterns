from dataclasses import dataclass

# Объект, состояние которого нужно сохранять
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text: str) -> None:
        self._content += text

    def save(self):
        return TextMemento(self._content)

    def restore(self, memento) -> None:
        self._content = memento.get_saved_content()

    def show_content(self) -> None:
        print(f"Текущий текст: {self._content}")

# Снимок состояния (Memento)
@dataclass
class TextMemento:
    _content: str

    def get_saved_content(self) -> str:
        return self._content

# Управляет историей снимков (Caretaker)
class History:
    def __init__(self, memento: TextMemento):
        self._mementos: list[TextMemento] = [memento] if memento else []

    def push(self, memento: TextMemento) -> None:
        self._mementos.append(memento)

    def pop(self) -> TextMemento:
        return self._mementos.pop()