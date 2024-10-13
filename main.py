from gcms import GCMS
from object import Color

if __name__ == "__main__":

    gcms = GCMS()

    # Adding bins with varying capacities
    gcms.add_bin(1001, 50)  # Bin 1001 with capacity 50
    gcms.add_bin(1002, 30)  # Bin 1002 with capacity 30
    gcms.add_bin(1003, 40)  # Bin 1003 with capacity 40
    gcms.add_bin(1004, 25)  # Bin 1004 with capacity 25
    gcms.add_bin(1005, 35)  # Bin 1005 with capacity 35

    # Adding objects with specific sizes and colors
    gcms.add_object(2001, 20, Color.RED)  # Object 2001 (Size 20, RED)
    gcms.add_object(2002, 15, Color.YELLOW)  # Object 2002 (Size 15, YELLOW)
    gcms.add_object(2003, 10, Color.BLUE)  # Object 2003 (Size 10, BLUE)
    gcms.add_object(2004, 25, Color.GREEN)  # Object 2004 (Size 25, GREEN)
    gcms.add_object(2005, 30, Color.RED)  # Object 2005 (Size 30, RED)
    gcms.add_object(2006, 5, Color.YELLOW)  # Object 2006 (Size 5, YELLOW)
    gcms.add_object(2007, 8, Color.BLUE)  # Object 2007 (Size 8, BLUE)
    gcms.add_object(2008, 22, Color.GREEN)  # Object 2008 (Size 22, GREEN)

    # Bin information based on the correct answer
    # bin_info returns the number of objects and the list of objects stored in it 
    # The order of elements in the list does not matter
    print(gcms.bin_info(1001))  # Expected: (30, [2001])
    print(gcms.bin_info(1002))  # Expected: (8, [2008])
    print(gcms.bin_info(1003))  # Expected: (7, [2004, 2007])
    print(gcms.bin_info(1004))  # Expected: (0, [2002, 2003])
    print(gcms.bin_info(1005))  # Expected: (0, [2005, 2006])

    # Object information based on the correct answer
    # object_info returns the value of the bin where the object is stored
    print(gcms.object_info(2001))  # Expected: 1001
    print(gcms.object_info(2002))  # Expected: 1004
    print(gcms.object_info(2003))  # Expected: 1004
    print(gcms.object_info(2004))  # Expected: 1003
    print(gcms.object_info(2005))  # Expected: 1005
    print(gcms.object_info(2006))  # Expected: 1005
    print(gcms.object_info(2007))  # Expected: 1003
    print(gcms.object_info(2008))  # Expected: 1002