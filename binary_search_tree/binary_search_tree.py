class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_bst = BinarySearchTree(value)
        if value < self.value:
            if self.left is None:
                self.left = new_bst
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = new_bst
            else:
                self.right.insert(value)
        return self

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, arr):
        # lets test for an empty array
        if self.value is None:
            return ("ur a big dummie")

        # traverse both left and right side if we have a tree
        if self.left is None and self.right is None:
            arr.append(self.value)

        if self.left is not None:
            arr.append(self.value)
            self.left.for_each(arr)
        if self.right is not None:
            arr.append(self.value)
            self.right.for_each(arr)
        return arr
    # def for_each(self, cb):
    #     value = self.value
    #     left = self.left
    #     right = self.right
    #     if value is None:
    #         return cb(value)
    #     elif left is None and right is None:
    #         cb(value)
    #     if left is not None:
    #         self.left.for_each(cb)
    #         cb(value)
    #     if right is not None:
    #         self.right.for_each(cb)
    #         cb(value)

    def __str__(self):
        return str(self.value)
    print("running")


# class BinaryTreeNode:
#     def __init__(self, value):
#         self.value = value;
#         self.left = None;
#         self.right = None;
#     def __repr__(self):
#         return str([self.value, self.left, self.right])

# def gen_bin(input_list):
#     if len(input_list) == 0:
#         return None
#     center = len(input_list) // 2
#     node = BinaryTreeNode(input_list[center])
#     node.left = gen_bin(input_list[:center])
#     node.right = gen_bin(input_list[center+1:])
#     return node


# print(gen_bin([1, 2, 3, 4, 5, 6, 7]))
