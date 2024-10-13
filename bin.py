from avl import AVLTree

class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.objects = AVLTree()

    def add_object(self, object):
        # Insert object into the AVL Tree of objects
        self.objects.insert(object.id, object)
        self.remaining_capacity -= object.size

    def remove_object(self, object_id):
        # Remove object from the AVL Tree of objects
        object_node = self.objects.find(object_id)
        if object_node:
            object_size = object_node.value.size
            self.objects.delete(object_id)
            self.remaining_capacity += object_size
            return object_size
        else:
            print("Object not found")