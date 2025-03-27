class RangeIterator:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f'TreeNode {self.value}'

class TreeIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self.stack.extend(reversed(node.children)) # Добавляем детей в стек
        return node.value



def main():

    # Использование RangeIterator
    for num in RangeIterator(1, 5):
        print(num)  # 1, 2, 3, 4

    # Использование TreeIterator
    # Создаем дерево
    root = TreeNode("A")
    root.add_child(TreeNode("B"))
    root.add_child(TreeNode("C"))
    root.children[0].add_child(TreeNode("D"))

    # Обход
    for value in TreeIterator(root):
        print(value)  # A, B, D, C


if __name__ == '__main__':
    main()