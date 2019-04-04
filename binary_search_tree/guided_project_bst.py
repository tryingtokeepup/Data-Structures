class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    def __str__(self):
        return str(self.value)
    print("running")


test = BinarySearchTree(20)
print(test)
test.insert(13)
print(test.left)
test.insert(4)
print(test.left.left)
test.insert(25)
print(test.right)
test.insert(29)
print(test.right.right)
