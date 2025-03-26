from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Лист
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f"📄 {self.name}")


# Узел 
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self, indent=0):
        print('  ' * indent + f"📁 {self.name}")
        for child in self.children:
            child.display(indent + 1)


def main():
    root = Folder("Корневая папка")

    docs = Folder("Документы")
    docs.add(File("resume.pdf"))
    docs.add(File("notes.txt"))

    pictures = Folder("Фото")
    pictures.add(File("vacation.jpg"))

    root.add(docs)
    root.add(pictures)

    root.display()

if __name__ == '__main__':
    main()