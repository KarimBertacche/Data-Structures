import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is not None:
               return  self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if tree is empty return None
        if not self:
            return None
        # search to the right, until you find the highest value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return 

        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            dequeued_node = queue.dequeue() 
            print(dequeued_node.value)
            if dequeued_node.left:
                queue.enqueue(dequeued_node.left)
            if dequeued_node.right:
                queue.enqueue(dequeued_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return 

        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            poped_node = stack.pop()
            print(poped_node.value)
            if poped_node.left:
                stack.push(poped_node.left)
            if poped_node.right:
                stack.push(poped_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left is not None:
            self.pre_order_dft(node.left)

        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):    
        if node.left is not None:
            self.post_order_dft(node.left)

        if node.right is not None:
            self.post_order_dft(node.right)

        print(node.value)
