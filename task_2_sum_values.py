class Node:
    """Store a tree node value and links to child nodes."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Represent a binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value while preserving the BST ordering rule."""

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


def sum_tree_values(root):
    """Return the sum of all values in a tree."""

    if root is None:
        return 0

    return (
        root.value
        + sum_tree_values(root.left)
        + sum_tree_values(root.right)
    )


if __name__ == "__main__":
    tree = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]

    for value in values:
        tree.insert(value)

    print(f"Values: {values}")
    print(f"Sum of all values: {sum_tree_values(tree.root)}")
