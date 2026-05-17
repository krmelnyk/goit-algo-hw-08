class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right


def find_min_value(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.value


if __name__ == "__main__":
    tree = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]

    for value in values:
        tree.insert(value)

    print(f"Values: {values}")
    print(f"Minimum value: {find_min_value(tree.root)}")
