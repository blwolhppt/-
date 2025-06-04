# Реализуйте структуру данных "Двоичное дерево поиска" на языке программирования по вашему выбору. 
# У двоичного дерева поиска есть два свойства: каждый узел имеет до двух дочерних узлов (потомков).
# Каждый узел меньше своих потомков справа, а его потомки слева меньше его самого.

# Необходимо реализовать создание пустого дерева, добавление элемента, 
# удаление элемента с автоматической балансировкой дерева, поиск элемента по значению. Желательно использовать ООП.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_recursive(self.root, data)

    def _add_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            succ = self._get_min_node(node.right)
            node.data = succ.data
            node.right = self._delete_recursive(node.right, succ.data)
        return node

    def _get_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("├── " if is_left else "└── ") + str(node.data))
        print_tree(node.left, prefix + ("│   " if is_left else "    "), is_left=True)
        print_tree(node.right, prefix + ("    " if is_left else "│   "), is_left=False)


if __name__ == "__main__":
    tree = BinTree()

    for val in [50, 30, 70, 20, 40, 60, 80]:
        tree.add(val)

    print("Структура дерева:")
    print_tree(tree.root)

    print("\nIn-order обход:", tree.inorder())

    found = tree.search(60)
    print("Поиск 60:", "Найдено" if found else "Не найдено")

    tree.delete(70)
    print("\nПосле удаления 70:")
    print_tree(tree.root)
    print("In-order обход после удаления:", tree.inorder())
