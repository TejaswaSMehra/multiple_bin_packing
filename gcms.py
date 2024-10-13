from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        pass 

    def add_bin(self, bin_id, capacity):
        pass

    def add_object(self, object_id, size, color):
        raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        pass
    
    