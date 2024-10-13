from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins_by_capacity = AVLTree()
        self.bin_id_to_node = AVLTree()
        self.object_id_to_bin_id = AVLTree()

    def add_bin(self, bin_id, capacity):
        # Create a new bin and insert it into the AVL Tree
        new_bin = Bin(bin_id, capacity)
        node = self.bins_by_capacity.insert((capacity, bin_id), new_bin)
        self.bin_id_to_node.insert(bin_id, node)

    def add_object(self, object_id, size, color):
        new_object = Object(object_id, size, color)
        
        bin_node = self.find_suitable_bin(size, color)
        if not bin_node or bin_node.key[0] < size:
            raise NoBinFoundException()
        if bin_node:
            bin_node.value.add_object(new_object)
            bin_node1 = self.bin_id_to_node.find(bin_node.key[1]).value
            self.object_id_to_bin_id.insert(object_id, bin_node.value.id)
            self.update_bin_capacity(bin_node, -size)
        else:
            raise NoBinFoundException()

    def delete_object(self, object_id):
        # Find the bin containing the object
        bin_id_node = self.object_id_to_bin_id.find(object_id)
        if bin_id_node:
            bin_id = bin_id_node.value
            bin_node = self.bin_id_to_node.find(bin_id).value
            if bin_node:
                object_size = bin_node.value.remove_object(object_id)
                self.object_id_to_bin_id.delete(object_id)
                # Update the bin's remaining capacity
                self.update_bin_capacity(bin_node, object_size)
        else:
            return None

    def bin_info(self, bin_id):
        # Find the bin and return its info
        bin_node = self.bin_id_to_node.find(bin_id).value
        if bin_node:
            current_capacity = bin_node.value.remaining_capacity
            objects = []
            bin_node.value.objects.in_order_traversal(bin_node.value.objects.root, objects)
            objects = [objects.id for objects in objects]
            return (current_capacity, objects)
        else:
            raise NoBinFoundException()

    def object_info(self, object_id):
        bin_id_node = self.object_id_to_bin_id.find(object_id)
        if bin_id_node:
            return bin_id_node.value
        else:
            return None

    def find_suitable_bin(self, size, color):
        if color == Color.BLUE:
            return self.compact_fit_least_id(size)
        elif color == Color.YELLOW:
            return self.compact_fit_largest_id(size)
        elif color == Color.RED:
            return self.largest_fit_least_id(size)
        elif color == Color.GREEN:
            return self.largest_fit_largest_id(size)
        return None

    def compact_fit_least_id(self, size):
        # Find the bin with the smallest remaining capacity that can accommodate the object
        node = self.bins_by_capacity.root
        suitable_bin = None
        while node:
            if node.key[0] >= size:
                if suitable_bin is None or node.key < suitable_bin.key:
                    suitable_bin = node
                node = node.left
            else:
                node = node.right
        return suitable_bin

    def compact_fit_largest_id(self, size):
        # Find the bin with the smallest remaining capacity that can accommodate the object
        node = self.bins_by_capacity.root
        suitable_bin = None
        minimum_approriate_capacity = 0
        while node:
            if node.key[0] >= size:
                if not minimum_approriate_capacity or node.key[0] < minimum_approriate_capacity:
                    minimum_approriate_capacity = node.key[0]
                node = node.left
            else:
                node = node.right
        node = self.bins_by_capacity.root
        if not minimum_approriate_capacity:
            return suitable_bin
        while node:
            if node.key[0] < minimum_approriate_capacity:
                node = node.right
            elif node.key[0] > minimum_approriate_capacity:
                node = node.left
            else:
                while node and node.key[0] == minimum_approriate_capacity:
                    suitable_bin = node
                    node = node.right
        return suitable_bin
    
    def largest_fit_least_id(self, size):
        # Find the bin with the largest remaining capacity that can accommodate the object
        node = self.bins_by_capacity.root
        suitable_bin = None
        maximum_approriate_capacity = 0
        while node:
            if node.key[0] >= size:
                if not maximum_approriate_capacity or node.key[0] > maximum_approriate_capacity:
                    maximum_approriate_capacity = node.key[0]
                node = node.right
            else:
                node = node.right
        if not maximum_approriate_capacity:
            return suitable_bin
        node = self.bins_by_capacity.root
        while node:
            if node.key[0] < maximum_approriate_capacity:
                node = node.right
            elif node.key[0] > maximum_approriate_capacity:
                node = node.left
            else:
                while node and node.key[0] == maximum_approriate_capacity:
                    suitable_bin = node
                    node = node.left
        return suitable_bin

    def largest_fit_largest_id(self, size):
        # Find the bin with the largest remaining capacity that can accommodate the object
        node = self.bins_by_capacity.root
        suitable_bin = None
        while node:
            if node.key[0] >= size:
                if suitable_bin is None or node.key > suitable_bin.key:
                    suitable_bin = node
                node = node.right
            else:
                node = node.right
        return suitable_bin

    def update_bin_capacity(self, bin_node, size):
        # Remove the bin from the AVL Tree
        self.bins_by_capacity.delete(bin_node.key)
        # Update the bin's remaining capacity
        result = self.bins_by_capacity.bfs_traversal(self.bins_by_capacity.root)
        bin_node.key = (bin_node.value.remaining_capacity, bin_node.value.id)
        # Reinsert the bin into the AVL Tree
        self.bins_by_capacity.insert(bin_node.key, bin_node.value)
        temp = self.bins_by_capacity.find(bin_node.key)
        bin_node1 = self.bin_id_to_node.find(bin_node.key[1]).value
        bin_node2 = bin_node1
        bin_node.left = None
        bin_node.right = None
        bin_node.parent = None
        self.bins_by_capacity.swap_nodes(bin_node, temp)