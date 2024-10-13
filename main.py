
from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
if __name__=="__main__":

    gcms = GCMS()

    gcms.add_bin(1234, 10)
    gcms.add_bin(4321, 20)
    gcms.add_bin(1111, 15)

    try:
        gcms.add_object(8989, 6, Color.RED )
    except: 
        print("Object 1 was not able to be added")
    
    try:
        gcms.add_object(2892, 8, Color.RED )
    except: 
        print("Object 2 was not able to be added")

    try:
        gcms.add_object(4839, 9, Color.RED )
    except: 
        print("Object 3 was not able to be added")

    try:
        gcms.add_object(3283, 2, Color.RED )
    except: 
        print("Object 4 was not able to be added")

    try:
        gcms.add_object(8983, 8, Color.RED )
    except: 
        print("Object 5 was not able to be added")

        


    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
