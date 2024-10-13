from node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    
    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)
        return self.find(key)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, key, value)
            node.right.parent = node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self._get_balance(node)
        
        self.update_height(node)
        balance = self._get_balance(node)

        # Left-heavy
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right-heavy
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                if node.right:
                    node.right.parent = node.parent
                return node.right
            elif not node.right:
                if node.left:
                    node.left.parent = node.parent
                return node.left

            temp = self._get_min_value_node(node.right)
            temp2 = Node(temp.key, temp.value)
            self.swap_nodes(temp2, temp)
            self.swap_nodes(node, temp)
            node = temp
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self._get_balance(node)
        
        self.update_height(node)
        balance = self._get_balance(node)

        # Left-heavy
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right-heavy
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def swap_nodes(self, node1, node2):
        # Swap keys and values
        if node1==self.root:
            self.root = node2
        elif node2==self.root: 
            self.root = node1
        node1.parent, node2.parent = node2.parent, node1.parent
        if node1.parent:
            if node1.parent.left == node2:
                node1.parent.left = node1
            else:
                node1.parent.right = node1
        if node2.parent:
            if node2.parent.left == node1:
                node2.parent.left = node2
            else:
                node2.parent.right = node2

        # Swap left children
        node1.left, node2.left = node2.left, node1.left
        if node1.left:
            node1.left.parent = node1
        if node2.left:
            node2.left.parent = node2

        # Swap right children
        node1.right, node2.right = node2.right, node1.right
        if node1.right:
            node1.right.parent = node1
        if node2.right:
            node2.right.parent = node2
        

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x
        
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        self.update_height(x)
        self.update_height(y)
        return y


    def _right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right:
            x.right.parent = y
        
        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

        self.update_height(y)
        self.update_height(x)
        return x



    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)

    def bfs_traversal(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            level = []
            next_queue = []
            for node in queue:
                if node:
                    level.append(node.key)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                else:
                    level.append(None)
            result.append(level)
            queue = next_queue
        return result