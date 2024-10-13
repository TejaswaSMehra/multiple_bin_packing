# Galactic Cargo Management System (GCMS)

## Description

The **Galactic Cargo Management System (GCMS)** is an implementation of an efficient cargo bin packing algorithm tailored for interstellar shipping companies. This system manages the packing of cargo into bins based on specified algorithms that optimize space usage according to cargo colors. The project includes the implementation of two primary algorithms: the **Compact Fit Algorithm** and the **Largest Fit Algorithm**.

## Features

- **Dynamic Bin Management**: Add and remove bins with specific capacities.
- **Cargo Object Management**: Add, delete, and track objects within bins.
- **Color-Coded Algorithms**: Different packing strategies based on cargo color:
  - Blue: Compact Fit, Least ID
  - Yellow: Compact Fit, Greatest ID
  - Red: Largest Fit, Least ID
  - Green: Largest Fit, Greatest ID
- **AVL Tree Structure**: Utilizes AVL trees for efficient insertions, deletions, and lookups.

## File Structure

```
GCMS/
│
├── gcms.py          # Main class for managing bins and cargo objects
├── bin.py           # Class defining the structure of a bin
├── object.py        # Class defining the structure of a cargo object
├── avl.py           # AVL tree implementation for bins and objects
├── node.py          # Node structure for the AVL tree
├── exceptions.py    # Custom exception classes
├── main.py          # Debugging and testing purposes
└── README.md        # Project documentation
```

## Requirements

- Python 3.x
- No external libraries required

## Usage

1. **Initialize the GCMS**:
   ```python
   from gcms import GCMS
   gcms = GCMS()
   ```

2. **Add Bins**:
   ```python
   gcms.add_bin(bin_id, capacity)
   ```

3. **Add Objects**:
   ```python
   gcms.add_object(object_id, size, color)
   ```

4. **Delete Objects**:
   ```python
   gcms.delete_object(object_id)
   ```

5. **Query Information**:
   - Object Location:
     ```python
     gcms.object_info(object_id)
     ```
   - Bin Information:
     ```python
     gcms.bin_info(bin_id)
     ```

## Acknowledgments

- Inspired by the challenges of interstellar cargo management.
- Special thanks to resources on AVL trees and bin packing algorithms.

---
